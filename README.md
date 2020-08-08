# SA-Practica1
Practica No.1 de Software Avanzado
Practica No.2 de Software Avanzado

# Practica 1
Programa realizado para el laboratorio de Software Avanzado, tomando en cuenta los siguiente lineamientos
* Utilizar api.softwareavanzado.world para desarrollar un cliente de webservice: https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal&format=doc
* Listar contactos.
* Crear 10 contactos incluyendo su número de carnet en el nombre.

# Practica 2
## Parte 1
* Repetir la práctica # 1 agregando credenciales tipo client_credentials y un token Bearer para poder volver a desarrollar el mismo ejercicio anterior (ahora requiere autenticación).  Documentación de client credentials.

* Usuario / Client ID: sa
* Client Secret: fb5089840031449f1a4bf2c91c2bd2261d5b2f122bd8754ffe23be17b107b8eb103b441de3771745

## Parte 2:
* Repetir la misma tarea # 1 utilizando SOAP y autenticación básica.

* WSDL:   https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl 
* Usuario: sa
* Contraseña: usac

* Entregar ambas partes en distintas carpetas de una nueva rama del mismo repositorio de la práctica # 1 y seguir las reglas de entrega.


# Requisitos
* Python 3.8+

# Librerias
```
pip install zeep
```

# Ejecucion
* Para ejecutar la parte 1 de la practica 2
```
Python Main.py
```
* Para ejecutar la parte 2 de la practica 2
```
Python Main2.py
```

# Colaborador

* Carlos Andree Avalos Soto 201408580

# Referencias
* [Documentacion SOAP](https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal&format=doc#delete)
* [Zeep](https://docs.python-zeep.org/en/master/)
