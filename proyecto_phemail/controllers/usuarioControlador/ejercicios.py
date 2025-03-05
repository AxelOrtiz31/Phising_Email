import web
from models.usuarios import Usuarios

render = web.template.render("views", base="master")

# Página de Ejercicios
class Ejercicios:
    def GET(self):
        return render.usuarioContenido.ejercicios()