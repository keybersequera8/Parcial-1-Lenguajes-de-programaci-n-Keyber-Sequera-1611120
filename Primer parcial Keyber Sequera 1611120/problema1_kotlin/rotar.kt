// rotar.kt

// Ejecución:
// 		kotlinc -include-runtime rotar.kt -d rotar.jar
// 		java -jar rotar.jar

// Estudiante: Keyber Sequera 16-11120

// Se implementa una función que rota palabras de acuerdo a las
// especificaciones señaladas en el enunciado del examen 1.

import kotlin.math.abs

// Función que rota una palabra la cantidad de posiciones que
// se desee:

fun rotar(palabra: String, valorRotacion: Int) : String {
	var palabraRotada : MutableList<Char> = mutableListOf()
	var palabraRetorno: String = ""
	val n: Int= palabra.length
	// Creamos una lista con un espacio por caracter de la palabra de interés:
	for (i in 0..palabra.length-1) {
		palabraRotada.add('0')
	}
	// Obtenemos los elementos de la palabra rotada en una lista:
	for (i in 0..palabra.length-1) {
		palabraRotada[abs(i + n - (valorRotacion % n)) % n] = palabra[i]
	}
	// Pasamos los elementos de la lista a un string:
	for (i in 0..palabra.length-1) {
		palabraRetorno += palabraRotada[i]
	}
	return palabraRetorno
}

// Se crea una pequeña prueba para demostrar el correcto
// funcionamiento de la función:
fun main() {
	val palabra : String = "hola"
	println("Palabra que se rotará: \"$palabra\"")
	println("rotar(\"$palabra\", 0) = \"${rotar(palabra, 0)}\"")
	println("rotar(\"$palabra\", 1) = \"${rotar(palabra, 1)}\"")
	println("rotar(\"$palabra\", 2) = \"${rotar(palabra, 2)}\"")
	println("rotar(\"$palabra\", 3) = \"${rotar(palabra, 3)}\"")
	println("rotar(\"$palabra\", 4) = \"${rotar(palabra, 4)}\"")
	println("rotar(\"$palabra\", 5) = \"${rotar(palabra, 5)}\"")
}