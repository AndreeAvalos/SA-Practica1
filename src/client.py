''' Importamos la libreria zeep la cual nos brindara soporte 
    para poder usar peticiones SOAP '''
from zeep import Client
import requests
import json

class Cliente():
    def __init__(self):
        #URL proporcionado con todos los servicios
        self.api = "https://api.softwareavanzado.world/index.php"
        self.url = self.api+ "?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl"
        self.url_token = self.api+"?option=token&api=oauth2"
        #objeto tipo cliente referente a la libreria zeep
        self.client = None

    def getToken(self):
        data = {"grant_type": "client_credentials","client_id":"sa", "client_secret":"fb5089840031449f1a4bf2c91c2bd2261d5b2f122bd8754ffe23be17b107b8eb103b441de3771745"}
        request = requests.post(self.url_token, data = data)
        res = json.loads(request.text)
        return res["token_type"] + " " + res["access_token"] 


    def authenticate(self, token = None, username = None, password = None):
        Client(self.url)


    #Metodo utilizado para crear contacto 
    def create(self,name="default",catid = 1, published = 1):
        '''Name:string(obligatorio), catid:int(opcional), published:int(opcional)'''
        #peticion para crear un contacto en el servidor SOAP
        self.client.service.create(name= name, catid=catid, published=published)


    #Metodo para listar contactos referentes al servidor
    def readList(self):
        #peticion al servicion readlList en el servidor SOAP
        result = self.client.service.readList()
        #recorremos el resultado para imprimirlo en consola
        for contact in result:
            print("ID:", contact["id"],"Nombre:",contact["name"])