# buddySystem.py

# Ejecución:
# 	python3 buddySystem.py

# Estudiante: Keyber Sequera 16-11120

# Implementación de Buddy System en Python usando 
# árboles binarios:

# ----------------------------------------------------------------------------------
# Clase Nodo: representa las hojas o nodos de nuestro árbol
# binario que usaremos para implementar el buddy system:
class Nodo:
	tamanio = None
	padre = None
	hijoI = None
	hijoD = None
	valor = None

	# Se define un constructor donde se define 
	def __init__(self, tamanio=1):
		self.tamanio = tamanio

	# Retorna el nodo como una cadena de caracteres:
	def __str__(self):
		return "({}, {})".format(self.tamanio, self.valor)

# ----------------------------------------------------------------------------------
# Clase BuddySystem: se implementa buddy system para gestionar la memoria, la
# estructura usada es la del árbol binario:
class BuddySystem:

	tamanio = None
	raiz = None
	auxiliar = False
	estaObjeto = False # Se usa para verificar si un objeto está en memoria
	memoria = ""

	def __init__(self, tamanio):
		self.tamanio = 2**self.potenciaDeDosCercana(tamanio)
		self.raiz = Nodo(self.tamanio)

	# Se reserva una cantidad de memoria para albergar a los
	# datos identificados con un nombre:
	def reservar(self, cantidad, nombre):
		# Encontramos la potencia de dos más cercana que coincida
		# con la cantidad de memoria que se quiere reservar:
		espacioDeseado = 2**self.potenciaDeDosCercana(cantidad)
		# Verificamos que el objeto ya no esté en memoria:
		self.verificarSiEstaEnMemoria(self.raiz, nombre)
		# Si no está en memoria:
		if (self.estaObjeto == False and cantidad >= 1):
			# Buscamos si hay un espacio libre:
			self.buscarEspacioLibre(self.raiz, espacioDeseado, nombre)
		else:
			# Se vuelve a colocar la variable pivote en false:
			self.estaObjeto = False
		# Verificamos si se pudo o no insertar el objeto:
		if (self.auxiliar == True):
			self.auxiliar = False
			print("\nSe reservan {} espacios para '{}'".format(cantidad, nombre))
		else:
			print("\nNo es posible reservar {} espacios para '{}'".format(cantidad, nombre))

	# Buscar espacio libre, la variable auxiliar se usará para determinar
	# si ya se encontró o no un espacio libre:
	def buscarEspacioLibre(self, nodo, cantidad, nombre):
		# Comprobamos si el nodo puede albergar al objeto:
		self.comprobarNodo(nodo, cantidad, nombre)
		# Si el nodo no puede albergar al objeto y el tamaño del nodo
		# es mayor a la cantidad que se desea reservar se divide el nodo
		# en dos:
		if (self.auxiliar == False):
			# Doy prioridad a los nodos que ya estén divididos:
			if (nodo.hijoI != None and nodo.hijoI.valor == "memoria_dividida"):
				self.buscarEspacioLibre(nodo.hijoI, cantidad, nombre)
			if (self.auxiliar == False and nodo.hijoD != None and
				nodo.hijoD.valor == "memoria_dividida"):
				self.buscarEspacioLibre(nodo.hijoD, cantidad, nombre)
			# Si no se ha ubicado el objeto y el nodo tiene hijos:
			if (self.auxiliar == False and nodo.hijoI != None and nodo.hijoD != None
				and nodo.tamanio > cantidad):
				self.buscarEspacioLibre(nodo.hijoI, cantidad, nombre)
				if (self.auxiliar == False):
					self.buscarEspacioLibre(nodo.hijoD, cantidad, nombre)
			# Si no se ha ubicado el objeto y el nodo no tiene hijos:
			if (self.auxiliar == False and nodo.hijoI == None and nodo.hijoD == None and
				nodo.valor == None and nodo.tamanio > cantidad):
				# Creo las dos nuevas particiones:
				nodo.valor = "memoria_dividida"
				nodo.hijoI = Nodo(int(nodo.tamanio / 2))
				nodo.hijoI.padre = nodo
				nodo.hijoD = Nodo(int(nodo.tamanio / 2))
				nodo.hijoD.padre = nodo
				# Compruebo si el objeto cabe en el hijo izquierdo:
				self.buscarEspacioLibre(nodo.hijoI, cantidad, nombre)
				# Si el nodo no entró en el hijo izquierdo compruebo el hijo
				# derecho:
				if (self.auxiliar == False):
					self.buscarEspacioLibre(nodo.hijoD, cantidad, nombre)

	# Verifica si el nodo actual puede contener el espacio que se desea reservar:
	def comprobarNodo(self, nodo, cantidad, nombre):
		# Comprobamos que el nodo tenga el espacio suficiente y esté libre:
		if (nodo.tamanio == cantidad and nodo.valor == None):
			nodo.valor = nombre
			self.auxiliar = True

	# Verifica si el nodo ya está en memoria:
	def verificarSiEstaEnMemoria(self, nodo, nombre):
		# Verificamos que el objeto ya no haya sido encontrado:
		if (self.estaObjeto == False):
			# Verificamos si el nodo actual no contiene al objeto:
			if (nodo.valor == nombre):
				self.estaObjeto = True
			else:
				if (nodo.hijoI != None):
					self.verificarSiEstaEnMemoria(nodo.hijoI, nombre)
				if (self.estaObjeto == False and nodo.hijoD != None):
					self.verificarSiEstaEnMemoria(nodo.hijoD, nombre)

	# Se libera al objeto con identificador "nombre" de la memoria:
	def liberar(self, nombre):
		self.verificarSiEstaEnMemoria(self.raiz, nombre)
		# Se le dice al usuario si nombre no está en memoria:
		if (self.estaObjeto == False):
			print("\n'{}' no se puede liberar puesto que no está en memoria".format(nombre))
		else:
			self.liberarEspacio(self.raiz, nombre)
			self.auxiliar = False
			# Se comprueba si se pueden unir dos espacios de memoria contiguos:
			self.unir(self.raiz)
			# Se verifica que no hallan mas uniones por hacer:
			while (self.auxiliar == True):
				self.auxiliar = False
				self.unir(self.raiz)
			print("\nSe libera de la memoria el espacio ocupado por '{}'".format(nombre))
			self.estaObjeto = False

	# Se libera el espacio ocupado por un objeto:
	def liberarEspacio(self, nodo, nombre):
		# Verificamos que el objeto ya no haya sido liberado
		# usando la variable auxiliar que será True en caso 
		# de que haya sido liberado:
		if (self.auxiliar == False):
			# Verificamos si el nodo actual contiene al objeto:
			if (nodo.valor == nombre):
				nodo.valor = None
				self.auxiliar = True
			else:
				if (nodo.hijoI != None):
					self.liberarEspacio(nodo.hijoI, nombre)
				if (self.auxiliar == False and nodo.hijoD != None):
					self.liberarEspacio(nodo.hijoD, nombre)

	# Se unen los nodos que se puedan unir:
	def unir(self, nodo):
		# Verificamos que ya no se haya hecho una unión:
		if (self.auxiliar == False):
			# Verificamos si el nodo tiene hijos:
			if (nodo.hijoI != None and nodo.hijoD != None):
				# Verificamos si los nodos están libres:
				if (nodo.hijoI.valor == None and nodo.hijoD.valor == None):
					nodo.hijoI = None
					nodo.hijoD = None
					nodo.valor = None
					self.auxiliar = True
				# Si los nodos no están libres verificamos a sus hijos:
				if (self.auxiliar == False and nodo.hijoI != None):
					self.unir(nodo.hijoI)
				if (self.auxiliar == False and nodo.hijoD != None):
					self.unir(nodo.hijoD)

	# Retorna la potencia de dos más cercana a un número,
	# si el número es negativo se retorna 0, si el número
	# es 0 o 1 se retorna 0
	def potenciaDeDosCercana(self, numero):
		valorRetorno = 0
		if (numero <= 0):
			return 0
		else:
			for i in range(0, 100):
				if (numero <= 2**i and numero > 2**(i-1)):
					return i

	# Muestra cada espacio de la memoria uno tras otro:
	def imprimirMemoria(self, nodo):
		if (nodo.valor != "memoria_dividida"):
			print(nodo)
		else:
			if (nodo.hijoI != None):
				self.imprimirMemoria(nodo.hijoI)
			if (nodo.hijoD != None):
				self.imprimirMemoria(nodo.hijoD)

	def imprimir(self, nodo):
		if (nodo.valor != "memoria_dividida"):
			self.memoria += "{} ".format(nodo)
		else:
			if (nodo.hijoI != None):
				self.imprimir(nodo.hijoI)
			if (nodo.hijoD != None):
				self.imprimir(nodo.hijoD)

	def __str__(self):
		self.memoria = ""
		self.imprimir(self.raiz)
		return self.memoria

