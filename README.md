📊 Análise Epidemiológica de SRAG e Imunização no Brasil com Neo4j
Projeto de pipeline e análise de dados focado no mapeamento de casos de Síndrome Respiratória Aguda Grave (SRAG), identificação de perfis de comorbidades e relacionamentos geográficos entre pacientes e municípios brasileiros utilizando bancos de dados em grafos.

🎯 Objetivos do Projeto
Tratamento & Pipeline: Limpeza e padronização de dados brutos epidemiológicos da base SIVEP-Gripe (Data/).

Modelagem em Grafos: Transforma a estrutura relacional/tabular em um grafo no Neo4j para mapear conexões complexas entre Paciente, Cidade e Comorbidade.

Análise Visual: Geração de gráficos explicativos sobre a distribuição de perfil demográfico (idade, sexo) e prevalência de comorbidades.

Engenharia Limpa: Código modular em Python com suporte a variáveis de ambiente (.env) e otimização de inserção em lote via operador UNWIND Cypher.


📐 Estrutura do Grafo (Modelagem):
(Cidade{nome}) <-- [RESIDE_EM]-- (Paciente) {id, idade, sexo})-- [:POSSUI COMORBIDADE]-> (Comorbidade) {nome})
° Paciente: É o nó central, que contém o id, idade e o sexo
° Cidade: Nó que contém a cidade em que o paciente reside e é padronizado (padrão com caixa alta e sem espaços extras)
° Comorbidade: Nó que mapeia as condições de risco pré existentes do paciente

📈 Visualizações e Insights:
As imagens dos resultados estão salvas na pasta img/.

1. Visualização das Comorbidades Mais Presentes
Análise gráfica das comorbidades de maior impacto entre os notificados na base processada.

2. Relações entre Comorbidades e Sexo
Cruzamento demográfico analisando o perfil de distribuição por sexo entre as principais condições de risco.

📂 Estrutura do Repositório:
analise-dados-srag/
├── img/                       # Gráficos e visualizações geradas na análise
│   ├── Relações entre comorbidades e sexos.png
│   └── Visualização das 25 comorbidades mais presentes...png
├── src/                       # Scripts do pipeline de dados
│   ├── limpeza.py             # Tratamento básico dos dados tabulares
│   ├── visualizacao.py        # Geração de gráficos explicativos
│   └── main.py                # Execução principal do pipeline
├── .env.exemplo               # Modelo seguro para variáveis de ambiente
├── .gitignore                 # Filtro para ignorar .env, Data/ e .venv/
├── banco_grafos.py            # Módulo de conexão e ingestão em lote no Neo4j
└── teste_conexao.py           # Script para validação da instância Neo4j

🚀 Como Executar o Projeto Localmente:
1. Pré-requisitos:
Python 3.10+
Instância ativa do Neo4j (local via Neo4j Desktop / Docker ou cloud via AuraDB)
2. Variáveis de Ambiente:
Crie um arquivo .env na raiz do projeto (baseado no .env.exemplo) e insira suas credenciais:
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=sua_senha_segura

3. Rodando o Pipeline
1. Clone o repositório:
git clone https://github.com/LarissaVitoria05/analise-dados-srag.git cd analise-dados-srag
2. Instale as dependências:
pip install pandas neo4j matplotlib seaborn python-dotenv
3. Execute o fluxo principal:
python src/main.py

 👩Autora
 Desenvolvido por Larissa Vitória.



