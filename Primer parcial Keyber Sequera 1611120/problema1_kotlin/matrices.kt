// matrices.kt

// Ejecución:
// 		kotlinc -include-runtime matrices.kt -d matrices.jar
// 		java -jar matrices.jar

// Estudiante: Keyber Sequera 16-11120

// Se implementa una clase que permite manipular de manera sencilla
// objetos del tipo matrices y las operaciones solicitadas para las
// mismas:

// Clase matriz:
class Matriz {

	var m : MutableList<MutableList<Int>> = mutableListOf()
	var numFilas : Int = 0;
	var numColumnas : Int = 0;

	// Se declara una matriz de ceros con (filas)x(columnas):
	constructor(filas: Int, columnas: Int ) {
		numFilas = filas
		numColumnas = columnas
		for (i in 0..filas-1) {
			m.add(mutableListOf())
			for (j in 0..columnas-1) {
				m[i].add(0)
			}
		}
	}

	// Se declara una matriz recibiendo los valores que tendrá
	// cada fila, si la matriz no es válida se creará una matriz 
	// vacía:
	constructor(vararg filas: MutableList<Int>) {
		for (fila in filas) {
			this.m.add(fila)
		}
		this.numFilas = m.size
		if (this.numFilas != 0) {
			this.numColumnas = m[0].size
		} else {
			this.numColumnas = 0
			this.numFilas = 0
		}
		if (this.verificarValidez() == false) {
			this.m = mutableListOf()
			this.numFilas = 0
			this.numColumnas = 0
		}
	}

	// Retorna la matriz traspuesta de la matriz actual
	// en caso de que la matriz no sea válida se devuelve
	// una matriz de dimensiones 0x0:
	fun calcularTraspuesta() : Matriz {
		var matrizRetorno : Matriz = Matriz()
		// Verificamos que la matriz tenga la misma
		// cantidad de columnas en todas sus filas:
		if (this.verificarValidez() == true) {
			matrizRetorno = Matriz(this.numColumnas, this.numFilas)
			for (i in 0..this.numFilas-1) {
				for (j in 0..this.numColumnas-1) {
					matrizRetorno.m[j][i] = this.m[i][j]
				}
			}
		}
		return matrizRetorno
	}

	// Multiplica la matriz actual con la matriz B, siempre y cuando
	// el número de columnas de la matriz actual sea el mismo que de filas
	// de la B,  si no se puede realizar la multiplicación se devuelve
	// una matriz con dimensiones 0x0:
	fun multiplicarConMatriz(matriz : Matriz) : Matriz {
		var matrizRetorno : Matriz = Matriz()
		if (this.verificarValidez() == true && matriz.verificarValidez() == true &&
			this.numColumnas == matriz.numFilas) {
			matrizRetorno = Matriz(this.numFilas, matriz.numColumnas)
			for (i in 0..this.numFilas-1) {
				for (j in 0..matriz.numColumnas-1) {
					for (k in 0..matriz.numFilas-1) {
						matrizRetorno.m[i][j] += this.m[i][k] * matriz.m[k][j]
					}
				}
			}
		}
		return matrizRetorno
	}


	// Se añade una fila nueva en la fila i:
	fun agregarFila(fila : Int, contenido : MutableList<Int>) {
		if (this.verificarValidez() && contenido.size == this.numColumnas && 
			fila < this.numFilas && fila >= 0) {
			this.m[fila] = contenido
		}
	}

	// Se verifica si la matriz es válida, es decir, tiene
	// la misma cantidad de columnas en cada una de sus filas:
	fun verificarValidez() : Boolean {
		var valorRetorno : Boolean = true
		var filas : Int = 0
		var columnas : Int = 0

		if (this.numFilas != 0 && this.numColumnas != 0) {
			for (fila in m) {
				filas += 1
				for (elemento in fila) {
					columnas += 1
				}
				if (this.numColumnas != columnas) {
					valorRetorno = false
					break
				}
				columnas = 0
			}
			if (filas != this.numFilas) {
				valorRetorno = false
			}
		}
		return valorRetorno
	}

	// Imprimimos la matriz, por filas y columnas:
	override fun toString() : String {
		var stringRetorno : String = "Matriz de tamanio ${numFilas}x${numColumnas}:\n"
		if (this.numFilas != 0 && this.numColumnas != 0) {
			for (i in 0..this.numFilas-1) {
				stringRetorno += "["
				for (j in 0..this.numColumnas-1) {
					if (j != this.numColumnas-1) {
						stringRetorno += " ${this.m[i][j]},"
					} else {
						stringRetorno += " ${this.m[i][j]}"
					}
				}
				if (i != this.numFilas - 1) {
					stringRetorno += " ]\n"
				} else {
					stringRetorno += " ]"
				}
			}
		}
		else {
			stringRetorno += "[ ]"
		}
		return stringRetorno
	}
}

fun main() {
	println("Probamos el correcto funcionamiento del programa:")
	println("\nMatriz m:")
	var m1 : Matriz = Matriz(mutableListOf(1, 2, 3), mutableListOf(4, 5, 6), mutableListOf(7, 8, 9))
	println(m1)
	println("\nMatriz traspuesta de m, m':")
	var m2 : Matriz = m1.calcularTraspuesta()
	println(m2)
	println("\nMatriz m x Matriz m':")
	println(m1.multiplicarConMatriz(m2))
}