#importamos nuestra clase cliente
from src2.client import Cliente

#inicializamos nuestro objeto
cliente = Cliente()
#nos autenticacion con un metodo basico 
cliente.auth()
#creamos los usuarios con autenticacion basica
cliente.create(name="201408580 Carlos Andree Avalos Soto Basic Auth", catid=201408580, published = 1)
cliente.create(name="201408580 Contacto 1", catid=2014085801, published = 1)
cliente.create(name="201408580 Contacto 2", catid=2014085802, published = 1)
cliente.create(name="201408580 Contacto 3", catid=2014085803, published = 1)
cliente.create(name="201408580 Contacto 4", catid=2014085804, published = 1)
cliente.create(name="201408580 Contacto 5", catid=2014085805, published = 1)
cliente.create(name="201408580 Contacto 6", catid=2014085806, published = 1)
cliente.create(name="201408580 Contacto 7", catid=2014085807, published = 1)
cliente.create(name="201408580 Contacto 8", catid=2014085808, published = 1)
cliente.create(name="201408580 Contacto 9", catid=2014085809, published = 1)
#leemos la lista con el filtro para buscar por carnet
cliente.readList()
