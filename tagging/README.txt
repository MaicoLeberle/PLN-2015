-------------------------------------------------------------------------------
EJERCICIO 1
-------------------------------------------------------------------------------

Estadísticas obtenidas sobre el corpus ancora:
	* Cantidad de oraciones: 17379.
	* Cantidad de palabras: 517268.
	* Tamaño del vocabulario: 46482 palabras.
	* Cantidad de etiquetas utilizadas: 48.
	* 10 etiquetas más frecuentes:
		- 'nc': 17.79% de las etiquetas del corpus (92002 ocurrencias). Su
		 significado es 'nombre común', y las 5 palabras más frecuentes con 
		 esta etiqueta son 'años', 'presidente', 'millones', 'equipo' y 
		 'partido'.
		- 'sp': 15.45% de las etiquetas del corpus (79904 ocurrencias). Su 
		 significado es 'preposición', y las 5 palabras más frecuentes con esta
		  etiqueta son 'de', 'en', 'a', 'del' y 'con'.
		- 'da': 10.55% de las etiquetas del corpus (54552 ocurrencias). Su 
		 significado es 'artículo', y las 5 palabras más frecuentes con esta
		 etiqueta son 'la', 'el', 'los', 'las' y 'El'.
		- 'vm': 9.78% de las etiquetas del corpus (50609 ocurrencias). Su
		 significado es 'verbo', y las 5 palabras más frecuentes con esta 
		 etiqueta son 'está', 'tiene', 'dijo', 'puede' y 'hace'.
		- 'aq': 6.55% de las etiquetas del corpus (33904 ocurrencias). Su
		 significado es 'adjetivo', y las 5 palabras más frecuentes con esta
		 etiqueta son 'pasado', 'gran', 'mayor', 'nuevo' y 'próximo'.
		- 'fc': 5.83% de las etiquetas del corpus (30148 ocurrencias). Su
		 significado es 'coma', y la única palabra asociada a esta etiqueta es
		 ','.
		- 'np': 5.63% de las etiquetas del corpus (29113 ocurrencias). Su 
		 significado es 'nombre propio', y las 5 palabras más frecuentes con 
		 esta etiqueta son 'Gobierno', 'España', 'PP', 'Barcelona' y 'Madrid'.
		- 'fp': 4.09% de las etiquetas del corpus (21157 ocurrencias). Su 
		 significaod es 'punto o paréntesis', y las palabras más frecuentes 
		 con esta etiqueta son '.', '(' y ')'.
		- 'rg': 2.96% de las etiquetas del corpus (15333 ocurrencias). Su
		 significado es 'adverbio', y las 5 palabras más frecuentes con esta 
		 etiqueta son 'más', 'hoy', 'también', 'ayer' y 'ya'.
		- 'cc': 2.90% de las etiquetas del corpus (15023 ocurrencias). Su
		 significado es 'conjunción', y las 5 palabras más frecuentes con esta 
		 etiqueta son 'y', 'pero', 'o', 'Pero' y 'e'.
    * Niveles de ambigüedad (cantidad de palabras con cierta cantidad de 
     etiquetas asociadas):
    	- 1 etiqueta: 94.89% de las palabras. Las más frecuentes son ',', 'el',
    	 'en', 'con' y 'por'.
    	- 2 etiquetas: 0.05% de las palabras. Las más frecuentes son 'la', 'y',
    	 '"', 'los' y 'del'.
    	- 3 etiquetas: menos del 0.01% de las palabras. Las más frecuentes son 
    	 '.', 'a', 'un', 'no' y 'es'.
    	- 4 etiquetas: menos del 0.01% de las palabras. Las más frecuentes son 
    	 'de', 'dos', 'este', 'tres' y 'todo'.
    	- 5 etiquetas: menos del 0.01% de las palabras. Las más frecuentes son 
    	 'que', 'mismo', 'cinco' y 'medio'.
    	- 6 etiquetas: menos del 0.01% de las palabras. Las más frecuentes son 
    	 'una', 'como' y 'uno'.



-------------------------------------------------------------------------------
EJERCICIO 2
-------------------------------------------------------------------------------

Implementar un etiquetador de tipo Baseline.
La metodología consiste en asignar a una palabra su etiqueta asociada vista más
 veces en el corpus de entrenamiento. Si se trata de una palabra desconocida, 
se le asigna la etiqueta más frecuente del corpus de entrenamiento.


-------------------------------------------------------------------------------
EJERCICIO 3
-------------------------------------------------------------------------------

Entrenamiento y evaluación de etiquetadores.
Comando a utilizar para entrenar un modelo m, con parámetro n (el cual no es 
obligatorio en todos los casos):
	
	python3 tagging/scripts/train.py [-m m [-n n]] -o output

Las opciones para m son 'base', 'mlhmm' y 'memm'. n debe ser un número natural,
 y output es el archivo de salida.
Comando a utilizar para evaluar un modelo almacenado en el archivo file:

	python3 tagging/scripts/train.py -i file


-------------------------------------------------------------------------------
EJERCICIO 4
-------------------------------------------------------------------------------

Implementación de un Hidden Markov Model. Implementación del algoritmo de 
Viterbi para encontrar la mejor manera de etiquetar una oración.


-------------------------------------------------------------------------------
EJERCICIO 5
-------------------------------------------------------------------------------



-------------------------------------------------------------------------------
EJERCICIO 6
-------------------------------------------------------------------------------



-------------------------------------------------------------------------------
EJERCICIO 7
-------------------------------------------------------------------------------

