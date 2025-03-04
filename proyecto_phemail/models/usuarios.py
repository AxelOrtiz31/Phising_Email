import pyrebase

# Configuración de Firebase
config = {
    "apiKey": "AIzaSyCq6Okil_OTGuhmSmzRfrbqyDjcxh5Ndds",
    "authDomain": "prueba-bdnube.firebaseapp.com",
    "databaseURL": "https://prueba-bdnube-default-rtdb.firebaseio.com",    # No me hackeen :(
    "projectId": "phishing-bd",
    "storageBucket": "phishing-bd.firebasestorage.app",
    "messagingSenderId": "1069261453435",
    "appId": "1:1069261453435:web:574d9aebd678dc900fcade",
    "measurementId": "G-N8FR9LNN56"
}

# Inicializamos Firebase y la base de datos
firebase = pyrebase.initialize_app(config)
db = firebase.database()

class Usuarios:
    def __init__(self):
        self.db = db  # Usamos una única instancia

    def consultaUsuarios(self):
        try:
            # Verifica si la conexión a la BD es correcta
            if self.db:
                usuarios = self.db.child("usuarios").get()
                if usuarios.val():
                    return {
                        "status": 200,
                        "message": "Consulta exitosa",
                        "data": usuarios
                    }
                elif usuarios.val() is None:
                    return {
                        "status": 204,
                        "message": "No hay registros en 'usuarios'"
                    }
                elif usuarios is None:
                    return {
                        "status": 400,
                        "message": "No se encontro 'usuarios' en Firebase"
                    }
        
        except Exception as e:
            return {
                "status": 500,
                "message": "Error del servidor -> Firebase",
                "error": str(e)
            }

''' Ejemplo de prueba (opcional)
if __name__ == '__main__':
    clientes_inst = Clientes()
    resultado = clientes_inst.consultaClientes()
    print(resultado)
'''