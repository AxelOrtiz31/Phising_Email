import web
from models.usuarios import Usuarios

render = web.template.render("views", base="master")

#GET
class VerUsuario:
    def GET(self):

        # Instanciamos la clase Usuarios
        usuarios_modelo = Usuarios()
        resultado = usuarios_modelo.consultaUsuarios() # db.child("usuarios").get()

        # Si la consulta es exitosa, procesamos los datos
        usuarios_data = []
        if resultado["status"] == 200:
            resultGET = resultado["data"]

            # Recorremos cada registro obtenido
            for usuario in resultGET.each():
                llave_externa = cliente.key()  # ID de Firebase
                diccionarioVal = cliente.val() # Datos del usuario

                # Caso 1: Registros con ID directamente en la raíz
                if "nombre" in diccionarioVal:
                    clientes_data.append({
                        "clave": llave_externa,
                        "id": llave_externa,
                        "nombre": diccionarioVal.get("nombre"),
                        "correo": diccionarioVal.get("correo")
                    })
                else:
                    # Caso 2: Registros anidados con una clave externa
                    llave_numerica = next(iter(diccionarioVal))  # Extrae el primer elemento (ID numérica)
                    ln_diccionarioVal = diccionarioVal[llave_numerica]
                    clientes_data.append({
                        "clave": llave_externa,
                        "id": llave_numerica,
                        "nombre": ln_diccionarioVal.get("nombre"),
                        "correo": ln_diccionarioVal.get("correo")
                    })

        return render.clientes_Temp.lista_clientes()

# GET Individual
class BuscarCliente:
    def GET(self):
        # Al cargar la página, no se muestra ningún resultado.
        return render.clientes.buscar(busqueda_data=None, buscar_id="")

    def POST(self):
        datos = web.input()
        buscar_id = datos.get("id_busqueda")
        busqueda_data = []  # Creamos previamente una lista que contendra el registro

        # Obtenemos todos los registros
        clientes = db.child("clientes").get()
        if clientes.each() is not None:

            # Separamos llaves de valores
            for cliente in clientes.each():
                llave = cliente.key()
                valores = cliente.val()

                # Caso 1: Registros que inician con numeraciones
                if llave == buscar_id:
                    busqueda_data = {
                        "clave": llave,     # 001
                        "id": llave,        # 001
                        "nombre": valores.get("nombre"),
                        "correo": valores.get("correo")
                    }
                    break

                # Caso 2: Registros que inician con claves
                elif isinstance(valores, dict) and buscar_id in valores:
                    registro = valores[buscar_id]
                    busqueda_data = {
                        "clave": llave,      # -OIIq2ngVQJHYhOVkilq
                        "id": buscar_id,     # 001
                        "nombre": registro.get("nombre"),
                        "correo": registro.get("correo")
                    }
                    break

        return render.clientes.buscar(busqueda_data, buscar_id)