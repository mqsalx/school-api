# 💼🧑‍💻 School API

## 📜 Descrição do Projeto

- Este projeto é uma API RESTful desenvolvida em **Django** e utilizando **MySQL** como banco de dados.
  A API permite a gestão de estudantes, cursos e matrículas, fornecendo operações CRUD (Criar, Ler, Atualizar e Deletar) para cada uma dessas entidades.
  Além disso, implementa funcionalidades avançadas como paginação, ordenação, filtragem, e está protegida com autenticação **JWT (JSON Web Token)**, garantindo a segurança das rotas.

## 📂 Estrutura do Projeto

```bash
school_api/
├── school/
│   ├── admin/                 # Configurações do admin Django
│   ├── migrations/            # Arquivos de migração do banco de dados
│   ├── models/                # Definição dos modelos de dados
│   ├── serializers/           # Serializadores para transformar dados da API
│   ├── urls/                  # Definição das rotas
│   ├── views/                 # Lógica das views da API (CRUD de usuários)
│   └── tests/                 # Testes automatizados da API
├── setup/                     # Configurações sensíveis e arquivos ASGI/WSGI
├── static/                    # Arquivos estáticos do projeto
├── utils/                     # Funções auxiliares
├── venv/                      # Ambiente virtual com dependências Python
├── .env                       # Variáveis de ambiente
├── .flake8                    # Configuração do Flake8
├── .gitignore                 # Arquivos ignorados pelo Git
├── pyproject.toml             # Configurações de formatação (Black, etc.)
├── manage.py                  # Comando de gerenciamento do Django
└── requirements.txt           # Dependências do projeto
```

## 🎛️ Funcionalidades:

- **Gestão de Estudantes**: Registre, atualize e gerencie dados dos estudantes, incluindo nome, email e CPF.
- **Gestão de Cursos**: Criação e gerenciamento de cursos com níveis de complexidade (Básico, Intermediário e Avançado).
- **Gestão de Matrículas**: Inscrição de estudantes em cursos, com opções de diferentes turnos (Manhã, Tarde, Noite).
- **Documentação interativa**: Utiliza Swagger e Redoc para exibir a documentação da API de forma interativa.
- **Autenticação JWT**: Para proteger as rotas e garantir que apenas usuários autenticados possam acessar as funcionalidades.
- [**Throttle**](./school/views/throttles/README.md): Limitação de requisições por usuário e anônimo para evitar consumo indesejado no uso da API.

## 🛠️ Tecnologias Utilizadas

- **Django**: Framework web robusto utilizado para criar a API RESTful.
- **Django REST Framework (DRF)**: Biblioteca poderosa para facilitar o desenvolvimento de APIs em - **Django**.
- **Django Filters**: Utilizado para implementar filtros avançados na API.
- **JWT (JSON Web Token)**: Implementado para autenticação segura.
- **MySQL**: Banco de dados relacional utilizado para armazenar os dados.
- **Swagger e Redoc**: Para geração e visualização da documentação interativa da API.
- **Throttle Rates**: Controle de limite de requisições com base no tipo de usuário (autenticado ou anônimo).

## 🛣️ Rotas da API

- ### 🔐 Rotas de Autenticação JWT

  - **POST /token/**

    Obter Token de Acesso (Access e Refresh Token).

    **Body**:

    ```json
    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhb...",
      "access": "eyJ0eXAiOiJKV1QiLCJh..."
    }
    ```

  - **POST /token/refresh/**

    Renovar o Token de Acesso (usando o Refresh Token).

    **Body**:

    ```json
    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhb..."
    }
    ```

  - **POST /token/verify/**

    Verificar o Token de Acesso (usando o Access Token).

    **Body**:

    ```json
    {
      "token": "eyJ0eXAiOiJKV1QiLCJhb..."
    }
    ```

- ### 🧑‍💻 Rotas do Estudante

  - **POST /students/**

    Registrar um novo usuário.

    **Body**:

    ```json
    {
      "name": "Alan Turing",
      "email": "alanemail@emailexample.com",
      "cpf": "36329833052",
      "b_day": "2010-01-01",
      "phone": "99 99999-9999"
    }
    ```

  - **GET /students/**

    Obter todos os estudantes registrados.

  - **GET /students/:id**

    Obter estudante específico registrado.

  - **GET /students/:id/registrations/**

    Obter todas matriculas em que um estudante está registrado mediante de um ID específico de estudante.

  - **PATCH /students/:id**

    Atualizar estudante registrado.

    **Body**:

    ```json
    {
      "name": "John Doe Steve",
      "email": "johnSteve@example.com"
    }
    ```

  - **DELETE /students/:id**

    Deletar estudante específico.

- ### 👨🏼‍🏫 Rotas do Curso

  - **POST /courses/**

    Registrar um novo curso.

    **Body**:

    ```json
    {
      "code": "12wee",
      "description": "Python Programming",
      "level": "B"
    }
    ```

  - **GET /courses/**

    Obter todos os cursos registrados.

  - **GET /courses/:id**

    Obter curso específico registrado.

  - **GET /courses/:id/registrations/**

    Obter alunos registrados mediante de um ID específico de curso.

  - **PATCH /courses/:id**

    Atualizar curso registrado.

    **Body**:

    ```json
    {
      "code": "123abc",
      "description": "Python Programming Language"
    }
    ```

  - **DELETE /courses/:id**

    Deletar curso específico.

- ### 📑 Rotas da Matrícula

  - **POST /registrations/**

    Registrar uma nova matrícula.

    **Body**:

    ```json
    {
      "code": "12wee",
      "description": "Python Programming",
      "level": "B"
    }
    ```

  - **GET /registrations/**

    Obter todos as matrículas registradas.

  - **GET /registrations/:id**

    Obter matrícula específica registrada.

## 🐳 Docker Compose

1. - **Construindo e iniciando a imagem**
   - Iniciando o MySQL
     ```bash
     docker-compose up -d db
     ```
   - Iniciando o Django

     ```bash
     docker-compose up -d web
     ```

   - Iniciando o Nginx

     ```bash
     docker-compose up -d nginx
     ```

2. - **Parar o contêiner**
   ```bash
   docker-compose down
   ```

## ▶️ Ambiente virtual:

1. - **Criando o ambiente**
   ```bash
   python -m venv venv
   ```
2. - **Ativando o Ambiente Virtual**
   ### - Windows:
   ```bash
   venv\scripts\activate
   ```
   ### - Linux:
   ```bash
   source venv/bin/activate
   ```
3. - **Instalação de Dependências**
   ```bash
   pip install -r requirements.txt
   ```
4. - **Adicionando o venv ao Jupyter como Kernel**
   ```bash
   python -m ipykernel install --user --name=venv
   ```

## ✅ Executando Migrações

```bash
python manage.py makemigrations

python manage.py migrate
```

## 🦸 Criando o SuperUser

```bash
python manage.py createsuperuser
```

## 🏁 Executando o Servidor

```bash
python manage.py runserver
```
