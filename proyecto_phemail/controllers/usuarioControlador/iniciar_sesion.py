import web
from models.usuarios import Usuarios

render = web.template.render("views", base="master")

# Página de Inicio de Sesion
class IniciarSesion:
    def GET(self):
        return render.usuarioContenido.iniciar_sesion()

    def POST(self):
        datos = web.input()
        email_User = datos.get("email")
        contrasena_User = datos.get("contrasena")

        # Usamos la instancia del modelo para acceder a la DB
        usuarios_modelo = Usuarios()
        db = usuarios_modelo.db

        inicio_usuario = {}  # Creamos previamente una lista que contendra el registro

        # Obtenemos todos los registros
        usuarios = db.child("usuarios").get()
        if usuarios.each() is not None:

            # Separamos llaves de valores
            for usuario in usuarios.each():
                llave = usuario.key()
                valores = usuario.val()

                if isinstance(valores, dict) and valores.get("correo") == email_User and valores.get("contrasena") == contrasena_User:
                        inicio_usuario = {
                            "id": llave,      # -OIIq2ngVQJHYhOVkilq
                            "nombre": valores.get("nombre"),
                            "correo": valores.get("correo")
                        }
                        break

        if inicio_usuario:
            session.logged_user = inicio_usuario  # Guarda los datos en la sesión
            raise web.seeother("/phishing")
