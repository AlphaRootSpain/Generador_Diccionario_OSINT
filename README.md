# Generador_Diccionario_OSINT

Script en Python para la generacion de diccionarios en base a informacion de fuentes abiertas del objetivo para posteriormente pasar a la fase de crackeo. Tras un estudio a una base de datos de contraseñas en Pastebin se comprobo la tendencia a  usar datos personales seguidos de un numero o fecha facil de recordar al establecer las contraseñas de usuario. Por ello, el procesamiento se basa en pequeñas permutaciones de los datos obtenidos y la introduccion de un numero al final del string -obtenidos del famoso diccionario rockyou-.

El codigo se ejecuta de forma intercativa:

  - Ejecutar diccionario_osint.py
  - Realizar el volcado de datos obtenidos
  - Generacion del diccionario
