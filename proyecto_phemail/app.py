import web

from controllers.index import Index
from controllers.usuarioControlador.iniciar_sesion import IniciarSesion
from controllers.usuarioControlador.registro import Registro
from controllers.usuarioControlador.phishing import Phishing

# Rutas
urls = (
    '/', 'Index',
    '/usuarioContenido/iniciar_sesion', 'IniciarSesion',
    '/usuarioContenido/registro', 'Registro',
    '/usuarioContenido/phishing', 'Phishing'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'logged_user': None})

if __name__ == "__main__":
    app.run()