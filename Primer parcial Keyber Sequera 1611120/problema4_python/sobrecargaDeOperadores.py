# sobrecargaDeOperadores.py

# Ejecución:
# 	python3 sobrecargaDeOperadores.py

# Estudiante: Keyber Sequera 16-11120

# Se busca sobrecargar algunos operadores binarios de python 
# con el objeto de que operen de manera más natural con objetos
# del tipo vector de tres dimensiones:

from math import sqrt

# -----------------------------------------------------------------
# Se define la clase vector de tres dimensiones:
class Vector:
	
	i = 0
	j = 0
	k = 0

	# Constructor que puede recibir entre 0 o 3 parámetros:
	def __init__(self, a=0, b=0, c=0):
		self.i = a
		self.j = b
		self.k = c

	# Se modifica la coordenada i (primer elemento del vector), 
	# la coordenada j (segundo elemento del vector) o la coordenada
	# k (tercer elemento del vector):
	def modificarCoordenada(coordenada, valor):
		if coordenada == "i":
			self.i = valor
		elif coordenada == "j":
			self.j = valor
		elif coordenada == "k":
			self.k = valor
		else:
			pass

	# Se sobrecarga el operador + para trabajar con suma de vectores
	# con vectores o con números:
	def __add__(self, vector):
		try:
			return Vector(self.i + vector.i, self.j + vector.j, self.k + vector.k)
		except:
			return Vector(self.i + vector, self.j + vector, self.k + vector)

	# Se sobrecarga el operador - para trabajar con resta de vectores
	# con vectores o con números:
	def __sub__(self, vector):
		try:
			return Vector(self.i - vector.i, self.j - vector.j, self.k - vector.k)
		except:
			return Vector(self.i - vector, self.j - vector, self.k - vector)

	# Se sobrecarga el operador * para trabajar con 
	# producto cruz de vectores con vectores o con números:
	def __mul__(self, vector):
		try:
			return Vector(self.j * vector.k - self.k * vector.j, 
						  -(self.i * vector.k - self.k * vector.i), 
						  self.i * vector.j - self.j * vector.i)
		except:
			return Vector(self.i * vector, self.j * vector, self.k * vector)

	# Se sobrecarga el operador % para trabajar con 
	# producto escalar de vectores:
	def __mod__(self, vector):
		return Vector(self.i * vector.i + self.j + vector.j + self.k * vector.k)

	# Se sobrecarga el operador ~ para trabajar con la norma de
	# un vector, no se usará el operador & porque en python ese
	# operador recibe dos parámetros, es un operador binario, en
	# cambio ~ es un operador unario y si puede ser usado:
	def __invert__(self):
		return sqrt((self.i)**2 + (self.j)**2 + (self.k)**2)


	# Se obtiene una representación como string del vector:
	def __str__(self):
		return "[{}, {}, {}]".format(self.i, self.j, self.k)

# -----------------------------------------------------------------------------
# Se crean tres vectores de prueba para probar el correcto funcionamiento
# de la sobrecarga de operadores:
a = Vector(1, 4, 3)
b = Vector(4, 0, -3)
c = Vector(1, 2, 3)

# Probamos las operaciones sugeridas en el enunciado del examen:

print("Prueba de funcionamiento de los operadores (Se usa ~ en lugar de &):")
print("\nb + c = {}".format(b + c))
print("\na * b + c = {}".format(a * b + c))
print("\n(b + b) * (c - a) = {}".format((b + b) * (c - a)))
print("\na % (c * b) = {}".format(a % (c * b)))
print("\nb + 3 = {}".format(b + 3))
print("\na * 3.0 + ~b = {}".format(a * 3.0 + ~b))
print("\n(b + b) * (c %  a) = {}".format((b + b) * (c %  a)))