# ----------------------------------------------------------------------------------------------------------------
# Código para interactuar con el usuario:
seguir = True
valor = None
print("Bienvenido al sistema Buddy System:\n")
while seguir == True:
	try:
		memoria = BuddySystem(int(input("Indique la cantidad de memoria que desea reservar (por ejemplo: 10): ")))
		seguir = False
	except:
		seguir = True
seguir = True
accion = []
while seguir == True:
	print("\nLista de acciones permitidas:")
	print("RESERVAR <cantidad> <nombre> (Reserva espacio en memoria <cantidad> > 0)")
	print("LIBERAR <nombre> (Libera el espacio de memoria ocupado por <nombre>)")
	print("MOSTRAR (Muestra en pantalla el estado de la memoria)")
	print("SALIR (Termina la ejecución del simulador)")
	accion = input("\nUsted decide: ")
	accion = accion.split(" ")
	if (len(accion) >= 1):
		if (accion[0].lower() == "reservar"):
			try:
				memoria.reservar(int(accion[1]), accion[2])
			except:
				mensaje = "'"
				for i in range(0,len(accion)):
					if (i != len(accion) - 1):
						mensaje += "{} ".format(accion[i])
					else:
						mensaje += "{}'".format(accion[i])
				print("\n{} no es una acción válida.".format(mensaje))
		elif (accion[0].lower() == "liberar"):
			try:
				memoria.liberar(accion[1])
			except:
				mensaje = "'"
				for i in range(0,len(accion)):
					if (i != len(accion) - 1):
						mensaje += "{} ".format(accion[i])
					else:
						mensaje += "{}'".format(accion[i])
				print("\n{} no es una acción válida.".format(mensaje))
		elif (accion[0].lower() == "mostrar"):
			try:
				print("\nEstado de la memoria:\n\n{}".format(memoria))
			except:
				pass
		elif (accion[0].lower() == "salir"):
			seguir = False
		else:
			mensaje = "'"
			for i in range(0,len(accion)):
				if (i != len(accion) - 1):
					mensaje += "{} ".format(accion[i])
				else:
					mensaje += "{}'".format(accion[i])
			print("\n{} no es una acción válida.".format(mensaje))

print("\nFin del programa.")