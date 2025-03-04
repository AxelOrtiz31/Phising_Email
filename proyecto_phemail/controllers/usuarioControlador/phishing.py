import web
from models.usuarios import Usuarios

render = web.template.render("views", base="master")

# Página de Phishing
class Phishing:
    def GET(self):

        if session.logged_user is None:
            raise web.seeother("/iniciar_sesion")
        
        nombre = session.logged_user.get("nombre", "Invitado")
        correo = session.logged_user.get("correo", "")

        return render.usuarioContenido.phishing(nombre, correo)