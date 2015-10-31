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
	(original tag) ao: 
		tag selected by model -> nc (with 0.2356% of the mistakes).
		tag selected by model -> rg (with 0.1320% of the mistakes).

	(original tag) aq: 
		tag selected by model -> di (with 0.0471% of the mistakes).
		tag selected by model -> fc (with 0.0094% of the mistakes).
		tag selected by model -> nc (with 21.2818% of the mistakes).
		tag selected by model -> rg (with 0.0283% of the mistakes).
		tag selected by model -> sp (with 0.0471% of the mistakes).
		tag selected by model -> vm (with 2.0075% of the mistakes).

	(original tag) cc: 
		tag selected by model -> cs (with 0.0094% of the mistakes).
		tag selected by model -> nc (with 0.1225% of the mistakes).
		tag selected by model -> np (with 0.0094% of the mistakes).
		tag selected by model -> rg (with 0.4336% of the mistakes).
		tag selected by model -> sp (with 0.0094% of the mistakes).
		tag selected by model -> vs (with 0.0094% of the mistakes).

	(original tag) cs: 
		tag selected by model -> cc (with 0.2074% of the mistakes).
		tag selected by model -> nc (with 0.2922% of the mistakes).
		tag selected by model -> pr (with 11.0273% of the mistakes).
		tag selected by model -> rg (with 0.0471% of the mistakes).
		tag selected by model -> sp (with 0.1791% of the mistakes).

	(original tag) da: 
		tag selected by model -> dn (with 0.0094% of the mistakes).
		tag selected by model -> nc (with 1.3478% of the mistakes).
		tag selected by model -> nu (with 0.0377% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0283% of the mistakes).
		tag selected by model -> nc (with 0.0189% of the mistakes).
		tag selected by model -> np (with 0.1414% of the mistakes).

	(original tag) de: 
		tag selected by model -> pt (with 0.0754% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.5467% of the mistakes).
		tag selected by model -> nc (with 0.1508% of the mistakes).
		tag selected by model -> pi (with 0.0189% of the mistakes).
		tag selected by model -> rg (with 0.2545% of the mistakes).

	(original tag) dn: 
		tag selected by model -> di (with 0.2639% of the mistakes).
		tag selected by model -> nc (with 0.3110% of the mistakes).
		tag selected by model -> nu (with 0.0094% of the mistakes).

	(original tag) dt: 
		tag selected by model -> nc (with 0.0189% of the mistakes).
		tag selected by model -> pt (with 0.1697% of the mistakes).

	(original tag) fs: 
		tag selected by model -> nc (with 0.0189% of the mistakes).

	(original tag) fz: 
		tag selected by model -> fe (with 0.0660% of the mistakes).
		tag selected by model -> nc (with 0.0471% of the mistakes).
		tag selected by model -> nu (with 0.0377% of the mistakes).
		tag selected by model -> sp (with 0.0189% of the mistakes).

	(original tag) nc: 
		tag selected by model -> aq (with 2.3845% of the mistakes).
		tag selected by model -> cc (with 0.0094% of the mistakes).
		tag selected by model -> da (with 0.0094% of the mistakes).
		tag selected by model -> di (with 0.0283% of the mistakes).
		tag selected by model -> dn (with 0.0471% of the mistakes).
		tag selected by model -> fc (with 0.0094% of the mistakes).
		tag selected by model -> np (with 0.0189% of the mistakes).
		tag selected by model -> pi (with 0.0189% of the mistakes).
		tag selected by model -> pp (with 0.0189% of the mistakes).
		tag selected by model -> rg (with 0.1225% of the mistakes).
		tag selected by model -> sp (with 0.1037% of the mistakes).
		tag selected by model -> un (with 0.0094% of the mistakes).
		tag selected by model -> va (with 0.0094% of the mistakes).
		tag selected by model -> vm (with 0.6032% of the mistakes).
		tag selected by model -> vs (with 0.2074% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.0094% of the mistakes).
		tag selected by model -> cc (with 0.0094% of the mistakes).
		tag selected by model -> dp (with 0.0094% of the mistakes).
		tag selected by model -> fc (with 0.0094% of the mistakes).
		tag selected by model -> nc (with 18.3035% of the mistakes).
		tag selected by model -> pd (with 0.0094% of the mistakes).
		tag selected by model -> sp (with 0.0283% of the mistakes).
		tag selected by model -> vs (with 0.0094% of the mistakes).

	(original tag) nu: 
		tag selected by model -> da (with 0.1508% of the mistakes).
		tag selected by model -> dn (with 0.0283% of the mistakes).
		tag selected by model -> nc (with 1.3855% of the mistakes).
		tag selected by model -> np (with 0.0094% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.3299% of the mistakes).

	(original tag) pd: 
		tag selected by model -> dd (with 0.1697% of the mistakes).
		tag selected by model -> nc (with 0.0283% of the mistakes).
		tag selected by model -> np (with 0.0283% of the mistakes).

	(original tag) pe: 
		tag selected by model -> pt (with 0.0094% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0660% of the mistakes).
		tag selected by model -> di (with 2.8087% of the mistakes).
		tag selected by model -> nc (with 0.0471% of the mistakes).
		tag selected by model -> pr (with 0.0094% of the mistakes).
		tag selected by model -> rg (with 0.5844% of the mistakes).

	(original tag) pn: 
		tag selected by model -> dn (with 0.4713% of the mistakes).
		tag selected by model -> nc (with 0.2451% of the mistakes).
		tag selected by model -> pi (with 0.0094% of the mistakes).

	(original tag) pp: 
		tag selected by model -> da (with 2.4222% of the mistakes).
		tag selected by model -> nc (with 0.0660% of the mistakes).
		tag selected by model -> p0 (with 0.4901% of the mistakes).
		tag selected by model -> rg (with 0.2168% of the mistakes).

	(original tag) pr: 
		tag selected by model -> cs (with 0.0660% of the mistakes).
		tag selected by model -> rg (with 0.0283% of the mistakes).

	(original tag) pt: 
		tag selected by model -> dt (with 0.0189% of the mistakes).
		tag selected by model -> nc (with 0.0094% of the mistakes).
		tag selected by model -> pr (with 0.0094% of the mistakes).
		tag selected by model -> rg (with 0.0754% of the mistakes).

	(original tag) px: 
		tag selected by model -> dp (with 0.0283% of the mistakes).
		tag selected by model -> nc (with 0.0660% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 0.3864% of the mistakes).
		tag selected by model -> cc (with 0.1979% of the mistakes).
		tag selected by model -> cs (with 0.0848% of the mistakes).
		tag selected by model -> di (with 0.0189% of the mistakes).
		tag selected by model -> nc (with 2.9029% of the mistakes).
		tag selected by model -> pi (with 0.0848% of the mistakes).
		tag selected by model -> rn (with 0.2168% of the mistakes).
		tag selected by model -> sp (with 0.2639% of the mistakes).
		tag selected by model -> vm (with 0.0094% of the mistakes).

	(original tag) rn: 
		tag selected by model -> cc (with 0.0283% of the mistakes).
		tag selected by model -> nc (with 0.0094% of the mistakes).
		tag selected by model -> rg (with 0.0283% of the mistakes).

	(original tag) sp: 
		tag selected by model -> cs (with 0.4713% of the mistakes).
		tag selected by model -> nc (with 0.4241% of the mistakes).
		tag selected by model -> rg (with 0.0189% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.0377% of the mistakes).
		tag selected by model -> cs (with 0.0189% of the mistakes).
		tag selected by model -> fe (with 0.1602% of the mistakes).
		tag selected by model -> fg (with 0.0094% of the mistakes).
		tag selected by model -> fp (with 0.0189% of the mistakes).
		tag selected by model -> nc (with 0.3016% of the mistakes).
		tag selected by model -> pt (with 0.0094% of the mistakes).
		tag selected by model -> rg (with 0.0189% of the mistakes).
		tag selected by model -> sp (with 0.0094% of the mistakes).
		tag selected by model -> vm (with 0.0189% of the mistakes).

	(original tag) va: 
		tag selected by model -> nc (with 0.0377% of the mistakes).
		tag selected by model -> vm (with 0.0094% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 1.0179% of the mistakes).
		tag selected by model -> nc (with 20.1791% of the mistakes).
		tag selected by model -> sp (with 0.0094% of the mistakes).
		tag selected by model -> un (with 0.0094% of the mistakes).
		tag selected by model -> va (with 0.0094% of the mistakes).
		tag selected by model -> vs (with 0.0943% of the mistakes).

	(original tag) vs: 
		tag selected by model -> nc (with 0.0566% of the mistakes).
		tag selected by model -> np (with 0.0283% of the mistakes).
		tag selected by model -> rg (with 0.0943% of the mistakes).
		tag selected by model -> vm (with 0.0471% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.0094% of the mistakes).
		tag selected by model -> nc (with 0.5278% of the mistakes).

	(original tag) zp: 
		tag selected by model -> nc (with 0.5278% of the mistakes).

