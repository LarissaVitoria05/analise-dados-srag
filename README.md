# 📊 Análise Epidemiológica de SRAG e Imunização no Brasil com Neo4j:

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Neo4j](https://img.shields.io/badge/Neo4j-Graph%20Database-008CC1?style=flat&logo=neo4j&logoColor=white)](https://neo4j.com/)
[![Git](https://img.shields.io/badge/Git-Security%20First-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/)

Projeto de pipeline e análise de dados focado no mapeamento de casos de **Síndrome Respiratória Aguda Grave (SRAG)**, identificação de perfis de comorbidades e relacionamentos geográficos entre pacientes e municípios brasileiros utilizando bancos de dados em grafos.

---

## 🎯 Objetivos do Projeto:

* **Tratamento & Pipeline:** Limpeza e padronização de dados brutos epidemiológicos da base SIVEP-Gripe (`Data/`).
* **Modelagem em Grafos:** Transforma a estrutura relacional/tabular em um grafo no **Neo4j** para mapear conexões complexas entre `Paciente`, `Cidade` e `Comorbidade`.
* **Análise Visual:** Geração de gráficos explicativos sobre a distribuição de perfil demográfico (idade, sexo) e prevalência de comorbidades.
* **Engenharia Limpa:** Código modular em Python com suporte a variáveis de ambiente (`.env`) e otimização de inserção em lote via operador `UNWIND` Cypher.

---

## 🛠️ Tecnologias e Ferramentas:

| Categoria | Tecnologia | Uso |
| :--- | :--- | :--- |
| **Linguagem** | Python | Processamento e pipeline de ingestão de dados |
| **Manipulação de Dados** | Pandas | Limpeza, filtragem e padronização |
| **Banco de Dados** | Neo4j (Cypher) | Armazenamento e modelagem do grafo epidemiológico |
| **Segurança/DevOps** | Dotenv / Os.getenv | Gestão de credenciais sem exposição de segredos |
| **Versionamento** | Git & GitHub | Controle de versão seguro com `.gitignore` customizado |

---

## 📐 Estrutura do Grafo (Modelagem):

(Cidade {nome}) <--[:RESIDE_EM]-- (Paciente {id, idade, sexo}) --[:POSSUI_COMORBIDADE]-> (Comorbidade {nome})


📂 Estrutura do Repositório:
analise-dados-srag/
├── img/
│   ├── Relações entre comorbidades e sexos.png
│   └── Visualização das 25 comorbidades mais presentes entre os notificados.png
├── src/
│   ├── limpeza.py          # Tratamento básico dos dados tabulares
│   ├── visualizacao.py     # Geração de gráficos explicativos
│   └── main.py             # Execução principal do pipeline
├── .env.exemplo            # Modelo seguro para variáveis de ambiente
├── .gitignore              # Filtro para ignorar .env, Data/ e .venv/
├── banco_grafos.py         # Módulo de conexão e ingestão em lote no Neo4j
└── teste_conexao.py        # Script para validação da instância Neo4j

## 👩‍💻 Autora:
Desenvolvido com 💖 por color $\color{hotblue}{\text{Larissa Vitoria}}$.




