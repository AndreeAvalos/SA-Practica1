import requests
import json

class Cliente():
    def __init__(self):
        #URL proporcionado con todos los servicios
        self.api = "https://api.softwareavanzado.world/index.php"
        self.url = self.api+"?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal"
        self.url_token = self.api+"?option=token&api=oauth2"
        #objeto tipo cliente referente a la libreria zeep
        self.headers = None

    def authenticate(self):
        data = {"grant_type": "client_credentials","client_id":"sa", "client_secret":"fb5089840031449f1a4bf2c91c2bd2261d5b2f122bd8754ffe23be17b107b8eb103b441de3771745"}
        request = requests.post(self.url_token, data = data)
        res = json.loads(request.text)
        token = 'Bearer {0}'.format(res["access_token"])
        self.headers = {
            'Authorization': token,
            'Content-Type': 'application/xml'
            }

    #Metodo para listar contactos referentes al servidor
    def readList(self):
        payload = '''<soap:Envelope xmlns:soap=\"http://www.w3.org/2003/05/soap-envelope\" 
                                    xmlns:adm=\"https://api.softwareavanzado.world/media/redcore/webservices/joomla/administrator.contact.1.0.0.wsdl\">\r\n   
                                    <soap:Header/>\r\n   
                                    <soap:Body>\r\n      
                                    <adm:readList>\r\n
                                    <filterSearch>201408580</filterSearch>\r\n\r\n   
                                    <limit>0</limit>\r\n\r\n   
                                    </adm:readList>\r\n   
                                    </soap:Body>\r\n</soap:Envelope>'''
        response = requests.request("GET", self.url, headers=self.headers, data = payload)
        result = json.loads(response.text)
        #recorremos el resultado para imprimirlo en consola
        for contact in result["_embedded"]["item"]:
            print("ID:", contact["id"],"Nombre:",contact["name"])