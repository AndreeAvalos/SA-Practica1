''' Importamos la libreria zeep la cual nos brindara soporte 
    para poder usar peticiones SOAP '''
from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth

class Cliente():
    def __init__(self):
        #URL proporcionado con todos los servicios
        self.url = "https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl"
        #objeto tipo cliente referente a la libreria zeep
        self.client = None
    
    #Metodo de autenticacion basica
    def auth(self):
        #creamos una session parte de la libreria reques
        session = Session()
        #nos autenticamos con nuestras credenciales
        session.auth = HTTPBasicAuth("sa","usac")
        #instanciamos el cliente con nuestras credenciales
        self.client = Client(self.url, transport= Transport(session=session))

    #Metodo utilizado para crear contacto 
    def create(self,name="default",catid = 1, published = 1):
        '''Name:string(obligatorio), catid:int(opcional), published:int(opcional)'''
        #peticion para crear un contacto en el servidor SOAP
        self.client.service.create(name= name, catid=catid, published=published)


    #Metodo para listar contactos referentes al servidor
    def readList(self):
        #peticion al servicion readlList en el servidor SOAP
        result = self.client.service.readList(filterSearch="201408580")
        #recorremos el resultado para imprimirlo en consola
        for contact in result:
            print("ID:", contact["id"],"Nombre:",contact["name"])