# 💼🧑‍💻 School API

## 📜 Project Description

- This project is a RESTful API developed in Django and using MySQL as a database. The API allows the management of students, courses and enrollments, providing CRUD (Create, Read, Update and Delete) operations for each of these entities. In addition, it implements advanced features such as paging, sorting, filtering, and is protected with JWT (JSON Web Token) authentication, ensuring the security of the routes.

## 📂 Project Structure

```bash
school_api/
├── school/
│   ├── admin/                 # Django admin settings
│   ├── migrations/            # Database migration files
│   ├── models/                # Defining data models
│   ├── serializers/           # Serializers to transform API data
│   ├── urls/                  # Route definition
│   ├── views/                 # API view logic (user CRUD)
│   └── tests/                 # Automated API Testing
├── setup/                     # Sensitive settings and ASGI/WSGI files
├── static/                    # Static project files
├── utils/                     # Auxiliary functions
├── venv/                      # Virtual environment with Python dependencies
├── .env                       # Environment variables
├── .flake8                    # Flake8 Configuration
├── .gitignore                 # Files ignored by Git
├── pyproject.toml             # Formatting settings (Black, etc.)
├── manage.py                  # Django Management Command
└── requirements.txt           # Project dependencies
```

## 🎛️ Features

- **Student Management**: Register, update and manage student data, including name, email and CPF.
- **Course Management**: Creation and management of courses with levels of complexity (Basic, Intermediate and Advanced).
- **Enrollment Management**: Enrollment of students in courses, with options for different shifts (Morning, Afternoon, Evening).
- **Interactive documentation**: Uses Swagger and Redoc to display API documentation interactively.
- **JWT authentication**: To secure routes and ensure that only authenticated users can access functionality.
- [**Throttle**](./school/views/throttles/README.md): Limitation of requests per user and anonymously to avoid unwanted consumption when using the API.

## 🛠️ Technologies Used

- **Django**: Robust web framework used to create the RESTful API.
- **Django REST Framework (DRF)**: Powerful library to facilitate API development in - **Django**.
- **Django Filters**: Used to implement advanced filters in the API.
- **JWT (JSON Web Token)**: Implemented for secure authentication.
- **MySQL**: Relational database used to store data.
- **Swagger e Redoc**: For generating and viewing interactive API documentation.
- **Throttle Rates**: Request limit control based on user type (authenticated or anonymous).

## 🛣️ API Routes

- ### 🔐 JWT Authentication Routes

  - **POST /token/**

    Get Access Token (Access and Refresh Token).

    **Body**:

    ```json
    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhb...",
      "access": "eyJ0eXAiOiJKV1QiLCJh..."
    }
    ```

  - **POST /token/refresh/**

    Renew the Access Token (using Refresh Token).

    **Body**:

    ```json
    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhb..."
    }
    ```

  - **POST /token/verify/**

    Verify Access Token (using Access Token).

    **Body**:

    ```json
    {
      "token": "eyJ0eXAiOiJKV1QiLCJhb..."
    }
    ```

- ### 🧑‍💻 Student Routes

  - **POST /students/**

    Register a new user.

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

    Get all registered students.

  - **GET /students/:id**

    Get specific student registered.

  - **GET /students/:id/registrations/**

    Get all enrollments where a student is registered using a specific student ID.

  - **PATCH /students/:id**

    Update registered student.

    **Body**:

    ```json
    {
      "name": "John Doe Steve",
      "email": "johnSteve@example.com"
    }
    ```

  - **DELETE /students/:id**

    Delete specific student.

- ### 👨🏼‍🏫 Course Routes

  - **POST /courses/**

    Register a new course.

    **Body**:

    ```json
    {
      "code": "12wee",
      "description": "Python Programming",
      "level": "B"
    }
    ```

  - **GET /courses/**

    Get all registered courses.

  - **GET /courses/:id**

    Get specific course registered.

  - **GET /courses/:id/registrations/**

    Get registered students using a specific course ID.

  - **PATCH /courses/:id**

    Update registered course.

    **Body**:

    ```json
    {
      "code": "123abc",
      "description": "Python Programming Language"
    }
    ```

  - **DELETE /courses/:id**

    Delete specific course.

- ### 📑 Enrollment Routes

  - **POST /registrations/**

    Register a new registration.

    **Body**:

    ```json
    {
      "code": "12wee",
      "description": "Python Programming",
      "level": "B"
    }
    ```

  - **GET /registrations/**

    Get all registered license plates.

  - **GET /registrations/:id**

    Get specific license plate registered.

## 🐳 Docker Compose

1. - **Building and starting the image**

   - Starting MySQL
     ```bash
     docker-compose up -d db
     ```

   - Starting Django

     ```bash
     docker-compose up -d web
     ```

   - Starting Nginx

     ```bash
     docker-compose up -d nginx
     ```

2. - **Stop the container**
   ```bash
   docker-compose down
   ```

## ▶️ Virtual environment

1. - **Creating the environment**
   ```bash
   python -m venv venv
   ```
2. - **Activating the Virtual Environment**
   ### - Windows:
   ```bash
   venv\scripts\activate
   ```
   ### - Linux:
   ```bash
   source venv/bin/activate
   ```
3. - **Installing Dependencies**
   ```bash
   pip install -r requirements.txt
   ```


## ✅ Running Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

## 🦸 Creating the SuperUser

```bash
python manage.py createsuperuser
```

## 🏁 Running the Server

```bash
python manage.py runserver
```
