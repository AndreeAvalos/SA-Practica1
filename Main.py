#importamos nuestra clase cliente
from src.client import Cliente

#inicializamos nuestro objeto
cliente = Cliente()
auth = cliente.getToken()


'''#creamos los contactos
cliente.create(name="Carlos Andree Avalos Soto", catid=201408580, published = 1)
cliente.create(name="201408580 Contacto 1", catid=2014085801, published = 1)
cliente.create(name="201408580 Contacto 2", catid=2014085802, published = 1)
cliente.create(name="201408580 Contacto 3", catid=2014085803, published = 1)
cliente.create(name="201408580 Contacto 4", catid=2014085804, published = 1)
cliente.create(name="201408580 Contacto 5", catid=2014085805, published = 1)
cliente.create(name="201408580 Contacto 6", catid=2014085806, published = 1)
cliente.create(name="201408580 Contacto 7", catid=2014085807, published = 1)
cliente.create(name="201408580 Contacto 8", catid=2014085808, published = 1)
cliente.create(name="201408580 Contacto 9", catid=2014085809, published = 1)
#listamos todos los contactos con nuestro cliente en el servidor SOAP
cliente.readList()'''
