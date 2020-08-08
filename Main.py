#importamos nuestra clase cliente
from src.client import Cliente
#inicializamos nuestro objeto
cliente = Cliente()
#nos autenticamos con autenticacion oauth 2.0
cliente.authenticate()
#obtenemos la lista de contactos
cliente.readList()

