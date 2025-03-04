import web
from models.usuarios import Usuarios

render = web.template.render("views", base="master")

# Página de Phishing
class Phishing:
    def GET(self):
        datos = web.input()
        nombre = datos.get("nombre", "Invitado")
        correo = datos.get("correo", "")
        return render.usuarioContenido.phishing(nombre, correo)
