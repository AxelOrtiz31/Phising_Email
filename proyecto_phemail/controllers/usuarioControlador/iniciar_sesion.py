import web
import os
from models.usuarios import Usuarios

BASE_URL = os.environ.get("BASE_URL", "https://solid-system-jjrj6wgpx9xj35549-8080.app.github.dev")

render = web.template.render("views", base="master")

# Página de Inicio de Sesion
class IniciarSesion:
    def GET(self):
        return render.usuarioContenido.iniciar_sesion(message=None)

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
            # Construir la URL con los datos
            url = f"{BASE_URL}/usuarioContenido/phishing?nombre={inicio_usuario['nombre']}&correo={inicio_usuario['correo']}"
            raise web.seeother(url)

        else:
            message = "Correo o contraseña incorrectos. Inténtalo de nuevo."
            return render.usuarioContenido.iniciar_sesion(message=message)  # Envía el mensaje de error a la plantilla
