import os


#SECCION DE ALMACENAJE
numeros = []
palabras_clave = []
palabras = []
cadenas = []
palabras_definitivas = []
nombre_del_archivo = 'diccionario'

#SECCION INTERACTIVA

def capturing_data():

	continuar = True
	while continuar != False:
		answer = input('INTRODUZCA LA SIGUIENTE PALABRA (introduce q para salir) -> ')

		if answer != 'q':
			palabras.append(answer)
		else:
			continuar = False


	continuar = True
	while continuar != False:
		answer = input('INTRODUZCA EL SIGUIENTE NUMERO (introduce q para salir) -> ')

		if answer != 'q':
			numeros.append(answer)
		else:
			continuar = False


#VOLCADO DE INFORMACION

def entrevista():

	print('-------------------------- DESTROYER-------------------------------\n')

	global nombre_del_archivo
	nombre_del_archivo = str(input('INTRODUZCA NOMBRE DEL DICCIONARIO A CREAR - > '))

	nombre = input('NOMBRE DEL SUJETO - > Pulsa 1 para nombre simple o pulsa 2 para nombre compuesto: ')
	if nombre == '1':
		nombre = input('NOMBRE DEL SUJETO - > ')
		palabras_clave.append(nombre.lower())
		palabras_clave.append(nombre[0])
		palabras_clave.append(nombre[0].upper() + nombre[0:])
		palabras_clave.append(nombre[:2])
	if nombre == '2':
		nombre = input('NOMBRE DEL SUJETO 1 - > ')
		palabras_clave.append(nombre.lower())
		palabras_clave.append(nombre[0])
		palabras_clave.append(nombre[0].upper() + nombre[0:])
		palabras_clave.append(nombre[:2])
		nombre2 = input('NOMBRE DEL SUJETO 2- > ')
		palabras_clave.append(nombre2.lower())
		palabras_clave.append(nombre2[0])
		palabras_clave.append(nombre2[0].upper() + nombre[0:])
		palabras_clave.append(nombre2[:2])


	apellido1 = input('APELLIDO 1 DEL SUJETO - > ')
	palabras_clave.append(apellido1.lower())
	palabras_clave.append(apellido1[0])
	palabras_clave.append(apellido1[0].upper() + nombre[0:])
	palabras_clave.append(apellido1[:2])

	apellido2 = input('APELLIDO 2 DEL SUJETO - > ')
	palabras_clave.append(apellido2.lower())
	palabras_clave.append(apellido2[0])
	palabras_clave.append(apellido2[0].upper() + nombre[0:])
	palabras_clave.append(apellido2[:2])

	fecha_de_nacimiento = input('FECHA DE NACIMINETO DEL SUJETO (XXYYZZZZ)- > ')
	numeros.append(fecha_de_nacimiento[0:2])
	numeros.append(fecha_de_nacimiento[2:4])
	numeros.append(fecha_de_nacimiento[4:])
	numeros.append(fecha_de_nacimiento[6:])
	numeros.append(fecha_de_nacimiento)

	trabajo = input('LUGAR DE TRABAJO - > ')
	palabras_clave.append(trabajo.lower())

	ciudad_de_origen = input('CIUDAD DE ORIGEN DEL SUJETO - > ')
	palabras_clave.append(ciudad_de_origen.lower())

	mascota = input('MASCOTA DEL SUJETO - > ')
	palabras_clave.append(mascota.lower())

	nombre_de_pareja = input('NOMBRE DE PAREJA DEL SUJETO - > ')
	palabras_clave.append(nombre_de_pareja.lower())
	palabras_clave.append(nombre_de_pareja[0])
	palabras_clave.append(nombre_de_pareja[:2])

	fecha_de_pareja = input('FECHA DE UNION DE PAREJA CON SUJETO - > ')
	numeros.append(fecha_de_pareja)

	hijos = input('TIENE HIJOS? (1 -SI 2 -NO) -> ')
	if hijos == '1':
		numero_de_hijos = input('CUANTOS HIJOS TIENE (1, 2, 3)-> ')
		for num in range(int(numero_de_hijos)):
			nombre_de_hijo = input('NOMBRE DEL HIJO/A ' + str(num) +  'DEL SUJETO - > ')
			palabras_clave.append(nombre_de_hijo.lower())
			palabras_clave.append(nombre_de_hijo[0:2])
			palabras_clave.append(nombre_de_hijo[0])

	dni = input('DNI DEL SUJETO - > ')
	numeros.append(dni)
	numeros.append(dni[:0])

	telefono = input('TELEFONO DEL SUJETO - > ')
	numeros.append(telefono)
	numeros.append(telefono[:2])
	numeros.append(telefono[:5])
	numeros.append(telefono[7:])

	correo = input('CORREO ELECTRONICO DEL SUJETO (SIN DOMINIO) - > ')
	palabras_clave.append(correo.lower())

	capturing_data()

#PROCESAMIENTO DE LA INFORMACION


def procesamiento():

	rock = open('numbers.txt').readlines()
	count = 0
	for num in rock:
		if count < 10000:
			cadenas.append(num[:-1])
			count += 1

	for primera_palabra in palabras_clave:
		palabras_definitivas.append(primera_palabra)
		for segunda_palabra in palabras_clave:
			palabras_definitivas.append(primera_palabra + segunda_palabra)
			for tercera_palabra in palabras_clave:
				palabras_definitivas.append(primera_palabra + segunda_palabra + tercera_palabra)
				for cuarta_palabra in palabras_clave:
					palabras_definitivas.append(primera_palabra + segunda_palabra + tercera_palabra + cuarta_palabra)


	for palabra in palabras:
		palabras_definitivas.append(palabra)

	dicc = open(nombre_del_archivo, 'w')

	for numero in numeros:
		dicc.write(numero + '\n')

	for palabra in palabras_definitivas:
		dicc.write(palabra+ '\n')

	for palabra in palabras_definitivas:
		for numero in numeros:
			dicc.write(palabra + numero + '\n')
			dicc.write(numero + palabra + '\n')

	for palabra in palabras_clave:
		for cadena in cadenas:
			dicc.write(palabra + cadena + '\n')
			dicc.write(cadena + palabra + '\n')



	dicc.close()

	print('\nEL DICCIONARIO SE HA CREADO CORRECTAMENTE - > ' + os.getcwd() + '/' + nombre_del_archivo + '\n')


if __name__ == '__main__':
	entrevista()
	procesamiento()






