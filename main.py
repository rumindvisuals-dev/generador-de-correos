# Generador de Correos Electrónicos

name = input('Cual es tu nombre?: ')
lastname = input('Cual es tu apellido?: ')
email = f'{name.lower()}.{lastname.lower()}@ciudadgotica.com'

message = f'''
Tu nuevo email generado por el sistema es:

{email}

*** Felicidades ***
'''

print(message)
