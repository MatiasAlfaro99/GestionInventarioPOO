# Sistema de Gestión de Inventarios

## 🚀 Descripción General
Este proyecto es un sistema integral de gestión de inventarios desarrollado con Django Rest Framework (DRF), que proporciona una API REST robusta para el manejo eficiente de inventarios, junto con un cliente Python implementado con Programación Orientada a Objetos (POO).

## ✨ Características
- **Backend**:
  - API REST completa construida con Django Rest Framework
  - Autenticación y autorización mediante tokens
  - Validación de datos y manejo de excepciones

- **Cliente Python**:
  - Clase de cliente para consumo de API REST
  - Métodos para realizar operaciones CRUD
  - Manejo de errores y excepciones
  - Implementación siguiendo principios de POO

## 🛠️ Tecnologías Utilizadas
- Python 3.13
- Django Rest Framework
- JWT para autenticación

## 📦 Instalación

### Requisitos Previos
- Python 3.9 o superior
- pip
- virtualenv (recomendado)

### Pasos de Instalación
1. Clonar el repositorio
git clone (https://github.com/MatiasAlfaro99/GestionInventarioPOO/)

2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate


3. Instalar dependencias

4. Configurar base de datos

python manage.py migrate
python manage.py createsuperuser

5. Ejecutar servidor de desarrollo
python manage.py runserver

## 🔐 Autenticación
La API utiliza autenticación basada en tokens JWT. Para obtener acceso:
1. Registrarse/Iniciar sesión
2. Obtener token de acceso

## 👥 Autores
Matías Alfaro Donoso y Dominique Inostroza

## 📞 Contacto
- Email: alfaromatias29@gmail.com
