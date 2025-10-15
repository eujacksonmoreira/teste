# Sistema de Gestão de Processos Backoffice

Este é um projeto full-stack completo para gestão e análise de processos de backoffice, incluindo backend em Python (FastAPI), frontend em HTML/CSS/JS (Bootstrap), e infraestrutura Docker.

## Funcionalidades Principais

- **Backend (FastAPI):** API RESTful para gerenciamento de usuários, processos, simulações de capacidade, relatórios e importação de dados.
- **Frontend (HTML/CSS/JS + Bootstrap):** Interface de usuário responsiva com telas de login, dashboard, processos, simulação de capacidade, relatórios e gerenciamento de usuários (admin).
- **Autenticação JWT:** Sistema de login/logout com tokens JWT para segurança.
- **Integração com IA:** Geração de comentários para gráficos do dashboard via API do ChatGPT.
- **Importação de Dados:** Módulo para consumir API externa e importar dados de processos, com agendamento periódico.
- **Simulação de Capacidade:** Ferramenta para simular a capacidade de atendimento da equipe com base em efetivos e estagiários.
- **Relatórios:** Exportação de dados de processos, capacidade e simulações em CSV/Excel.
- **Infraestrutura:** Docker e Docker Compose para fácil setup e execução.
- **Banco de Dados:** SQLite para desenvolvimento e `schema.sql` para migração ao PostgreSQL.

## Stack Técnica

- **Backend:** Python 3.11, FastAPI, Uvicorn, Pydantic, httpx, APScheduler, aiosmtplib, aiosqlite, pandas, numpy, prophet.
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, Chart.js.
- **Banco de Dados:** SQLite (desenvolvimento), PostgreSQL (produção).
- **Containerização:** Docker, Docker Compose.

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto usando Docker Compose.

### Pré-requisitos

- Docker Desktop (ou Docker Engine e Docker Compose) instalado.

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd projeto-backoffice
    ```

2.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto (`projeto-backoffice/`) baseado no `.env.template` fornecido. Preencha as variáveis com seus valores. As chaves `OPENAI_API_KEY` (ou `CHATGPT_API_KEY`) e `API_TOKEN` são essenciais para as funcionalidades de IA e importação de dados, respectivamente.

3.  **Construa e inicie os serviços:**
    ```bash
    docker compose up --build -d
    ```
    Isso irá construir as imagens Docker, criar os contêineres para o backend (`api`) e frontend (`web`), e iniciá-los em segundo plano.

4.  **Execute o script de seed (opcional, mas recomendado para dados de exemplo):**
    Este script irá popular o banco de dados SQLite com usuários de exemplo, unidades, tipos de processo e 200 processos fictícios.
    ```bash
    docker compose exec api python3 backend/database/seed.py
    ```

5.  **Acesse a aplicação:**
    Abra seu navegador e acesse:
    -   **Frontend:** `http://localhost:8080`

## Credenciais de Acesso (após executar o seed.py)

**Administrador:**
-   **Email:** `admin@sistema.com`
-   **Senha:** `admin123`

**Usuário Comum:**
-   **Email:** `usuario@sistema.com`
-   **Senha:** `user123`

## Estrutura do Projeto

```
projeto-backoffice/
├── backend/                  # Código do backend (FastAPI)
│   ├── Dockerfile
│   ├── main.py               # Aplicação principal
│   ├── database.py           # Configuração do banco de dados (SQLite)
│   ├── autenticacao.py       # Módulo de autenticação JWT
│   ├── email_service.py      # Serviço de envio de e-mails
│   ├── ia_comentarios.py     # Integração com ChatGPT
│   ├── agendador.py          # Agendador de tarefas (APScheduler)
│   ├── requirements.txt      # Dependências Python
│   └── rotas/                # Módulos de rotas da API
│       ├── __init__.py
│       ├── auth.py
│       ├── usuarios.py
│       ├── processos.py
│       ├── dashboard.py
│       ├── simulacao.py
│       ├── relatorios.py
│       └── importacao.py
├── frontend/                 # Código do frontend (HTML/CSS/JS)
│   ├── Dockerfile
│   ├── nginx.conf            # Configuração do Nginx
│   ├── index.html            # Dashboard
│   ├── login.html            # Tela de Login
│   ├── definir-senha.html    # Tela de Definição de Senha
│   ├── processos.html        # Listagem de Processos
│   ├── simulacao.html        # Simulação de Capacidade
│   ├── usuarios.html         # Gerenciamento de Usuários
│   ├── relatorios.html       # Relatórios e Importação
│   ├── css/                  # Estilos CSS
│   │   └── styles.css
│   └── js/                   # Scripts JavaScript
│       ├── config.js
│       ├── auth.js
│       ├── login.js
│       ├── definir-senha.js
│       ├── dashboard.js
│       ├── processos.js
│       ├── simulacao.js
│       ├── usuarios.js
│       └── relatorios.js
├── database/                 # Arquivos de banco de dados
│   ├── schema.sql            # Esquema para PostgreSQL
│   └── seed.py               # Script para popular o SQLite com dados de exemplo
├── .env.template             # Modelo de variáveis de ambiente
└── docker-compose.yml        # Configuração do Docker Compose
```
```
## Migração para PostgreSQL

O arquivo `database/schema.sql` contém o DDL (Data Definition Language) para criar as tabelas no PostgreSQL. Para migrar, você pode:

1.  Criar um banco de dados PostgreSQL.
2.  Conectar-se ao banco de dados usando um cliente como `psql`.
3.  Executar o conteúdo de `schema.sql`:
    ```bash
    psql -U seu_usuario -d seu_banco -f database/schema.sql
    ```
4.  No `docker-compose.yml`, você precisaria adicionar um serviço de PostgreSQL e configurar o backend para usar o PostgreSQL em vez do SQLite (ajustando a string de conexão no `database.py` e as variáveis de ambiente).

## Variáveis de Ambiente

Consulte o arquivo `.env.template` para uma lista completa das variáveis de ambiente necessárias e suas descrições.

---

**Desenvolvido por Manus AI**