N = 2:

	Time:
		real	0m31.865s
		user	0m30.300s
		sys	0m0.332s
	Accuracy: 92.16%
	Accuracy of known words: 90.0640383174908%.
	Accuracy of unknown words: 9.935961682509205%.
	(original tag) ao: 
		tag selected by model -> nc (with 0.1346% of the mistakes).
		tag selected by model -> rg (with 0.0539% of the mistakes).

	(original tag) aq: 
		tag selected by model -> ao (with 0.5116% of the mistakes).
		tag selected by model -> cc (with 0.0135% of the mistakes).
		tag selected by model -> da (with 1.3599% of the mistakes).
		tag selected by model -> dd (with 0.0673% of the mistakes).
		tag selected by model -> di (with 0.1750% of the mistakes).
		tag selected by model -> dn (with 0.0673% of the mistakes).
		tag selected by model -> fc (with 1.1310% of the mistakes).
		tag selected by model -> fe (with 0.2020% of the mistakes).
		tag selected by model -> fg (with 0.2020% of the mistakes).
		tag selected by model -> fp (with 0.0539% of the mistakes).
		tag selected by model -> nc (with 6.3956% of the mistakes).
		tag selected by model -> np (with 1.8985% of the mistakes).
		tag selected by model -> p0 (with 0.1481% of the mistakes).
		tag selected by model -> pd (with 0.0404% of the mistakes).
		tag selected by model -> pr (with 0.0943% of the mistakes).
		tag selected by model -> pt (with 0.0135% of the mistakes).
		tag selected by model -> px (with 0.1346% of the mistakes).
		tag selected by model -> rg (with 0.5520% of the mistakes).
		tag selected by model -> rn (with 0.0269% of the mistakes).
		tag selected by model -> sp (with 2.7737% of the mistakes).
		tag selected by model -> un (with 0.0135% of the mistakes).
		tag selected by model -> va (with 0.0269% of the mistakes).
		tag selected by model -> vm (with 4.1740% of the mistakes).
		tag selected by model -> zm (with 0.0135% of the mistakes).

	(original tag) cc: 
		tag selected by model -> cs (with 0.0135% of the mistakes).
		tag selected by model -> np (with 0.1481% of the mistakes).
		tag selected by model -> pr (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.6867% of the mistakes).
		tag selected by model -> sp (with 0.0269% of the mistakes).
		tag selected by model -> vs (with 0.0135% of the mistakes).

	(original tag) cs: 
		tag selected by model -> cc (with 0.3366% of the mistakes).
		tag selected by model -> da (with 0.0269% of the mistakes).
		tag selected by model -> fc (with 0.0269% of the mistakes).
		tag selected by model -> fe (with 0.0135% of the mistakes).
		tag selected by model -> fg (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.0135% of the mistakes).
		tag selected by model -> np (with 0.0404% of the mistakes).
		tag selected by model -> p0 (with 0.0135% of the mistakes).
		tag selected by model -> pr (with 2.6659% of the mistakes).
		tag selected by model -> rg (with 0.0808% of the mistakes).
		tag selected by model -> sp (with 0.6194% of the mistakes).
		tag selected by model -> vm (with 0.0135% of the mistakes).

	(original tag) da: 
		tag selected by model -> ao (with 0.0269% of the mistakes).
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> fg (with 0.1077% of the mistakes).
		tag selected by model -> fh (with 0.0943% of the mistakes).
		tag selected by model -> nc (with 0.9290% of the mistakes).
		tag selected by model -> np (with 0.5116% of the mistakes).
		tag selected by model -> nu (with 0.0539% of the mistakes).
		tag selected by model -> pp (with 0.0269% of the mistakes).
		tag selected by model -> sp (with 0.0539% of the mistakes).
		tag selected by model -> vm (with 0.1212% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0404% of the mistakes).
		tag selected by model -> da (with 0.0269% of the mistakes).
		tag selected by model -> nc (with 0.0135% of the mistakes).
		tag selected by model -> np (with 0.0135% of the mistakes).
		tag selected by model -> pd (with 0.0269% of the mistakes).

	(original tag) de: 
		tag selected by model -> pt (with 0.0943% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.7136% of the mistakes).
		tag selected by model -> da (with 0.0673% of the mistakes).
		tag selected by model -> nc (with 0.0404% of the mistakes).
		tag selected by model -> pi (with 0.2289% of the mistakes).
		tag selected by model -> rg (with 0.0135% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.0539% of the mistakes).
		tag selected by model -> da (with 0.0539% of the mistakes).
		tag selected by model -> di (with 0.3770% of the mistakes).
		tag selected by model -> nc (with 0.0539% of the mistakes).
		tag selected by model -> nu (with 0.0539% of the mistakes).

	(original tag) dp: 
		tag selected by model -> px (with 0.0404% of the mistakes).

	(original tag) dt: 
		tag selected by model -> da (with 0.0269% of the mistakes).
		tag selected by model -> pt (with 0.0269% of the mistakes).

	(original tag) fs: 
		tag selected by model -> np (with 0.0135% of the mistakes).
		tag selected by model -> sp (with 0.0135% of the mistakes).

	(original tag) fz: 
		tag selected by model -> da (with 0.0539% of the mistakes).
		tag selected by model -> fe (with 0.0404% of the mistakes).
		tag selected by model -> nu (with 0.0404% of the mistakes).
		tag selected by model -> sp (with 0.0539% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.1616% of the mistakes).
		tag selected by model -> aq (with 3.8777% of the mistakes).
		tag selected by model -> cc (with 0.0269% of the mistakes).
		tag selected by model -> cs (with 0.0135% of the mistakes).
		tag selected by model -> da (with 2.4505% of the mistakes).
		tag selected by model -> dd (with 0.0269% of the mistakes).
		tag selected by model -> di (with 0.1616% of the mistakes).
		tag selected by model -> dn (with 0.0808% of the mistakes).
		tag selected by model -> dt (with 0.0269% of the mistakes).
		tag selected by model -> fa (with 0.0135% of the mistakes).
		tag selected by model -> fc (with 0.4174% of the mistakes).
		tag selected by model -> fe (with 0.1212% of the mistakes).
		tag selected by model -> fg (with 0.8752% of the mistakes).
		tag selected by model -> fp (with 0.0135% of the mistakes).
		tag selected by model -> fz (with 0.1077% of the mistakes).
		tag selected by model -> np (with 6.1936% of the mistakes).
		tag selected by model -> p0 (with 0.1077% of the mistakes).
		tag selected by model -> pd (with 0.0135% of the mistakes).
		tag selected by model -> pi (with 0.0539% of the mistakes).
		tag selected by model -> pp (with 0.0269% of the mistakes).
		tag selected by model -> pr (with 0.1346% of the mistakes).
		tag selected by model -> pt (with 0.0135% of the mistakes).
		tag selected by model -> px (with 0.1616% of the mistakes).
		tag selected by model -> rg (with 0.4847% of the mistakes).
		tag selected by model -> rn (with 0.0404% of the mistakes).
		tag selected by model -> sp (with 1.0502% of the mistakes).
		tag selected by model -> un (with 0.0135% of the mistakes).
		tag selected by model -> va (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 2.3159% of the mistakes).
		tag selected by model -> vs (with 0.1750% of the mistakes).
		tag selected by model -> zm (with 0.0135% of the mistakes).

	(original tag) np: 
		tag selected by model -> ao (with 0.0269% of the mistakes).
		tag selected by model -> aq (with 1.9523% of the mistakes).
		tag selected by model -> cc (with 0.0135% of the mistakes).
		tag selected by model -> cs (with 0.0269% of the mistakes).
		tag selected by model -> da (with 0.5790% of the mistakes).
		tag selected by model -> dd (with 0.0269% of the mistakes).
		tag selected by model -> di (with 0.1616% of the mistakes).
		tag selected by model -> dp (with 0.0135% of the mistakes).
		tag selected by model -> fc (with 0.2289% of the mistakes).
		tag selected by model -> fd (with 0.0269% of the mistakes).
		tag selected by model -> fe (with 0.5386% of the mistakes).
		tag selected by model -> fg (with 0.5116% of the mistakes).
		tag selected by model -> fi (with 0.0269% of the mistakes).
		tag selected by model -> fp (with 0.0539% of the mistakes).
		tag selected by model -> fz (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 6.1263% of the mistakes).
		tag selected by model -> p0 (with 0.5790% of the mistakes).
		tag selected by model -> pd (with 0.0269% of the mistakes).
		tag selected by model -> pr (with 0.5520% of the mistakes).
		tag selected by model -> pt (with 0.2154% of the mistakes).
		tag selected by model -> px (with 0.2154% of the mistakes).
		tag selected by model -> rg (with 0.2558% of the mistakes).
		tag selected by model -> rn (with 0.2424% of the mistakes).
		tag selected by model -> sp (with 1.2253% of the mistakes).
		tag selected by model -> vm (with 1.2253% of the mistakes).
		tag selected by model -> vs (with 0.0135% of the mistakes).
		tag selected by model -> zm (with 0.0135% of the mistakes).

	(original tag) nu: 
		tag selected by model -> ao (with 0.1077% of the mistakes).
		tag selected by model -> aq (with 0.0539% of the mistakes).
		tag selected by model -> da (with 0.8079% of the mistakes).
		tag selected by model -> dn (with 0.0404% of the mistakes).
		tag selected by model -> dt (with 0.0943% of the mistakes).
		tag selected by model -> fc (with 0.0135% of the mistakes).
		tag selected by model -> fe (with 0.0135% of the mistakes).
		tag selected by model -> fg (with 0.0269% of the mistakes).
		tag selected by model -> nc (with 0.1750% of the mistakes).
		tag selected by model -> np (with 0.4982% of the mistakes).
		tag selected by model -> p0 (with 0.0269% of the mistakes).
		tag selected by model -> pr (with 0.0404% of the mistakes).
		tag selected by model -> rg (with 0.0673% of the mistakes).
		tag selected by model -> sp (with 0.0673% of the mistakes).
		tag selected by model -> va (with 0.0269% of the mistakes).
		tag selected by model -> vm (with 0.0943% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.4039% of the mistakes).

	(original tag) pd: 
		tag selected by model -> da (with 0.0135% of the mistakes).
		tag selected by model -> dd (with 0.1750% of the mistakes).
		tag selected by model -> fe (with 0.0135% of the mistakes).
		tag selected by model -> fg (with 0.0135% of the mistakes).
		tag selected by model -> np (with 0.0269% of the mistakes).

	(original tag) pe: 
		tag selected by model -> dt (with 0.0135% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.3097% of the mistakes).
		tag selected by model -> di (with 1.4138% of the mistakes).
		tag selected by model -> nc (with 0.0404% of the mistakes).
		tag selected by model -> np (with 0.0269% of the mistakes).
		tag selected by model -> pr (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.4309% of the mistakes).
		tag selected by model -> vm (with 0.0673% of the mistakes).

	(original tag) pn: 
		tag selected by model -> dn (with 0.4174% of the mistakes).
		tag selected by model -> fe (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.3635% of the mistakes).
		tag selected by model -> nu (with 0.0135% of the mistakes).
		tag selected by model -> pi (with 0.0135% of the mistakes).

	(original tag) pp: 
		tag selected by model -> da (with 1.4811% of the mistakes).
		tag selected by model -> nc (with 0.0539% of the mistakes).
		tag selected by model -> np (with 0.0135% of the mistakes).
		tag selected by model -> p0 (with 1.1579% of the mistakes).
		tag selected by model -> rg (with 0.3231% of the mistakes).

	(original tag) pr: 
		tag selected by model -> cs (with 2.4371% of the mistakes).
		tag selected by model -> pi (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.0135% of the mistakes).

	(original tag) pt: 
		tag selected by model -> dt (with 0.0404% of the mistakes).
		tag selected by model -> p0 (with 0.0135% of the mistakes).
		tag selected by model -> pr (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.0269% of the mistakes).

	(original tag) px: 
		tag selected by model -> da (with 0.0135% of the mistakes).
		tag selected by model -> dp (with 0.0269% of the mistakes).
		tag selected by model -> np (with 0.0539% of the mistakes).
		tag selected by model -> pt (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 0.0135% of the mistakes).

	(original tag) rg: 
		tag selected by model -> ao (with 0.0135% of the mistakes).
		tag selected by model -> aq (with 0.7271% of the mistakes).
		tag selected by model -> cc (with 0.3501% of the mistakes).
		tag selected by model -> cs (with 0.0269% of the mistakes).
		tag selected by model -> da (with 0.3097% of the mistakes).
		tag selected by model -> di (with 0.0404% of the mistakes).
		tag selected by model -> fc (with 0.0135% of the mistakes).
		tag selected by model -> fe (with 0.0808% of the mistakes).
		tag selected by model -> fg (with 0.0539% of the mistakes).
		tag selected by model -> nc (with 0.6867% of the mistakes).
		tag selected by model -> np (with 0.8483% of the mistakes).
		tag selected by model -> p0 (with 0.0673% of the mistakes).
		tag selected by model -> pi (with 0.0404% of the mistakes).
		tag selected by model -> pp (with 0.0269% of the mistakes).
		tag selected by model -> pr (with 0.0404% of the mistakes).
		tag selected by model -> rn (with 0.3097% of the mistakes).
		tag selected by model -> sp (with 1.1175% of the mistakes).
		tag selected by model -> vm (with 0.5924% of the mistakes).

	(original tag) rn: 
		tag selected by model -> cc (with 0.0404% of the mistakes).
		tag selected by model -> da (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.1885% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> cc (with 0.0135% of the mistakes).
		tag selected by model -> cs (with 0.6463% of the mistakes).
		tag selected by model -> da (with 0.1750% of the mistakes).
		tag selected by model -> fc (with 0.0135% of the mistakes).
		tag selected by model -> fe (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.0269% of the mistakes).
		tag selected by model -> pr (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.1077% of the mistakes).
		tag selected by model -> vm (with 0.0404% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.0673% of the mistakes).
		tag selected by model -> cc (with 0.0808% of the mistakes).
		tag selected by model -> cs (with 0.0269% of the mistakes).
		tag selected by model -> fe (with 0.2289% of the mistakes).
		tag selected by model -> fg (with 0.0673% of the mistakes).
		tag selected by model -> fp (with 0.0269% of the mistakes).
		tag selected by model -> nc (with 0.0808% of the mistakes).
		tag selected by model -> np (with 0.1885% of the mistakes).
		tag selected by model -> pt (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.0269% of the mistakes).
		tag selected by model -> sp (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 0.0269% of the mistakes).

	(original tag) va: 
		tag selected by model -> nc (with 0.0673% of the mistakes).
		tag selected by model -> np (with 0.0135% of the mistakes).
		tag selected by model -> p0 (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 0.0269% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 2.5852% of the mistakes).
		tag selected by model -> cc (with 0.0135% of the mistakes).
		tag selected by model -> cs (with 0.0673% of the mistakes).
		tag selected by model -> da (with 1.2118% of the mistakes).
		tag selected by model -> di (with 0.0135% of the mistakes).
		tag selected by model -> fc (with 0.4443% of the mistakes).
		tag selected by model -> fd (with 0.0135% of the mistakes).
		tag selected by model -> fe (with 0.2289% of the mistakes).
		tag selected by model -> fg (with 0.3366% of the mistakes).
		tag selected by model -> fi (with 0.0269% of the mistakes).
		tag selected by model -> fp (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 3.0295% of the mistakes).
		tag selected by model -> np (with 1.5349% of the mistakes).
		tag selected by model -> p0 (with 0.1885% of the mistakes).
		tag selected by model -> pn (with 0.0135% of the mistakes).
		tag selected by model -> pp (with 0.0404% of the mistakes).
		tag selected by model -> pr (with 0.1616% of the mistakes).
		tag selected by model -> pt (with 0.0135% of the mistakes).
		tag selected by model -> px (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.7675% of the mistakes).
		tag selected by model -> rn (with 0.0539% of the mistakes).
		tag selected by model -> sp (with 4.5375% of the mistakes).
		tag selected by model -> un (with 0.0135% of the mistakes).
		tag selected by model -> va (with 0.1750% of the mistakes).
		tag selected by model -> vs (with 0.0808% of the mistakes).
		tag selected by model -> zm (with 0.0135% of the mistakes).

	(original tag) vs: 
		tag selected by model -> da (with 0.0269% of the mistakes).
		tag selected by model -> nc (with 0.4982% of the mistakes).
		tag selected by model -> np (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.0539% of the mistakes).
		tag selected by model -> sp (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 0.1885% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> fc (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.2962% of the mistakes).

	(original tag) zp: 
		tag selected by model -> da (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.6059% of the mistakes).
		tag selected by model -> np (with 0.1077% of the mistakes).
		tag selected by model -> pr (with 0.0135% of the mistakes).
		tag selected by model -> sp (with 0.0135% of the mistakes).

N = 3:

	Time:
		real	2m9.417s
		user	2m6.772s
		sys	0m0.456s
	Accuracy: 83.49%
	Accuracy of known words: 90.0640383174908%.
	Accuracy of unknown words: 9.935961682509205%.
	(original tag) ao: 
		tag selected by model -> nc (with 0.0384% of the mistakes).
		tag selected by model -> rg (with 0.0064% of the mistakes).

	(original tag) aq: 
		tag selected by model -> ao (with 0.0064% of the mistakes).
		tag selected by model -> cc (with 0.0767% of the mistakes).
		tag selected by model -> cs (with 0.1662% of the mistakes).
		tag selected by model -> da (with 0.8565% of the mistakes).
		tag selected by model -> dd (with 0.0384% of the mistakes).
		tag selected by model -> di (with 0.3004% of the mistakes).
		tag selected by model -> dn (with 0.0511% of the mistakes).
		tag selected by model -> dp (with 0.0128% of the mistakes).
		tag selected by model -> dt (with 0.0128% of the mistakes).
		tag selected by model -> fc (with 0.2621% of the mistakes).
		tag selected by model -> fd (with 0.0064% of the mistakes).
		tag selected by model -> fe (with 0.3068% of the mistakes).
		tag selected by model -> fg (with 0.0959% of the mistakes).
		tag selected by model -> fi (with 0.0064% of the mistakes).
		tag selected by model -> fp (with 0.6711% of the mistakes).
		tag selected by model -> fx (with 0.0767% of the mistakes).
		tag selected by model -> nc (with 5.5992% of the mistakes).
		tag selected by model -> np (with 0.4538% of the mistakes).
		tag selected by model -> nu (with 0.0128% of the mistakes).
		tag selected by model -> p0 (with 0.0447% of the mistakes).
		tag selected by model -> pd (with 0.0192% of the mistakes).
		tag selected by model -> pi (with 0.0192% of the mistakes).
		tag selected by model -> pn (with 0.0256% of the mistakes).
		tag selected by model -> pp (with 0.1278% of the mistakes).
		tag selected by model -> pr (with 0.1023% of the mistakes).
		tag selected by model -> rg (with 0.4602% of the mistakes).
		tag selected by model -> sp (with 1.6043% of the mistakes).
		tag selected by model -> un (with 0.0767% of the mistakes).
		tag selected by model -> va (with 0.0959% of the mistakes).
		tag selected by model -> vm (with 2.7677% of the mistakes).
		tag selected by model -> vs (with 0.0703% of the mistakes).
		tag selected by model -> zm (with 0.0511% of the mistakes).
		tag selected by model -> zp (with 0.0575% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0064% of the mistakes).
		tag selected by model -> cs (with 0.0128% of the mistakes).
		tag selected by model -> da (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0064% of the mistakes).
		tag selected by model -> np (with 0.0064% of the mistakes).
		tag selected by model -> rg (with 0.3963% of the mistakes).
		tag selected by model -> sp (with 0.0575% of the mistakes).
		tag selected by model -> vs (with 0.0064% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.0192% of the mistakes).
		tag selected by model -> cc (with 0.1662% of the mistakes).
		tag selected by model -> da (with 0.0384% of the mistakes).
		tag selected by model -> fc (with 0.0064% of the mistakes).
		tag selected by model -> fe (with 0.0128% of the mistakes).
		tag selected by model -> nc (with 0.0256% of the mistakes).
		tag selected by model -> np (with 0.0192% of the mistakes).
		tag selected by model -> pr (with 2.5823% of the mistakes).
		tag selected by model -> rg (with 0.0703% of the mistakes).
		tag selected by model -> sp (with 0.1598% of the mistakes).
		tag selected by model -> un (with 0.0384% of the mistakes).

	(original tag) da: 
		tag selected by model -> aq (with 0.0639% of the mistakes).
		tag selected by model -> cc (with 0.0064% of the mistakes).
		tag selected by model -> di (with 0.0447% of the mistakes).
		tag selected by model -> fc (with 0.0384% of the mistakes).
		tag selected by model -> fe (with 0.0064% of the mistakes).
		tag selected by model -> fg (with 0.0192% of the mistakes).
		tag selected by model -> fp (with 0.0895% of the mistakes).
		tag selected by model -> fx (with 0.0256% of the mistakes).
		tag selected by model -> nc (with 0.0511% of the mistakes).
		tag selected by model -> np (with 0.0320% of the mistakes).
		tag selected by model -> nu (with 0.0575% of the mistakes).
		tag selected by model -> p0 (with 0.0256% of the mistakes).
		tag selected by model -> pi (with 0.0128% of the mistakes).
		tag selected by model -> pn (with 0.0064% of the mistakes).
		tag selected by model -> pp (with 3.9118% of the mistakes).
		tag selected by model -> pr (with 0.0192% of the mistakes).
		tag selected by model -> rg (with 0.0128% of the mistakes).
		tag selected by model -> sp (with 0.1406% of the mistakes).
		tag selected by model -> un (with 0.0192% of the mistakes).
		tag selected by model -> va (with 0.0192% of the mistakes).
		tag selected by model -> vm (with 0.0384% of the mistakes).
		tag selected by model -> w (with 0.0639% of the mistakes).
		tag selected by model -> zm (with 0.0064% of the mistakes).
		tag selected by model -> zp (with 0.0064% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0192% of the mistakes).
		tag selected by model -> da (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0256% of the mistakes).
		tag selected by model -> np (with 0.0192% of the mistakes).
		tag selected by model -> pd (with 1.1441% of the mistakes).

	(original tag) de: 
		tag selected by model -> dt (with 0.0447% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.3643% of the mistakes).
		tag selected by model -> da (with 0.0256% of the mistakes).
		tag selected by model -> fc (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0320% of the mistakes).
		tag selected by model -> np (with 0.0064% of the mistakes).
		tag selected by model -> pi (with 3.0042% of the mistakes).
		tag selected by model -> pr (with 0.0064% of the mistakes).
		tag selected by model -> rg (with 0.1598% of the mistakes).
		tag selected by model -> un (with 0.1087% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.0064% of the mistakes).
		tag selected by model -> cc (with 0.0064% of the mistakes).
		tag selected by model -> da (with 0.0064% of the mistakes).
		tag selected by model -> di (with 0.1470% of the mistakes).
		tag selected by model -> nc (with 0.0128% of the mistakes).
		tag selected by model -> np (with 0.0064% of the mistakes).
		tag selected by model -> nu (with 0.0256% of the mistakes).
		tag selected by model -> pi (with 0.0320% of the mistakes).
		tag selected by model -> pn (with 1.3934% of the mistakes).
		tag selected by model -> rg (with 0.0064% of the mistakes).

	(original tag) dp: 
		tag selected by model -> px (with 0.3068% of the mistakes).

	(original tag) dt: 
		tag selected by model -> de (with 0.0128% of the mistakes).
		tag selected by model -> nc (with 0.0064% of the mistakes).
		tag selected by model -> pt (with 0.0192% of the mistakes).
		tag selected by model -> rn (with 0.0064% of the mistakes).

	(original tag) fe: 
		tag selected by model -> un (with 0.5817% of the mistakes).

	(original tag) fp: 
		tag selected by model -> un (with 2.8891% of the mistakes).

	(original tag) fs: 
		tag selected by model -> sp (with 0.0064% of the mistakes).
		tag selected by model -> zp (with 0.0064% of the mistakes).

	(original tag) fz: 
		tag selected by model -> da (with 0.0064% of the mistakes).
		tag selected by model -> di (with 0.0064% of the mistakes).
		tag selected by model -> fc (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0064% of the mistakes).
		tag selected by model -> nu (with 0.0192% of the mistakes).
		tag selected by model -> pr (with 0.0064% of the mistakes).
		tag selected by model -> sp (with 0.0192% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.1023% of the mistakes).
		tag selected by model -> aq (with 6.6858% of the mistakes).
		tag selected by model -> cc (with 0.2045% of the mistakes).
		tag selected by model -> cs (with 0.3260% of the mistakes).
		tag selected by model -> da (with 4.1163% of the mistakes).
		tag selected by model -> dd (with 0.2812% of the mistakes).
		tag selected by model -> de (with 0.0128% of the mistakes).
		tag selected by model -> di (with 0.1406% of the mistakes).
		tag selected by model -> dn (with 0.1534% of the mistakes).
		tag selected by model -> dp (with 0.0192% of the mistakes).
		tag selected by model -> fc (with 0.7031% of the mistakes).
		tag selected by model -> fd (with 0.0128% of the mistakes).
		tag selected by model -> fe (with 0.3516% of the mistakes).
		tag selected by model -> fg (with 0.1470% of the mistakes).
		tag selected by model -> fi (with 0.0192% of the mistakes).
		tag selected by model -> fp (with 0.9268% of the mistakes).
		tag selected by model -> fx (with 0.3452% of the mistakes).
		tag selected by model -> i (with 0.0064% of the mistakes).
		tag selected by model -> np (with 1.2592% of the mistakes).
		tag selected by model -> nu (with 0.0639% of the mistakes).
		tag selected by model -> p0 (with 0.2940% of the mistakes).
		tag selected by model -> pd (with 0.0511% of the mistakes).
		tag selected by model -> pi (with 0.0639% of the mistakes).
		tag selected by model -> pn (with 0.0831% of the mistakes).
		tag selected by model -> pp (with 0.1406% of the mistakes).
		tag selected by model -> pr (with 0.2109% of the mistakes).
		tag selected by model -> pt (with 0.0128% of the mistakes).
		tag selected by model -> rg (with 0.5113% of the mistakes).
		tag selected by model -> rn (with 0.1470% of the mistakes).
		tag selected by model -> sp (with 2.9147% of the mistakes).
		tag selected by model -> un (with 0.2812% of the mistakes).
		tag selected by model -> va (with 0.3260% of the mistakes).
		tag selected by model -> vm (with 2.8699% of the mistakes).
		tag selected by model -> vs (with 0.2621% of the mistakes).
		tag selected by model -> zm (with 0.0959% of the mistakes).
		tag selected by model -> zp (with 0.0447% of the mistakes).

	(original tag) np: 
		tag selected by model -> ao (with 0.0064% of the mistakes).
		tag selected by model -> aq (with 0.9396% of the mistakes).
		tag selected by model -> cc (with 0.3132% of the mistakes).
		tag selected by model -> cs (with 0.1087% of the mistakes).
		tag selected by model -> da (with 2.0709% of the mistakes).
		tag selected by model -> dd (with 0.0639% of the mistakes).
		tag selected by model -> de (with 0.0128% of the mistakes).
		tag selected by model -> di (with 0.1406% of the mistakes).
		tag selected by model -> dn (with 0.0064% of the mistakes).
		tag selected by model -> dp (with 0.0256% of the mistakes).
		tag selected by model -> fc (with 0.4602% of the mistakes).
		tag selected by model -> fd (with 0.0128% of the mistakes).
		tag selected by model -> fe (with 0.2045% of the mistakes).
		tag selected by model -> fg (with 0.0639% of the mistakes).
		tag selected by model -> fp (with 0.7031% of the mistakes).
		tag selected by model -> fx (with 0.2237% of the mistakes).
		tag selected by model -> nc (with 1.5276% of the mistakes).
		tag selected by model -> nu (with 0.1342% of the mistakes).
		tag selected by model -> p0 (with 0.1981% of the mistakes).
		tag selected by model -> pd (with 0.0703% of the mistakes).
		tag selected by model -> pi (with 0.0575% of the mistakes).
		tag selected by model -> pp (with 0.1214% of the mistakes).
		tag selected by model -> pr (with 0.2237% of the mistakes).
		tag selected by model -> rg (with 0.3324% of the mistakes).
		tag selected by model -> rn (with 0.0895% of the mistakes).
		tag selected by model -> sp (with 2.8699% of the mistakes).
		tag selected by model -> un (with 0.0064% of the mistakes).
		tag selected by model -> va (with 0.1662% of the mistakes).
		tag selected by model -> vm (with 0.7287% of the mistakes).
		tag selected by model -> vs (with 0.0384% of the mistakes).
		tag selected by model -> z (with 0.0064% of the mistakes).
		tag selected by model -> zm (with 0.0128% of the mistakes).
		tag selected by model -> zp (with 0.0767% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.1023% of the mistakes).
		tag selected by model -> cs (with 0.0064% of the mistakes).
		tag selected by model -> da (with 0.1151% of the mistakes).
		tag selected by model -> de (with 0.0064% of the mistakes).
		tag selected by model -> di (with 0.0256% of the mistakes).
		tag selected by model -> dn (with 0.0128% of the mistakes).
		tag selected by model -> fc (with 0.0320% of the mistakes).
		tag selected by model -> fe (with 0.0192% of the mistakes).
		tag selected by model -> fp (with 0.0895% of the mistakes).
		tag selected by model -> fx (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.2173% of the mistakes).
		tag selected by model -> np (with 0.0575% of the mistakes).
		tag selected by model -> pn (with 0.0384% of the mistakes).
		tag selected by model -> pp (with 0.0128% of the mistakes).
		tag selected by model -> pt (with 0.0128% of the mistakes).
		tag selected by model -> rg (with 0.0192% of the mistakes).
		tag selected by model -> sp (with 0.1342% of the mistakes).
		tag selected by model -> vm (with 0.0575% of the mistakes).
		tag selected by model -> z (with 0.0192% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.3899% of the mistakes).

	(original tag) pd: 
		tag selected by model -> aq (with 0.0064% of the mistakes).
		tag selected by model -> dd (with 0.0703% of the mistakes).
		tag selected by model -> nc (with 0.0064% of the mistakes).
		tag selected by model -> sp (with 0.0064% of the mistakes).

	(original tag) pe: 
		tag selected by model -> dt (with 0.0064% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0320% of the mistakes).
		tag selected by model -> da (with 0.0064% of the mistakes).
		tag selected by model -> di (with 0.7670% of the mistakes).
		tag selected by model -> pr (with 0.0064% of the mistakes).
		tag selected by model -> rg (with 0.0831% of the mistakes).
		tag selected by model -> sp (with 0.0128% of the mistakes).
		tag selected by model -> un (with 0.0128% of the mistakes).
		tag selected by model -> vm (with 0.0128% of the mistakes).

	(original tag) pn: 
		tag selected by model -> aq (with 0.0128% of the mistakes).
		tag selected by model -> dn (with 0.1918% of the mistakes).
		tag selected by model -> fp (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0128% of the mistakes).
		tag selected by model -> pi (with 0.0064% of the mistakes).

	(original tag) pp: 
		tag selected by model -> da (with 0.5944% of the mistakes).
		tag selected by model -> fe (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0064% of the mistakes).
		tag selected by model -> p0 (with 0.3771% of the mistakes).
		tag selected by model -> rg (with 0.0703% of the mistakes).
		tag selected by model -> sp (with 0.0064% of the mistakes).

	(original tag) pr: 
		tag selected by model -> cs (with 3.7584% of the mistakes).
		tag selected by model -> pi (with 0.0384% of the mistakes).
		tag selected by model -> rg (with 0.0320% of the mistakes).
		tag selected by model -> un (with 0.0511% of the mistakes).

	(original tag) pt: 
		tag selected by model -> cs (with 0.0064% of the mistakes).
		tag selected by model -> de (with 0.0639% of the mistakes).
		tag selected by model -> dt (with 0.2429% of the mistakes).
		tag selected by model -> pr (with 0.0064% of the mistakes).

	(original tag) px: 
		tag selected by model -> cc (with 0.0064% of the mistakes).
		tag selected by model -> da (with 0.0064% of the mistakes).
		tag selected by model -> fc (with 0.0064% of the mistakes).
		tag selected by model -> pp (with 0.0064% of the mistakes).
		tag selected by model -> rg (with 0.0128% of the mistakes).
		tag selected by model -> sp (with 0.0064% of the mistakes).

	(original tag) rg: 
		tag selected by model -> ao (with 0.0384% of the mistakes).
		tag selected by model -> aq (with 0.2812% of the mistakes).
		tag selected by model -> cc (with 0.2045% of the mistakes).
		tag selected by model -> cs (with 0.0384% of the mistakes).
		tag selected by model -> da (with 0.2748% of the mistakes).
		tag selected by model -> di (with 0.1470% of the mistakes).
		tag selected by model -> dn (with 0.0064% of the mistakes).
		tag selected by model -> dp (with 0.0064% of the mistakes).
		tag selected by model -> dt (with 0.0064% of the mistakes).
		tag selected by model -> fc (with 0.0320% of the mistakes).
		tag selected by model -> fe (with 0.0831% of the mistakes).
		tag selected by model -> fg (with 0.0064% of the mistakes).
		tag selected by model -> fp (with 0.0895% of the mistakes).
		tag selected by model -> fx (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.2365% of the mistakes).
		tag selected by model -> np (with 0.0831% of the mistakes).
		tag selected by model -> p0 (with 0.0192% of the mistakes).
		tag selected by model -> pi (with 0.2109% of the mistakes).
		tag selected by model -> pn (with 0.0192% of the mistakes).
		tag selected by model -> pp (with 0.0575% of the mistakes).
		tag selected by model -> pr (with 0.0128% of the mistakes).
		tag selected by model -> rn (with 0.1534% of the mistakes).
		tag selected by model -> sp (with 0.5177% of the mistakes).
		tag selected by model -> un (with 0.0575% of the mistakes).
		tag selected by model -> va (with 0.0064% of the mistakes).
		tag selected by model -> vm (with 0.2748% of the mistakes).
		tag selected by model -> vs (with 0.0384% of the mistakes).
		tag selected by model -> zp (with 0.0128% of the mistakes).

	(original tag) rn: 
		tag selected by model -> cc (with 0.0256% of the mistakes).
		tag selected by model -> da (with 0.0064% of the mistakes).
		tag selected by model -> rg (with 0.0447% of the mistakes).

	(original tag) sp: 
		tag selected by model -> ao (with 0.0064% of the mistakes).
		tag selected by model -> aq (with 0.1023% of the mistakes).
		tag selected by model -> cc (with 0.0511% of the mistakes).
		tag selected by model -> cs (with 0.4538% of the mistakes).
		tag selected by model -> da (with 0.0575% of the mistakes).
		tag selected by model -> di (with 0.0064% of the mistakes).
		tag selected by model -> dn (with 0.0064% of the mistakes).
		tag selected by model -> fe (with 0.0256% of the mistakes).
		tag selected by model -> fg (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.2557% of the mistakes).
		tag selected by model -> np (with 0.1342% of the mistakes).
		tag selected by model -> pr (with 0.0064% of the mistakes).
		tag selected by model -> rg (with 0.3963% of the mistakes).
		tag selected by model -> un (with 3.7840% of the mistakes).
		tag selected by model -> vm (with 0.1534% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.0128% of the mistakes).
		tag selected by model -> cs (with 0.0064% of the mistakes).
		tag selected by model -> da (with 0.0384% of the mistakes).
		tag selected by model -> fe (with 0.1087% of the mistakes).
		tag selected by model -> fg (with 0.0256% of the mistakes).
		tag selected by model -> fi (with 0.0064% of the mistakes).
		tag selected by model -> fp (with 0.0128% of the mistakes).
		tag selected by model -> fz (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0447% of the mistakes).
		tag selected by model -> np (with 0.0064% of the mistakes).
		tag selected by model -> nu (with 0.0128% of the mistakes).
		tag selected by model -> pr (with 0.0128% of the mistakes).
		tag selected by model -> pt (with 0.0064% of the mistakes).
		tag selected by model -> rg (with 0.0128% of the mistakes).
		tag selected by model -> sp (with 0.0320% of the mistakes).
		tag selected by model -> vm (with 0.0192% of the mistakes).
		tag selected by model -> zp (with 0.0128% of the mistakes).

	(original tag) va: 
		tag selected by model -> da (with 0.0064% of the mistakes).
		tag selected by model -> fc (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0064% of the mistakes).
		tag selected by model -> rn (with 0.0064% of the mistakes).
		tag selected by model -> sp (with 0.0064% of the mistakes).
		tag selected by model -> vm (with 0.0064% of the mistakes).

	(original tag) vm: 
		tag selected by model -> ao (with 0.1087% of the mistakes).
		tag selected by model -> aq (with 3.0745% of the mistakes).
		tag selected by model -> cc (with 0.1662% of the mistakes).
		tag selected by model -> cs (with 0.2748% of the mistakes).
		tag selected by model -> da (with 1.1633% of the mistakes).
		tag selected by model -> dd (with 0.1534% of the mistakes).
		tag selected by model -> di (with 0.4346% of the mistakes).
		tag selected by model -> dn (with 0.1726% of the mistakes).
		tag selected by model -> dp (with 0.0192% of the mistakes).
		tag selected by model -> fc (with 0.3899% of the mistakes).
		tag selected by model -> fe (with 0.4666% of the mistakes).
		tag selected by model -> fg (with 0.0320% of the mistakes).
		tag selected by model -> fi (with 0.0256% of the mistakes).
		tag selected by model -> fp (with 0.2301% of the mistakes).
		tag selected by model -> fx (with 0.0895% of the mistakes).
		tag selected by model -> nc (with 1.5916% of the mistakes).
		tag selected by model -> np (with 0.3643% of the mistakes).
		tag selected by model -> nu (with 0.0639% of the mistakes).
		tag selected by model -> p0 (with 0.1214% of the mistakes).
		tag selected by model -> pd (with 0.0128% of the mistakes).
		tag selected by model -> pi (with 0.0447% of the mistakes).
		tag selected by model -> pp (with 0.0959% of the mistakes).
		tag selected by model -> pr (with 0.1214% of the mistakes).
		tag selected by model -> pt (with 0.0575% of the mistakes).
		tag selected by model -> rg (with 0.4922% of the mistakes).
		tag selected by model -> rn (with 0.1087% of the mistakes).
		tag selected by model -> sp (with 2.5503% of the mistakes).
		tag selected by model -> un (with 0.0575% of the mistakes).
		tag selected by model -> va (with 0.1981% of the mistakes).
		tag selected by model -> vs (with 0.2109% of the mistakes).
		tag selected by model -> zm (with 0.0192% of the mistakes).
		tag selected by model -> zp (with 0.0767% of the mistakes).

	(original tag) vs: 
		tag selected by model -> aq (with 0.0128% of the mistakes).
		tag selected by model -> da (with 0.0192% of the mistakes).
		tag selected by model -> fe (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0895% of the mistakes).
		tag selected by model -> np (with 0.0064% of the mistakes).
		tag selected by model -> rg (with 0.0384% of the mistakes).
		tag selected by model -> vm (with 0.0064% of the mistakes).

	(original tag) zm: 
		tag selected by model -> da (with 0.0064% of the mistakes).
		tag selected by model -> fc (with 0.0064% of the mistakes).
		tag selected by model -> nc (with 0.0064% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0384% of the mistakes).
		tag selected by model -> cc (with 0.0128% of the mistakes).
		tag selected by model -> cs (with 0.0128% of the mistakes).
		tag selected by model -> da (with 0.0959% of the mistakes).
		tag selected by model -> di (with 0.0064% of the mistakes).
		tag selected by model -> fc (with 0.0064% of the mistakes).
		tag selected by model -> fx (with 0.0320% of the mistakes).
		tag selected by model -> nc (with 0.0256% of the mistakes).
		tag selected by model -> np (with 0.0192% of the mistakes).
		tag selected by model -> nu (with 0.0064% of the mistakes).
		tag selected by model -> sp (with 0.0895% of the mistakes).
		tag selected by model -> vm (with 0.0128% of the mistakes).

N = 4:

	Time:
		real	29m25.166s
		user	28m57.416s
		sys	0m3.584s
	Accuracy: 85.37%
	Accuracy of known words: 90.0640383174908%.
	Accuracy of unknown words: 9.935961682509205%.
	(original tag) ao: 
		tag selected by model -> rg (with 0.0216% of the mistakes).

	(original tag) aq: 
		tag selected by model -> ao (with 0.0144% of the mistakes).
		tag selected by model -> cc (with 0.3389% of the mistakes).
		tag selected by model -> cs (with 0.3894% of the mistakes).
		tag selected by model -> da (with 2.2642% of the mistakes).
		tag selected by model -> dd (with 0.1803% of the mistakes).
		tag selected by model -> de (with 0.0288% of the mistakes).
		tag selected by model -> di (with 0.2956% of the mistakes).
		tag selected by model -> dn (with 0.0721% of the mistakes).
		tag selected by model -> dp (with 0.0649% of the mistakes).
		tag selected by model -> dt (with 0.0144% of the mistakes).
		tag selected by model -> fa (with 0.0144% of the mistakes).
		tag selected by model -> fc (with 0.3605% of the mistakes).
		tag selected by model -> fd (with 0.0144% of the mistakes).
		tag selected by model -> fe (with 0.1803% of the mistakes).
		tag selected by model -> fg (with 0.0649% of the mistakes).
		tag selected by model -> fh (with 0.0216% of the mistakes).
		tag selected by model -> fi (with 0.0505% of the mistakes).
		tag selected by model -> fp (with 0.0865% of the mistakes).
		tag selected by model -> fx (with 0.1803% of the mistakes).
		tag selected by model -> fz (with 0.0144% of the mistakes).
		tag selected by model -> i (with 0.0216% of the mistakes).
		tag selected by model -> nc (with 4.1246% of the mistakes).
		tag selected by model -> np (with 0.5624% of the mistakes).
		tag selected by model -> nu (with 0.2452% of the mistakes).
		tag selected by model -> ot (with 0.0144% of the mistakes).
		tag selected by model -> p0 (with 0.1082% of the mistakes).
		tag selected by model -> pd (with 0.0361% of the mistakes).
		tag selected by model -> pi (with 0.0144% of the mistakes).
		tag selected by model -> pn (with 0.0721% of the mistakes).
		tag selected by model -> pp (with 0.0072% of the mistakes).
		tag selected by model -> pr (with 0.1875% of the mistakes).
		tag selected by model -> pt (with 0.0505% of the mistakes).
		tag selected by model -> px (with 0.0577% of the mistakes).
		tag selected by model -> rg (with 0.5408% of the mistakes).
		tag selected by model -> rn (with 0.0577% of the mistakes).
		tag selected by model -> sp (with 1.6297% of the mistakes).
		tag selected by model -> un (with 0.1658% of the mistakes).
		tag selected by model -> va (with 0.0361% of the mistakes).
		tag selected by model -> vm (with 3.5189% of the mistakes).
		tag selected by model -> vs (with 0.0865% of the mistakes).
		tag selected by model -> zm (with 0.0505% of the mistakes).
		tag selected by model -> zp (with 0.0433% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0361% of the mistakes).
		tag selected by model -> cs (with 0.0072% of the mistakes).
		tag selected by model -> da (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.0144% of the mistakes).
		tag selected by model -> np (with 0.0072% of the mistakes).
		tag selected by model -> rg (with 0.4254% of the mistakes).
		tag selected by model -> sp (with 0.0144% of the mistakes).
		tag selected by model -> vm (with 0.0072% of the mistakes).
		tag selected by model -> vs (with 0.0072% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.0072% of the mistakes).
		tag selected by model -> cc (with 0.1514% of the mistakes).
		tag selected by model -> da (with 0.0793% of the mistakes).
		tag selected by model -> di (with 0.0072% of the mistakes).
		tag selected by model -> fe (with 0.0072% of the mistakes).
		tag selected by model -> fg (with 0.0072% of the mistakes).
		tag selected by model -> fh (with 0.0072% of the mistakes).
		tag selected by model -> fx (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.0216% of the mistakes).
		tag selected by model -> pr (with 5.2855% of the mistakes).
		tag selected by model -> pt (with 0.0072% of the mistakes).
		tag selected by model -> rg (with 0.0721% of the mistakes).
		tag selected by model -> sp (with 0.0865% of the mistakes).
		tag selected by model -> un (with 0.0216% of the mistakes).
		tag selected by model -> vm (with 0.0361% of the mistakes).

	(original tag) da: 
		tag selected by model -> ao (with 0.0072% of the mistakes).
		tag selected by model -> aq (with 0.0721% of the mistakes).
		tag selected by model -> cc (with 0.0144% of the mistakes).
		tag selected by model -> cs (with 0.0288% of the mistakes).
		tag selected by model -> dd (with 0.0072% of the mistakes).
		tag selected by model -> di (with 0.0216% of the mistakes).
		tag selected by model -> dn (with 0.0072% of the mistakes).
		tag selected by model -> dp (with 0.0072% of the mistakes).
		tag selected by model -> fc (with 0.0433% of the mistakes).
		tag selected by model -> fd (with 0.0072% of the mistakes).
		tag selected by model -> fg (with 0.0361% of the mistakes).
		tag selected by model -> fi (with 0.0288% of the mistakes).
		tag selected by model -> fp (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.1586% of the mistakes).
		tag selected by model -> np (with 0.0793% of the mistakes).
		tag selected by model -> nu (with 0.0577% of the mistakes).
		tag selected by model -> pi (with 0.0577% of the mistakes).
		tag selected by model -> pn (with 0.0072% of the mistakes).
		tag selected by model -> pp (with 2.6247% of the mistakes).
		tag selected by model -> pr (with 0.0072% of the mistakes).
		tag selected by model -> rg (with 0.0288% of the mistakes).
		tag selected by model -> rn (with 0.0072% of the mistakes).
		tag selected by model -> sp (with 0.1226% of the mistakes).
		tag selected by model -> un (with 0.0072% of the mistakes).
		tag selected by model -> vm (with 0.1082% of the mistakes).
		tag selected by model -> w (with 0.0649% of the mistakes).
		tag selected by model -> zp (with 0.0072% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0072% of the mistakes).
		tag selected by model -> da (with 0.0072% of the mistakes).
		tag selected by model -> pd (with 0.4831% of the mistakes).
		tag selected by model -> rg (with 0.0072% of the mistakes).

	(original tag) de: 
		tag selected by model -> dt (with 0.0288% of the mistakes).
		tag selected by model -> pt (with 0.0288% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.3533% of the mistakes).
		tag selected by model -> da (with 0.0216% of the mistakes).
		tag selected by model -> nc (with 0.0144% of the mistakes).
		tag selected by model -> np (with 0.0072% of the mistakes).
		tag selected by model -> nu (with 0.0072% of the mistakes).
		tag selected by model -> pi (with 3.5045% of the mistakes).
		tag selected by model -> pr (with 0.0072% of the mistakes).
		tag selected by model -> rg (with 0.1370% of the mistakes).
		tag selected by model -> un (with 0.0216% of the mistakes).
		tag selected by model -> vm (with 0.0072% of the mistakes).

	(original tag) dn: 
		tag selected by model -> ao (with 0.0072% of the mistakes).
		tag selected by model -> aq (with 0.0144% of the mistakes).
		tag selected by model -> da (with 0.0144% of the mistakes).
		tag selected by model -> di (with 0.1803% of the mistakes).
		tag selected by model -> nu (with 0.0144% of the mistakes).
		tag selected by model -> pi (with 0.0216% of the mistakes).
		tag selected by model -> pn (with 0.6634% of the mistakes).
		tag selected by model -> sp (with 0.0144% of the mistakes).

	(original tag) dp: 
		tag selected by model -> pp (with 0.0072% of the mistakes).
		tag selected by model -> px (with 0.3101% of the mistakes).

	(original tag) dt: 
		tag selected by model -> da (with 0.0072% of the mistakes).
		tag selected by model -> de (with 0.0288% of the mistakes).
		tag selected by model -> nc (with 0.0072% of the mistakes).
		tag selected by model -> pt (with 0.0216% of the mistakes).

	(original tag) fe: 
		tag selected by model -> un (with 0.1875% of the mistakes).

	(original tag) fp: 
		tag selected by model -> un (with 0.2380% of the mistakes).

	(original tag) fs: 
		tag selected by model -> nc (with 0.0072% of the mistakes).
		tag selected by model -> p0 (with 0.0072% of the mistakes).

	(original tag) fz: 
		tag selected by model -> da (with 0.0072% of the mistakes).
		tag selected by model -> dd (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.0072% of the mistakes).
		tag selected by model -> np (with 0.0072% of the mistakes).
		tag selected by model -> nu (with 0.0216% of the mistakes).
		tag selected by model -> sp (with 0.0288% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.1370% of the mistakes).
		tag selected by model -> aq (with 5.9057% of the mistakes).
		tag selected by model -> cc (with 0.3894% of the mistakes).
		tag selected by model -> cs (with 0.4975% of the mistakes).
		tag selected by model -> da (with 3.5477% of the mistakes).
		tag selected by model -> dd (with 0.1226% of the mistakes).
		tag selected by model -> de (with 0.0649% of the mistakes).
		tag selected by model -> di (with 0.4110% of the mistakes).
		tag selected by model -> dn (with 0.1010% of the mistakes).
		tag selected by model -> dp (with 0.0721% of the mistakes).
		tag selected by model -> dt (with 0.0144% of the mistakes).
		tag selected by model -> fa (with 0.1370% of the mistakes).
		tag selected by model -> fc (with 0.6490% of the mistakes).
		tag selected by model -> fd (with 0.0216% of the mistakes).
		tag selected by model -> fe (with 0.2740% of the mistakes).
		tag selected by model -> fg (with 0.1082% of the mistakes).
		tag selected by model -> fh (with 0.0361% of the mistakes).
		tag selected by model -> fi (with 0.0072% of the mistakes).
		tag selected by model -> fp (with 0.0937% of the mistakes).
		tag selected by model -> fs (with 0.0072% of the mistakes).
		tag selected by model -> fx (with 0.1010% of the mistakes).
		tag selected by model -> fz (with 0.0649% of the mistakes).
		tag selected by model -> i (with 0.0144% of the mistakes).
		tag selected by model -> np (with 1.3773% of the mistakes).
		tag selected by model -> nu (with 0.0649% of the mistakes).
		tag selected by model -> ot (with 0.0505% of the mistakes).
		tag selected by model -> p0 (with 0.1370% of the mistakes).
		tag selected by model -> pd (with 0.0505% of the mistakes).
		tag selected by model -> pi (with 0.6346% of the mistakes).
		tag selected by model -> pn (with 0.1226% of the mistakes).
		tag selected by model -> pp (with 0.1010% of the mistakes).
		tag selected by model -> pr (with 0.1803% of the mistakes).
		tag selected by model -> px (with 0.0649% of the mistakes).
		tag selected by model -> rg (with 0.7211% of the mistakes).
		tag selected by model -> rn (with 0.1947% of the mistakes).
		tag selected by model -> sp (with 3.2377% of the mistakes).
		tag selected by model -> un (with 0.2596% of the mistakes).
		tag selected by model -> va (with 0.0577% of the mistakes).
		tag selected by model -> vm (with 3.3458% of the mistakes).
		tag selected by model -> vs (with 0.3461% of the mistakes).
		tag selected by model -> z (with 0.0072% of the mistakes).
		tag selected by model -> zm (with 0.0721% of the mistakes).
		tag selected by model -> zp (with 0.0793% of the mistakes).
		tag selected by model -> zu (with 0.0144% of the mistakes).

	(original tag) np: 
		tag selected by model -> ao (with 0.0865% of the mistakes).
		tag selected by model -> aq (with 0.9879% of the mistakes).
		tag selected by model -> cc (with 0.3029% of the mistakes).
		tag selected by model -> cs (with 0.3389% of the mistakes).
		tag selected by model -> da (with 2.0551% of the mistakes).
		tag selected by model -> dd (with 0.0433% of the mistakes).
		tag selected by model -> de (with 0.0072% of the mistakes).
		tag selected by model -> di (with 0.1586% of the mistakes).
		tag selected by model -> dn (with 0.0288% of the mistakes).
		tag selected by model -> dp (with 0.0649% of the mistakes).
		tag selected by model -> dt (with 0.0144% of the mistakes).
		tag selected by model -> fa (with 0.0361% of the mistakes).
		tag selected by model -> fc (with 0.3101% of the mistakes).
		tag selected by model -> fd (with 0.0144% of the mistakes).
		tag selected by model -> fe (with 0.1442% of the mistakes).
		tag selected by model -> fg (with 0.1082% of the mistakes).
		tag selected by model -> fh (with 0.0072% of the mistakes).
		tag selected by model -> fi (with 0.0144% of the mistakes).
		tag selected by model -> fp (with 0.0937% of the mistakes).
		tag selected by model -> fx (with 0.0649% of the mistakes).
		tag selected by model -> fz (with 0.0072% of the mistakes).
		tag selected by model -> i (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 3.1079% of the mistakes).
		tag selected by model -> nu (with 0.1226% of the mistakes).
		tag selected by model -> ot (with 0.0072% of the mistakes).
		tag selected by model -> p0 (with 0.1154% of the mistakes).
		tag selected by model -> pd (with 0.1010% of the mistakes).
		tag selected by model -> pi (with 0.3461% of the mistakes).
		tag selected by model -> pn (with 0.0361% of the mistakes).
		tag selected by model -> pp (with 0.0144% of the mistakes).
		tag selected by model -> pr (with 0.0433% of the mistakes).
		tag selected by model -> pt (with 0.0433% of the mistakes).
		tag selected by model -> px (with 0.0288% of the mistakes).
		tag selected by model -> rg (with 0.4327% of the mistakes).
		tag selected by model -> rn (with 0.0433% of the mistakes).
		tag selected by model -> sp (with 1.7234% of the mistakes).
		tag selected by model -> un (with 0.0072% of the mistakes).
		tag selected by model -> va (with 0.0361% of the mistakes).
		tag selected by model -> vm (with 1.3556% of the mistakes).
		tag selected by model -> vs (with 0.1154% of the mistakes).
		tag selected by model -> w (with 0.0072% of the mistakes).
		tag selected by model -> zm (with 0.0216% of the mistakes).
		tag selected by model -> zp (with 0.0577% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.0865% of the mistakes).
		tag selected by model -> cc (with 0.0216% of the mistakes).
		tag selected by model -> cs (with 0.0433% of the mistakes).
		tag selected by model -> da (with 0.1442% of the mistakes).
		tag selected by model -> di (with 0.0072% of the mistakes).
		tag selected by model -> dn (with 0.0216% of the mistakes).
		tag selected by model -> fc (with 0.0072% of the mistakes).
		tag selected by model -> fd (with 0.0072% of the mistakes).
		tag selected by model -> fh (with 0.0072% of the mistakes).
		tag selected by model -> fi (with 0.0072% of the mistakes).
		tag selected by model -> fp (with 0.0288% of the mistakes).
		tag selected by model -> nc (with 0.2091% of the mistakes).
		tag selected by model -> np (with 0.1298% of the mistakes).
		tag selected by model -> pd (with 0.0072% of the mistakes).
		tag selected by model -> pr (with 0.0288% of the mistakes).
		tag selected by model -> rg (with 0.0144% of the mistakes).
		tag selected by model -> sp (with 0.0793% of the mistakes).
		tag selected by model -> vm (with 0.1586% of the mistakes).
		tag selected by model -> vs (with 0.0072% of the mistakes).
		tag selected by model -> z (with 0.0361% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.2524% of the mistakes).

	(original tag) pd: 
		tag selected by model -> dd (with 0.0865% of the mistakes).
		tag selected by model -> fi (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.0144% of the mistakes).

	(original tag) pe: 
		tag selected by model -> dt (with 0.0072% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0072% of the mistakes).
		tag selected by model -> cs (with 0.0072% of the mistakes).
		tag selected by model -> da (with 0.0144% of the mistakes).
		tag selected by model -> di (with 0.7499% of the mistakes).
		tag selected by model -> pr (with 0.0072% of the mistakes).
		tag selected by model -> rg (with 0.1154% of the mistakes).
		tag selected by model -> un (with 0.0144% of the mistakes).

	(original tag) pn: 
		tag selected by model -> aq (with 0.0072% of the mistakes).
		tag selected by model -> cc (with 0.0072% of the mistakes).
		tag selected by model -> dn (with 0.2019% of the mistakes).
		tag selected by model -> nc (with 0.0144% of the mistakes).
		tag selected by model -> pi (with 0.0072% of the mistakes).

	(original tag) pp: 
		tag selected by model -> da (with 1.1177% of the mistakes).
		tag selected by model -> p0 (with 0.4831% of the mistakes).
		tag selected by model -> rg (with 0.0865% of the mistakes).
		tag selected by model -> sp (with 0.0072% of the mistakes).
		tag selected by model -> un (with 0.0072% of the mistakes).

	(original tag) pr: 
		tag selected by model -> cs (with 4.9322% of the mistakes).
		tag selected by model -> rg (with 0.0216% of the mistakes).

	(original tag) pt: 
		tag selected by model -> de (with 0.0649% of the mistakes).
		tag selected by model -> dt (with 0.2884% of the mistakes).
		tag selected by model -> pr (with 0.0072% of the mistakes).
		tag selected by model -> sp (with 0.0072% of the mistakes).

	(original tag) px: 
		tag selected by model -> da (with 0.0072% of the mistakes).
		tag selected by model -> sp (with 0.0144% of the mistakes).
		tag selected by model -> vm (with 0.0288% of the mistakes).

	(original tag) rg: 
		tag selected by model -> ao (with 0.0288% of the mistakes).
		tag selected by model -> aq (with 0.2235% of the mistakes).
		tag selected by model -> cc (with 0.2307% of the mistakes).
		tag selected by model -> cs (with 0.0865% of the mistakes).
		tag selected by model -> da (with 0.4687% of the mistakes).
		tag selected by model -> de (with 0.0072% of the mistakes).
		tag selected by model -> di (with 0.1226% of the mistakes).
		tag selected by model -> dn (with 0.0288% of the mistakes).
		tag selected by model -> fc (with 0.0577% of the mistakes).
		tag selected by model -> fe (with 0.0144% of the mistakes).
		tag selected by model -> fg (with 0.0144% of the mistakes).
		tag selected by model -> fh (with 0.0072% of the mistakes).
		tag selected by model -> fi (with 0.0144% of the mistakes).
		tag selected by model -> fx (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.4038% of the mistakes).
		tag selected by model -> np (with 0.1154% of the mistakes).
		tag selected by model -> pi (with 0.2163% of the mistakes).
		tag selected by model -> pn (with 0.0216% of the mistakes).
		tag selected by model -> pp (with 0.0505% of the mistakes).
		tag selected by model -> pr (with 0.0433% of the mistakes).
		tag selected by model -> pt (with 0.0072% of the mistakes).
		tag selected by model -> rn (with 0.1731% of the mistakes).
		tag selected by model -> sp (with 0.4831% of the mistakes).
		tag selected by model -> un (with 0.0865% of the mistakes).
		tag selected by model -> va (with 0.0144% of the mistakes).
		tag selected by model -> vm (with 0.2163% of the mistakes).
		tag selected by model -> vs (with 0.0288% of the mistakes).
		tag selected by model -> zp (with 0.0072% of the mistakes).

	(original tag) rn: 
		tag selected by model -> cc (with 0.0216% of the mistakes).
		tag selected by model -> nc (with 0.0072% of the mistakes).
		tag selected by model -> rg (with 0.0361% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.0433% of the mistakes).
		tag selected by model -> cc (with 0.0865% of the mistakes).
		tag selected by model -> cs (with 0.5624% of the mistakes).
		tag selected by model -> da (with 0.0937% of the mistakes).
		tag selected by model -> fe (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.2091% of the mistakes).
		tag selected by model -> np (with 0.0505% of the mistakes).
		tag selected by model -> pd (with 0.0072% of the mistakes).
		tag selected by model -> rg (with 0.1947% of the mistakes).
		tag selected by model -> un (with 0.1947% of the mistakes).
		tag selected by model -> va (with 0.0072% of the mistakes).
		tag selected by model -> vm (with 0.0649% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.0072% of the mistakes).
		tag selected by model -> cs (with 0.0144% of the mistakes).
		tag selected by model -> da (with 0.0361% of the mistakes).
		tag selected by model -> di (with 0.0288% of the mistakes).
		tag selected by model -> fe (with 0.0865% of the mistakes).
		tag selected by model -> fg (with 0.0144% of the mistakes).
		tag selected by model -> fp (with 0.0144% of the mistakes).
		tag selected by model -> fz (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.0793% of the mistakes).
		tag selected by model -> np (with 0.0288% of the mistakes).
		tag selected by model -> p0 (with 0.0072% of the mistakes).
		tag selected by model -> pt (with 0.0072% of the mistakes).
		tag selected by model -> rg (with 0.0144% of the mistakes).
		tag selected by model -> sp (with 0.0288% of the mistakes).
		tag selected by model -> va (with 0.0072% of the mistakes).
		tag selected by model -> vm (with 0.0216% of the mistakes).

	(original tag) va: 
		tag selected by model -> dn (with 0.0072% of the mistakes).
		tag selected by model -> fc (with 0.0144% of the mistakes).
		tag selected by model -> nc (with 0.0072% of the mistakes).
		tag selected by model -> vm (with 0.0072% of the mistakes).

	(original tag) vm: 
		tag selected by model -> ao (with 0.0361% of the mistakes).
		tag selected by model -> aq (with 2.4156% of the mistakes).
		tag selected by model -> cc (with 0.2163% of the mistakes).
		tag selected by model -> cs (with 0.2884% of the mistakes).
		tag selected by model -> da (with 2.7041% of the mistakes).
		tag selected by model -> dd (with 0.1082% of the mistakes).
		tag selected by model -> de (with 0.0505% of the mistakes).
		tag selected by model -> di (with 0.1514% of the mistakes).
		tag selected by model -> dn (with 0.0505% of the mistakes).
		tag selected by model -> dp (with 0.0361% of the mistakes).
		tag selected by model -> dt (with 0.0577% of the mistakes).
		tag selected by model -> fa (with 0.0361% of the mistakes).
		tag selected by model -> fc (with 0.3461% of the mistakes).
		tag selected by model -> fd (with 0.0288% of the mistakes).
		tag selected by model -> fe (with 0.1298% of the mistakes).
		tag selected by model -> fg (with 0.0649% of the mistakes).
		tag selected by model -> fh (with 0.0361% of the mistakes).
		tag selected by model -> fi (with 0.0288% of the mistakes).
		tag selected by model -> fp (with 0.1226% of the mistakes).
		tag selected by model -> fs (with 0.0144% of the mistakes).
		tag selected by model -> fx (with 0.0505% of the mistakes).
		tag selected by model -> i (with 0.0288% of the mistakes).
		tag selected by model -> nc (with 4.5500% of the mistakes).
		tag selected by model -> np (with 0.8292% of the mistakes).
		tag selected by model -> nu (with 0.1082% of the mistakes).
		tag selected by model -> p0 (with 0.1226% of the mistakes).
		tag selected by model -> pd (with 0.0288% of the mistakes).
		tag selected by model -> pi (with 0.0865% of the mistakes).
		tag selected by model -> pn (with 0.0216% of the mistakes).
		tag selected by model -> pp (with 0.0649% of the mistakes).
		tag selected by model -> pr (with 0.1514% of the mistakes).
		tag selected by model -> pt (with 0.0144% of the mistakes).
		tag selected by model -> px (with 0.0216% of the mistakes).
		tag selected by model -> rg (with 0.3894% of the mistakes).
		tag selected by model -> rn (with 0.0649% of the mistakes).
		tag selected by model -> sp (with 1.4350% of the mistakes).
		tag selected by model -> un (with 0.0361% of the mistakes).
		tag selected by model -> va (with 0.0649% of the mistakes).
		tag selected by model -> vs (with 0.1370% of the mistakes).
		tag selected by model -> z (with 0.0072% of the mistakes).
		tag selected by model -> zm (with 0.0216% of the mistakes).
		tag selected by model -> zp (with 0.1010% of the mistakes).
		tag selected by model -> zu (with 0.0144% of the mistakes).

	(original tag) vs: 
		tag selected by model -> cs (with 0.0072% of the mistakes).
		tag selected by model -> da (with 0.0144% of the mistakes).
		tag selected by model -> nc (with 0.0865% of the mistakes).
		tag selected by model -> rg (with 0.0144% of the mistakes).
		tag selected by model -> sp (with 0.0144% of the mistakes).
		tag selected by model -> vm (with 0.0144% of the mistakes).

	(original tag) zm: 
		tag selected by model -> di (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.0144% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0144% of the mistakes).
		tag selected by model -> cs (with 0.0072% of the mistakes).
		tag selected by model -> da (with 0.0649% of the mistakes).
		tag selected by model -> di (with 0.0216% of the mistakes).
		tag selected by model -> fp (with 0.0072% of the mistakes).
		tag selected by model -> fs (with 0.0072% of the mistakes).
		tag selected by model -> nc (with 0.1154% of the mistakes).
		tag selected by model -> np (with 0.0433% of the mistakes).
		tag selected by model -> nu (with 0.0144% of the mistakes).
		tag selected by model -> rn (with 0.0288% of the mistakes).
		tag selected by model -> sp (with 0.0433% of the mistakes).
		tag selected by model -> vm (with 0.0288% of the mistakes).
		tag selected by model -> vs (with 0.0072% of the mistakes).


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

N = 1:

