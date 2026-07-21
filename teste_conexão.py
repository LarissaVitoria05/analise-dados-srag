from neo4j import GraphDatabase

#dados do banco neo4j
URI = "neo4j://127.0.0.1:7687"
USER = "neo4j"
PASSWORD = "Imunização081"


def testar_ponte():
    try:
        # Tenta criar o driver e verificar a conexão
        with GraphDatabase.driver(URI, auth=(USER, PASSWORD)) as driver:
            driver.verify_connectivity()
            print("🚀 SUCESSO: O PyCharm está conectado ao Neo4j!")

            # Teste extra: perguntar a versão do banco
            with driver.session() as session:
                result = session.run("RETURN 'Conexão ativa!' AS msg")
                print(f"Mensagem do banco: {result.single()['msg']}")

    except Exception as e:
        print(f"❌ FALHA NA CONEXÃO: {e}")
        print("\nVerifique se o banco está com o 'Start' ligado no Neo4j Desktop.")


if __name__ == "__main__":
    testar_ponte()