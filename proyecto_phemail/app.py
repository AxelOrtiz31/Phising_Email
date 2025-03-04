import web

from controllers.index import Index
from controllers.usuarioControlador.iniciar_sesion import IniciarSesion

# Rutas
urls = (
    '/', 'Index',
    '/usuarioContenido/iniciar_sesion'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()