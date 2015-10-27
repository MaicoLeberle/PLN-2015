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
	
	* Precisión: 54.57%
	* Precisión sobre palabras conocidas: 90.06%
	* Precisión sobre palabras desconocidas: 9.94%

Matrix de confusión:

ao': 
	confundido por nc (0.0557%% de los errores).
	confundido por rg (0.0325%% de los errores).

'aq': 
	confundido por dd (0.0186%% de los errores).
	confundido por di (0.0557%% de los errores).
	confundido por nc (5.9754%% de los errores).
	confundido por np (0.0023%% de los errores).
	confundido por pn (0.0093%% de los errores).
	confundido por rg (0.4111%% de los errores).
	confundido por un (0.1068%% de los errores).
	confundido por vm (0.7594%% de los errores).
	confundido por zm (0.0325%% de los errores).

'cc': 
	confundido por cs (0.0209%% de los errores).
	confundido por nc (0.0279%% de los errores).
	confundido por pt (0.0023%% de los errores).
	confundido por rg (0.0581%% de los errores).
	confundido por rn (0.1440%% de los errores).
	confundido por sp (5.1161%% de los errores).
	confundido por vs (0.0023%% de los errores).

'cs': 
	confundido por cc (0.0325%% de los errores).
	confundido por nc (0.0720%% de los errores).
	confundido por pr (0.0023%% de los errores).
	confundido por pt (0.8778%% de los errores).
	confundido por rg (0.2137%% de los errores).
	confundido por sp (0.0604%% de los errores).
	confundido por un (0.2787%% de los errores).
	confundido por vm (2.7102%% de los errores).

'da': 
	confundido por nc (0.3321%% de los errores).
	confundido por nu (0.0070%% de los errores).
	confundido por pp (13.1050%% de los errores).
	confundido por un (1.1890%% de los errores).
	confundido por w (0.0209%% de los errores).

'dd': 
	confundido por aq (0.2671%% de los errores).
	confundido por nc (0.0046%% de los errores).
	confundido por np (0.0348%% de los errores).
	confundido por pd (1.0195%% de los errores).

'di': 
	confundido por aq (0.2880%% de los errores).
	confundido por nc (0.1742%% de los errores).
	confundido por nu (2.4245%% de los errores).
	confundido por pi (0.7594%% de los errores).
	confundido por pr (0.0046%% de los errores).
	confundido por rg (0.0023%% de los errores).
	confundido por un (2.3107%% de los errores).

'dn': 
	confundido por ao (0.0023%% de los errores).
	confundido por da (0.0673%% de los errores).
	confundido por di (0.0023%% de los errores).
	confundido por nc (0.4111%% de los errores).
	confundido por nu (0.1277%% de los errores).
	confundido por pn (0.1347%% de los errores).
	confundido por rg (0.0186%% de los errores).
	confundido por un (0.0395%% de los errores).

'dp': 
	confundido por pp (0.1161%% de los errores).
	confundido por px (0.0836%% de los errores).

'dt': 
	confundido por de (0.0395%% de los errores).
	confundido por nc (0.0046%% de los errores).

'fe': 
	confundido por un (1.3841%% de los errores).

'fp': 
	confundido por fg (7.8124%% de los errores).
	confundido por un (0.7385%% de los errores).

'fs': 
	confundido por nc (0.0046%% de los errores).

'fz': 
	confundido por da (0.0023%% de los errores).
	confundido por nc (0.0163%% de los errores).
	confundido por nu (0.0070%% de los errores).
	confundido por un (0.0163%% de los errores).

'nc': 
	confundido por ao (0.0186%% de los errores).
	confundido por aq (2.0181%% de los errores).
	confundido por cc (0.0186%% de los errores).
	confundido por da (0.0441%% de los errores).
	confundido por dd (0.0046%% de los errores).
	confundido por di (0.0070%% de los errores).
	confundido por dn (0.0163%% de los errores).
	confundido por i (0.0023%% de los errores).
	confundido por np (0.0093%% de los errores).
	confundido por nu (0.0023%% de los errores).
	confundido por pn (0.0046%% de los errores).
	confundido por pp (0.0046%% de los errores).
	confundido por rg (0.1719%% de los errores).
	confundido por sp (0.0046%% de los errores).
	confundido por un (0.2764%% de los errores).
	confundido por vm (1.6976%% de los errores).
	confundido por vs (0.0023%% de los errores).

'np': 
	confundido por aq (0.0023%% de los errores).
	confundido por cc (0.0023%% de los errores).
	confundido por dp (0.0023%% de los errores).
	confundido por nc (4.5030%% de los errores).
	confundido por pd (0.0023%% de los errores).
	confundido por vm (0.0023%% de los errores).
	confundido por vs (0.0023%% de los errores).

