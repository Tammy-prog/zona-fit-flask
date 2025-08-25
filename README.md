# Zona Fit (GYM) - Aplicación web con Flask

## Descripción
Aplicación web para la gestión de clientes de un gimnasio. Permite:
- Agregar nuevos clientes
- Editar clientes existentes
- Eliminar clientes
- Listar todos los clientes

La aplicación utiliza Flask como framework web, MySQL como base de datos y Bootstrap 5 para el diseño responsivo.

## Tecnologías utilizadas
- Python 3.13
- Flask
- Flask-WTF
- MySQL
- SQLAlchemy
- Bootstrap 5
- Visual Studio Code

## Instalación y ejecución
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Tammy-prog/zona-fit-flask.git
   cd zona-fit-flask
2. Crear un entorno virtual:
   python -m venv venv
3. Activar el entorno virtual:
   venv\Scripts\activate
4. Instalar dependencias:
   pip install -r requirements.txt
5. Ejecutar la aplicación:
   python app.py
Abrir en el navegador:
   http://localhost:5000/
   
Estructura del proyecto
├── app.py
├── cliente.py
├── clienteDAO.py
├── cliente_forma.py
├── conexion.py
├── templates/
│   └── index.html
├── static/
│   └── (CSS, JS, imágenes)
├── venv/
├── .gitignore
└── README.md
Licencia
Este proyecto es de libre uso educativo.

