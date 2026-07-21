import os
import pandas as pd
from src.limpeza import processar_dados_pe
from banco_grafos import BancoDadosGrafo


def executar_pipeline():
    # 1. LOCALIZAÇÃO DO ARQUIVO (Caminho Robusto)
    # Pega a pasta onde este arquivo main.py está (src) e sobe um nível
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_csv = os.path.join(base_dir, "Data", "INFLUD19-23-03-2026.csv")

    print(f"🚀 Iniciando Pipeline...")
    print(f"📂 Buscando arquivo em: {caminho_csv}")

    try:
        # 2. LIMPEZA E FILTRAGEM
        # Sua função já filtra por 'PE' e seleciona as colunas necessárias
        df_limpo = processar_dados_pe(caminho_csv)

        if df_limpo.empty:
            print("⚠️ O DataFrame está vazio. Verifique os filtros no limpeza.py.")
            return

        print(f"✅ Dados carregados: {len(df_limpo)} registros de Pernambuco.")

        # 3. CONEXÃO COM O NEO4J
        db = BancoDadosGrafo()

        # 4. DEFINIÇÃO DA AMOSTRA
        # Vamos usar 2000 linhas para garantir que apareçam várias cidades e sintomas
        amostra = df_limpo.head(2000)

        # 5. INJEÇÃO DOS DADOS
        print(f"⚡ Injetando {len(amostra)} pacientes no Grafo...")
        db.inserir_pacientes(amostra)

        print("🧬 Vinculando sintomas e comorbidades (MORB_DESC)...")
        db.inserir_comorbidades_detalhadas(amostra)

        # 6. FECHAMENTO
        db.close()
        print("\n✨ FINALIZADO COM SUCESSO!")
        print("Dica: No Neo4j, rode 'MATCH (p:Paciente)-[r]->(n) RETURN p,r,n LIMIT 100' para ver as conexões.")

    except FileNotFoundError:
        print(f"❌ ERRO: O arquivo CSV não foi encontrado no caminho: {caminho_csv}")
    except Exception as e:
        print(f"❌ OCORREU UM ERRO INESPERADO: {e}")


if __name__ == "__main__":
    executar_pipeline()
