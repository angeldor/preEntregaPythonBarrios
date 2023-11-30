#Base de datos de Universidad con Django

Este proyecto es una base de datos comtemplada en la pagina /admin de Django

##Características

- Se pueden agregar y eliminar Carreras, Estudiantes, y Cursos
- Se puede obtener una lista de los distintos tipos de Cursos, Estudiantes, Carreras y Matriculas
- Usa la interfaz por defecto de Django

##Tecnologías usadas

- Django
- Python
- HTML
- CSS

##Instalación

1. Instala las dependencias necesarias:
`pip install -r requirements.txt`
2. Crea una base de datos y configurala en el archivo settings.py.
3. Migra los datos de la base de datos:
`python manage.py migrate`
4. Crea un superusuario:
`python manage.py createsuperuser`
5. Inicia el servidor:
`python manage.py runserver`

##Uso
Para acceder al blog, abre tu navegador y navega a la siguiente URL:
`http://localhost:8000`

###Ejemplos
Para entrar a la pagina, ve a la siguiente URL:
`http://localhost:8000/admin/`



