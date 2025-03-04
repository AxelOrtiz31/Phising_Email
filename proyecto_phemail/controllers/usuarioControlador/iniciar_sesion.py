import web

render = web.template.render("views", base="master")

# Página de inicio
class IniciarSesion:
    def GET(self):
        return render.iniciar_sesion()