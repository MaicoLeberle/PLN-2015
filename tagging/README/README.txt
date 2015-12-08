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

	python3 tagging/scripts/eval.py -i file

Resultados del etiquetador Baseline:
	* Accuracy: 89.00%
	* Accuracy known: 95.31%
	* Accuracy unknown: 31.80%
	* Tiempo de evaluación: 0m7.226s

-------------------------------------------------------------------------------
EJERCICIO 4
-------------------------------------------------------------------------------

Implementación de un Hidden Markov Model. Implementación del algoritmo de 
Viterbi para encontrar la mejor manera de etiquetar una oración.


-------------------------------------------------------------------------------
EJERCICIO 5
-------------------------------------------------------------------------------

Implementación de un Maximum Likelihood Markov Model. El método tag utiliza un 
objeto de tipo ViterbiTagger implementado en el ejercicio 4. Varios de los 
métodos son parecidos a los de la clase HMM, y todos los cálculos que se desean
 desarrollar con este modelo son implementados en el __init__ para evitar 
recomputar innecesariamente.

Los resultados obtenidos al entrenar modelos MLHMM son, dependiendo del valor 
de n:

N = 1:

	Time:
		real	0m30.505s
		user	0m29.212s
		sys	0m0.448s
	Accuracy: 88.81%
	Accuracy of known words: 90.0640383174908%.
	Accuracy of unknown words: 9.935961682509205%.

N = 2:

	Time:
		real	0m31.865s
		user	0m30.300s
		sys	0m0.332s
	Accuracy: 92.16%
	Accuracy of known words: 90.0640383174908%.
	Accuracy of unknown words: 9.935961682509205%.
	
N = 3:

	Time:
		real	2m9.417s
		user	2m6.772s
		sys	0m0.456s
	Accuracy: 83.49%
	Accuracy of known words: 90.0640383174908%.
	Accuracy of unknown words: 9.935961682509205%.
	
N = 4:

	Time:
		real	29m25.166s
		user	28m57.416s
		sys	0m3.584s

-------------------------------------------------------------------------------
EJERCICIO 6
-------------------------------------------------------------------------------

Implementación de features básicas (word_lower, word_istitle, etc.) que toman 
como parámetros una History ; e implementación de features paramétricas 
(NPrevTags, PrevWord) que se inicializan con diversos valores (features 
básicas, el valor de n correspondiente a las n etiquetas anteriores) y se 
utilizan mediante el método _evaluate (el cual recibe una History).


-------------------------------------------------------------------------------
EJERCICIO 7
-------------------------------------------------------------------------------

Implementación de un modelo Markov de máxima entropía, utilizando un pipeline 
de scikit-learn (sklearn.pipeline). Dicho pipeline contiene un vectorizador de 
featureforge (featureforge.vectorizer.Vectorizer), y contiene un clasificador 
de scikit-learn (sklearn.linear_model.LogisticRegression, 
sklearn.naive_bayes.MultinomialNB o sklearn.svm.LinearSVC).
Además, el algoritmo de tagging utilizado por este modelo se llama beam 
inference, con un beam de tamaño 1.

Los resultados obtenidos al entrenar modelos MLHMM son, dependiendo del valor 
de n y del clasificador utilizado:

N = 1, clasificador = linear_model.LogisticRegression:

	Time:
		real	0m50.215s
		user	0m36.396s
		sys	0m0.296s
	Accuracy: 92.70%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.

N = 2, clasificador = linear_model.LogisticRegression:

	Time:
		real	0m38.826s
		user	0m36.980s
		sys	0m0.304s
	Accuracy: 91.99%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 3, clasificador = linear_model.LogisticRegression:

	Time:
		real	0m54.151s
		user	0m40.772s
		sys	0m0.780s
	Accuracy: 92.18%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 4, clasificador = linear_model.LogisticRegression:

	Time:
		real	0m53.532s
		user	0m43.544s
		sys	0m0.288s
	Accuracy: 92.23%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 1, clasificador = svm.LinearSVC:

	Time:
		real	0m43.646s
		user	0m35.172s
		sys	0m0.320s
	Accuracy: 94.43%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 2, clasificador = svm.LinearSVC:

	Time:
		real	0m48.687s
		user	0m38.060s
		sys	0m0.356s
	Accuracy: 94.29%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 3, clasificador = svm.LinearSVC:

	Time:
		real	0m54.834s
		user	0m41.292s
		sys	0m0.324s
	Accuracy: 94.40%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 4, clasificador = svm.LinearSVC:

	Time:
		real	0m42.796s
		user	0m41.364s
		sys	0m0.316s
	Accuracy: 94.46%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 1, clasificador = naive_bayes.MultinomialNB:
	
	Time:
		real	44m16.957s
		user	37m26.332s
		sys	0m5.784s
	Accuracy: 82.18%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 2, clasificador = naive_bayes.MultinomialNB:

	Time:
		real	59m11.925s
		user	36m36.420s
		sys	0m4.628s
	Accuracy: 76.46%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 3, clasificador = naive_bayes.MultinomialNB:

	Time:
		real	61m7.078s
		user	37m55.548s
		sys	0m4.328s
	Accuracy: 71.47%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	
N = 4, clasificador = naive_bayes.MultinomialNB:

	Time:
		real	61m9.887s
		user	38m5.160s
		sys	0m4.164s
	Accuracy: 68.20%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.