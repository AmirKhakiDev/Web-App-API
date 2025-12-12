# Web-App-API

A **Backend / REST API service** built with Django, providing user
authentication, file upload and management, profile viewing, and
file-sharing features. This backend is part of a web application
project.

## Table of Contents

-   [Overview](#overview)
-   [Features](#features)
-   [Technology Stack](#technology-stack)
-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [Environment Configuration](#environment-configuration)
-   [Running the Server](#running-the-server)
-   [API Endpoints](#api-endpoints)
-   [Example Requests](#example-requests)
-   [Project Structure](#project-structure)
-   [Testing](#testing)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)

## Overview

**Web-App-API** is the backend component of a Django-based web
application.\
It implements essential user functionalities such as registration,
login, file handling, and profile management.\
All services are exposed through a clean RESTful API suitable for
frontend clients or external integrations.

## Features

### Core Capabilities

-   User registration and authentication
-   Session/token-based login
-   File upload
-   File download
-   Viewing user's own uploaded files
-   Viewing other users' profiles
-   Sharing files with other users
-   Viewing shared files

## Technology Stack

-   Python\
-   Django\
-   Django REST Framework\
-   HTML, CSS, JavaScript\
-   Bootstrap

## Prerequisites

-   Python 3.8+\
-   pip\
-   virtualenv (optional)

## Installation

### Clone the repository

``` bash
git clone https://github.com/AmirKhakiDev/Web-App-API.git
cd Web-App-API
```

### Create and activate a virtual environment

``` bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate  # macOS / Linux
```

### Install dependencies

``` bash
pip install -r requirements.txt
```

### Apply migrations

``` bash
python django_web_app/manage.py makemigrations
python django_web_app/manage.py migrate
```

## Environment Configuration

Create a `.env` file:

    SECRET_KEY=your_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

## Running the Server

``` bash
python django_web_app/manage.py runserver
```

## API Endpoints

### Authentication

  Method   Endpoint         Description
  -------- ---------------- -------------------
  POST     /api/register/   Register new user
  POST     /api/login/      Login user
  POST     /api/logout/     Logout

### Files

  Method   Endpoint                             Description
  -------- ------------------------------------ -----------------
  GET      /api/files/                          List user files
  POST     /api/files/upload/                   Upload a file
  GET      /api/files/`<id>`{=html}/download/   Download file

### Profiles

  Method   Endpoint                                  Description
  -------- ----------------------------------------- --------------
  GET      /api/users/`<username>`{=html}/profile/   View profile
  POST     /api/users/`<username>`{=html}/share/     Share a file

## Example Requests

### Register

``` bash
curl -X POST http://localhost:8000/api/register/ -H "Content-Type: application/json" -d '{"username":"alice","password":"pass123"}'
```

### Login

``` bash
curl -X POST http://localhost:8000/api/login/ -H "Content-Type: application/json" -d '{"username":"alice","password":"pass123"}'
```

## Project Structure

    Web-App-API/
    ├── django_web_app/
    │   ├── app/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── requirements.txt
    ├── README.md
    └── test.py

## Testing

``` bash
python django_web_app/manage.py test
```

## Contributing

1.  Fork the repo\
2.  Create a branch\
3.  Commit changes\
4.  Create a Pull Request

## License

MIT License.

## Contact

Maintained by **AmirKhakiDev**.
