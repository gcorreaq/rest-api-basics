# rest-api-basics

Construcción de una API REST (Representational state transfer) con [Python 3.9](https://docs.python.org/3/) y [Flask](https://flask.palletsprojects.com/en/1.1.x/) para aprender los conceptos básicos de REST. Todos los Domingos a las 15:00 hora del Pácifico en [twitch.tv/gonchimon](https://twitch.tv/gonchimon). ([Ver en tu hora local](https://www.timeanddate.com/worldclock/converter.html?iso=20201213T230000&p1=388))

La documentación (incluyendo en el código) será en español, pero el código en si estará en inglés.

Si tienes dudas/consultas/sugerencias, puedes crear un nuevo Issue o Pull Request.

# Objetivos

- Construir una API REST que nos permita la creación y manejo de eventos, con invitados y sus respectivas reservaciones.
- Usar Python 3.9 y Flask.
- Los datos no serán persistidos, todo se almacenará en memoria.
- No usaremos autenticación o autorización. El objetivo principal es aprender de REST, no como construir una API lista para producción.

# Definiciones de nuestro sistema

## Entidades

Las entidades en nuestro sistema serán

- Eventos
- Invitados
- Reservaciones

Estos serán los recursos que expondremos en nuestra API REST.

## Operaciones soportadas

La siguiente tabla muestra el tipo de operaciones que vamos a soportar para cada entidad. Usaremos el acrónimo CRUD (Create, Read, Update, Delete; Crear, Leer, Actualizar, Borrar) para listar las operaciones básicas que queremos soportar.

Elemento | Recurso (1) | Crear | Leer | Actualizar | Borrar
---------|---------|-------|------|------------|-------
Eventos | Events | X | X | X | X
Invitados | Guests | X | X | X | X
Reservaciones | Reservations | | X | X | 

(1): El nombre del recurso en nuestra API

# Material adicional (en inglés)

- Documentación de Python 3.9: https://docs.python.org/3/
- Documentación de Flask: https://flask.palletsprojects.com/en/1.1.x/
- Conceptos sobre REST: https://restfulapi.net/