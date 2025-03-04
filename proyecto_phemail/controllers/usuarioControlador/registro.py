import web
from models.usuarios import Usuarios

render = web.template.render("views", base="master")

# Página de Registro
class Registro:
    def GET(self):
        return render.usuarioContenido.registro()

    def POST(self):
        datos = web.input()
        nombre_newUser = datos.get("nombre")
        email_newUser = datos.get("email")
        contrasena_newUser = datos.get("contrasena")
        
        # Detectamos el método
        if "metodo-push" in datos:
            metodo = "push"

        # Usamos la instancia del modelo para acceder a la DB
        usuarios_modelo = Usuarios()
        db = usuarios_modelo.db

        if metodo == "push":
            # Con push se inserta un objeto que tiene como clave la nueva ID
            datos_registro = {"nombre": nombre_newUser, "correo": email_newUser, "contrasena": contrasena_newUser}
            db.child("usuarios").push(datos_registro)

        return render.usuarioContenido.registro()