'nu': 
	confundido por da (0.0975%% de los errores).
	confundido por nc (0.3437%% de los errores).
	confundido por np (0.0023%% de los errores).
	confundido por pn (0.0070%% de los errores).
	confundido por un (0.0046%% de los errores).

'p0': 
	confundido por pp (2.4106%% de los errores).

'pd': 
	confundido por aq (0.0023%% de los errores).
	confundido por dd (0.0070%% de los errores).
	confundido por nc (0.0070%% de los errores).
	confundido por np (0.0070%% de los errores).

'pe': 
	confundido por de (0.0023%% de los errores).

'pi': 
	confundido por aq (0.0975%% de los errores).
	confundido por dd (0.0023%% de los errores).
	confundido por di (0.2206%% de los errores).
	confundido por nc (0.1045%% de los errores).
	confundido por rg (0.1997%% de los errores).
	confundido por un (0.2229%% de los errores).

'pn': 
	confundido por da (0.0046%% de los errores).
	confundido por di (0.0023%% de los errores).
	confundido por dn (0.0093%% de los errores).
	confundido por nc (0.0929%% de los errores).
	confundido por nu (0.0186%% de los errores).
	confundido por rg (0.0163%% de los errores).

'pp': 
	confundido por da (0.1045%% de los errores).
	confundido por nc (0.0163%% de los errores).
	confundido por p0 (0.4343%% de los errores).
	confundido por un (0.3275%% de los errores).

'pr': 
	confundido por dd (0.0418%% de los errores).
	confundido por rg (0.1811%% de los errores).
	confundido por un (0.0163%% de los errores).
	confundido por vm (3.3604%% de los errores).

'pt': 
	confundido por de (0.1347%% de los errores).
	confundido por dt (0.0046%% de los errores).
	confundido por nc (0.0023%% de los errores).
	confundido por pr (0.0023%% de los errores).
	confundido por rg (0.0186%% de los errores).

'px': 
	confundido por nc (0.0163%% de los errores).

'rg': 
	confundido por ao (0.0046%% de los errores).
	confundido por aq (0.2856%% de los errores).
	confundido por cc (1.0869%% de los errores).
	confundido por cs (0.0093%% de los errores).
	confundido por di (0.1440%% de los errores).
	confundido por nc (0.7431%% de los errores).
	confundido por pi (0.1045%% de los errores).
	confundido por pp (0.0325%% de los errores).
	confundido por pr (0.0046%% de los errores).
	confundido por rn (0.0557%% de los errores).
	confundido por sp (0.1370%% de los errores).
	confundido por un (0.2926%% de los errores).
	confundido por vm (0.0325%% de los errores).

'rn': 
	confundido por cc (0.0046%% de los errores).
	confundido por nc (1.8579%% de los errores).
	confundido por rg (0.0023%% de los errores).

'sp': 
	confundido por cc (0.1022%% de los errores).
	confundido por cs (0.1510%% de los errores).
	confundido por nc (3.8481%% de los errores).
	confundido por np (0.1463%% de los errores).
	confundido por pt (0.1068%% de los errores).
	confundido por rg (0.3321%% de los errores).
	confundido por un (2.3990%% de los errores).
	confundido por vm (13.2977%% de los errores).

'un': 
	confundido por aq (0.0093%% de los errores).
	confundido por fg (0.0046%% de los errores).
	confundido por fp (0.0023%% de los errores).
	confundido por nc (0.0720%% de los errores).
	confundido por pt (0.0023%% de los errores).
	confundido por rg (0.0046%% de los errores).
	confundido por sp (0.0023%% de los errores).
	confundido por vm (0.0046%% de los errores).

'va': 
	confundido por nc (0.0906%% de los errores).
	confundido por vm (0.0441%% de los errores).

'vm': 
	confundido por aq (0.7896%% de los errores).
	confundido por nc (4.9164%% de los errores).
	confundido por rg (0.0046%% de los errores).
	confundido por un (0.0046%% de los errores).
	confundido por va (0.0023%% de los errores).

'vs': 
	confundido por nc (0.8453%% de los errores).
	confundido por np (0.0070%% de los errores).
	confundido por vm (0.3367%% de los errores).

'zm': 
	confundido por nc (0.1301%% de los errores).

'zp': 
	confundido por nc (0.1301%% de los errores).


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


-------------------------------------------------------------------------------
EJERCICIO 6
-------------------------------------------------------------------------------



-------------------------------------------------------------------------------
EJERCICIO 7
-------------------------------------------------------------------------------

