# Generador de Correos Electrónicos

Este proyecto permite generar un correo electrónico personalizado basado en el nombre y apellido de un usuario. Es una herramienta sencilla que muestra cómo crear una dirección de correo utilizando información proporcionada por el usuario.

## Descripción

El programa solicita al usuario su nombre y apellido, y luego genera un correo electrónico de la siguiente forma:

```
nombre.apellido@ciudadgotica.com
```

El correo generado se muestra al usuario junto con un mensaje de felicitaciones.

## Características

- Generación automática de correos electrónicos personalizados.
- Utiliza el formato de nombre y apellido del usuario para crear la dirección de email.
- Mensaje de felicitaciones al final del proceso.

## Instalación

Este proyecto no requiere ninguna instalación adicional, ya que está escrito en Python y puede ejecutarse directamente desde un archivo `.py`. Solo necesitas tener Python 3 instalado en tu sistema.

1. Clona este repositorio:
    ```bash
    git clone https://github.com/rumindvisuals-dev/generador-de-correos.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd generador-de-correos
    ```

3. Ejecuta el script:
    ```bash
    python main.py
    ```

## Uso

Cuando ejecutes el script, se te pedirá que ingreses tu nombre y apellido. El sistema generará un correo electrónico con el siguiente formato: `nombre.apellido@ciudadgotica.com`.

### Ejemplo de ejecución:

```
Cual es tu nombre?: Juan
Cual es tu apellido?: Pérez

Tu nuevo email generado por el sistema es:

juan.perez@ciudadgotica.com

*** Felicidades ***
```

# Contribuciones
Si deseas contribuir a este proyecto, no dudes en hacer un fork del repositorio y enviar tus pull requests. Asegúrate de seguir las buenas prácticas de codificación y agregar pruebas si es necesario.
