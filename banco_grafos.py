import os
import pandas as pd
from neo4j import GraphDatabase
URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
USER = os.getenv("NEO4J_USER", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD")

class BancoDadosGrafo:
    def __init__(self):
        if not PASSWORD:
          raise ValueError("❌ A variável de ambiente NEO4J_PASSWORD não foi configurada!")
            
        self.driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

    def close(self):
        self.driver.close()

    def inserir_pacientes(self, df):
        """
        Cria os nós de Paciente e Cidade e o relacionamento RESIDE_EM usando lote (UNWIND).
        """
        print(f"⚡ Injetando {len(df)} pacientes e cidades no Neo4j...")
        
        # Converte o DataFrame para uma lista de dicionários nativos do Python
        dados_pacientes = []
        for _, row in df.iterrows():
            cidade = str(row['ID_MUNICIP']).strip().upper() if pd.notna(row['ID_MUNICIP']) else "NÃO INFORMADO"
            dados_pacientes.append({
                'id': str(row['NU_NOTIFIC']),
                'idade': int(row['NU_IDADE_N']) if pd.notna(row['NU_IDADE_N']) else None,
                'sexo': str(row['CS_SEXO']) if pd.notna(row['CS_SEXO']) else "IGNORADO",
                'cidade': cidade
            })

        query = """
            UNWIND $batch AS row
            MERGE (c:Cidade {nome: row.cidade})
            MERGE (p:Paciente {id: row.id})
            SET p.idade = row.idade, p.sexo = row.sexo
            MERGE (p)-[:RESIDE_EM]->(c)
        """

        with self.driver.session() as session:
            session.run(query, batch=dados_pacientes)
            
        print("✅ Pacientes e Cidades injetados com sucesso!")

    def inserir_comorbidades_detalhadas(self, df):
        """
        Cria os nós de Comorbidade e vincula aos pacientes existentes em lote (UNWIND).
        """
        print("🧬 Processando vínculos de comorbidades (MORB_DESC)...")

        dados_comorbidades = []
        for _, row in df.iterrows():
            if pd.notna(row['MORB_DESC']) and str(row['MORB_DESC']).strip() != "":
                dados_comorbidades.append({
                    'id': str(row['NU_NOTIFIC']),
                    'nome': str(row['MORB_DESC']).strip().upper()
                })

        query = """
            UNWIND $batch AS row
            MATCH (p:Paciente {id: row.id})
            MERGE (c:Comorbidade {nome: row.nome})
            MERGE (p)-[:POSSUI_COMORBIDADE]->(c)
        """

        with self.driver.session() as session:
            session.run(query, batch=dados_comorbidades)

        print(f"✅ {len(dados_comorbidades)} vínculos de comorbidades criados!")

if __name__ == "__main__":
    print("Execute a main.py para rodar o pipeline completo.")