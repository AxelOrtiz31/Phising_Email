import web

from controllers.index import Index
from controllers.usuarioControlador.iniciar_sesion import IniciarSesion
from controllers.usuarioControlador.registro import Registro
from controllers.usuarioControlador.phishing import Phishing
from controllers.usuarioControlador.ejercicios import Ejercicios

# Rutas
urls = (
    '/', 'Index',
    '/usuarioContenido/iniciar_sesion', 'IniciarSesion',
    '/usuarioContenido/registro', 'Registro',
    '/usuarioContenido/phishing', 'Phishing',
    '/usuarioContenido/ejercicios', 'Ejercicios'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()