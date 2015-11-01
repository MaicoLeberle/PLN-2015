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

N = 1, clasificador = linear_model.LogisticRegression:

	Time:
		real	0m50.215s
		user	0m36.396s
		sys	0m0.296s
	Accuracy: 92.70%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> nc (with 0.0867% of the mistakes).
		tag selected by model -> rg (with 0.0289% of the mistakes).
		tag selected by model -> vm (with 0.0145% of the mistakes).

	(original tag) aq: 
		tag selected by model -> di (with 0.2457% of the mistakes).
		tag selected by model -> dn (with 0.0578% of the mistakes).
		tag selected by model -> nc (with 9.7124% of the mistakes).
		tag selected by model -> np (with 0.6359% of the mistakes).
		tag selected by model -> nu (with 0.0723% of the mistakes).
		tag selected by model -> rg (with 0.0289% of the mistakes).
		tag selected by model -> sp (with 0.0723% of the mistakes).
		tag selected by model -> un (with 0.0145% of the mistakes).
		tag selected by model -> vm (with 7.8913% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0289% of the mistakes).
		tag selected by model -> cs (with 0.0145% of the mistakes).
		tag selected by model -> nc (with 0.0145% of the mistakes).
		tag selected by model -> np (with 0.0145% of the mistakes).
		tag selected by model -> rg (with 0.6359% of the mistakes).
		tag selected by model -> sp (with 0.0145% of the mistakes).
		tag selected by model -> vm (with 0.1879% of the mistakes).
		tag selected by model -> vs (with 0.0145% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.2457% of the mistakes).
		tag selected by model -> cc (with 0.2602% of the mistakes).
		tag selected by model -> nc (with 0.0145% of the mistakes).
		tag selected by model -> np (with 0.0145% of the mistakes).
		tag selected by model -> pr (with 5.3331% of the mistakes).
		tag selected by model -> rg (with 0.1012% of the mistakes).
		tag selected by model -> sp (with 0.2746% of the mistakes).
		tag selected by model -> vm (with 0.4914% of the mistakes).

	(original tag) da: 
		tag selected by model -> dn (with 0.0145% of the mistakes).
		tag selected by model -> nc (with 1.7054% of the mistakes).
		tag selected by model -> np (with 0.0578% of the mistakes).
		tag selected by model -> nu (with 0.9683% of the mistakes).
		tag selected by model -> pp (with 0.2746% of the mistakes).
		tag selected by model -> vm (with 0.0578% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.1012% of the mistakes).
		tag selected by model -> nc (with 0.1156% of the mistakes).
		tag selected by model -> np (with 0.0723% of the mistakes).
		tag selected by model -> pd (with 0.0578% of the mistakes).
		tag selected by model -> vm (with 0.0723% of the mistakes).

	(original tag) de: 
		tag selected by model -> dt (with 0.0434% of the mistakes).
		tag selected by model -> pt (with 0.0723% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.6070% of the mistakes).
		tag selected by model -> nc (with 0.2457% of the mistakes).
		tag selected by model -> np (with 0.0867% of the mistakes).
		tag selected by model -> pi (with 0.4191% of the mistakes).
		tag selected by model -> rg (with 0.3758% of the mistakes).
		tag selected by model -> vm (with 0.1156% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.1879% of the mistakes).
		tag selected by model -> di (with 0.4047% of the mistakes).
		tag selected by model -> nc (with 0.3469% of the mistakes).
		tag selected by model -> np (with 0.0578% of the mistakes).
		tag selected by model -> nu (with 0.0145% of the mistakes).
		tag selected by model -> pn (with 0.0434% of the mistakes).
		tag selected by model -> vm (with 0.1156% of the mistakes).

	(original tag) dp: 
		tag selected by model -> aq (with 0.0289% of the mistakes).
		tag selected by model -> nc (with 0.0434% of the mistakes).
		tag selected by model -> vm (with 0.0145% of the mistakes).

	(original tag) dt: 
		tag selected by model -> nc (with 0.0289% of the mistakes).
		tag selected by model -> pt (with 0.2457% of the mistakes).
		tag selected by model -> vm (with 0.0145% of the mistakes).

	(original tag) fh: 
		tag selected by model -> aq (with 0.0434% of the mistakes).
		tag selected by model -> nc (with 0.0145% of the mistakes).

	(original tag) fs: 
		tag selected by model -> vm (with 0.0289% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0145% of the mistakes).
		tag selected by model -> nc (with 0.0434% of the mistakes).
		tag selected by model -> nu (with 0.0578% of the mistakes).
		tag selected by model -> sp (with 0.0289% of the mistakes).
		tag selected by model -> vm (with 0.0145% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.1445% of the mistakes).
		tag selected by model -> aq (with 7.7468% of the mistakes).
		tag selected by model -> cc (with 0.0145% of the mistakes).
		tag selected by model -> da (with 0.0867% of the mistakes).
		tag selected by model -> di (with 0.0434% of the mistakes).
		tag selected by model -> dn (with 0.0145% of the mistakes).
		tag selected by model -> np (with 1.6621% of the mistakes).
		tag selected by model -> nu (with 0.3180% of the mistakes).
		tag selected by model -> pi (with 0.0289% of the mistakes).
		tag selected by model -> pn (with 0.0289% of the mistakes).
		tag selected by model -> pp (with 0.0145% of the mistakes).
		tag selected by model -> rg (with 0.2312% of the mistakes).
		tag selected by model -> sp (with 0.1301% of the mistakes).
		tag selected by model -> va (with 0.0145% of the mistakes).
		tag selected by model -> vm (with 7.2120% of the mistakes).
		tag selected by model -> vs (with 0.3035% of the mistakes).
		tag selected by model -> zm (with 0.0289% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.3324% of the mistakes).
		tag selected by model -> cc (with 0.0145% of the mistakes).
		tag selected by model -> dd (with 0.0145% of the mistakes).
		tag selected by model -> nc (with 3.4398% of the mistakes).
		tag selected by model -> nu (with 0.0578% of the mistakes).
		tag selected by model -> pd (with 0.0145% of the mistakes).
		tag selected by model -> sp (with 0.0289% of the mistakes).
		tag selected by model -> vm (with 1.2574% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.4914% of the mistakes).
		tag selected by model -> da (with 0.0145% of the mistakes).
		tag selected by model -> dn (with 0.0289% of the mistakes).
		tag selected by model -> nc (with 1.2574% of the mistakes).
		tag selected by model -> np (with 0.0289% of the mistakes).
		tag selected by model -> vm (with 0.4336% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.5059% of the mistakes).

	(original tag) pd: 
		tag selected by model -> aq (with 0.0289% of the mistakes).
		tag selected by model -> dd (with 0.2023% of the mistakes).
		tag selected by model -> nc (with 0.0578% of the mistakes).
		tag selected by model -> np (with 0.0145% of the mistakes).
		tag selected by model -> vm (with 0.1012% of the mistakes).

	(original tag) pe: 
		tag selected by model -> pt (with 0.0145% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0434% of the mistakes).
		tag selected by model -> di (with 3.4398% of the mistakes).
		tag selected by model -> nc (with 0.0145% of the mistakes).
		tag selected by model -> np (with 0.0434% of the mistakes).
		tag selected by model -> pr (with 0.0145% of the mistakes).
		tag selected by model -> rg (with 0.1879% of the mistakes).
		tag selected by model -> vm (with 0.0434% of the mistakes).

	(original tag) pn: 
		tag selected by model -> aq (with 0.0145% of the mistakes).
		tag selected by model -> dn (with 0.6793% of the mistakes).
		tag selected by model -> nc (with 0.0723% of the mistakes).
		tag selected by model -> pi (with 0.0145% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0723% of the mistakes).
		tag selected by model -> da (with 2.4425% of the mistakes).
		tag selected by model -> nc (with 0.0723% of the mistakes).
		tag selected by model -> np (with 0.0723% of the mistakes).
		tag selected by model -> p0 (with 0.7516% of the mistakes).
		tag selected by model -> rg (with 0.3324% of the mistakes).
		tag selected by model -> vm (with 0.0578% of the mistakes).

	(original tag) pr: 
		tag selected by model -> aq (with 0.0289% of the mistakes).
		tag selected by model -> cs (with 0.8094% of the mistakes).
		tag selected by model -> nc (with 0.0289% of the mistakes).
		tag selected by model -> rg (with 0.0289% of the mistakes).
		tag selected by model -> vm (with 0.0145% of the mistakes).

	(original tag) pt: 
		tag selected by model -> aq (with 0.0289% of the mistakes).
		tag selected by model -> pr (with 0.0145% of the mistakes).
		tag selected by model -> vm (with 0.0289% of the mistakes).

	(original tag) px: 
		tag selected by model -> aq (with 0.0145% of the mistakes).
		tag selected by model -> dp (with 0.0145% of the mistakes).
		tag selected by model -> nc (with 0.1301% of the mistakes).
		tag selected by model -> vm (with 0.1301% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 4.2203% of the mistakes).
		tag selected by model -> cc (with 0.3035% of the mistakes).
		tag selected by model -> cs (with 0.1301% of the mistakes).
		tag selected by model -> da (with 0.0145% of the mistakes).
		tag selected by model -> di (with 0.0289% of the mistakes).
		tag selected by model -> dn (with 0.0145% of the mistakes).
		tag selected by model -> nc (with 0.6937% of the mistakes).
		tag selected by model -> np (with 0.4625% of the mistakes).
		tag selected by model -> nu (with 0.0578% of the mistakes).
		tag selected by model -> pi (with 0.2312% of the mistakes).
		tag selected by model -> rn (with 0.3324% of the mistakes).
		tag selected by model -> sp (with 0.2312% of the mistakes).
		tag selected by model -> vm (with 2.9484% of the mistakes).

	(original tag) rn: 
		tag selected by model -> aq (with 0.0289% of the mistakes).
		tag selected by model -> cc (with 0.0145% of the mistakes).
		tag selected by model -> rg (with 0.0289% of the mistakes).
		tag selected by model -> vm (with 0.0289% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.5926% of the mistakes).
		tag selected by model -> cs (with 0.7082% of the mistakes).
		tag selected by model -> nc (with 0.1590% of the mistakes).
		tag selected by model -> rg (with 0.0578% of the mistakes).
		tag selected by model -> vm (with 0.4480% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.1012% of the mistakes).
		tag selected by model -> cs (with 0.0289% of the mistakes).
		tag selected by model -> fe (with 0.2312% of the mistakes).
		tag selected by model -> fg (with 0.0145% of the mistakes).
		tag selected by model -> fp (with 0.0289% of the mistakes).
		tag selected by model -> fz (with 0.0145% of the mistakes).
		tag selected by model -> nc (with 0.1156% of the mistakes).
		tag selected by model -> np (with 0.1879% of the mistakes).
		tag selected by model -> nu (with 0.0578% of the mistakes).
		tag selected by model -> pt (with 0.0145% of the mistakes).
		tag selected by model -> rg (with 0.0145% of the mistakes).
		tag selected by model -> sp (with 0.0145% of the mistakes).
		tag selected by model -> vm (with 0.1590% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.0578% of the mistakes).
		tag selected by model -> nc (with 0.0145% of the mistakes).
		tag selected by model -> vm (with 0.2891% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 7.1398% of the mistakes).
		tag selected by model -> nc (with 5.6945% of the mistakes).
		tag selected by model -> np (with 2.4136% of the mistakes).
		tag selected by model -> nu (with 0.1156% of the mistakes).
		tag selected by model -> sp (with 0.0145% of the mistakes).
		tag selected by model -> va (with 0.0145% of the mistakes).
		tag selected by model -> vs (with 0.1301% of the mistakes).

	(original tag) vs: 
		tag selected by model -> aq (with 0.0867% of the mistakes).
		tag selected by model -> nc (with 0.0145% of the mistakes).
		tag selected by model -> np (with 0.0434% of the mistakes).
		tag selected by model -> rg (with 0.0867% of the mistakes).
		tag selected by model -> vm (with 0.1734% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.0434% of the mistakes).
		tag selected by model -> nc (with 0.1156% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0289% of the mistakes).
		tag selected by model -> nc (with 0.9683% of the mistakes).
		tag selected by model -> nu (with 0.0578% of the mistakes).

N = 2, clasificador = linear_model.LogisticRegression:

	Time:
		real	0m38.826s
		user	0m36.980s
		sys	0m0.304s
	Accuracy: 91.99%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> nc (with 0.0658% of the mistakes).
		tag selected by model -> rg (with 0.0263% of the mistakes).
		tag selected by model -> vm (with 0.0132% of the mistakes).

	(original tag) aq: 
		tag selected by model -> di (with 0.2634% of the mistakes).
		tag selected by model -> dn (with 0.0527% of the mistakes).
		tag selected by model -> nc (with 12.0226% of the mistakes).
		tag selected by model -> np (with 0.5794% of the mistakes).
		tag selected by model -> nu (with 0.0658% of the mistakes).
		tag selected by model -> rg (with 0.0395% of the mistakes).
		tag selected by model -> sp (with 0.0658% of the mistakes).
		tag selected by model -> un (with 0.0132% of the mistakes).
		tag selected by model -> vm (with 7.0977% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0132% of the mistakes).
		tag selected by model -> cs (with 0.0132% of the mistakes).
		tag selected by model -> nc (with 0.0395% of the mistakes).
		tag selected by model -> np (with 0.0132% of the mistakes).
		tag selected by model -> rg (with 0.5926% of the mistakes).
		tag selected by model -> sp (with 0.0132% of the mistakes).
		tag selected by model -> vm (with 0.1712% of the mistakes).
		tag selected by model -> vs (with 0.0132% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.1185% of the mistakes).
		tag selected by model -> cc (with 0.2370% of the mistakes).
		tag selected by model -> nc (with 0.1844% of the mistakes).
		tag selected by model -> np (with 0.0132% of the mistakes).
		tag selected by model -> pr (with 3.5159% of the mistakes).
		tag selected by model -> rg (with 0.0922% of the mistakes).
		tag selected by model -> sp (with 0.2502% of the mistakes).
		tag selected by model -> vm (with 0.4214% of the mistakes).

	(original tag) da: 
		tag selected by model -> dn (with 0.0132% of the mistakes).
		tag selected by model -> nc (with 1.5539% of the mistakes).
		tag selected by model -> np (with 0.0527% of the mistakes).
		tag selected by model -> nu (with 0.8691% of the mistakes).
		tag selected by model -> pp (with 0.4082% of the mistakes).
		tag selected by model -> vm (with 0.0395% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0922% of the mistakes).
		tag selected by model -> nc (with 0.1580% of the mistakes).
		tag selected by model -> np (with 0.0658% of the mistakes).
		tag selected by model -> pd (with 0.0527% of the mistakes).
		tag selected by model -> vm (with 0.1053% of the mistakes).

	(original tag) de: 
		tag selected by model -> dt (with 0.0395% of the mistakes).
		tag selected by model -> pt (with 0.0658% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.5267% of the mistakes).
		tag selected by model -> nc (with 0.2765% of the mistakes).
		tag selected by model -> np (with 0.0790% of the mistakes).
		tag selected by model -> pi (with 0.4082% of the mistakes).
		tag selected by model -> rg (with 0.3160% of the mistakes).
		tag selected by model -> vm (with 0.1580% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.1053% of the mistakes).
		tag selected by model -> di (with 0.3687% of the mistakes).
		tag selected by model -> nc (with 0.3424% of the mistakes).
		tag selected by model -> np (with 0.0527% of the mistakes).
		tag selected by model -> nu (with 0.0132% of the mistakes).
		tag selected by model -> pn (with 0.0395% of the mistakes).
		tag selected by model -> vm (with 0.1317% of the mistakes).

	(original tag) dp: 
		tag selected by model -> aq (with 0.0132% of the mistakes).
		tag selected by model -> nc (with 0.0658% of the mistakes).
		tag selected by model -> vm (with 0.0263% of the mistakes).

	(original tag) dt: 
		tag selected by model -> aq (with 0.0263% of the mistakes).
		tag selected by model -> nc (with 0.0263% of the mistakes).
		tag selected by model -> pt (with 0.1975% of the mistakes).
		tag selected by model -> vm (with 0.0132% of the mistakes).

	(original tag) fh: 
		tag selected by model -> aq (with 0.0263% of the mistakes).
		tag selected by model -> nc (with 0.0263% of the mistakes).

	(original tag) fs: 
		tag selected by model -> vm (with 0.0263% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0132% of the mistakes).
		tag selected by model -> nc (with 0.0395% of the mistakes).
		tag selected by model -> nu (with 0.0527% of the mistakes).
		tag selected by model -> sp (with 0.0263% of the mistakes).
		tag selected by model -> vm (with 0.0132% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.1317% of the mistakes).
		tag selected by model -> aq (with 9.3495% of the mistakes).
		tag selected by model -> da (with 0.0790% of the mistakes).
		tag selected by model -> di (with 0.0527% of the mistakes).
		tag selected by model -> dn (with 0.0132% of the mistakes).
		tag selected by model -> np (with 1.5275% of the mistakes).
		tag selected by model -> nu (with 0.2897% of the mistakes).
		tag selected by model -> pi (with 0.0263% of the mistakes).
		tag selected by model -> pn (with 0.0263% of the mistakes).
		tag selected by model -> pp (with 0.0132% of the mistakes).
		tag selected by model -> rg (with 0.1449% of the mistakes).
		tag selected by model -> sp (with 0.1053% of the mistakes).
		tag selected by model -> va (with 0.0132% of the mistakes).
		tag selected by model -> vm (with 7.1504% of the mistakes).
		tag selected by model -> vs (with 0.2634% of the mistakes).
		tag selected by model -> zm (with 0.0263% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.2107% of the mistakes).
		tag selected by model -> cc (with 0.0132% of the mistakes).
		tag selected by model -> dd (with 0.0132% of the mistakes).
		tag selected by model -> nc (with 3.2131% of the mistakes).
		tag selected by model -> nu (with 0.0527% of the mistakes).
		tag selected by model -> pd (with 0.0132% of the mistakes).
		tag selected by model -> sp (with 0.0263% of the mistakes).
		tag selected by model -> vm (with 1.1588% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.2239% of the mistakes).
		tag selected by model -> da (with 0.0132% of the mistakes).
		tag selected by model -> dn (with 0.0263% of the mistakes).
		tag selected by model -> nc (with 1.3037% of the mistakes).
		tag selected by model -> np (with 0.0263% of the mistakes).
		tag selected by model -> vm (with 0.4346% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.4609% of the mistakes).

	(original tag) pd: 
		tag selected by model -> aq (with 0.0395% of the mistakes).
		tag selected by model -> dd (with 0.1844% of the mistakes).
		tag selected by model -> nc (with 0.0658% of the mistakes).
		tag selected by model -> np (with 0.0263% of the mistakes).
		tag selected by model -> rg (with 0.0132% of the mistakes).
		tag selected by model -> vm (with 0.0658% of the mistakes).

	(original tag) pe: 
		tag selected by model -> pt (with 0.0132% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.1317% of the mistakes).
		tag selected by model -> di (with 3.0419% of the mistakes).
		tag selected by model -> nc (with 0.0263% of the mistakes).
		tag selected by model -> np (with 0.0395% of the mistakes).
		tag selected by model -> pr (with 0.0132% of the mistakes).
		tag selected by model -> rg (with 0.1580% of the mistakes).
		tag selected by model -> vm (with 0.0263% of the mistakes).

	(original tag) pn: 
		tag selected by model -> aq (with 0.0263% of the mistakes).
		tag selected by model -> dn (with 0.6189% of the mistakes).
		tag selected by model -> nc (with 0.0658% of the mistakes).
		tag selected by model -> pi (with 0.0132% of the mistakes).
		tag selected by model -> vm (with 0.0132% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0263% of the mistakes).
		tag selected by model -> da (with 2.0147% of the mistakes).
		tag selected by model -> nc (with 0.1580% of the mistakes).
		tag selected by model -> np (with 0.0658% of the mistakes).
		tag selected by model -> p0 (with 0.6848% of the mistakes).
		tag selected by model -> rg (with 0.3029% of the mistakes).
		tag selected by model -> vm (with 0.0790% of the mistakes).

	(original tag) pr: 
		tag selected by model -> aq (with 0.0132% of the mistakes).
		tag selected by model -> cs (with 1.4617% of the mistakes).
		tag selected by model -> nc (with 0.0658% of the mistakes).
		tag selected by model -> rg (with 0.0263% of the mistakes).
		tag selected by model -> vm (with 0.0132% of the mistakes).

	(original tag) pt: 
		tag selected by model -> np (with 0.0263% of the mistakes).
		tag selected by model -> pr (with 0.0132% of the mistakes).
		tag selected by model -> vm (with 0.0658% of the mistakes).

	(original tag) px: 
		tag selected by model -> dp (with 0.0132% of the mistakes).
		tag selected by model -> nc (with 0.1185% of the mistakes).
		tag selected by model -> vm (with 0.1317% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 2.3176% of the mistakes).
		tag selected by model -> cc (with 0.2765% of the mistakes).
		tag selected by model -> cs (with 0.1185% of the mistakes).
		tag selected by model -> da (with 0.0132% of the mistakes).
		tag selected by model -> di (with 0.0263% of the mistakes).
		tag selected by model -> dn (with 0.0263% of the mistakes).
		tag selected by model -> nc (with 2.1859% of the mistakes).
		tag selected by model -> np (with 0.4214% of the mistakes).
		tag selected by model -> nu (with 0.0527% of the mistakes).
		tag selected by model -> pi (with 0.2107% of the mistakes).
		tag selected by model -> rn (with 0.3029% of the mistakes).
		tag selected by model -> sp (with 0.2107% of the mistakes).
		tag selected by model -> vm (with 2.7258% of the mistakes).
		tag selected by model -> vs (with 0.0132% of the mistakes).

	(original tag) rn: 
		tag selected by model -> cc (with 0.0132% of the mistakes).
		tag selected by model -> nc (with 0.0263% of the mistakes).
		tag selected by model -> rg (with 0.0263% of the mistakes).
		tag selected by model -> vm (with 0.0263% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.4346% of the mistakes).
		tag selected by model -> cs (with 0.6584% of the mistakes).
		tag selected by model -> nc (with 0.3292% of the mistakes).
		tag selected by model -> rg (with 0.0527% of the mistakes).
		tag selected by model -> vm (with 0.4477% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.0790% of the mistakes).
		tag selected by model -> cs (with 0.0263% of the mistakes).
		tag selected by model -> fe (with 0.2107% of the mistakes).
		tag selected by model -> fg (with 0.0132% of the mistakes).
		tag selected by model -> fp (with 0.0263% of the mistakes).
		tag selected by model -> fz (with 0.0132% of the mistakes).
		tag selected by model -> nc (with 0.1185% of the mistakes).
		tag selected by model -> np (with 0.1712% of the mistakes).
		tag selected by model -> nu (with 0.0527% of the mistakes).
		tag selected by model -> pt (with 0.0132% of the mistakes).
		tag selected by model -> rg (with 0.0132% of the mistakes).
		tag selected by model -> sp (with 0.0132% of the mistakes).
		tag selected by model -> vm (with 0.1449% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.0263% of the mistakes).
		tag selected by model -> nc (with 0.1185% of the mistakes).
		tag selected by model -> vm (with 0.2370% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 7.4664% of the mistakes).
		tag selected by model -> nc (with 7.0319% of the mistakes).
		tag selected by model -> np (with 2.2386% of the mistakes).
		tag selected by model -> nu (with 0.1053% of the mistakes).
		tag selected by model -> sp (with 0.0132% of the mistakes).
		tag selected by model -> va (with 0.0132% of the mistakes).
		tag selected by model -> vs (with 0.1185% of the mistakes).

	(original tag) vs: 
		tag selected by model -> aq (with 0.0527% of the mistakes).
		tag selected by model -> nc (with 0.0790% of the mistakes).
		tag selected by model -> np (with 0.0395% of the mistakes).
		tag selected by model -> rg (with 0.0790% of the mistakes).
		tag selected by model -> vm (with 0.1580% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.1449% of the mistakes).
		tag selected by model -> nc (with 0.1053% of the mistakes).
		tag selected by model -> vm (with 0.0132% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0263% of the mistakes).
		tag selected by model -> nc (with 0.8823% of the mistakes).
		tag selected by model -> nu (with 0.0395% of the mistakes).

N = 3, clasificador = linear_model.LogisticRegression:

	Time:
		real	0m54.151s
		user	0m40.772s
		sys	0m0.780s
	Accuracy: 92.18%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> nc (with 0.0675% of the mistakes).
		tag selected by model -> rg (with 0.0270% of the mistakes).
		tag selected by model -> vm (with 0.0135% of the mistakes).

	(original tag) aq: 
		tag selected by model -> di (with 0.2564% of the mistakes).
		tag selected by model -> dn (with 0.0540% of the mistakes).
		tag selected by model -> nc (with 11.7949% of the mistakes).
		tag selected by model -> np (with 0.5938% of the mistakes).
		tag selected by model -> nu (with 0.0270% of the mistakes).
		tag selected by model -> rg (with 0.0405% of the mistakes).
		tag selected by model -> sp (with 0.0675% of the mistakes).
		tag selected by model -> un (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 7.0580% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0405% of the mistakes).
		tag selected by model -> cs (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.0675% of the mistakes).
		tag selected by model -> np (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.6073% of the mistakes).
		tag selected by model -> sp (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 0.1619% of the mistakes).
		tag selected by model -> vs (with 0.0135% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.1350% of the mistakes).
		tag selected by model -> cc (with 0.2294% of the mistakes).
		tag selected by model -> nc (with 0.1619% of the mistakes).
		tag selected by model -> np (with 0.0135% of the mistakes).
		tag selected by model -> pr (with 3.2389% of the mistakes).
		tag selected by model -> rg (with 0.0945% of the mistakes).
		tag selected by model -> sp (with 0.2564% of the mistakes).
		tag selected by model -> vm (with 0.4723% of the mistakes).

	(original tag) da: 
		tag selected by model -> dn (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 1.6059% of the mistakes).
		tag selected by model -> np (with 0.0540% of the mistakes).
		tag selected by model -> nu (with 0.9447% of the mistakes).
		tag selected by model -> pp (with 0.4453% of the mistakes).
		tag selected by model -> vm (with 0.0405% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0810% of the mistakes).
		tag selected by model -> nc (with 0.1754% of the mistakes).
		tag selected by model -> np (with 0.0675% of the mistakes).
		tag selected by model -> pd (with 0.0810% of the mistakes).
		tag selected by model -> vm (with 0.1080% of the mistakes).

	(original tag) de: 
		tag selected by model -> dt (with 0.0540% of the mistakes).
		tag selected by model -> pt (with 0.0540% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.5128% of the mistakes).
		tag selected by model -> nc (with 0.3509% of the mistakes).
		tag selected by model -> np (with 0.0675% of the mistakes).
		tag selected by model -> pi (with 0.5128% of the mistakes).
		tag selected by model -> rg (with 0.3104% of the mistakes).
		tag selected by model -> vm (with 0.1619% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.0945% of the mistakes).
		tag selected by model -> di (with 0.3779% of the mistakes).
		tag selected by model -> nc (with 0.3374% of the mistakes).
		tag selected by model -> np (with 0.0540% of the mistakes).
		tag selected by model -> nu (with 0.0135% of the mistakes).
		tag selected by model -> pn (with 0.0540% of the mistakes).
		tag selected by model -> vm (with 0.1484% of the mistakes).

	(original tag) dp: 
		tag selected by model -> aq (with 0.0270% of the mistakes).
		tag selected by model -> nc (with 0.0675% of the mistakes).
		tag selected by model -> vm (with 0.0405% of the mistakes).

	(original tag) dt: 
		tag selected by model -> aq (with 0.0270% of the mistakes).
		tag selected by model -> nc (with 0.0270% of the mistakes).
		tag selected by model -> pt (with 0.1080% of the mistakes).
		tag selected by model -> vm (with 0.0270% of the mistakes).

	(original tag) fa: 
		tag selected by model -> aq (with 0.0135% of the mistakes).

	(original tag) fh: 
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.0270% of the mistakes).
		tag selected by model -> vm (with 0.0135% of the mistakes).

	(original tag) fs: 
		tag selected by model -> vm (with 0.0270% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.0405% of the mistakes).
		tag selected by model -> nu (with 0.0540% of the mistakes).
		tag selected by model -> sp (with 0.0270% of the mistakes).
		tag selected by model -> vm (with 0.0135% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.1619% of the mistakes).
		tag selected by model -> aq (with 9.3927% of the mistakes).
		tag selected by model -> da (with 0.0810% of the mistakes).
		tag selected by model -> di (with 0.0405% of the mistakes).
		tag selected by model -> dn (with 0.0135% of the mistakes).
		tag selected by model -> np (with 1.5250% of the mistakes).
		tag selected by model -> nu (with 0.1619% of the mistakes).
		tag selected by model -> pi (with 0.0270% of the mistakes).
		tag selected by model -> pn (with 0.0270% of the mistakes).
		tag selected by model -> pp (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.1484% of the mistakes).
		tag selected by model -> sp (with 0.1350% of the mistakes).
		tag selected by model -> va (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 6.8691% of the mistakes).
		tag selected by model -> vs (with 0.2699% of the mistakes).
		tag selected by model -> zm (with 0.0270% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.2564% of the mistakes).
		tag selected by model -> cc (with 0.0135% of the mistakes).
		tag selected by model -> dd (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 3.4278% of the mistakes).
		tag selected by model -> nu (with 0.0270% of the mistakes).
		tag selected by model -> pd (with 0.0135% of the mistakes).
		tag selected by model -> sp (with 0.0405% of the mistakes).
		tag selected by model -> vm (with 1.0796% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.2159% of the mistakes).
		tag selected by model -> da (with 0.0135% of the mistakes).
		tag selected by model -> dn (with 0.0405% of the mistakes).
		tag selected by model -> nc (with 1.2821% of the mistakes).
		tag selected by model -> np (with 0.0270% of the mistakes).
		tag selected by model -> vm (with 0.5533% of the mistakes).

	(original tag) p0: 
		tag selected by model -> nc (with 0.0135% of the mistakes).
		tag selected by model -> pp (with 0.4453% of the mistakes).

	(original tag) pd: 
		tag selected by model -> aq (with 0.0270% of the mistakes).
		tag selected by model -> dd (with 0.1889% of the mistakes).
		tag selected by model -> nc (with 0.0675% of the mistakes).
		tag selected by model -> np (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 0.0675% of the mistakes).

	(original tag) pe: 
		tag selected by model -> pt (with 0.0135% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0945% of the mistakes).
		tag selected by model -> di (with 3.1174% of the mistakes).
		tag selected by model -> nc (with 0.0405% of the mistakes).
		tag selected by model -> np (with 0.0405% of the mistakes).
		tag selected by model -> pr (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.1619% of the mistakes).
		tag selected by model -> vm (with 0.0405% of the mistakes).

	(original tag) pn: 
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> dn (with 0.6073% of the mistakes).
		tag selected by model -> nc (with 0.0810% of the mistakes).
		tag selected by model -> pi (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 0.0135% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0405% of the mistakes).
		tag selected by model -> da (with 2.0378% of the mistakes).
		tag selected by model -> nc (with 0.1350% of the mistakes).
		tag selected by model -> np (with 0.0675% of the mistakes).
		tag selected by model -> p0 (with 0.7018% of the mistakes).
		tag selected by model -> rg (with 0.3104% of the mistakes).
		tag selected by model -> vm (with 0.0945% of the mistakes).

	(original tag) pr: 
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> cs (with 1.1201% of the mistakes).
		tag selected by model -> nc (with 0.0540% of the mistakes).
		tag selected by model -> rg (with 0.0270% of the mistakes).
		tag selected by model -> vm (with 0.0270% of the mistakes).

	(original tag) pt: 
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> dt (with 0.1484% of the mistakes).
		tag selected by model -> np (with 0.0675% of the mistakes).
		tag selected by model -> pr (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 0.1215% of the mistakes).

	(original tag) px: 
		tag selected by model -> dp (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.1215% of the mistakes).
		tag selected by model -> vm (with 0.1350% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 2.4426% of the mistakes).
		tag selected by model -> cc (with 0.2834% of the mistakes).
		tag selected by model -> cs (with 0.1215% of the mistakes).
		tag selected by model -> da (with 0.0135% of the mistakes).
		tag selected by model -> di (with 0.0270% of the mistakes).
		tag selected by model -> dn (with 0.0270% of the mistakes).
		tag selected by model -> nc (with 1.5655% of the mistakes).
		tag selected by model -> np (with 0.4318% of the mistakes).
		tag selected by model -> pi (with 0.2159% of the mistakes).
		tag selected by model -> rn (with 0.3104% of the mistakes).
		tag selected by model -> sp (with 0.2159% of the mistakes).
		tag selected by model -> vm (with 3.4818% of the mistakes).
		tag selected by model -> vs (with 0.0135% of the mistakes).

	(original tag) rn: 
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> cc (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.0270% of the mistakes).
		tag selected by model -> vm (with 0.0270% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.4858% of the mistakes).
		tag selected by model -> cs (with 0.6748% of the mistakes).
		tag selected by model -> nc (with 0.2699% of the mistakes).
		tag selected by model -> rg (with 0.0540% of the mistakes).
		tag selected by model -> vm (with 0.4993% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.0945% of the mistakes).
		tag selected by model -> cs (with 0.0270% of the mistakes).
		tag selected by model -> fe (with 0.2159% of the mistakes).
		tag selected by model -> fg (with 0.0135% of the mistakes).
		tag selected by model -> fp (with 0.0270% of the mistakes).
		tag selected by model -> fz (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.1080% of the mistakes).
		tag selected by model -> np (with 0.1754% of the mistakes).
		tag selected by model -> nu (with 0.0405% of the mistakes).
		tag selected by model -> pt (with 0.0135% of the mistakes).
		tag selected by model -> rg (with 0.0135% of the mistakes).
		tag selected by model -> sp (with 0.0135% of the mistakes).
		tag selected by model -> vm (with 0.1619% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.0540% of the mistakes).
		tag selected by model -> nc (with 0.0810% of the mistakes).
		tag selected by model -> vm (with 0.2564% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 7.1930% of the mistakes).
		tag selected by model -> nc (with 7.0715% of the mistakes).
		tag selected by model -> np (with 2.2672% of the mistakes).
		tag selected by model -> nu (with 0.0540% of the mistakes).
		tag selected by model -> sp (with 0.0135% of the mistakes).
		tag selected by model -> va (with 0.0135% of the mistakes).
		tag selected by model -> vs (with 0.1215% of the mistakes).

	(original tag) vs: 
		tag selected by model -> aq (with 0.0405% of the mistakes).
		tag selected by model -> nc (with 0.1215% of the mistakes).
		tag selected by model -> np (with 0.0405% of the mistakes).
		tag selected by model -> rg (with 0.0810% of the mistakes).
		tag selected by model -> vm (with 0.1215% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.1350% of the mistakes).
		tag selected by model -> nc (with 0.1080% of the mistakes).
		tag selected by model -> vm (with 0.0135% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0135% of the mistakes).
		tag selected by model -> nc (with 0.9042% of the mistakes).
		tag selected by model -> nu (with 0.0405% of the mistakes).
		tag selected by model -> vm (with 0.0135% of the mistakes).

N = 4, clasificador = linear_model.LogisticRegression:

	Time:
		real	0m53.532s
		user	0m43.544s
		sys	0m0.288s
	Accuracy: 92.23%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> aq (with 0.0136% of the mistakes).
		tag selected by model -> nc (with 0.0679% of the mistakes).
		tag selected by model -> rg (with 0.0136% of the mistakes).
		tag selected by model -> vm (with 0.0136% of the mistakes).

	(original tag) aq: 
		tag selected by model -> di (with 0.2308% of the mistakes).
		tag selected by model -> dn (with 0.0543% of the mistakes).
		tag selected by model -> nc (with 12.0027% of the mistakes).
		tag selected by model -> np (with 0.5974% of the mistakes).
		tag selected by model -> nu (with 0.0543% of the mistakes).
		tag selected by model -> rg (with 0.0543% of the mistakes).
		tag selected by model -> sp (with 0.0679% of the mistakes).
		tag selected by model -> un (with 0.0136% of the mistakes).
		tag selected by model -> vm (with 6.7074% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0407% of the mistakes).
		tag selected by model -> cs (with 0.0136% of the mistakes).
		tag selected by model -> nc (with 0.0543% of the mistakes).
		tag selected by model -> np (with 0.0136% of the mistakes).
		tag selected by model -> rg (with 0.5974% of the mistakes).
		tag selected by model -> sp (with 0.0136% of the mistakes).
		tag selected by model -> vm (with 0.1629% of the mistakes).
		tag selected by model -> vs (with 0.0136% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.1494% of the mistakes).
		tag selected by model -> cc (with 0.2172% of the mistakes).
		tag selected by model -> nc (with 0.1765% of the mistakes).
		tag selected by model -> np (with 0.0136% of the mistakes).
		tag selected by model -> pr (with 3.0550% of the mistakes).
		tag selected by model -> rg (with 0.0950% of the mistakes).
		tag selected by model -> sp (with 0.2580% of the mistakes).
		tag selected by model -> vm (with 0.4481% of the mistakes).

	(original tag) da: 
		tag selected by model -> dn (with 0.0136% of the mistakes).
		tag selected by model -> nc (with 1.6022% of the mistakes).
		tag selected by model -> np (with 0.0543% of the mistakes).
		tag selected by model -> nu (with 0.9233% of the mistakes).
		tag selected by model -> pp (with 0.4209% of the mistakes).
		tag selected by model -> vm (with 0.0407% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0950% of the mistakes).
		tag selected by model -> nc (with 0.1629% of the mistakes).
		tag selected by model -> np (with 0.0679% of the mistakes).
		tag selected by model -> pd (with 0.0950% of the mistakes).
		tag selected by model -> vm (with 0.1086% of the mistakes).

	(original tag) de: 
		tag selected by model -> dt (with 0.0543% of the mistakes).
		tag selected by model -> pt (with 0.0543% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.5703% of the mistakes).
		tag selected by model -> nc (with 0.3259% of the mistakes).
		tag selected by model -> np (with 0.0679% of the mistakes).
		tag selected by model -> pi (with 0.5295% of the mistakes).
		tag selected by model -> rg (with 0.3123% of the mistakes).
		tag selected by model -> vm (with 0.1222% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.0679% of the mistakes).
		tag selected by model -> di (with 0.3802% of the mistakes).
		tag selected by model -> nc (with 0.3530% of the mistakes).
		tag selected by model -> np (with 0.0407% of the mistakes).
		tag selected by model -> nu (with 0.0136% of the mistakes).
		tag selected by model -> pn (with 0.0815% of the mistakes).
		tag selected by model -> vm (with 0.1765% of the mistakes).

	(original tag) dp: 
		tag selected by model -> aq (with 0.0272% of the mistakes).
		tag selected by model -> nc (with 0.0679% of the mistakes).
		tag selected by model -> vm (with 0.0407% of the mistakes).

	(original tag) dt: 
		tag selected by model -> aq (with 0.0272% of the mistakes).
		tag selected by model -> nc (with 0.0272% of the mistakes).
		tag selected by model -> pt (with 0.0950% of the mistakes).
		tag selected by model -> vm (with 0.0272% of the mistakes).

	(original tag) fh: 
		tag selected by model -> aq (with 0.0272% of the mistakes).
		tag selected by model -> nc (with 0.0272% of the mistakes).

	(original tag) fs: 
		tag selected by model -> vm (with 0.0272% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0136% of the mistakes).
		tag selected by model -> nc (with 0.0407% of the mistakes).
		tag selected by model -> nu (with 0.0543% of the mistakes).
		tag selected by model -> sp (with 0.0272% of the mistakes).
		tag selected by model -> vm (with 0.0136% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.1629% of the mistakes).
		tag selected by model -> aq (with 9.5587% of the mistakes).
		tag selected by model -> da (with 0.0543% of the mistakes).
		tag selected by model -> di (with 0.0407% of the mistakes).
		tag selected by model -> dn (with 0.0136% of the mistakes).
		tag selected by model -> np (with 1.5343% of the mistakes).
		tag selected by model -> nu (with 0.1629% of the mistakes).
		tag selected by model -> pi (with 0.0272% of the mistakes).
		tag selected by model -> pn (with 0.0272% of the mistakes).
		tag selected by model -> pp (with 0.0136% of the mistakes).
		tag selected by model -> rg (with 0.1494% of the mistakes).
		tag selected by model -> sp (with 0.1358% of the mistakes).
		tag selected by model -> va (with 0.0136% of the mistakes).
		tag selected by model -> vm (with 6.0014% of the mistakes).
		tag selected by model -> vs (with 0.2580% of the mistakes).
		tag selected by model -> zm (with 0.0136% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.2851% of the mistakes).
		tag selected by model -> cc (with 0.0136% of the mistakes).
		tag selected by model -> dd (with 0.0136% of the mistakes).
		tag selected by model -> nc (with 3.5031% of the mistakes).
		tag selected by model -> nu (with 0.0272% of the mistakes).
		tag selected by model -> pd (with 0.0136% of the mistakes).
		tag selected by model -> sp (with 0.0407% of the mistakes).
		tag selected by model -> vm (with 1.0455% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.2308% of the mistakes).
		tag selected by model -> da (with 0.0272% of the mistakes).
		tag selected by model -> dn (with 0.0407% of the mistakes).
		tag selected by model -> nc (with 1.3306% of the mistakes).
		tag selected by model -> np (with 0.0272% of the mistakes).
		tag selected by model -> vm (with 0.5295% of the mistakes).

	(original tag) p0: 
		tag selected by model -> nc (with 0.0136% of the mistakes).
		tag selected by model -> pp (with 0.4481% of the mistakes).

	(original tag) pd: 
		tag selected by model -> aq (with 0.0272% of the mistakes).
		tag selected by model -> dd (with 0.1901% of the mistakes).
		tag selected by model -> nc (with 0.0815% of the mistakes).
		tag selected by model -> np (with 0.0136% of the mistakes).
		tag selected by model -> rg (with 0.0136% of the mistakes).
		tag selected by model -> vm (with 0.0679% of the mistakes).

	(original tag) pe: 
		tag selected by model -> pt (with 0.0136% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0950% of the mistakes).
		tag selected by model -> di (with 3.1093% of the mistakes).
		tag selected by model -> nc (with 0.0543% of the mistakes).
		tag selected by model -> np (with 0.0272% of the mistakes).
		tag selected by model -> pr (with 0.0136% of the mistakes).
		tag selected by model -> rg (with 0.1629% of the mistakes).
		tag selected by model -> vm (with 0.0407% of the mistakes).

	(original tag) pn: 
		tag selected by model -> dn (with 0.6110% of the mistakes).
		tag selected by model -> nc (with 0.0815% of the mistakes).
		tag selected by model -> pi (with 0.0136% of the mistakes).
		tag selected by model -> vm (with 0.0136% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0272% of the mistakes).
		tag selected by model -> da (with 2.0638% of the mistakes).
		tag selected by model -> nc (with 0.1494% of the mistakes).
		tag selected by model -> np (with 0.0679% of the mistakes).
		tag selected by model -> p0 (with 0.7060% of the mistakes).
		tag selected by model -> rg (with 0.3123% of the mistakes).
		tag selected by model -> vm (with 0.0815% of the mistakes).

	(original tag) pr: 
		tag selected by model -> aq (with 0.0407% of the mistakes).
		tag selected by model -> cs (with 1.2356% of the mistakes).
		tag selected by model -> nc (with 0.0407% of the mistakes).
		tag selected by model -> rg (with 0.0136% of the mistakes).
		tag selected by model -> vm (with 0.0272% of the mistakes).

	(original tag) pt: 
		tag selected by model -> aq (with 0.0136% of the mistakes).
		tag selected by model -> dt (with 0.1086% of the mistakes).
		tag selected by model -> np (with 0.0679% of the mistakes).
		tag selected by model -> pr (with 0.0136% of the mistakes).
		tag selected by model -> vm (with 0.1222% of the mistakes).

	(original tag) px: 
		tag selected by model -> dp (with 0.0136% of the mistakes).
		tag selected by model -> nc (with 0.1222% of the mistakes).
		tag selected by model -> vm (with 0.1358% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 2.6069% of the mistakes).
		tag selected by model -> cc (with 0.2851% of the mistakes).
		tag selected by model -> cs (with 0.1222% of the mistakes).
		tag selected by model -> da (with 0.0136% of the mistakes).
		tag selected by model -> di (with 0.0272% of the mistakes).
		tag selected by model -> dn (with 0.0272% of the mistakes).
		tag selected by model -> nc (with 1.6836% of the mistakes).
		tag selected by model -> np (with 0.4345% of the mistakes).
		tag selected by model -> nu (with 0.0136% of the mistakes).
		tag selected by model -> pi (with 0.2172% of the mistakes).
		tag selected by model -> pp (with 0.0136% of the mistakes).
		tag selected by model -> rn (with 0.3123% of the mistakes).
		tag selected by model -> sp (with 0.2172% of the mistakes).
		tag selected by model -> vm (with 3.3537% of the mistakes).
		tag selected by model -> vs (with 0.0136% of the mistakes).

	(original tag) rn: 
		tag selected by model -> aq (with 0.0136% of the mistakes).
		tag selected by model -> cc (with 0.0136% of the mistakes).
		tag selected by model -> nc (with 0.0136% of the mistakes).
		tag selected by model -> rg (with 0.0272% of the mistakes).
		tag selected by model -> vm (with 0.0272% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.4752% of the mistakes).
		tag selected by model -> cs (with 0.6789% of the mistakes).
		tag selected by model -> nc (with 0.2444% of the mistakes).
		tag selected by model -> rg (with 0.0543% of the mistakes).
		tag selected by model -> vm (with 0.5160% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.1222% of the mistakes).
		tag selected by model -> cs (with 0.0272% of the mistakes).
		tag selected by model -> fe (with 0.2172% of the mistakes).
		tag selected by model -> fg (with 0.0136% of the mistakes).
		tag selected by model -> fp (with 0.0272% of the mistakes).
		tag selected by model -> fz (with 0.0136% of the mistakes).
		tag selected by model -> nc (with 0.1222% of the mistakes).
		tag selected by model -> np (with 0.1765% of the mistakes).
		tag selected by model -> nu (with 0.0272% of the mistakes).
		tag selected by model -> pt (with 0.0136% of the mistakes).
		tag selected by model -> rg (with 0.0136% of the mistakes).
		tag selected by model -> sp (with 0.0136% of the mistakes).
		tag selected by model -> vm (with 0.1358% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.0543% of the mistakes).
		tag selected by model -> nc (with 0.0950% of the mistakes).
		tag selected by model -> vm (with 0.2444% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 7.3048% of the mistakes).
		tag selected by model -> nc (with 7.5356% of the mistakes).
		tag selected by model -> np (with 2.3218% of the mistakes).
		tag selected by model -> nu (with 0.0679% of the mistakes).
		tag selected by model -> sp (with 0.0136% of the mistakes).
		tag selected by model -> va (with 0.0136% of the mistakes).
		tag selected by model -> vs (with 0.1222% of the mistakes).

	(original tag) vs: 
		tag selected by model -> aq (with 0.0543% of the mistakes).
		tag selected by model -> nc (with 0.1086% of the mistakes).
		tag selected by model -> np (with 0.0407% of the mistakes).
		tag selected by model -> rg (with 0.0679% of the mistakes).
		tag selected by model -> vm (with 0.1358% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.1629% of the mistakes).
		tag selected by model -> nc (with 0.1086% of the mistakes).
		tag selected by model -> vm (with 0.0136% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0272% of the mistakes).
		tag selected by model -> nc (with 0.8961% of the mistakes).
		tag selected by model -> nu (with 0.0407% of the mistakes).


N = 1, clasificador = svm.LinearSVC:

	Time:
		real	0m43.646s
		user	0m35.172s
		sys	0m0.320s
	Accuracy: 94.43%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> nc (with 0.0190% of the mistakes).
		tag selected by model -> rg (with 0.0379% of the mistakes).

	(original tag) aq: 
		tag selected by model -> di (with 0.4550% of the mistakes).
		tag selected by model -> dn (with 0.1327% of the mistakes).
		tag selected by model -> nc (with 9.9716% of the mistakes).
		tag selected by model -> np (with 0.6256% of the mistakes).
		tag selected by model -> rg (with 0.1896% of the mistakes).
		tag selected by model -> sp (with 0.1137% of the mistakes).
		tag selected by model -> un (with 0.0379% of the mistakes).
		tag selected by model -> vm (with 7.3555% of the mistakes).

	(original tag) cc: 
		tag selected by model -> cs (with 0.0190% of the mistakes).
		tag selected by model -> nc (with 0.0190% of the mistakes).
		tag selected by model -> np (with 0.0190% of the mistakes).
		tag selected by model -> rg (with 0.8531% of the mistakes).
		tag selected by model -> sp (with 0.0190% of the mistakes).
		tag selected by model -> vm (with 0.1896% of the mistakes).
		tag selected by model -> vs (with 0.0190% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.1137% of the mistakes).
		tag selected by model -> cc (with 0.3791% of the mistakes).
		tag selected by model -> nc (with 0.1327% of the mistakes).
		tag selected by model -> pr (with 6.2180% of the mistakes).
		tag selected by model -> rg (with 0.1137% of the mistakes).
		tag selected by model -> sp (with 0.3602% of the mistakes).
		tag selected by model -> vm (with 0.3223% of the mistakes).

	(original tag) da: 
		tag selected by model -> dn (with 0.0190% of the mistakes).
		tag selected by model -> nc (with 1.6303% of the mistakes).
		tag selected by model -> np (with 0.0758% of the mistakes).
		tag selected by model -> nu (with 1.0616% of the mistakes).
		tag selected by model -> pp (with 0.1517% of the mistakes).
		tag selected by model -> vm (with 0.0190% of the mistakes).
		tag selected by model -> w (with 0.0190% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0190% of the mistakes).
		tag selected by model -> np (with 0.0190% of the mistakes).
		tag selected by model -> pd (with 0.1137% of the mistakes).

	(original tag) de: 
		tag selected by model -> pt (with 0.0948% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.6445% of the mistakes).
		tag selected by model -> nc (with 0.0948% of the mistakes).
		tag selected by model -> np (with 0.0190% of the mistakes).
		tag selected by model -> pi (with 0.4929% of the mistakes).
		tag selected by model -> rg (with 0.4550% of the mistakes).
		tag selected by model -> vm (with 0.0379% of the mistakes).

	(original tag) dn: 
		tag selected by model -> di (with 0.5308% of the mistakes).
		tag selected by model -> nc (with 0.0569% of the mistakes).
		tag selected by model -> np (with 0.0379% of the mistakes).
		tag selected by model -> nu (with 0.0379% of the mistakes).
		tag selected by model -> pn (with 0.0758% of the mistakes).
		tag selected by model -> vm (with 0.0190% of the mistakes).

	(original tag) dt: 
		tag selected by model -> nc (with 0.0190% of the mistakes).
		tag selected by model -> pt (with 0.2844% of the mistakes).
		tag selected by model -> vm (with 0.0190% of the mistakes).

	(original tag) fs: 
		tag selected by model -> vm (with 0.0379% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0190% of the mistakes).
		tag selected by model -> nc (with 0.0758% of the mistakes).
		tag selected by model -> nu (with 0.0758% of the mistakes).
		tag selected by model -> sp (with 0.0379% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.2275% of the mistakes).
		tag selected by model -> aq (with 7.3555% of the mistakes).
		tag selected by model -> cc (with 0.0190% of the mistakes).
		tag selected by model -> da (with 0.0190% of the mistakes).
		tag selected by model -> dd (with 0.0379% of the mistakes).
		tag selected by model -> di (with 0.0758% of the mistakes).
		tag selected by model -> dn (with 0.1706% of the mistakes).
		tag selected by model -> np (with 2.1043% of the mistakes).
		tag selected by model -> nu (with 0.0379% of the mistakes).
		tag selected by model -> pi (with 0.0379% of the mistakes).
		tag selected by model -> pn (with 0.0948% of the mistakes).
		tag selected by model -> pp (with 0.0379% of the mistakes).
		tag selected by model -> rg (with 0.3602% of the mistakes).
		tag selected by model -> sp (with 0.1896% of the mistakes).
		tag selected by model -> un (with 0.0190% of the mistakes).
		tag selected by model -> vm (with 6.2749% of the mistakes).
		tag selected by model -> vs (with 0.3223% of the mistakes).
		tag selected by model -> zm (with 0.0379% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.3602% of the mistakes).
		tag selected by model -> cc (with 0.0190% of the mistakes).
		tag selected by model -> dd (with 0.0190% of the mistakes).
		tag selected by model -> nc (with 4.6445% of the mistakes).
		tag selected by model -> pd (with 0.0190% of the mistakes).
		tag selected by model -> pp (with 0.0190% of the mistakes).
		tag selected by model -> sp (with 0.0569% of the mistakes).
		tag selected by model -> vm (with 1.1185% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.2654% of the mistakes).
		tag selected by model -> dn (with 0.0569% of the mistakes).
		tag selected by model -> nc (with 1.7820% of the mistakes).
		tag selected by model -> np (with 0.0569% of the mistakes).
		tag selected by model -> vm (with 0.3602% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.6445% of the mistakes).

	(original tag) pd: 
		tag selected by model -> dd (with 0.3033% of the mistakes).
		tag selected by model -> nc (with 0.0569% of the mistakes).

	(original tag) pe: 
		tag selected by model -> pt (with 0.0190% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0379% of the mistakes).
		tag selected by model -> di (with 4.7773% of the mistakes).
		tag selected by model -> nc (with 0.0190% of the mistakes).
		tag selected by model -> pr (with 0.0190% of the mistakes).
		tag selected by model -> rg (with 0.2464% of the mistakes).

	(original tag) pn: 
		tag selected by model -> aq (with 0.0190% of the mistakes).
		tag selected by model -> dn (with 0.9668% of the mistakes).
		tag selected by model -> pi (with 0.0190% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0190% of the mistakes).
		tag selected by model -> da (with 3.6209% of the mistakes).
		tag selected by model -> p0 (with 1.1564% of the mistakes).
		tag selected by model -> rg (with 0.4360% of the mistakes).

	(original tag) pr: 
		tag selected by model -> cs (with 1.6872% of the mistakes).
		tag selected by model -> rg (with 0.0569% of the mistakes).
		tag selected by model -> un (with 0.0190% of the mistakes).

	(original tag) pt: 
		tag selected by model -> aq (with 0.0190% of the mistakes).
		tag selected by model -> dt (with 0.0569% of the mistakes).
		tag selected by model -> pr (with 0.0190% of the mistakes).

	(original tag) px: 
		tag selected by model -> aq (with 0.0190% of the mistakes).
		tag selected by model -> dp (with 0.0569% of the mistakes).
		tag selected by model -> nc (with 0.0569% of the mistakes).
		tag selected by model -> vm (with 0.0569% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 2.8626% of the mistakes).
		tag selected by model -> cc (with 0.3981% of the mistakes).
		tag selected by model -> cs (with 0.2275% of the mistakes).
		tag selected by model -> di (with 0.0379% of the mistakes).
		tag selected by model -> dn (with 0.0569% of the mistakes).
		tag selected by model -> nc (with 0.7204% of the mistakes).
		tag selected by model -> np (with 0.0569% of the mistakes).
		tag selected by model -> pi (with 0.3033% of the mistakes).
		tag selected by model -> rn (with 0.4360% of the mistakes).
		tag selected by model -> sp (with 0.3223% of the mistakes).
		tag selected by model -> vm (with 1.3839% of the mistakes).
		tag selected by model -> vs (with 0.0190% of the mistakes).

	(original tag) rn: 
		tag selected by model -> cc (with 0.0569% of the mistakes).
		tag selected by model -> rg (with 0.0569% of the mistakes).
		tag selected by model -> vm (with 0.0190% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.3033% of the mistakes).
		tag selected by model -> cs (with 0.9858% of the mistakes).
		tag selected by model -> nc (with 0.0948% of the mistakes).
		tag selected by model -> rg (with 0.0758% of the mistakes).
		tag selected by model -> vm (with 0.2085% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.1896% of the mistakes).
		tag selected by model -> cs (with 0.0379% of the mistakes).
		tag selected by model -> fe (with 0.3033% of the mistakes).
		tag selected by model -> fg (with 0.0190% of the mistakes).
		tag selected by model -> fp (with 0.0379% of the mistakes).
		tag selected by model -> fz (with 0.0190% of the mistakes).
		tag selected by model -> nc (with 0.2085% of the mistakes).
		tag selected by model -> np (with 0.1896% of the mistakes).
		tag selected by model -> pt (with 0.0190% of the mistakes).
		tag selected by model -> rg (with 0.0190% of the mistakes).
		tag selected by model -> sp (with 0.0190% of the mistakes).
		tag selected by model -> vm (with 0.1517% of the mistakes).

	(original tag) va: 
		tag selected by model -> vm (with 0.1896% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 6.9763% of the mistakes).
		tag selected by model -> nc (with 4.7583% of the mistakes).
		tag selected by model -> np (with 2.0853% of the mistakes).
		tag selected by model -> sp (with 0.0190% of the mistakes).
		tag selected by model -> va (with 0.0190% of the mistakes).
		tag selected by model -> vs (with 0.1517% of the mistakes).

	(original tag) vs: 
		tag selected by model -> nc (with 0.0190% of the mistakes).
		tag selected by model -> np (with 0.0379% of the mistakes).
		tag selected by model -> rg (with 0.1137% of the mistakes).
		tag selected by model -> vm (with 0.0569% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.0379% of the mistakes).
		tag selected by model -> nc (with 0.0190% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0190% of the mistakes).
		tag selected by model -> nc (with 1.0427% of the mistakes).

N = 2, clasificador = svm.LinearSVC:

	Time:
		real	0m48.687s
		user	0m38.060s
		sys	0m0.356s
	Accuracy: 94.29%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> nc (with 0.0185% of the mistakes).
		tag selected by model -> rg (with 0.0185% of the mistakes).

	(original tag) aq: 
		tag selected by model -> dd (with 0.0185% of the mistakes).
		tag selected by model -> di (with 0.4437% of the mistakes).
		tag selected by model -> dn (with 0.0740% of the mistakes).
		tag selected by model -> nc (with 10.8893% of the mistakes).
		tag selected by model -> np (with 0.6286% of the mistakes).
		tag selected by model -> rg (with 0.1664% of the mistakes).
		tag selected by model -> sp (with 0.0924% of the mistakes).
		tag selected by model -> un (with 0.0185% of the mistakes).
		tag selected by model -> vm (with 6.9329% of the mistakes).

	(original tag) cc: 
		tag selected by model -> cs (with 0.0185% of the mistakes).
		tag selected by model -> nc (with 0.0185% of the mistakes).
		tag selected by model -> np (with 0.0185% of the mistakes).
		tag selected by model -> rg (with 0.8319% of the mistakes).
		tag selected by model -> sp (with 0.0185% of the mistakes).
		tag selected by model -> vm (with 0.1849% of the mistakes).
		tag selected by model -> vs (with 0.0185% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.0555% of the mistakes).
		tag selected by model -> cc (with 0.3698% of the mistakes).
		tag selected by model -> nc (with 0.1849% of the mistakes).
		tag selected by model -> pr (with 4.2337% of the mistakes).
		tag selected by model -> rg (with 0.1109% of the mistakes).
		tag selected by model -> sp (with 0.3513% of the mistakes).
		tag selected by model -> vm (with 0.2958% of the mistakes).

	(original tag) da: 
		tag selected by model -> dn (with 0.0185% of the mistakes).
		tag selected by model -> nc (with 1.5899% of the mistakes).
		tag selected by model -> np (with 0.0740% of the mistakes).
		tag selected by model -> nu (with 1.0353% of the mistakes).
		tag selected by model -> pp (with 0.3698% of the mistakes).
		tag selected by model -> vm (with 0.0185% of the mistakes).
		tag selected by model -> w (with 0.0185% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0370% of the mistakes).
		tag selected by model -> np (with 0.0185% of the mistakes).
		tag selected by model -> pd (with 0.1109% of the mistakes).

	(original tag) de: 
		tag selected by model -> pt (with 0.0924% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.5361% of the mistakes).
		tag selected by model -> nc (with 0.0924% of the mistakes).
		tag selected by model -> np (with 0.0185% of the mistakes).
		tag selected by model -> pi (with 0.6101% of the mistakes).
		tag selected by model -> rg (with 0.4437% of the mistakes).
		tag selected by model -> vm (with 0.0370% of the mistakes).

	(original tag) dn: 
		tag selected by model -> di (with 0.5177% of the mistakes).
		tag selected by model -> nc (with 0.0740% of the mistakes).
		tag selected by model -> np (with 0.0370% of the mistakes).
		tag selected by model -> nu (with 0.0370% of the mistakes).
		tag selected by model -> pn (with 0.0924% of the mistakes).
		tag selected by model -> vm (with 0.0185% of the mistakes).

	(original tag) dt: 
		tag selected by model -> nc (with 0.0185% of the mistakes).
		tag selected by model -> pt (with 0.2773% of the mistakes).
		tag selected by model -> vm (with 0.0185% of the mistakes).

	(original tag) fs: 
		tag selected by model -> vm (with 0.0370% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0185% of the mistakes).
		tag selected by model -> nc (with 0.0740% of the mistakes).
		tag selected by model -> nu (with 0.0740% of the mistakes).
		tag selected by model -> sp (with 0.0370% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.2219% of the mistakes).
		tag selected by model -> aq (with 8.8186% of the mistakes).
		tag selected by model -> cc (with 0.0185% of the mistakes).
		tag selected by model -> cs (with 0.0185% of the mistakes).
		tag selected by model -> da (with 0.0185% of the mistakes).
		tag selected by model -> dd (with 0.0370% of the mistakes).
		tag selected by model -> di (with 0.0740% of the mistakes).
		tag selected by model -> dn (with 0.1479% of the mistakes).
		tag selected by model -> np (with 2.0336% of the mistakes).
		tag selected by model -> nu (with 0.0370% of the mistakes).
		tag selected by model -> pi (with 0.0370% of the mistakes).
		tag selected by model -> pn (with 0.0924% of the mistakes).
		tag selected by model -> pp (with 0.0370% of the mistakes).
		tag selected by model -> rg (with 0.2219% of the mistakes).
		tag selected by model -> sp (with 0.1849% of the mistakes).
		tag selected by model -> un (with 0.0185% of the mistakes).
		tag selected by model -> vm (with 6.3598% of the mistakes).
		tag selected by model -> vs (with 0.2588% of the mistakes).
		tag selected by model -> zm (with 0.0370% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.3143% of the mistakes).
		tag selected by model -> cc (with 0.0185% of the mistakes).
		tag selected by model -> dd (with 0.0185% of the mistakes).
		tag selected by model -> nc (with 4.5850% of the mistakes).
		tag selected by model -> pd (with 0.0185% of the mistakes).
		tag selected by model -> pp (with 0.0185% of the mistakes).
		tag selected by model -> sp (with 0.0555% of the mistakes).
		tag selected by model -> vm (with 1.0538% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.1109% of the mistakes).
		tag selected by model -> dn (with 0.0555% of the mistakes).
		tag selected by model -> nc (with 1.8673% of the mistakes).
		tag selected by model -> np (with 0.0555% of the mistakes).
		tag selected by model -> vm (with 0.3698% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.6286% of the mistakes).

	(original tag) pd: 
		tag selected by model -> dd (with 0.2958% of the mistakes).
		tag selected by model -> nc (with 0.0555% of the mistakes).

	(original tag) pe: 
		tag selected by model -> pt (with 0.0185% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.1479% of the mistakes).
		tag selected by model -> di (with 4.5480% of the mistakes).
		tag selected by model -> nc (with 0.0370% of the mistakes).
		tag selected by model -> pr (with 0.0185% of the mistakes).
		tag selected by model -> rg (with 0.2219% of the mistakes).

	(original tag) pn: 
		tag selected by model -> dn (with 0.9798% of the mistakes).
		tag selected by model -> nc (with 0.0185% of the mistakes).
		tag selected by model -> pi (with 0.0185% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0185% of the mistakes).
		tag selected by model -> da (with 2.9026% of the mistakes).
		tag selected by model -> nc (with 0.0185% of the mistakes).
		tag selected by model -> p0 (with 1.1647% of the mistakes).
		tag selected by model -> rg (with 0.3698% of the mistakes).

	(original tag) pr: 
		tag selected by model -> cs (with 2.0521% of the mistakes).
		tag selected by model -> rg (with 0.0555% of the mistakes).
		tag selected by model -> un (with 0.0185% of the mistakes).

	(original tag) pt: 
		tag selected by model -> aq (with 0.0185% of the mistakes).
		tag selected by model -> dt (with 0.0555% of the mistakes).
		tag selected by model -> pr (with 0.0185% of the mistakes).

	(original tag) px: 
		tag selected by model -> dp (with 0.0555% of the mistakes).
		tag selected by model -> nc (with 0.0555% of the mistakes).
		tag selected by model -> vm (with 0.0740% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 1.7563% of the mistakes).
		tag selected by model -> cc (with 0.3882% of the mistakes).
		tag selected by model -> cs (with 0.2403% of the mistakes).
		tag selected by model -> da (with 0.0185% of the mistakes).
		tag selected by model -> di (with 0.0555% of the mistakes).
		tag selected by model -> dn (with 0.0370% of the mistakes).
		tag selected by model -> nc (with 1.8488% of the mistakes).
		tag selected by model -> np (with 0.0555% of the mistakes).
		tag selected by model -> pi (with 0.2958% of the mistakes).
		tag selected by model -> pr (with 0.0185% of the mistakes).
		tag selected by model -> rn (with 0.4252% of the mistakes).
		tag selected by model -> sp (with 0.3143% of the mistakes).
		tag selected by model -> vm (with 1.3311% of the mistakes).
		tag selected by model -> vs (with 0.0185% of the mistakes).

	(original tag) rn: 
		tag selected by model -> cc (with 0.0555% of the mistakes).
		tag selected by model -> rg (with 0.0555% of the mistakes).
		tag selected by model -> vm (with 0.0185% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.1849% of the mistakes).
		tag selected by model -> cs (with 0.9983% of the mistakes).
		tag selected by model -> nc (with 0.1849% of the mistakes).
		tag selected by model -> rg (with 0.0740% of the mistakes).
		tag selected by model -> vm (with 0.2034% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.1849% of the mistakes).
		tag selected by model -> cs (with 0.0370% of the mistakes).
		tag selected by model -> fe (with 0.2958% of the mistakes).
		tag selected by model -> fg (with 0.0185% of the mistakes).
		tag selected by model -> fp (with 0.0370% of the mistakes).
		tag selected by model -> fz (with 0.0185% of the mistakes).
		tag selected by model -> nc (with 0.2034% of the mistakes).
		tag selected by model -> np (with 0.1849% of the mistakes).
		tag selected by model -> pt (with 0.0185% of the mistakes).
		tag selected by model -> rg (with 0.0185% of the mistakes).
		tag selected by model -> sp (with 0.0185% of the mistakes).
		tag selected by model -> vm (with 0.1479% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.0185% of the mistakes).
		tag selected by model -> vm (with 0.1109% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 6.6001% of the mistakes).
		tag selected by model -> nc (with 6.3598% of the mistakes).
		tag selected by model -> np (with 2.0706% of the mistakes).
		tag selected by model -> sp (with 0.0185% of the mistakes).
		tag selected by model -> va (with 0.0185% of the mistakes).
		tag selected by model -> vs (with 0.1479% of the mistakes).

	(original tag) vs: 
		tag selected by model -> nc (with 0.0555% of the mistakes).
		tag selected by model -> np (with 0.0370% of the mistakes).
		tag selected by model -> rg (with 0.0924% of the mistakes).
		tag selected by model -> vm (with 0.0555% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.0185% of the mistakes).
		tag selected by model -> nc (with 0.0370% of the mistakes).
		tag selected by model -> np (with 0.0185% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0185% of the mistakes).
		tag selected by model -> nc (with 1.0168% of the mistakes).

N = 3, clasificador = svm.LinearSVC:

	Time:
		real	0m54.834s
		user	0m41.292s
		sys	0m0.324s
	Accuracy: 94.40%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> nc (with 0.0188% of the mistakes).
		tag selected by model -> rg (with 0.0188% of the mistakes).

	(original tag) aq: 
		tag selected by model -> dd (with 0.0188% of the mistakes).
		tag selected by model -> di (with 0.4331% of the mistakes).
		tag selected by model -> dn (with 0.0753% of the mistakes).
		tag selected by model -> nc (with 10.7533% of the mistakes).
		tag selected by model -> np (with 0.6026% of the mistakes).
		tag selected by model -> rg (with 0.1507% of the mistakes).
		tag selected by model -> sp (with 0.0942% of the mistakes).
		tag selected by model -> un (with 0.0188% of the mistakes).
		tag selected by model -> vm (with 6.5725% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0942% of the mistakes).
		tag selected by model -> cs (with 0.0188% of the mistakes).
		tag selected by model -> nc (with 0.0565% of the mistakes).
		tag selected by model -> np (with 0.0188% of the mistakes).
		tag selected by model -> rg (with 0.8851% of the mistakes).
		tag selected by model -> sp (with 0.0188% of the mistakes).
		tag selected by model -> vm (with 0.0942% of the mistakes).
		tag selected by model -> vs (with 0.0188% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.1130% of the mistakes).
		tag selected by model -> cc (with 0.3766% of the mistakes).
		tag selected by model -> nc (with 0.1695% of the mistakes).
		tag selected by model -> pr (with 4.1431% of the mistakes).
		tag selected by model -> rg (with 0.0753% of the mistakes).
		tag selected by model -> sp (with 0.3578% of the mistakes).
		tag selected by model -> vm (with 0.3013% of the mistakes).

	(original tag) da: 
		tag selected by model -> dn (with 0.0188% of the mistakes).
		tag selected by model -> nc (with 1.6196% of the mistakes).
		tag selected by model -> np (with 0.0753% of the mistakes).
		tag selected by model -> nu (with 1.0546% of the mistakes).
		tag selected by model -> pp (with 0.4331% of the mistakes).
		tag selected by model -> vm (with 0.0188% of the mistakes).
		tag selected by model -> w (with 0.0188% of the mistakes).

	(original tag) dd: 
		tag selected by model -> np (with 0.0188% of the mistakes).
		tag selected by model -> pd (with 0.1318% of the mistakes).

	(original tag) de: 
		tag selected by model -> dt (with 0.0377% of the mistakes).
		tag selected by model -> pt (with 0.0565% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.5838% of the mistakes).
		tag selected by model -> nc (with 0.0942% of the mistakes).
		tag selected by model -> np (with 0.0188% of the mistakes).
		tag selected by model -> pi (with 0.6403% of the mistakes).
		tag selected by model -> rg (with 0.4520% of the mistakes).
		tag selected by model -> vm (with 0.0377% of the mistakes).

	(original tag) dn: 
		tag selected by model -> di (with 0.5273% of the mistakes).
		tag selected by model -> nc (with 0.0565% of the mistakes).
		tag selected by model -> np (with 0.0377% of the mistakes).
		tag selected by model -> nu (with 0.0377% of the mistakes).
		tag selected by model -> pn (with 0.1507% of the mistakes).
		tag selected by model -> vm (with 0.0188% of the mistakes).

	(original tag) dt: 
		tag selected by model -> nc (with 0.0188% of the mistakes).
		tag selected by model -> pt (with 0.1883% of the mistakes).
		tag selected by model -> vm (with 0.0188% of the mistakes).

	(original tag) fs: 
		tag selected by model -> vm (with 0.0377% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0188% of the mistakes).
		tag selected by model -> nc (with 0.0753% of the mistakes).
		tag selected by model -> nu (with 0.0753% of the mistakes).
		tag selected by model -> sp (with 0.0377% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.2260% of the mistakes).
		tag selected by model -> aq (with 9.2279% of the mistakes).
		tag selected by model -> cc (with 0.0188% of the mistakes).
		tag selected by model -> da (with 0.0188% of the mistakes).
		tag selected by model -> dd (with 0.0377% of the mistakes).
		tag selected by model -> di (with 0.0753% of the mistakes).
		tag selected by model -> dn (with 0.1507% of the mistakes).
		tag selected by model -> np (with 1.9962% of the mistakes).
		tag selected by model -> nu (with 0.0377% of the mistakes).
		tag selected by model -> pi (with 0.0377% of the mistakes).
		tag selected by model -> pn (with 0.0942% of the mistakes).
		tag selected by model -> pp (with 0.0377% of the mistakes).
		tag selected by model -> rg (with 0.2260% of the mistakes).
		tag selected by model -> sp (with 0.1883% of the mistakes).
		tag selected by model -> un (with 0.0188% of the mistakes).
		tag selected by model -> vm (with 6.0075% of the mistakes).
		tag selected by model -> vs (with 0.2637% of the mistakes).
		tag selected by model -> zm (with 0.0377% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.3578% of the mistakes).
		tag selected by model -> cc (with 0.0188% of the mistakes).
		tag selected by model -> dd (with 0.0188% of the mistakes).
		tag selected by model -> nc (with 4.5386% of the mistakes).
		tag selected by model -> pd (with 0.0188% of the mistakes).
		tag selected by model -> pp (with 0.0188% of the mistakes).
		tag selected by model -> sp (with 0.0565% of the mistakes).
		tag selected by model -> vm (with 1.1864% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.1318% of the mistakes).
		tag selected by model -> dn (with 0.0565% of the mistakes).
		tag selected by model -> nc (with 1.7137% of the mistakes).
		tag selected by model -> np (with 0.0565% of the mistakes).
		tag selected by model -> vm (with 0.4708% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.6215% of the mistakes).

	(original tag) pd: 
		tag selected by model -> dd (with 0.3013% of the mistakes).
		tag selected by model -> nc (with 0.0565% of the mistakes).

	(original tag) pe: 
		tag selected by model -> dt (with 0.0188% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0565% of the mistakes).
		tag selected by model -> di (with 4.6704% of the mistakes).
		tag selected by model -> nc (with 0.0377% of the mistakes).
		tag selected by model -> pr (with 0.0188% of the mistakes).
		tag selected by model -> rg (with 0.2260% of the mistakes).

	(original tag) pn: 
		tag selected by model -> dn (with 1.0169% of the mistakes).
		tag selected by model -> pi (with 0.0188% of the mistakes).
		tag selected by model -> vm (with 0.0188% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0188% of the mistakes).
		tag selected by model -> da (with 2.9567% of the mistakes).
		tag selected by model -> nc (with 0.0188% of the mistakes).
		tag selected by model -> p0 (with 1.1676% of the mistakes).
		tag selected by model -> rg (with 0.4143% of the mistakes).

	(original tag) pr: 
		tag selected by model -> cs (with 1.4313% of the mistakes).
		tag selected by model -> rg (with 0.0565% of the mistakes).

	(original tag) pt: 
		tag selected by model -> dt (with 0.2825% of the mistakes).
		tag selected by model -> pr (with 0.0188% of the mistakes).
		tag selected by model -> vm (with 0.0188% of the mistakes).

	(original tag) px: 
		tag selected by model -> dp (with 0.0565% of the mistakes).
		tag selected by model -> nc (with 0.0753% of the mistakes).
		tag selected by model -> vm (with 0.0753% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 1.8456% of the mistakes).
		tag selected by model -> cc (with 0.3766% of the mistakes).
		tag selected by model -> cs (with 0.2260% of the mistakes).
		tag selected by model -> di (with 0.0565% of the mistakes).
		tag selected by model -> dn (with 0.0377% of the mistakes).
		tag selected by model -> nc (with 1.4878% of the mistakes).
		tag selected by model -> np (with 0.0565% of the mistakes).
		tag selected by model -> pi (with 0.3013% of the mistakes).
		tag selected by model -> pr (with 0.0188% of the mistakes).
		tag selected by model -> rn (with 0.4331% of the mistakes).
		tag selected by model -> sp (with 0.3202% of the mistakes).
		tag selected by model -> vm (with 1.7702% of the mistakes).
		tag selected by model -> vs (with 0.0188% of the mistakes).

	(original tag) rn: 
		tag selected by model -> cc (with 0.0565% of the mistakes).
		tag selected by model -> rg (with 0.0565% of the mistakes).
		tag selected by model -> vm (with 0.0188% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.1883% of the mistakes).
		tag selected by model -> cs (with 1.0169% of the mistakes).
		tag selected by model -> nc (with 0.1883% of the mistakes).
		tag selected by model -> rg (with 0.0753% of the mistakes).
		tag selected by model -> vm (with 0.2072% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.2260% of the mistakes).
		tag selected by model -> cs (with 0.0377% of the mistakes).
		tag selected by model -> fe (with 0.3013% of the mistakes).
		tag selected by model -> fg (with 0.0188% of the mistakes).
		tag selected by model -> fp (with 0.0377% of the mistakes).
		tag selected by model -> fz (with 0.0188% of the mistakes).
		tag selected by model -> nc (with 0.2072% of the mistakes).
		tag selected by model -> np (with 0.1695% of the mistakes).
		tag selected by model -> pt (with 0.0188% of the mistakes).
		tag selected by model -> rg (with 0.0188% of the mistakes).
		tag selected by model -> sp (with 0.0188% of the mistakes).
		tag selected by model -> vm (with 0.1318% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.0188% of the mistakes).
		tag selected by model -> vm (with 0.1130% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 6.9868% of the mistakes).
		tag selected by model -> nc (with 6.0829% of the mistakes).
		tag selected by model -> np (with 2.1092% of the mistakes).
		tag selected by model -> sp (with 0.0188% of the mistakes).
		tag selected by model -> va (with 0.0188% of the mistakes).
		tag selected by model -> vs (with 0.1507% of the mistakes).

	(original tag) vs: 
		tag selected by model -> nc (with 0.0942% of the mistakes).
		tag selected by model -> np (with 0.0377% of the mistakes).
		tag selected by model -> rg (with 0.1130% of the mistakes).
		tag selected by model -> vm (with 0.0565% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.0188% of the mistakes).
		tag selected by model -> nc (with 0.0377% of the mistakes).
		tag selected by model -> np (with 0.0188% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0188% of the mistakes).
		tag selected by model -> nc (with 1.0358% of the mistakes).

N = 4, clasificador = svm.LinearSVC:

	Time:
		real	0m42.796s
		user	0m41.364s
		sys	0m0.316s
	Accuracy: 94.46%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> nc (with 0.0191% of the mistakes).
		tag selected by model -> rg (with 0.0191% of the mistakes).

	(original tag) aq: 
		tag selected by model -> dd (with 0.0191% of the mistakes).
		tag selected by model -> di (with 0.4383% of the mistakes).
		tag selected by model -> dn (with 0.0762% of the mistakes).
		tag selected by model -> nc (with 11.0328% of the mistakes).
		tag selected by model -> np (with 0.6098% of the mistakes).
		tag selected by model -> pr (with 0.0191% of the mistakes).
		tag selected by model -> rg (with 0.1524% of the mistakes).
		tag selected by model -> sp (with 0.0953% of the mistakes).
		tag selected by model -> un (with 0.0191% of the mistakes).
		tag selected by model -> vm (with 6.5358% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0762% of the mistakes).
		tag selected by model -> cs (with 0.0191% of the mistakes).
		tag selected by model -> nc (with 0.0572% of the mistakes).
		tag selected by model -> np (with 0.0191% of the mistakes).
		tag selected by model -> rg (with 0.8956% of the mistakes).
		tag selected by model -> sp (with 0.0191% of the mistakes).
		tag selected by model -> vm (with 0.1143% of the mistakes).
		tag selected by model -> vs (with 0.0191% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.0762% of the mistakes).
		tag selected by model -> cc (with 0.3811% of the mistakes).
		tag selected by model -> nc (with 0.1524% of the mistakes).
		tag selected by model -> pr (with 3.7729% of the mistakes).
		tag selected by model -> rg (with 0.0762% of the mistakes).
		tag selected by model -> sp (with 0.3620% of the mistakes).
		tag selected by model -> vm (with 0.3620% of the mistakes).

	(original tag) da: 
		tag selected by model -> dn (with 0.0191% of the mistakes).
		tag selected by model -> nc (with 1.6578% of the mistakes).
		tag selected by model -> np (with 0.0762% of the mistakes).
		tag selected by model -> nu (with 1.0671% of the mistakes).
		tag selected by model -> pp (with 0.5145% of the mistakes).
		tag selected by model -> w (with 0.0191% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0191% of the mistakes).
		tag selected by model -> np (with 0.0191% of the mistakes).
		tag selected by model -> pd (with 0.1143% of the mistakes).

	(original tag) de: 
		tag selected by model -> dt (with 0.0572% of the mistakes).
		tag selected by model -> pt (with 0.0381% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.5907% of the mistakes).
		tag selected by model -> nc (with 0.0953% of the mistakes).
		tag selected by model -> np (with 0.0191% of the mistakes).
		tag selected by model -> pi (with 0.6669% of the mistakes).
		tag selected by model -> rg (with 0.4573% of the mistakes).
		tag selected by model -> vm (with 0.0381% of the mistakes).

	(original tag) dn: 
		tag selected by model -> di (with 0.5335% of the mistakes).
		tag selected by model -> nc (with 0.0572% of the mistakes).
		tag selected by model -> np (with 0.0381% of the mistakes).
		tag selected by model -> nu (with 0.0381% of the mistakes).
		tag selected by model -> pn (with 0.1334% of the mistakes).
		tag selected by model -> vm (with 0.0191% of the mistakes).

	(original tag) dt: 
		tag selected by model -> nc (with 0.0191% of the mistakes).
		tag selected by model -> pt (with 0.1715% of the mistakes).
		tag selected by model -> vm (with 0.0191% of the mistakes).

	(original tag) fs: 
		tag selected by model -> vm (with 0.0381% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0191% of the mistakes).
		tag selected by model -> nc (with 0.0762% of the mistakes).
		tag selected by model -> nu (with 0.0762% of the mistakes).
		tag selected by model -> sp (with 0.0381% of the mistakes).

	(original tag) nc: 
		tag selected by model -> ao (with 0.2287% of the mistakes).
		tag selected by model -> aq (with 9.3178% of the mistakes).
		tag selected by model -> cc (with 0.0191% of the mistakes).
		tag selected by model -> da (with 0.0191% of the mistakes).
		tag selected by model -> dd (with 0.0381% of the mistakes).
		tag selected by model -> di (with 0.0762% of the mistakes).
		tag selected by model -> dn (with 0.1334% of the mistakes).
		tag selected by model -> np (with 2.0198% of the mistakes).
		tag selected by model -> nu (with 0.0762% of the mistakes).
		tag selected by model -> pi (with 0.0381% of the mistakes).
		tag selected by model -> pn (with 0.0762% of the mistakes).
		tag selected by model -> pp (with 0.0381% of the mistakes).
		tag selected by model -> rg (with 0.2287% of the mistakes).
		tag selected by model -> sp (with 0.1905% of the mistakes).
		tag selected by model -> un (with 0.0191% of the mistakes).
		tag selected by model -> vm (with 5.2401% of the mistakes).
		tag selected by model -> vs (with 0.2668% of the mistakes).
		tag selected by model -> zm (with 0.0381% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.3620% of the mistakes).
		tag selected by model -> cc (with 0.0191% of the mistakes).
		tag selected by model -> dd (with 0.0191% of the mistakes).
		tag selected by model -> nc (with 4.6113% of the mistakes).
		tag selected by model -> pd (with 0.0191% of the mistakes).
		tag selected by model -> pp (with 0.0191% of the mistakes).
		tag selected by model -> sp (with 0.0572% of the mistakes).
		tag selected by model -> vm (with 1.1623% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.1143% of the mistakes).
		tag selected by model -> dn (with 0.0572% of the mistakes).
		tag selected by model -> nc (with 1.7340% of the mistakes).
		tag selected by model -> np (with 0.0572% of the mistakes).
		tag selected by model -> vm (with 0.4954% of the mistakes).

	(original tag) p0: 
		tag selected by model -> pp (with 0.6479% of the mistakes).

	(original tag) pd: 
		tag selected by model -> dd (with 0.3049% of the mistakes).
		tag selected by model -> nc (with 0.0572% of the mistakes).

	(original tag) pe: 
		tag selected by model -> dt (with 0.0191% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0762% of the mistakes).
		tag selected by model -> di (with 4.6684% of the mistakes).
		tag selected by model -> nc (with 0.0381% of the mistakes).
		tag selected by model -> pr (with 0.0191% of the mistakes).
		tag selected by model -> rg (with 0.2287% of the mistakes).

	(original tag) pn: 
		tag selected by model -> dn (with 0.9337% of the mistakes).
		tag selected by model -> pi (with 0.0191% of the mistakes).
		tag selected by model -> vm (with 0.0191% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0191% of the mistakes).
		tag selected by model -> da (with 2.9726% of the mistakes).
		tag selected by model -> nc (with 0.0381% of the mistakes).
		tag selected by model -> p0 (with 1.1433% of the mistakes).
		tag selected by model -> rg (with 0.4383% of the mistakes).

	(original tag) pr: 
		tag selected by model -> cs (with 1.3720% of the mistakes).
		tag selected by model -> rg (with 0.0572% of the mistakes).
		tag selected by model -> un (with 0.0191% of the mistakes).

	(original tag) pt: 
		tag selected by model -> dt (with 0.2668% of the mistakes).
		tag selected by model -> pr (with 0.0191% of the mistakes).
		tag selected by model -> vm (with 0.0191% of the mistakes).

	(original tag) px: 
		tag selected by model -> dp (with 0.0572% of the mistakes).
		tag selected by model -> nc (with 0.0762% of the mistakes).
		tag selected by model -> vm (with 0.0762% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 1.8102% of the mistakes).
		tag selected by model -> cc (with 0.4002% of the mistakes).
		tag selected by model -> cs (with 0.2287% of the mistakes).
		tag selected by model -> di (with 0.0572% of the mistakes).
		tag selected by model -> dn (with 0.0381% of the mistakes).
		tag selected by model -> nc (with 1.4863% of the mistakes).
		tag selected by model -> np (with 0.0572% of the mistakes).
		tag selected by model -> pi (with 0.3049% of the mistakes).
		tag selected by model -> pr (with 0.0191% of the mistakes).
		tag selected by model -> rn (with 0.4383% of the mistakes).
		tag selected by model -> sp (with 0.3239% of the mistakes).
		tag selected by model -> vm (with 1.8864% of the mistakes).
		tag selected by model -> vs (with 0.0191% of the mistakes).

	(original tag) rn: 
		tag selected by model -> cc (with 0.0572% of the mistakes).
		tag selected by model -> rg (with 0.0572% of the mistakes).
		tag selected by model -> vm (with 0.0191% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.1524% of the mistakes).
		tag selected by model -> cs (with 1.0290% of the mistakes).
		tag selected by model -> nc (with 0.1905% of the mistakes).
		tag selected by model -> rg (with 0.0762% of the mistakes).
		tag selected by model -> vm (with 0.2477% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.2287% of the mistakes).
		tag selected by model -> cs (with 0.0381% of the mistakes).
		tag selected by model -> fe (with 0.3049% of the mistakes).
		tag selected by model -> fg (with 0.0191% of the mistakes).
		tag selected by model -> fp (with 0.0381% of the mistakes).
		tag selected by model -> fz (with 0.0191% of the mistakes).
		tag selected by model -> nc (with 0.1905% of the mistakes).
		tag selected by model -> np (with 0.1715% of the mistakes).
		tag selected by model -> pt (with 0.0191% of the mistakes).
		tag selected by model -> rg (with 0.0381% of the mistakes).
		tag selected by model -> sp (with 0.0191% of the mistakes).
		tag selected by model -> vm (with 0.1334% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.0191% of the mistakes).
		tag selected by model -> vm (with 0.1143% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 6.7835% of the mistakes).
		tag selected by model -> nc (with 6.6311% of the mistakes).
		tag selected by model -> np (with 2.1341% of the mistakes).
		tag selected by model -> sp (with 0.0191% of the mistakes).
		tag selected by model -> va (with 0.0191% of the mistakes).
		tag selected by model -> vs (with 0.1524% of the mistakes).

	(original tag) vs: 
		tag selected by model -> nc (with 0.0953% of the mistakes).
		tag selected by model -> np (with 0.0381% of the mistakes).
		tag selected by model -> rg (with 0.0953% of the mistakes).
		tag selected by model -> vm (with 0.0572% of the mistakes).

	(original tag) zm: 
		tag selected by model -> nc (with 0.0572% of the mistakes).
		tag selected by model -> np (with 0.0191% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0191% of the mistakes).
		tag selected by model -> nc (with 1.0480% of the mistakes).


N = 1, clasificador = naive_bayes.MultinomialNB:
	
	Time:
		real	44m16.957s
		user	37m26.332s
		sys	0m5.784s
	Accuracy: 82.18%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> aq (with 0.0059% of the mistakes).
		tag selected by model -> da (with 0.1125% of the mistakes).
		tag selected by model -> fc (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 1.3558% of the mistakes).
		tag selected by model -> np (with 0.0296% of the mistakes).
		tag selected by model -> rg (with 0.0059% of the mistakes).
		tag selected by model -> sp (with 0.0237% of the mistakes).
		tag selected by model -> vm (with 0.0178% of the mistakes).

	(original tag) aq: 
		tag selected by model -> da (with 0.7460% of the mistakes).
		tag selected by model -> di (with 0.0178% of the mistakes).
		tag selected by model -> fc (with 0.2724% of the mistakes).
		tag selected by model -> fp (with 0.0237% of the mistakes).
		tag selected by model -> nc (with 7.8390% of the mistakes).
		tag selected by model -> np (with 0.1066% of the mistakes).
		tag selected by model -> sp (with 7.3061% of the mistakes).
		tag selected by model -> vm (with 1.7880% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0059% of the mistakes).
		tag selected by model -> cs (with 0.0059% of the mistakes).
		tag selected by model -> da (with 0.7638% of the mistakes).
		tag selected by model -> nc (with 0.0710% of the mistakes).
		tag selected by model -> np (with 0.6157% of the mistakes).
		tag selected by model -> rg (with 0.2724% of the mistakes).
		tag selected by model -> sp (with 0.1007% of the mistakes).
		tag selected by model -> vm (with 0.0059% of the mistakes).
		tag selected by model -> vs (with 0.0059% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.0059% of the mistakes).
		tag selected by model -> cc (with 0.0947% of the mistakes).
		tag selected by model -> da (with 0.9473% of the mistakes).
		tag selected by model -> fp (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 0.0651% of the mistakes).
		tag selected by model -> np (with 0.0178% of the mistakes).
		tag selected by model -> pr (with 0.5625% of the mistakes).
		tag selected by model -> sp (with 0.4855% of the mistakes).
		tag selected by model -> vm (with 0.0592% of the mistakes).

	(original tag) da: 
		tag selected by model -> nc (with 0.6335% of the mistakes).
		tag selected by model -> np (with 0.0296% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0414% of the mistakes).
		tag selected by model -> cs (with 0.0118% of the mistakes).
		tag selected by model -> da (with 1.0539% of the mistakes).
		tag selected by model -> fc (with 0.0355% of the mistakes).
		tag selected by model -> nc (with 1.4446% of the mistakes).
		tag selected by model -> np (with 0.1362% of the mistakes).
		tag selected by model -> sp (with 0.3552% of the mistakes).
		tag selected by model -> vm (with 0.3789% of the mistakes).

	(original tag) de: 
		tag selected by model -> da (with 0.0178% of the mistakes).
		tag selected by model -> nc (with 0.0059% of the mistakes).
		tag selected by model -> np (with 0.0059% of the mistakes).
		tag selected by model -> sp (with 0.0178% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.6098% of the mistakes).
		tag selected by model -> da (with 0.7697% of the mistakes).
		tag selected by model -> fc (with 0.0237% of the mistakes).
		tag selected by model -> nc (with 0.7046% of the mistakes).
		tag selected by model -> np (with 0.0118% of the mistakes).
		tag selected by model -> rg (with 0.0888% of the mistakes).
		tag selected by model -> sp (with 0.0237% of the mistakes).
		tag selected by model -> vm (with 0.2013% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.0592% of the mistakes).
		tag selected by model -> da (with 0.3020% of the mistakes).
		tag selected by model -> di (with 0.1599% of the mistakes).
		tag selected by model -> fc (with 0.0237% of the mistakes).
		tag selected by model -> nc (with 0.9888% of the mistakes).
		tag selected by model -> np (with 0.3375% of the mistakes).
		tag selected by model -> sp (with 0.1599% of the mistakes).
		tag selected by model -> vm (with 0.1184% of the mistakes).

	(original tag) dp: 
		tag selected by model -> aq (with 0.0118% of the mistakes).
		tag selected by model -> da (with 0.5033% of the mistakes).
		tag selected by model -> fc (with 0.0118% of the mistakes).
		tag selected by model -> nc (with 0.2901% of the mistakes).
		tag selected by model -> np (with 0.0059% of the mistakes).
		tag selected by model -> sp (with 0.1421% of the mistakes).
		tag selected by model -> vm (with 0.1362% of the mistakes).

	(original tag) dt: 
		tag selected by model -> cs (with 0.0059% of the mistakes).
		tag selected by model -> da (with 0.0474% of the mistakes).
		tag selected by model -> fc (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 0.0178% of the mistakes).
		tag selected by model -> np (with 0.0178% of the mistakes).
		tag selected by model -> sp (with 0.0118% of the mistakes).
		tag selected by model -> vm (with 0.0118% of the mistakes).

	(original tag) fa: 
		tag selected by model -> aq (with 0.0118% of the mistakes).
		tag selected by model -> da (with 0.0355% of the mistakes).
		tag selected by model -> fc (with 0.0474% of the mistakes).
		tag selected by model -> nc (with 0.0770% of the mistakes).
		tag selected by model -> np (with 0.0059% of the mistakes).
		tag selected by model -> sp (with 0.0770% of the mistakes).
		tag selected by model -> vm (with 0.0533% of the mistakes).

	(original tag) fc: 
		tag selected by model -> da (with 0.0059% of the mistakes).

	(original tag) fd: 
		tag selected by model -> aq (with 0.1539% of the mistakes).
		tag selected by model -> da (with 0.0296% of the mistakes).
		tag selected by model -> fc (with 0.2131% of the mistakes).
		tag selected by model -> nc (with 0.4085% of the mistakes).
		tag selected by model -> sp (with 0.8171% of the mistakes).
		tag selected by model -> vm (with 0.0474% of the mistakes).

	(original tag) fg: 
		tag selected by model -> aq (with 0.2546% of the mistakes).
		tag selected by model -> da (with 1.5335% of the mistakes).
		tag selected by model -> fc (with 0.3612% of the mistakes).
		tag selected by model -> fp (with 0.0474% of the mistakes).
		tag selected by model -> nc (with 1.5098% of the mistakes).
		tag selected by model -> np (with 0.0770% of the mistakes).
		tag selected by model -> sp (with 1.2552% of the mistakes).
		tag selected by model -> vm (with 0.3138% of the mistakes).

	(original tag) fh: 
		tag selected by model -> nc (with 0.0118% of the mistakes).
		tag selected by model -> sp (with 0.0118% of the mistakes).

	(original tag) fi: 
		tag selected by model -> aq (with 0.0296% of the mistakes).
		tag selected by model -> da (with 0.1480% of the mistakes).
		tag selected by model -> fc (with 0.1599% of the mistakes).
		tag selected by model -> fp (with 0.0237% of the mistakes).
		tag selected by model -> nc (with 0.1776% of the mistakes).
		tag selected by model -> sp (with 0.2487% of the mistakes).
		tag selected by model -> vm (with 0.1717% of the mistakes).

	(original tag) fp: 
		tag selected by model -> da (with 0.0474% of the mistakes).
		tag selected by model -> nc (with 0.0118% of the mistakes).
		tag selected by model -> sp (with 0.0059% of the mistakes).
		tag selected by model -> vm (with 0.0059% of the mistakes).

	(original tag) fs: 
		tag selected by model -> aq (with 0.0118% of the mistakes).
		tag selected by model -> da (with 0.0059% of the mistakes).
		tag selected by model -> fc (with 0.0414% of the mistakes).
		tag selected by model -> fp (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 0.0770% of the mistakes).
		tag selected by model -> sp (with 0.1066% of the mistakes).
		tag selected by model -> vm (with 0.0118% of the mistakes).

	(original tag) fx: 
		tag selected by model -> aq (with 0.0355% of the mistakes).
		tag selected by model -> fc (with 0.1362% of the mistakes).
		tag selected by model -> nc (with 0.2191% of the mistakes).
		tag selected by model -> sp (with 0.2072% of the mistakes).
		tag selected by model -> vm (with 0.0770% of the mistakes).

	(original tag) fz: 
		tag selected by model -> da (with 0.0355% of the mistakes).
		tag selected by model -> fc (with 0.0118% of the mistakes).
		tag selected by model -> fp (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 0.0118% of the mistakes).
		tag selected by model -> np (with 0.0178% of the mistakes).
		tag selected by model -> sp (with 0.0237% of the mistakes).

	(original tag) nc: 
		tag selected by model -> aq (with 0.4559% of the mistakes).
		tag selected by model -> da (with 1.4861% of the mistakes).
		tag selected by model -> di (with 0.0059% of the mistakes).
		tag selected by model -> fc (with 0.0592% of the mistakes).
		tag selected by model -> np (with 0.6572% of the mistakes).
		tag selected by model -> rg (with 0.0118% of the mistakes).
		tag selected by model -> sp (with 2.4038% of the mistakes).
		tag selected by model -> vm (with 0.5802% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.0059% of the mistakes).
		tag selected by model -> cc (with 0.0059% of the mistakes).
		tag selected by model -> da (with 2.7709% of the mistakes).
		tag selected by model -> fc (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 2.0722% of the mistakes).
		tag selected by model -> sp (with 0.8289% of the mistakes).
		tag selected by model -> vm (with 0.1243% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.0237% of the mistakes).
		tag selected by model -> da (with 1.1368% of the mistakes).
		tag selected by model -> fc (with 0.0118% of the mistakes).
		tag selected by model -> nc (with 0.4796% of the mistakes).
		tag selected by model -> np (with 0.1243% of the mistakes).
		tag selected by model -> sp (with 0.1184% of the mistakes).
		tag selected by model -> vm (with 0.0651% of the mistakes).

	(original tag) p0: 
		tag selected by model -> aq (with 0.0118% of the mistakes).
		tag selected by model -> da (with 0.2191% of the mistakes).
		tag selected by model -> nc (with 0.0355% of the mistakes).
		tag selected by model -> np (with 0.0474% of the mistakes).
		tag selected by model -> sp (with 0.0414% of the mistakes).
		tag selected by model -> vm (with 0.1303% of the mistakes).

	(original tag) pd: 
		tag selected by model -> aq (with 0.0355% of the mistakes).
		tag selected by model -> da (with 0.4263% of the mistakes).
		tag selected by model -> fc (with 0.0296% of the mistakes).
		tag selected by model -> nc (with 0.1125% of the mistakes).
		tag selected by model -> np (with 0.1954% of the mistakes).
		tag selected by model -> sp (with 0.1125% of the mistakes).
		tag selected by model -> vm (with 0.2191% of the mistakes).

	(original tag) pe: 
		tag selected by model -> sp (with 0.0059% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.0888% of the mistakes).
		tag selected by model -> da (with 0.6631% of the mistakes).
		tag selected by model -> di (with 1.1664% of the mistakes).
		tag selected by model -> fc (with 0.0237% of the mistakes).
		tag selected by model -> nc (with 0.6098% of the mistakes).
		tag selected by model -> np (with 0.0118% of the mistakes).
		tag selected by model -> pr (with 0.0059% of the mistakes).
		tag selected by model -> rg (with 0.1776% of the mistakes).
		tag selected by model -> sp (with 0.2605% of the mistakes).
		tag selected by model -> vm (with 0.3730% of the mistakes).

	(original tag) pn: 
		tag selected by model -> da (with 0.0651% of the mistakes).
		tag selected by model -> fc (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 0.3138% of the mistakes).
		tag selected by model -> np (with 0.0414% of the mistakes).
		tag selected by model -> sp (with 0.0296% of the mistakes).
		tag selected by model -> vm (with 0.0414% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0355% of the mistakes).
		tag selected by model -> cs (with 0.0118% of the mistakes).
		tag selected by model -> da (with 2.5577% of the mistakes).
		tag selected by model -> fc (with 0.1539% of the mistakes).
		tag selected by model -> nc (with 0.5743% of the mistakes).
		tag selected by model -> np (with 0.1184% of the mistakes).
		tag selected by model -> p0 (with 0.3020% of the mistakes).
		tag selected by model -> rg (with 0.0118% of the mistakes).
		tag selected by model -> sp (with 0.6335% of the mistakes).
		tag selected by model -> vm (with 1.8887% of the mistakes).

	(original tag) pr: 
		tag selected by model -> cs (with 3.4932% of the mistakes).
		tag selected by model -> da (with 0.1007% of the mistakes).
		tag selected by model -> nc (with 0.2013% of the mistakes).
		tag selected by model -> np (with 0.0059% of the mistakes).
		tag selected by model -> sp (with 0.0059% of the mistakes).
		tag selected by model -> vm (with 0.0296% of the mistakes).

	(original tag) pt: 
		tag selected by model -> cs (with 0.0178% of the mistakes).
		tag selected by model -> da (with 0.2724% of the mistakes).
		tag selected by model -> fc (with 0.0178% of the mistakes).
		tag selected by model -> fp (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 0.0829% of the mistakes).
		tag selected by model -> np (with 0.0770% of the mistakes).
		tag selected by model -> sp (with 0.1007% of the mistakes).
		tag selected by model -> vm (with 0.2072% of the mistakes).

	(original tag) px: 
		tag selected by model -> da (with 0.0355% of the mistakes).
		tag selected by model -> nc (with 0.0414% of the mistakes).
		tag selected by model -> sp (with 0.0059% of the mistakes).
		tag selected by model -> vm (with 0.0355% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 0.6335% of the mistakes).
		tag selected by model -> cc (with 0.0829% of the mistakes).
		tag selected by model -> cs (with 0.0414% of the mistakes).
		tag selected by model -> da (with 1.6874% of the mistakes).
		tag selected by model -> di (with 0.0059% of the mistakes).
		tag selected by model -> fc (with 0.1895% of the mistakes).
		tag selected by model -> fp (with 0.0178% of the mistakes).
		tag selected by model -> nc (with 1.5867% of the mistakes).
		tag selected by model -> np (with 0.0414% of the mistakes).
		tag selected by model -> rn (with 0.0829% of the mistakes).
		tag selected by model -> sp (with 2.3979% of the mistakes).
		tag selected by model -> vm (with 0.9118% of the mistakes).

	(original tag) rn: 
		tag selected by model -> aq (with 0.0178% of the mistakes).
		tag selected by model -> cc (with 0.0059% of the mistakes).
		tag selected by model -> da (with 0.4322% of the mistakes).
		tag selected by model -> fc (with 0.0474% of the mistakes).
		tag selected by model -> fp (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 0.5329% of the mistakes).
		tag selected by model -> np (with 0.0947% of the mistakes).
		tag selected by model -> rg (with 0.0296% of the mistakes).
		tag selected by model -> sp (with 0.5092% of the mistakes).
		tag selected by model -> vm (with 0.1243% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.0059% of the mistakes).
		tag selected by model -> cs (with 0.2664% of the mistakes).
		tag selected by model -> da (with 0.3493% of the mistakes).
		tag selected by model -> fc (with 0.0059% of the mistakes).
		tag selected by model -> fp (with 0.0059% of the mistakes).
		tag selected by model -> nc (with 0.0592% of the mistakes).
		tag selected by model -> np (with 0.2546% of the mistakes).
		tag selected by model -> rg (with 0.0118% of the mistakes).

	(original tag) un: 
		tag selected by model -> cs (with 0.0118% of the mistakes).
		tag selected by model -> da (with 0.0414% of the mistakes).
		tag selected by model -> fc (with 0.0059% of the mistakes).
		tag selected by model -> fe (with 0.0947% of the mistakes).
		tag selected by model -> fp (with 0.0178% of the mistakes).
		tag selected by model -> nc (with 0.0651% of the mistakes).
		tag selected by model -> np (with 0.0770% of the mistakes).
		tag selected by model -> rg (with 0.0059% of the mistakes).
		tag selected by model -> sp (with 0.0710% of the mistakes).
		tag selected by model -> vm (with 0.0178% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.0237% of the mistakes).
		tag selected by model -> da (with 0.2724% of the mistakes).
		tag selected by model -> fc (with 0.0651% of the mistakes).
		tag selected by model -> nc (with 0.3316% of the mistakes).
		tag selected by model -> np (with 0.0414% of the mistakes).
		tag selected by model -> sp (with 0.3552% of the mistakes).
		tag selected by model -> vm (with 1.1249% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 0.4085% of the mistakes).
		tag selected by model -> da (with 2.1966% of the mistakes).
		tag selected by model -> fc (with 0.3552% of the mistakes).
		tag selected by model -> fp (with 0.0296% of the mistakes).
		tag selected by model -> nc (with 2.8360% of the mistakes).
		tag selected by model -> np (with 0.1539% of the mistakes).
		tag selected by model -> sp (with 3.7004% of the mistakes).
		tag selected by model -> vs (with 0.0059% of the mistakes).

	(original tag) vs: 
		tag selected by model -> aq (with 0.0592% of the mistakes).
		tag selected by model -> da (with 0.5210% of the mistakes).
		tag selected by model -> fc (with 0.0710% of the mistakes).
		tag selected by model -> nc (with 0.8822% of the mistakes).
		tag selected by model -> np (with 0.0296% of the mistakes).
		tag selected by model -> rg (with 0.0178% of the mistakes).
		tag selected by model -> sp (with 0.3375% of the mistakes).
		tag selected by model -> vm (with 1.3914% of the mistakes).

	(original tag) zm: 
		tag selected by model -> nc (with 0.3434% of the mistakes).
		tag selected by model -> sp (with 0.0059% of the mistakes).

	(original tag) zp: 
		tag selected by model -> nc (with 0.4559% of the mistakes).
		tag selected by model -> np (with 0.0237% of the mistakes).
		tag selected by model -> sp (with 0.0059% of the mistakes).


N = 2, clasificador = naive_bayes.MultinomialNB:

	Time:
		real	59m11.925s
		user	36m36.420s
		sys	0m4.628s
	Accuracy: 76.46%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> aq (with 0.0179% of the mistakes).
		tag selected by model -> da (with 0.0986% of the mistakes).
		tag selected by model -> fc (with 0.0090% of the mistakes).
		tag selected by model -> nc (with 0.9815% of the mistakes).
		tag selected by model -> np (with 0.0224% of the mistakes).
		tag selected by model -> sp (with 0.0314% of the mistakes).
		tag selected by model -> vm (with 0.0179% of the mistakes).

	(original tag) aq: 
		tag selected by model -> cs (with 0.0090% of the mistakes).
		tag selected by model -> da (with 1.7658% of the mistakes).
		tag selected by model -> di (with 0.0314% of the mistakes).
		tag selected by model -> fc (with 0.3899% of the mistakes).
		tag selected by model -> fp (with 0.0179% of the mistakes).
		tag selected by model -> nc (with 4.9881% of the mistakes).
		tag selected by model -> np (with 0.0762% of the mistakes).
		tag selected by model -> rg (with 0.0045% of the mistakes).
		tag selected by model -> sp (with 6.2564% of the mistakes).
		tag selected by model -> vm (with 1.6941% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0134% of the mistakes).
		tag selected by model -> cs (with 0.0090% of the mistakes).
		tag selected by model -> da (with 1.8240% of the mistakes).
		tag selected by model -> fc (with 0.0134% of the mistakes).
		tag selected by model -> nc (with 0.2555% of the mistakes).
		tag selected by model -> np (with 0.4930% of the mistakes).
		tag selected by model -> rg (with 0.2196% of the mistakes).
		tag selected by model -> sp (with 0.0896% of the mistakes).
		tag selected by model -> vm (with 0.0493% of the mistakes).
		tag selected by model -> vs (with 0.0045% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.0179% of the mistakes).
		tag selected by model -> cc (with 0.0986% of the mistakes).
		tag selected by model -> da (with 0.7664% of the mistakes).
		tag selected by model -> fc (with 0.0493% of the mistakes).
		tag selected by model -> fp (with 0.0045% of the mistakes).
		tag selected by model -> nc (with 0.1837% of the mistakes).
		tag selected by model -> np (with 0.0448% of the mistakes).
		tag selected by model -> pr (with 1.2235% of the mistakes).
		tag selected by model -> sp (with 0.5423% of the mistakes).
		tag selected by model -> vm (with 0.1793% of the mistakes).

	(original tag) da: 
		tag selected by model -> nc (with 0.5692% of the mistakes).
		tag selected by model -> np (with 0.0179% of the mistakes).
		tag selected by model -> nu (with 0.0045% of the mistakes).
		tag selected by model -> sp (with 0.0314% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0448% of the mistakes).
		tag selected by model -> cs (with 0.0090% of the mistakes).
		tag selected by model -> da (with 1.3445% of the mistakes).
		tag selected by model -> fc (with 0.0269% of the mistakes).
		tag selected by model -> nc (with 0.4751% of the mistakes).
		tag selected by model -> np (with 0.1165% of the mistakes).
		tag selected by model -> rg (with 0.0045% of the mistakes).
		tag selected by model -> sp (with 0.2689% of the mistakes).
		tag selected by model -> vm (with 0.3272% of the mistakes).

	(original tag) de: 
		tag selected by model -> da (with 0.0134% of the mistakes).
		tag selected by model -> sp (with 0.0090% of the mistakes).
		tag selected by model -> vm (with 0.0134% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.2644% of the mistakes).
		tag selected by model -> da (with 0.6812% of the mistakes).
		tag selected by model -> fc (with 0.0403% of the mistakes).
		tag selected by model -> nc (with 0.7798% of the mistakes).
		tag selected by model -> np (with 0.0269% of the mistakes).
		tag selected by model -> rg (with 0.0672% of the mistakes).
		tag selected by model -> sp (with 0.1837% of the mistakes).
		tag selected by model -> vm (with 0.2241% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.0538% of the mistakes).
		tag selected by model -> da (with 0.3406% of the mistakes).
		tag selected by model -> di (with 0.1479% of the mistakes).
		tag selected by model -> fc (with 0.0090% of the mistakes).
		tag selected by model -> nc (with 0.5916% of the mistakes).
		tag selected by model -> np (with 0.2330% of the mistakes).
		tag selected by model -> sp (with 0.1793% of the mistakes).
		tag selected by model -> vm (with 0.1031% of the mistakes).

	(original tag) dp: 
		tag selected by model -> aq (with 0.0179% of the mistakes).
		tag selected by model -> da (with 0.5826% of the mistakes).
		tag selected by model -> fc (with 0.0448% of the mistakes).
		tag selected by model -> nc (with 0.2196% of the mistakes).
		tag selected by model -> np (with 0.0045% of the mistakes).
		tag selected by model -> sp (with 0.2286% of the mistakes).
		tag selected by model -> vm (with 0.3182% of the mistakes).

	(original tag) dt: 
		tag selected by model -> cs (with 0.0045% of the mistakes).
		tag selected by model -> da (with 0.0448% of the mistakes).
		tag selected by model -> nc (with 0.0045% of the mistakes).
		tag selected by model -> np (with 0.0134% of the mistakes).
		tag selected by model -> sp (with 0.0134% of the mistakes).
		tag selected by model -> vm (with 0.0090% of the mistakes).

	(original tag) fa: 
		tag selected by model -> aq (with 0.0090% of the mistakes).
		tag selected by model -> da (with 0.0493% of the mistakes).
		tag selected by model -> fc (with 0.0224% of the mistakes).
		tag selected by model -> nc (with 0.0359% of the mistakes).
		tag selected by model -> np (with 0.0045% of the mistakes).
		tag selected by model -> sp (with 0.0807% of the mistakes).
		tag selected by model -> vm (with 0.0314% of the mistakes).

	(original tag) fc: 
		tag selected by model -> da (with 0.0224% of the mistakes).
		tag selected by model -> nc (with 0.0179% of the mistakes).
		tag selected by model -> vm (with 0.0045% of the mistakes).

	(original tag) fd: 
		tag selected by model -> aq (with 0.1210% of the mistakes).
		tag selected by model -> da (with 0.1300% of the mistakes).
		tag selected by model -> fc (with 0.0941% of the mistakes).
		tag selected by model -> nc (with 0.1120% of the mistakes).
		tag selected by model -> sp (with 0.7977% of the mistakes).
		tag selected by model -> vm (with 0.0090% of the mistakes).

	(original tag) fe: 
		tag selected by model -> da (with 0.0359% of the mistakes).
		tag selected by model -> nc (with 0.1927% of the mistakes).

	(original tag) fg: 
		tag selected by model -> aq (with 0.1972% of the mistakes).
		tag selected by model -> cc (with 0.0090% of the mistakes).
		tag selected by model -> cs (with 0.0134% of the mistakes).
		tag selected by model -> da (with 1.7389% of the mistakes).
		tag selected by model -> fc (with 0.2196% of the mistakes).
		tag selected by model -> fp (with 0.0672% of the mistakes).
		tag selected by model -> nc (with 1.1025% of the mistakes).
		tag selected by model -> np (with 0.0538% of the mistakes).
		tag selected by model -> sp (with 1.2638% of the mistakes).
		tag selected by model -> vm (with 0.2958% of the mistakes).

	(original tag) fh: 
		tag selected by model -> nc (with 0.0045% of the mistakes).
		tag selected by model -> sp (with 0.0134% of the mistakes).

	(original tag) fi: 
		tag selected by model -> aq (with 0.0179% of the mistakes).
		tag selected by model -> cs (with 0.0090% of the mistakes).
		tag selected by model -> da (with 0.1434% of the mistakes).
		tag selected by model -> fc (with 0.0807% of the mistakes).
		tag selected by model -> fp (with 0.0134% of the mistakes).
		tag selected by model -> nc (with 0.1345% of the mistakes).
		tag selected by model -> sp (with 0.2689% of the mistakes).
		tag selected by model -> vm (with 0.0583% of the mistakes).

	(original tag) fp: 
		tag selected by model -> da (with 0.3406% of the mistakes).
		tag selected by model -> nc (with 0.0986% of the mistakes).
		tag selected by model -> np (with 0.0090% of the mistakes).
		tag selected by model -> vm (with 0.0538% of the mistakes).

	(original tag) fs: 
		tag selected by model -> aq (with 0.0090% of the mistakes).
		tag selected by model -> da (with 0.0359% of the mistakes).
		tag selected by model -> fc (with 0.0269% of the mistakes).
		tag selected by model -> nc (with 0.0224% of the mistakes).
		tag selected by model -> sp (with 0.0807% of the mistakes).
		tag selected by model -> vm (with 0.0224% of the mistakes).

	(original tag) fx: 
		tag selected by model -> aq (with 0.0224% of the mistakes).
		tag selected by model -> da (with 0.0627% of the mistakes).
		tag selected by model -> fc (with 0.0941% of the mistakes).
		tag selected by model -> nc (with 0.0672% of the mistakes).
		tag selected by model -> sp (with 0.2555% of the mistakes).
		tag selected by model -> vm (with 0.0090% of the mistakes).

	(original tag) fz: 
		tag selected by model -> da (with 0.0403% of the mistakes).
		tag selected by model -> fc (with 0.0090% of the mistakes).
		tag selected by model -> np (with 0.0134% of the mistakes).
		tag selected by model -> sp (with 0.0179% of the mistakes).

	(original tag) nc: 
		tag selected by model -> aq (with 0.8963% of the mistakes).
		tag selected by model -> cs (with 0.0045% of the mistakes).
		tag selected by model -> da (with 3.2447% of the mistakes).
		tag selected by model -> di (with 0.0090% of the mistakes).
		tag selected by model -> fc (with 0.2286% of the mistakes).
		tag selected by model -> fp (with 0.0045% of the mistakes).
		tag selected by model -> np (with 0.5512% of the mistakes).
		tag selected by model -> rg (with 0.0090% of the mistakes).
		tag selected by model -> sp (with 4.8716% of the mistakes).
		tag selected by model -> vm (with 1.2862% of the mistakes).
		tag selected by model -> vs (with 0.0045% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.0090% of the mistakes).
		tag selected by model -> cc (with 0.0045% of the mistakes).
		tag selected by model -> da (with 2.4022% of the mistakes).
		tag selected by model -> fc (with 0.0538% of the mistakes).
		tag selected by model -> nc (with 1.4879% of the mistakes).
		tag selected by model -> sp (with 1.2907% of the mistakes).
		tag selected by model -> vm (with 0.1837% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.0179% of the mistakes).
		tag selected by model -> cs (with 0.0045% of the mistakes).
		tag selected by model -> da (with 0.9815% of the mistakes).
		tag selected by model -> fc (with 0.0179% of the mistakes).
		tag selected by model -> fp (with 0.0045% of the mistakes).
		tag selected by model -> nc (with 0.2196% of the mistakes).
		tag selected by model -> np (with 0.0896% of the mistakes).
		tag selected by model -> sp (with 0.1165% of the mistakes).
		tag selected by model -> vm (with 0.0538% of the mistakes).

	(original tag) p0: 
		tag selected by model -> aq (with 0.0269% of the mistakes).
		tag selected by model -> da (with 0.3899% of the mistakes).
		tag selected by model -> fc (with 0.0314% of the mistakes).
		tag selected by model -> fp (with 0.0045% of the mistakes).
		tag selected by model -> nc (with 0.2151% of the mistakes).
		tag selected by model -> np (with 0.0314% of the mistakes).
		tag selected by model -> sp (with 0.2151% of the mistakes).
		tag selected by model -> vm (with 0.2689% of the mistakes).

	(original tag) pd: 
		tag selected by model -> aq (with 0.0090% of the mistakes).
		tag selected by model -> da (with 0.3630% of the mistakes).
		tag selected by model -> fc (with 0.0314% of the mistakes).
		tag selected by model -> nc (with 0.0852% of the mistakes).
		tag selected by model -> np (with 0.1300% of the mistakes).
		tag selected by model -> sp (with 0.0538% of the mistakes).
		tag selected by model -> vm (with 0.1837% of the mistakes).

	(original tag) pe: 
		tag selected by model -> da (with 0.0045% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.1120% of the mistakes).
		tag selected by model -> cs (with 0.0045% of the mistakes).
		tag selected by model -> da (with 0.5647% of the mistakes).
		tag selected by model -> di (with 0.7529% of the mistakes).
		tag selected by model -> fc (with 0.0583% of the mistakes).
		tag selected by model -> fp (with 0.0090% of the mistakes).
		tag selected by model -> nc (with 0.3541% of the mistakes).
		tag selected by model -> np (with 0.0224% of the mistakes).
		tag selected by model -> pr (with 0.0045% of the mistakes).
		tag selected by model -> rg (with 0.1479% of the mistakes).
		tag selected by model -> sp (with 0.1345% of the mistakes).
		tag selected by model -> vm (with 0.3944% of the mistakes).

	(original tag) pn: 
		tag selected by model -> aq (with 0.0090% of the mistakes).
		tag selected by model -> da (with 0.1031% of the mistakes).
		tag selected by model -> nc (with 0.1613% of the mistakes).
		tag selected by model -> np (with 0.0314% of the mistakes).
		tag selected by model -> sp (with 0.0448% of the mistakes).
		tag selected by model -> vm (with 0.0269% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.0538% of the mistakes).
		tag selected by model -> cs (with 0.0090% of the mistakes).
		tag selected by model -> da (with 2.1691% of the mistakes).
		tag selected by model -> fc (with 0.2241% of the mistakes).
		tag selected by model -> nc (with 0.2599% of the mistakes).
		tag selected by model -> np (with 0.0986% of the mistakes).
		tag selected by model -> p0 (with 0.2241% of the mistakes).
		tag selected by model -> sp (with 0.4930% of the mistakes).
		tag selected by model -> vm (with 1.4431% of the mistakes).

	(original tag) pr: 
		tag selected by model -> aq (with 0.0134% of the mistakes).
		tag selected by model -> cs (with 1.0263% of the mistakes).
		tag selected by model -> da (with 0.1703% of the mistakes).
		tag selected by model -> fc (with 0.0269% of the mistakes).
		tag selected by model -> nc (with 0.1434% of the mistakes).
		tag selected by model -> np (with 0.0045% of the mistakes).
		tag selected by model -> sp (with 0.0314% of the mistakes).
		tag selected by model -> vm (with 0.0224% of the mistakes).

	(original tag) pt: 
		tag selected by model -> cs (with 0.0224% of the mistakes).
		tag selected by model -> da (with 0.2599% of the mistakes).
		tag selected by model -> fc (with 0.0224% of the mistakes).
		tag selected by model -> nc (with 0.0134% of the mistakes).
		tag selected by model -> np (with 0.0717% of the mistakes).
		tag selected by model -> sp (with 0.1031% of the mistakes).
		tag selected by model -> vm (with 0.0986% of the mistakes).

	(original tag) px: 
		tag selected by model -> da (with 0.0583% of the mistakes).
		tag selected by model -> nc (with 0.0045% of the mistakes).
		tag selected by model -> vm (with 0.0269% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 0.5961% of the mistakes).
		tag selected by model -> cc (with 0.0538% of the mistakes).
		tag selected by model -> cs (with 0.0224% of the mistakes).
		tag selected by model -> da (with 2.0123% of the mistakes).
		tag selected by model -> di (with 0.0045% of the mistakes).
		tag selected by model -> fc (with 0.2958% of the mistakes).
		tag selected by model -> fp (with 0.0090% of the mistakes).
		tag selected by model -> nc (with 1.1787% of the mistakes).
		tag selected by model -> np (with 0.0583% of the mistakes).
		tag selected by model -> rn (with 0.0179% of the mistakes).
		tag selected by model -> sp (with 1.8509% of the mistakes).
		tag selected by model -> vm (with 0.9636% of the mistakes).

	(original tag) rn: 
		tag selected by model -> aq (with 0.0762% of the mistakes).
		tag selected by model -> da (with 0.4123% of the mistakes).
		tag selected by model -> fc (with 0.1300% of the mistakes).
		tag selected by model -> fp (with 0.0045% of the mistakes).
		tag selected by model -> nc (with 0.4751% of the mistakes).
		tag selected by model -> np (with 0.0807% of the mistakes).
		tag selected by model -> rg (with 0.1837% of the mistakes).
		tag selected by model -> sp (with 0.5019% of the mistakes).
		tag selected by model -> vm (with 0.6005% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.0045% of the mistakes).
		tag selected by model -> cs (with 0.1569% of the mistakes).
		tag selected by model -> da (with 0.9456% of the mistakes).
		tag selected by model -> fc (with 0.0134% of the mistakes).
		tag selected by model -> fp (with 0.0045% of the mistakes).
		tag selected by model -> nc (with 0.1748% of the mistakes).
		tag selected by model -> np (with 0.2196% of the mistakes).
		tag selected by model -> rg (with 0.0045% of the mistakes).
		tag selected by model -> vm (with 0.0403% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.0045% of the mistakes).
		tag selected by model -> cs (with 0.0090% of the mistakes).
		tag selected by model -> da (with 0.0493% of the mistakes).
		tag selected by model -> fc (with 0.0045% of the mistakes).
		tag selected by model -> fe (with 0.0717% of the mistakes).
		tag selected by model -> fp (with 0.0090% of the mistakes).
		tag selected by model -> nc (with 0.0269% of the mistakes).
		tag selected by model -> np (with 0.0448% of the mistakes).
		tag selected by model -> sp (with 0.0717% of the mistakes).
		tag selected by model -> vm (with 0.0179% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.1479% of the mistakes).
		tag selected by model -> da (with 0.2868% of the mistakes).
		tag selected by model -> fc (with 0.1345% of the mistakes).
		tag selected by model -> fp (with 0.0090% of the mistakes).
		tag selected by model -> nc (with 0.2644% of the mistakes).
		tag selected by model -> np (with 0.0314% of the mistakes).
		tag selected by model -> sp (with 0.4751% of the mistakes).
		tag selected by model -> vm (with 1.2190% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 0.7753% of the mistakes).
		tag selected by model -> cs (with 0.0045% of the mistakes).
		tag selected by model -> da (with 3.3971% of the mistakes).
		tag selected by model -> fc (with 0.6857% of the mistakes).
		tag selected by model -> fp (with 0.0269% of the mistakes).
		tag selected by model -> nc (with 2.3529% of the mistakes).
		tag selected by model -> np (with 0.1658% of the mistakes).
		tag selected by model -> sp (with 4.2307% of the mistakes).

	(original tag) vs: 
		tag selected by model -> aq (with 0.1300% of the mistakes).
		tag selected by model -> da (with 0.5378% of the mistakes).
		tag selected by model -> fc (with 0.1793% of the mistakes).
		tag selected by model -> fp (with 0.0090% of the mistakes).
		tag selected by model -> nc (with 0.6140% of the mistakes).
		tag selected by model -> np (with 0.0583% of the mistakes).
		tag selected by model -> rg (with 0.0090% of the mistakes).
		tag selected by model -> sp (with 0.7126% of the mistakes).
		tag selected by model -> vm (with 1.4207% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.0090% of the mistakes).
		tag selected by model -> da (with 0.0045% of the mistakes).
		tag selected by model -> nc (with 0.2151% of the mistakes).
		tag selected by model -> sp (with 0.0359% of the mistakes).

	(original tag) zp: 
		tag selected by model -> nc (with 0.3496% of the mistakes).
		tag selected by model -> np (with 0.0134% of the mistakes).
		tag selected by model -> sp (with 0.0045% of the mistakes).

N = 3, clasificador = naive_bayes.MultinomialNB:

	Time:
		real	61m7.078s
		user	37m55.548s
		sys	0m4.328s
	Accuracy: 71.47%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> aq (with 0.0444% of the mistakes).
		tag selected by model -> da (with 0.0702% of the mistakes).
		tag selected by model -> nc (with 0.7986% of the mistakes).
		tag selected by model -> np (with 0.0111% of the mistakes).
		tag selected by model -> sp (with 0.0296% of the mistakes).
		tag selected by model -> vm (with 0.0185% of the mistakes).

	(original tag) aq: 
		tag selected by model -> cc (with 0.0037% of the mistakes).
		tag selected by model -> cs (with 0.0333% of the mistakes).
		tag selected by model -> da (with 1.9632% of the mistakes).
		tag selected by model -> di (with 0.0333% of the mistakes).
		tag selected by model -> fc (with 0.2847% of the mistakes).
		tag selected by model -> fp (with 0.0555% of the mistakes).
		tag selected by model -> nc (with 4.6844% of the mistakes).
		tag selected by model -> np (with 0.0555% of the mistakes).
		tag selected by model -> pr (with 0.0037% of the mistakes).
		tag selected by model -> rg (with 0.0333% of the mistakes).
		tag selected by model -> sp (with 4.7362% of the mistakes).
		tag selected by model -> vm (with 1.3310% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0296% of the mistakes).
		tag selected by model -> cs (with 0.0074% of the mistakes).
		tag selected by model -> da (with 1.5565% of the mistakes).
		tag selected by model -> di (with 0.0074% of the mistakes).
		tag selected by model -> fc (with 0.0111% of the mistakes).
		tag selected by model -> nc (with 0.4104% of the mistakes).
		tag selected by model -> np (with 0.4289% of the mistakes).
		tag selected by model -> rg (with 0.1590% of the mistakes).
		tag selected by model -> sp (with 0.1516% of the mistakes).
		tag selected by model -> vm (with 0.0407% of the mistakes).
		tag selected by model -> vs (with 0.0037% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.0592% of the mistakes).
		tag selected by model -> cc (with 0.1109% of the mistakes).
		tag selected by model -> da (with 0.6951% of the mistakes).
		tag selected by model -> fc (with 0.0702% of the mistakes).
		tag selected by model -> fp (with 0.0074% of the mistakes).
		tag selected by model -> nc (with 0.2847% of the mistakes).
		tag selected by model -> np (with 0.0407% of the mistakes).
		tag selected by model -> pr (with 1.1388% of the mistakes).
		tag selected by model -> sp (with 0.7764% of the mistakes).
		tag selected by model -> vm (with 0.1442% of the mistakes).

	(original tag) da: 
		tag selected by model -> aq (with 0.0407% of the mistakes).
		tag selected by model -> fc (with 0.0148% of the mistakes).
		tag selected by model -> nc (with 0.5398% of the mistakes).
		tag selected by model -> np (with 0.0185% of the mistakes).
		tag selected by model -> nu (with 0.0407% of the mistakes).
		tag selected by model -> sp (with 0.1257% of the mistakes).
		tag selected by model -> vm (with 0.0074% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0518% of the mistakes).
		tag selected by model -> cs (with 0.0148% of the mistakes).
		tag selected by model -> da (with 1.1055% of the mistakes).
		tag selected by model -> di (with 0.0037% of the mistakes).
		tag selected by model -> fc (with 0.0074% of the mistakes).
		tag selected by model -> nc (with 0.4400% of the mistakes).
		tag selected by model -> np (with 0.0666% of the mistakes).
		tag selected by model -> rg (with 0.0111% of the mistakes).
		tag selected by model -> sp (with 0.1960% of the mistakes).
		tag selected by model -> vm (with 0.2625% of the mistakes).

	(original tag) de: 
		tag selected by model -> da (with 0.0111% of the mistakes).
		tag selected by model -> sp (with 0.0074% of the mistakes).
		tag selected by model -> vm (with 0.0111% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.3365% of the mistakes).
		tag selected by model -> da (with 0.6470% of the mistakes).
		tag selected by model -> fc (with 0.0518% of the mistakes).
		tag selected by model -> fp (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 1.1240% of the mistakes).
		tag selected by model -> np (with 0.0481% of the mistakes).
		tag selected by model -> rg (with 0.0481% of the mistakes).
		tag selected by model -> sp (with 0.3919% of the mistakes).
		tag selected by model -> vm (with 0.2403% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.0924% of the mistakes).
		tag selected by model -> da (with 0.2995% of the mistakes).
		tag selected by model -> di (with 0.1257% of the mistakes).
		tag selected by model -> fc (with 0.0074% of the mistakes).
		tag selected by model -> fp (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.4622% of the mistakes).
		tag selected by model -> np (with 0.1590% of the mistakes).
		tag selected by model -> rg (with 0.0074% of the mistakes).
		tag selected by model -> sp (with 0.1368% of the mistakes).
		tag selected by model -> vm (with 0.0739% of the mistakes).

	(original tag) dp: 
		tag selected by model -> aq (with 0.0666% of the mistakes).
		tag selected by model -> da (with 0.7432% of the mistakes).
		tag selected by model -> fc (with 0.0185% of the mistakes).
		tag selected by model -> fp (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.5546% of the mistakes).
		tag selected by model -> np (with 0.0074% of the mistakes).
		tag selected by model -> sp (with 0.2255% of the mistakes).
		tag selected by model -> vm (with 0.3217% of the mistakes).

	(original tag) dt: 
		tag selected by model -> cs (with 0.0037% of the mistakes).
		tag selected by model -> da (with 0.0296% of the mistakes).
		tag selected by model -> fc (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.0111% of the mistakes).
		tag selected by model -> np (with 0.0111% of the mistakes).
		tag selected by model -> sp (with 0.0148% of the mistakes).

	(original tag) fa: 
		tag selected by model -> aq (with 0.0037% of the mistakes).
		tag selected by model -> da (with 0.0481% of the mistakes).
		tag selected by model -> fc (with 0.0111% of the mistakes).
		tag selected by model -> fp (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.0296% of the mistakes).
		tag selected by model -> np (with 0.0037% of the mistakes).
		tag selected by model -> rg (with 0.0037% of the mistakes).
		tag selected by model -> sp (with 0.0702% of the mistakes).
		tag selected by model -> vm (with 0.0185% of the mistakes).

	(original tag) fc: 
		tag selected by model -> da (with 0.0259% of the mistakes).
		tag selected by model -> nc (with 0.1035% of the mistakes).
		tag selected by model -> vm (with 0.0148% of the mistakes).

	(original tag) fd: 
		tag selected by model -> aq (with 0.1812% of the mistakes).
		tag selected by model -> cs (with 0.0148% of the mistakes).
		tag selected by model -> da (with 0.1368% of the mistakes).
		tag selected by model -> di (with 0.0111% of the mistakes).
		tag selected by model -> fc (with 0.0481% of the mistakes).
		tag selected by model -> fp (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.1035% of the mistakes).
		tag selected by model -> rg (with 0.0037% of the mistakes).
		tag selected by model -> sp (with 0.5361% of the mistakes).
		tag selected by model -> vm (with 0.0037% of the mistakes).

	(original tag) fe: 
		tag selected by model -> da (with 0.0998% of the mistakes).
		tag selected by model -> fc (with 0.0074% of the mistakes).
		tag selected by model -> nc (with 0.2403% of the mistakes).
		tag selected by model -> np (with 0.0037% of the mistakes).
		tag selected by model -> vm (with 0.0259% of the mistakes).

	(original tag) fg: 
		tag selected by model -> aq (with 0.2514% of the mistakes).
		tag selected by model -> cc (with 0.0074% of the mistakes).
		tag selected by model -> cs (with 0.0148% of the mistakes).
		tag selected by model -> da (with 1.4234% of the mistakes).
		tag selected by model -> di (with 0.0037% of the mistakes).
		tag selected by model -> fc (with 0.1516% of the mistakes).
		tag selected by model -> fp (with 0.0444% of the mistakes).
		tag selected by model -> nc (with 0.9872% of the mistakes).
		tag selected by model -> np (with 0.0518% of the mistakes).
		tag selected by model -> rg (with 0.0074% of the mistakes).
		tag selected by model -> sp (with 1.0167% of the mistakes).
		tag selected by model -> vm (with 0.1738% of the mistakes).

	(original tag) fh: 
		tag selected by model -> da (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.0037% of the mistakes).
		tag selected by model -> sp (with 0.0074% of the mistakes).

	(original tag) fi: 
		tag selected by model -> aq (with 0.0666% of the mistakes).
		tag selected by model -> cs (with 0.0074% of the mistakes).
		tag selected by model -> da (with 0.1220% of the mistakes).
		tag selected by model -> fc (with 0.0666% of the mistakes).
		tag selected by model -> fp (with 0.0148% of the mistakes).
		tag selected by model -> nc (with 0.0961% of the mistakes).
		tag selected by model -> rg (with 0.0037% of the mistakes).
		tag selected by model -> sp (with 0.1849% of the mistakes).
		tag selected by model -> vm (with 0.0370% of the mistakes).

	(original tag) fp: 
		tag selected by model -> aq (with 0.0037% of the mistakes).
		tag selected by model -> cc (with 0.0037% of the mistakes).
		tag selected by model -> cs (with 0.0037% of the mistakes).
		tag selected by model -> da (with 0.6064% of the mistakes).
		tag selected by model -> nc (with 0.1553% of the mistakes).
		tag selected by model -> sp (with 0.0074% of the mistakes).
		tag selected by model -> vm (with 0.0666% of the mistakes).

	(original tag) fs: 
		tag selected by model -> aq (with 0.0148% of the mistakes).
		tag selected by model -> da (with 0.0148% of the mistakes).
		tag selected by model -> fc (with 0.0185% of the mistakes).
		tag selected by model -> nc (with 0.0185% of the mistakes).
		tag selected by model -> sp (with 0.0739% of the mistakes).
		tag selected by model -> vm (with 0.0222% of the mistakes).

	(original tag) fx: 
		tag selected by model -> aq (with 0.0296% of the mistakes).
		tag selected by model -> da (with 0.0518% of the mistakes).
		tag selected by model -> fc (with 0.0555% of the mistakes).
		tag selected by model -> fp (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.0629% of the mistakes).
		tag selected by model -> sp (with 0.2070% of the mistakes).
		tag selected by model -> vm (with 0.0111% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0037% of the mistakes).
		tag selected by model -> da (with 0.0296% of the mistakes).
		tag selected by model -> fc (with 0.0074% of the mistakes).
		tag selected by model -> nc (with 0.0074% of the mistakes).
		tag selected by model -> np (with 0.0074% of the mistakes).
		tag selected by model -> sp (with 0.0111% of the mistakes).

	(original tag) nc: 
		tag selected by model -> aq (with 1.8486% of the mistakes).
		tag selected by model -> cs (with 0.0259% of the mistakes).
		tag selected by model -> da (with 3.2795% of the mistakes).
		tag selected by model -> di (with 0.0370% of the mistakes).
		tag selected by model -> fc (with 0.2958% of the mistakes).
		tag selected by model -> fp (with 0.0924% of the mistakes).
		tag selected by model -> np (with 0.4585% of the mistakes).
		tag selected by model -> rg (with 0.0222% of the mistakes).
		tag selected by model -> sp (with 4.0374% of the mistakes).
		tag selected by model -> vm (with 1.2645% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.0222% of the mistakes).
		tag selected by model -> cc (with 0.0037% of the mistakes).
		tag selected by model -> da (with 2.1999% of the mistakes).
		tag selected by model -> fc (with 0.0333% of the mistakes).
		tag selected by model -> nc (with 1.4752% of the mistakes).
		tag selected by model -> sp (with 1.1055% of the mistakes).
		tag selected by model -> vm (with 0.2329% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.0296% of the mistakes).
		tag selected by model -> cs (with 0.0037% of the mistakes).
		tag selected by model -> da (with 0.7432% of the mistakes).
		tag selected by model -> fc (with 0.0185% of the mistakes).
		tag selected by model -> fp (with 0.0111% of the mistakes).
		tag selected by model -> nc (with 0.2440% of the mistakes).
		tag selected by model -> np (with 0.0776% of the mistakes).
		tag selected by model -> pr (with 0.0037% of the mistakes).
		tag selected by model -> sp (with 0.1072% of the mistakes).
		tag selected by model -> vm (with 0.0481% of the mistakes).

	(original tag) p0: 
		tag selected by model -> aq (with 0.1664% of the mistakes).
		tag selected by model -> cc (with 0.0037% of the mistakes).
		tag selected by model -> da (with 0.3919% of the mistakes).
		tag selected by model -> fc (with 0.1183% of the mistakes).
		tag selected by model -> fp (with 0.0259% of the mistakes).
		tag selected by model -> nc (with 0.3032% of the mistakes).
		tag selected by model -> np (with 0.0259% of the mistakes).
		tag selected by model -> sp (with 0.6285% of the mistakes).
		tag selected by model -> vm (with 0.2773% of the mistakes).

	(original tag) pd: 
		tag selected by model -> aq (with 0.0111% of the mistakes).
		tag selected by model -> da (with 0.2329% of the mistakes).
		tag selected by model -> fc (with 0.0259% of the mistakes).
		tag selected by model -> nc (with 0.1664% of the mistakes).
		tag selected by model -> np (with 0.0813% of the mistakes).
		tag selected by model -> sp (with 0.0702% of the mistakes).
		tag selected by model -> vm (with 0.1183% of the mistakes).

	(original tag) pe: 
		tag selected by model -> da (with 0.0037% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.1220% of the mistakes).
		tag selected by model -> cs (with 0.0111% of the mistakes).
		tag selected by model -> da (with 0.4954% of the mistakes).
		tag selected by model -> di (with 0.5546% of the mistakes).
		tag selected by model -> fc (with 0.0259% of the mistakes).
		tag selected by model -> nc (with 0.3365% of the mistakes).
		tag selected by model -> np (with 0.0148% of the mistakes).
		tag selected by model -> pr (with 0.0074% of the mistakes).
		tag selected by model -> rg (with 0.0924% of the mistakes).
		tag selected by model -> sp (with 0.1627% of the mistakes).
		tag selected by model -> vm (with 0.2884% of the mistakes).

	(original tag) pn: 
		tag selected by model -> aq (with 0.0296% of the mistakes).
		tag selected by model -> da (with 0.0924% of the mistakes).
		tag selected by model -> fc (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.1035% of the mistakes).
		tag selected by model -> np (with 0.0259% of the mistakes).
		tag selected by model -> sp (with 0.0296% of the mistakes).
		tag selected by model -> vm (with 0.0259% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.1368% of the mistakes).
		tag selected by model -> cs (with 0.0074% of the mistakes).
		tag selected by model -> da (with 1.7673% of the mistakes).
		tag selected by model -> di (with 0.0037% of the mistakes).
		tag selected by model -> fc (with 0.1664% of the mistakes).
		tag selected by model -> fp (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.3697% of the mistakes).
		tag selected by model -> np (with 0.1035% of the mistakes).
		tag selected by model -> p0 (with 0.0998% of the mistakes).
		tag selected by model -> rg (with 0.0037% of the mistakes).
		tag selected by model -> sp (with 0.4252% of the mistakes).
		tag selected by model -> vm (with 1.0204% of the mistakes).

	(original tag) pr: 
		tag selected by model -> aq (with 0.0185% of the mistakes).
		tag selected by model -> cs (with 0.7653% of the mistakes).
		tag selected by model -> da (with 0.1812% of the mistakes).
		tag selected by model -> di (with 0.0037% of the mistakes).
		tag selected by model -> fc (with 0.0259% of the mistakes).
		tag selected by model -> fp (with 0.0111% of the mistakes).
		tag selected by model -> nc (with 0.1849% of the mistakes).
		tag selected by model -> np (with 0.0074% of the mistakes).
		tag selected by model -> sp (with 0.0296% of the mistakes).
		tag selected by model -> vm (with 0.0185% of the mistakes).

	(original tag) pt: 
		tag selected by model -> aq (with 0.0037% of the mistakes).
		tag selected by model -> cs (with 0.0296% of the mistakes).
		tag selected by model -> da (with 0.1775% of the mistakes).
		tag selected by model -> fc (with 0.0259% of the mistakes).
		tag selected by model -> nc (with 0.0518% of the mistakes).
		tag selected by model -> np (with 0.0592% of the mistakes).
		tag selected by model -> sp (with 0.0702% of the mistakes).
		tag selected by model -> vm (with 0.0702% of the mistakes).

	(original tag) px: 
		tag selected by model -> da (with 0.0444% of the mistakes).
		tag selected by model -> nc (with 0.0111% of the mistakes).
		tag selected by model -> sp (with 0.0037% of the mistakes).
		tag selected by model -> vm (with 0.0148% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 0.8652% of the mistakes).
		tag selected by model -> cc (with 0.0555% of the mistakes).
		tag selected by model -> cs (with 0.0074% of the mistakes).
		tag selected by model -> da (with 2.1074% of the mistakes).
		tag selected by model -> di (with 0.0259% of the mistakes).
		tag selected by model -> fc (with 0.2255% of the mistakes).
		tag selected by model -> fp (with 0.0222% of the mistakes).
		tag selected by model -> nc (with 1.2275% of the mistakes).
		tag selected by model -> np (with 0.0629% of the mistakes).
		tag selected by model -> pr (with 0.0037% of the mistakes).
		tag selected by model -> sp (with 1.8893% of the mistakes).
		tag selected by model -> vm (with 0.8615% of the mistakes).

	(original tag) rn: 
		tag selected by model -> aq (with 0.1590% of the mistakes).
		tag selected by model -> cc (with 0.0074% of the mistakes).
		tag selected by model -> da (with 0.4178% of the mistakes).
		tag selected by model -> fc (with 0.1405% of the mistakes).
		tag selected by model -> fp (with 0.0296% of the mistakes).
		tag selected by model -> nc (with 0.4178% of the mistakes).
		tag selected by model -> np (with 0.0702% of the mistakes).
		tag selected by model -> rg (with 0.2070% of the mistakes).
		tag selected by model -> sp (with 0.5102% of the mistakes).
		tag selected by model -> vm (with 0.6988% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.0074% of the mistakes).
		tag selected by model -> cs (with 0.1072% of the mistakes).
		tag selected by model -> da (with 1.8819% of the mistakes).
		tag selected by model -> fc (with 0.0666% of the mistakes).
		tag selected by model -> nc (with 0.5620% of the mistakes).
		tag selected by model -> np (with 0.1664% of the mistakes).
		tag selected by model -> rg (with 0.0037% of the mistakes).
		tag selected by model -> vm (with 0.1220% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.0037% of the mistakes).
		tag selected by model -> da (with 0.0407% of the mistakes).
		tag selected by model -> fe (with 0.0555% of the mistakes).
		tag selected by model -> fp (with 0.0111% of the mistakes).
		tag selected by model -> nc (with 0.0259% of the mistakes).
		tag selected by model -> np (with 0.0296% of the mistakes).
		tag selected by model -> pr (with 0.0074% of the mistakes).
		tag selected by model -> rg (with 0.0037% of the mistakes).
		tag selected by model -> sp (with 0.0518% of the mistakes).
		tag selected by model -> vm (with 0.0259% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.2107% of the mistakes).
		tag selected by model -> da (with 0.2995% of the mistakes).
		tag selected by model -> fc (with 0.1368% of the mistakes).
		tag selected by model -> fp (with 0.0111% of the mistakes).
		tag selected by model -> nc (with 0.3475% of the mistakes).
		tag selected by model -> np (with 0.0222% of the mistakes).
		tag selected by model -> pr (with 0.0074% of the mistakes).
		tag selected by model -> sp (with 0.4659% of the mistakes).
		tag selected by model -> vm (with 1.2830% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 1.0241% of the mistakes).
		tag selected by model -> cs (with 0.0148% of the mistakes).
		tag selected by model -> da (with 3.9930% of the mistakes).
		tag selected by model -> di (with 0.0111% of the mistakes).
		tag selected by model -> fc (with 0.6470% of the mistakes).
		tag selected by model -> fp (with 0.0333% of the mistakes).
		tag selected by model -> nc (with 2.8617% of the mistakes).
		tag selected by model -> np (with 0.1553% of the mistakes).
		tag selected by model -> pr (with 0.0296% of the mistakes).
		tag selected by model -> rg (with 0.0148% of the mistakes).
		tag selected by model -> sp (with 4.0448% of the mistakes).

	(original tag) vs: 
		tag selected by model -> aq (with 0.3365% of the mistakes).
		tag selected by model -> cs (with 0.0148% of the mistakes).
		tag selected by model -> da (with 0.6322% of the mistakes).
		tag selected by model -> fc (with 0.2403% of the mistakes).
		tag selected by model -> fp (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.5879% of the mistakes).
		tag selected by model -> np (with 0.0518% of the mistakes).
		tag selected by model -> rg (with 0.0037% of the mistakes).
		tag selected by model -> sp (with 1.1794% of the mistakes).
		tag selected by model -> vm (with 1.3458% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.0111% of the mistakes).
		tag selected by model -> da (with 0.0037% of the mistakes).
		tag selected by model -> nc (with 0.1775% of the mistakes).
		tag selected by model -> sp (with 0.0259% of the mistakes).

	(original tag) zp: 
		tag selected by model -> nc (with 0.2810% of the mistakes).
		tag selected by model -> np (with 0.0185% of the mistakes).
		tag selected by model -> sp (with 0.0037% of the mistakes).

N = 4, clasificador = naive_bayes.MultinomialNB:

	Time:
		real	61m9.887s
		user	38m5.160s
		sys	0m4.164s
	Accuracy: 68.20%
	Accuracy of known words: 9.935961682509205%.
	Accuracy of unknown words: 90.0640383174908%.
	(original tag) ao: 
		tag selected by model -> aq (with 0.0564% of the mistakes).
		tag selected by model -> cc (with 0.0033% of the mistakes).
		tag selected by model -> da (with 0.0630% of the mistakes).
		tag selected by model -> fp (with 0.0066% of the mistakes).
		tag selected by model -> nc (with 0.6933% of the mistakes).
		tag selected by model -> np (with 0.0166% of the mistakes).
		tag selected by model -> sp (with 0.0199% of the mistakes).
		tag selected by model -> vm (with 0.0133% of the mistakes).

	(original tag) aq: 
		tag selected by model -> cc (with 0.1128% of the mistakes).
		tag selected by model -> cs (with 0.0531% of the mistakes).
		tag selected by model -> da (with 1.6056% of the mistakes).
		tag selected by model -> di (with 0.0431% of the mistakes).
		tag selected by model -> fc (with 0.2554% of the mistakes).
		tag selected by model -> fp (with 0.2024% of the mistakes).
		tag selected by model -> nc (with 4.1833% of the mistakes).
		tag selected by model -> np (with 0.1692% of the mistakes).
		tag selected by model -> pr (with 0.0299% of the mistakes).
		tag selected by model -> rg (with 0.0796% of the mistakes).
		tag selected by model -> sp (with 4.3591% of the mistakes).
		tag selected by model -> vm (with 0.8924% of the mistakes).

	(original tag) cc: 
		tag selected by model -> aq (with 0.0763% of the mistakes).
		tag selected by model -> da (with 1.1611% of the mistakes).
		tag selected by model -> di (with 0.0100% of the mistakes).
		tag selected by model -> fc (with 0.0133% of the mistakes).
		tag selected by model -> fp (with 0.0033% of the mistakes).
		tag selected by model -> nc (with 0.7730% of the mistakes).
		tag selected by model -> np (with 0.4246% of the mistakes).
		tag selected by model -> rg (with 0.1526% of the mistakes).
		tag selected by model -> sp (with 0.2488% of the mistakes).
		tag selected by model -> vm (with 0.1028% of the mistakes).

	(original tag) cs: 
		tag selected by model -> aq (with 0.1095% of the mistakes).
		tag selected by model -> cc (with 0.1227% of the mistakes).
		tag selected by model -> da (with 0.7564% of the mistakes).
		tag selected by model -> fc (with 0.0896% of the mistakes).
		tag selected by model -> fp (with 0.0431% of the mistakes).
		tag selected by model -> nc (with 0.4313% of the mistakes).
		tag selected by model -> np (with 0.0663% of the mistakes).
		tag selected by model -> pr (with 1.2573% of the mistakes).
		tag selected by model -> rg (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.7696% of the mistakes).
		tag selected by model -> vm (with 0.1161% of the mistakes).

	(original tag) da: 
		tag selected by model -> aq (with 0.0962% of the mistakes).
		tag selected by model -> fc (with 0.0498% of the mistakes).
		tag selected by model -> fp (with 0.0365% of the mistakes).
		tag selected by model -> nc (with 0.4711% of the mistakes).
		tag selected by model -> np (with 0.0663% of the mistakes).
		tag selected by model -> nu (with 0.0332% of the mistakes).
		tag selected by model -> sp (with 0.1360% of the mistakes).

	(original tag) dd: 
		tag selected by model -> aq (with 0.0531% of the mistakes).
		tag selected by model -> cc (with 0.0033% of the mistakes).
		tag selected by model -> cs (with 0.0265% of the mistakes).
		tag selected by model -> da (with 0.9156% of the mistakes).
		tag selected by model -> di (with 0.0033% of the mistakes).
		tag selected by model -> fc (with 0.0066% of the mistakes).
		tag selected by model -> fp (with 0.0066% of the mistakes).
		tag selected by model -> nc (with 0.4014% of the mistakes).
		tag selected by model -> np (with 0.1360% of the mistakes).
		tag selected by model -> pr (with 0.0100% of the mistakes).
		tag selected by model -> rg (with 0.0066% of the mistakes).
		tag selected by model -> sp (with 0.1626% of the mistakes).
		tag selected by model -> vm (with 0.2057% of the mistakes).

	(original tag) de: 
		tag selected by model -> da (with 0.0100% of the mistakes).
		tag selected by model -> np (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.0066% of the mistakes).
		tag selected by model -> vm (with 0.0066% of the mistakes).

	(original tag) di: 
		tag selected by model -> aq (with 0.4445% of the mistakes).
		tag selected by model -> cc (with 0.0100% of the mistakes).
		tag selected by model -> da (with 0.6900% of the mistakes).
		tag selected by model -> fc (with 0.0564% of the mistakes).
		tag selected by model -> fp (with 0.0464% of the mistakes).
		tag selected by model -> nc (with 1.1910% of the mistakes).
		tag selected by model -> np (with 0.1062% of the mistakes).
		tag selected by model -> pr (with 0.0166% of the mistakes).
		tag selected by model -> rg (with 0.0431% of the mistakes).
		tag selected by model -> sp (with 0.5640% of the mistakes).
		tag selected by model -> vm (with 0.2322% of the mistakes).

	(original tag) dn: 
		tag selected by model -> aq (with 0.1062% of the mistakes).
		tag selected by model -> da (with 0.2820% of the mistakes).
		tag selected by model -> di (with 0.0962% of the mistakes).
		tag selected by model -> fc (with 0.0100% of the mistakes).
		tag selected by model -> fp (with 0.0033% of the mistakes).
		tag selected by model -> nc (with 0.4047% of the mistakes).
		tag selected by model -> np (with 0.1426% of the mistakes).
		tag selected by model -> rg (with 0.0166% of the mistakes).
		tag selected by model -> sp (with 0.1194% of the mistakes).
		tag selected by model -> vm (with 0.0464% of the mistakes).

	(original tag) dp: 
		tag selected by model -> aq (with 0.1128% of the mistakes).
		tag selected by model -> cc (with 0.0199% of the mistakes).
		tag selected by model -> cs (with 0.0066% of the mistakes).
		tag selected by model -> da (with 1.4962% of the mistakes).
		tag selected by model -> di (with 0.0033% of the mistakes).
		tag selected by model -> fc (with 0.0265% of the mistakes).
		tag selected by model -> fp (with 0.0033% of the mistakes).
		tag selected by model -> nc (with 0.5606% of the mistakes).
		tag selected by model -> np (with 0.0630% of the mistakes).
		tag selected by model -> pr (with 0.0199% of the mistakes).
		tag selected by model -> sp (with 0.2919% of the mistakes).
		tag selected by model -> vm (with 0.2422% of the mistakes).

	(original tag) dt: 
		tag selected by model -> aq (with 0.0066% of the mistakes).
		tag selected by model -> da (with 0.0265% of the mistakes).
		tag selected by model -> fc (with 0.0033% of the mistakes).
		tag selected by model -> nc (with 0.0066% of the mistakes).
		tag selected by model -> np (with 0.0100% of the mistakes).
		tag selected by model -> sp (with 0.0133% of the mistakes).

	(original tag) fa: 
		tag selected by model -> aq (with 0.0166% of the mistakes).
		tag selected by model -> da (with 0.0365% of the mistakes).
		tag selected by model -> fc (with 0.0066% of the mistakes).
		tag selected by model -> fp (with 0.0033% of the mistakes).
		tag selected by model -> nc (with 0.0398% of the mistakes).
		tag selected by model -> np (with 0.0100% of the mistakes).
		tag selected by model -> rg (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.0431% of the mistakes).
		tag selected by model -> vm (with 0.0133% of the mistakes).

	(original tag) fc: 
		tag selected by model -> da (with 0.1161% of the mistakes).
		tag selected by model -> nc (with 0.0929% of the mistakes).
		tag selected by model -> sp (with 0.0133% of the mistakes).
		tag selected by model -> vm (with 0.0829% of the mistakes).

	(original tag) fd: 
		tag selected by model -> aq (with 0.2488% of the mistakes).
		tag selected by model -> cs (with 0.0166% of the mistakes).
		tag selected by model -> da (with 0.0597% of the mistakes).
		tag selected by model -> di (with 0.0100% of the mistakes).
		tag selected by model -> fc (with 0.0498% of the mistakes).
		tag selected by model -> fp (with 0.0100% of the mistakes).
		tag selected by model -> nc (with 0.1095% of the mistakes).
		tag selected by model -> np (with 0.0066% of the mistakes).
		tag selected by model -> pr (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.3948% of the mistakes).
		tag selected by model -> vm (with 0.0265% of the mistakes).

	(original tag) fe: 
		tag selected by model -> aq (with 0.0265% of the mistakes).
		tag selected by model -> da (with 0.0962% of the mistakes).
		tag selected by model -> fc (with 0.0299% of the mistakes).
		tag selected by model -> fp (with 0.1161% of the mistakes).
		tag selected by model -> nc (with 0.2256% of the mistakes).
		tag selected by model -> np (with 0.0066% of the mistakes).
		tag selected by model -> sp (with 0.0100% of the mistakes).
		tag selected by model -> vm (with 0.0630% of the mistakes).

	(original tag) fg: 
		tag selected by model -> aq (with 0.4279% of the mistakes).
		tag selected by model -> cc (with 0.0265% of the mistakes).
		tag selected by model -> cs (with 0.0265% of the mistakes).
		tag selected by model -> da (with 1.0815% of the mistakes).
		tag selected by model -> di (with 0.0033% of the mistakes).
		tag selected by model -> fc (with 0.1426% of the mistakes).
		tag selected by model -> fp (with 0.0730% of the mistakes).
		tag selected by model -> nc (with 0.8891% of the mistakes).
		tag selected by model -> np (with 0.1028% of the mistakes).
		tag selected by model -> pr (with 0.0066% of the mistakes).
		tag selected by model -> rg (with 0.0100% of the mistakes).
		tag selected by model -> sp (with 0.7763% of the mistakes).
		tag selected by model -> vm (with 0.1426% of the mistakes).

	(original tag) fh: 
		tag selected by model -> da (with 0.0033% of the mistakes).
		tag selected by model -> nc (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.0066% of the mistakes).

	(original tag) fi: 
		tag selected by model -> aq (with 0.0896% of the mistakes).
		tag selected by model -> cc (with 0.0100% of the mistakes).
		tag selected by model -> cs (with 0.0066% of the mistakes).
		tag selected by model -> da (with 0.1028% of the mistakes).
		tag selected by model -> fc (with 0.0630% of the mistakes).
		tag selected by model -> fp (with 0.0199% of the mistakes).
		tag selected by model -> nc (with 0.0697% of the mistakes).
		tag selected by model -> np (with 0.0066% of the mistakes).
		tag selected by model -> rg (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.1327% of the mistakes).
		tag selected by model -> vm (with 0.0332% of the mistakes).

	(original tag) fp: 
		tag selected by model -> aq (with 0.0033% of the mistakes).
		tag selected by model -> cc (with 0.0066% of the mistakes).
		tag selected by model -> cs (with 0.0100% of the mistakes).
		tag selected by model -> da (with 0.5739% of the mistakes).
		tag selected by model -> nc (with 0.2820% of the mistakes).
		tag selected by model -> np (with 0.0199% of the mistakes).
		tag selected by model -> sp (with 0.0464% of the mistakes).
		tag selected by model -> vm (with 0.0929% of the mistakes).

	(original tag) fs: 
		tag selected by model -> aq (with 0.0332% of the mistakes).
		tag selected by model -> da (with 0.0066% of the mistakes).
		tag selected by model -> fc (with 0.0166% of the mistakes).
		tag selected by model -> nc (with 0.0166% of the mistakes).
		tag selected by model -> sp (with 0.0531% of the mistakes).
		tag selected by model -> vm (with 0.0199% of the mistakes).

	(original tag) fx: 
		tag selected by model -> aq (with 0.0896% of the mistakes).
		tag selected by model -> cs (with 0.0033% of the mistakes).
		tag selected by model -> da (with 0.0133% of the mistakes).
		tag selected by model -> fc (with 0.0299% of the mistakes).
		tag selected by model -> fp (with 0.0199% of the mistakes).
		tag selected by model -> nc (with 0.0697% of the mistakes).
		tag selected by model -> sp (with 0.1360% of the mistakes).
		tag selected by model -> vm (with 0.0166% of the mistakes).

	(original tag) fz: 
		tag selected by model -> aq (with 0.0033% of the mistakes).
		tag selected by model -> da (with 0.0299% of the mistakes).
		tag selected by model -> fc (with 0.0066% of the mistakes).
		tag selected by model -> nc (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.0166% of the mistakes).

	(original tag) nc: 
		tag selected by model -> aq (with 2.5909% of the mistakes).
		tag selected by model -> cc (with 0.0498% of the mistakes).
		tag selected by model -> cs (with 0.0896% of the mistakes).
		tag selected by model -> da (with 2.6075% of the mistakes).
		tag selected by model -> di (with 0.0498% of the mistakes).
		tag selected by model -> fc (with 0.4479% of the mistakes).
		tag selected by model -> fp (with 0.2455% of the mistakes).
		tag selected by model -> np (with 0.6369% of the mistakes).
		tag selected by model -> pr (with 0.0299% of the mistakes).
		tag selected by model -> rg (with 0.0398% of the mistakes).
		tag selected by model -> sp (with 3.2146% of the mistakes).
		tag selected by model -> vm (with 0.9189% of the mistakes).

	(original tag) np: 
		tag selected by model -> aq (with 0.0365% of the mistakes).
		tag selected by model -> cc (with 0.0033% of the mistakes).
		tag selected by model -> cs (with 0.0066% of the mistakes).
		tag selected by model -> da (with 1.8511% of the mistakes).
		tag selected by model -> fc (with 0.0066% of the mistakes).
		tag selected by model -> fp (with 0.0100% of the mistakes).
		tag selected by model -> nc (with 1.3900% of the mistakes).
		tag selected by model -> rg (with 0.0066% of the mistakes).
		tag selected by model -> sp (with 1.0284% of the mistakes).
		tag selected by model -> vm (with 0.2588% of the mistakes).

	(original tag) nu: 
		tag selected by model -> aq (with 0.0630% of the mistakes).
		tag selected by model -> da (with 0.5971% of the mistakes).
		tag selected by model -> fc (with 0.0133% of the mistakes).
		tag selected by model -> fp (with 0.0299% of the mistakes).
		tag selected by model -> nc (with 0.2787% of the mistakes).
		tag selected by model -> np (with 0.0763% of the mistakes).
		tag selected by model -> pr (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.1194% of the mistakes).
		tag selected by model -> vm (with 0.0398% of the mistakes).

	(original tag) p0: 
		tag selected by model -> aq (with 0.3583% of the mistakes).
		tag selected by model -> cc (with 0.0464% of the mistakes).
		tag selected by model -> cs (with 0.0133% of the mistakes).
		tag selected by model -> da (with 0.3317% of the mistakes).
		tag selected by model -> fc (with 0.1393% of the mistakes).
		tag selected by model -> fp (with 0.0431% of the mistakes).
		tag selected by model -> nc (with 0.3649% of the mistakes).
		tag selected by model -> np (with 0.0498% of the mistakes).
		tag selected by model -> pr (with 0.0265% of the mistakes).
		tag selected by model -> rg (with 0.0066% of the mistakes).
		tag selected by model -> sp (with 0.6436% of the mistakes).
		tag selected by model -> vm (with 0.2853% of the mistakes).

	(original tag) pd: 
		tag selected by model -> aq (with 0.0166% of the mistakes).
		tag selected by model -> cc (with 0.0133% of the mistakes).
		tag selected by model -> cs (with 0.0033% of the mistakes).
		tag selected by model -> da (with 0.1957% of the mistakes).
		tag selected by model -> di (with 0.0033% of the mistakes).
		tag selected by model -> fc (with 0.0232% of the mistakes).
		tag selected by model -> nc (with 0.0995% of the mistakes).
		tag selected by model -> np (with 0.1227% of the mistakes).
		tag selected by model -> pr (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.0763% of the mistakes).
		tag selected by model -> vm (with 0.0763% of the mistakes).

	(original tag) pe: 
		tag selected by model -> sp (with 0.0033% of the mistakes).

	(original tag) pi: 
		tag selected by model -> aq (with 0.1161% of the mistakes).
		tag selected by model -> cc (with 0.0365% of the mistakes).
		tag selected by model -> cs (with 0.0100% of the mistakes).
		tag selected by model -> da (with 0.5175% of the mistakes).
		tag selected by model -> di (with 0.3881% of the mistakes).
		tag selected by model -> fc (with 0.0332% of the mistakes).
		tag selected by model -> fp (with 0.0033% of the mistakes).
		tag selected by model -> nc (with 0.3351% of the mistakes).
		tag selected by model -> np (with 0.0365% of the mistakes).
		tag selected by model -> pr (with 0.0133% of the mistakes).
		tag selected by model -> rg (with 0.0498% of the mistakes).
		tag selected by model -> sp (with 0.1891% of the mistakes).
		tag selected by model -> vm (with 0.1659% of the mistakes).

	(original tag) pn: 
		tag selected by model -> aq (with 0.0365% of the mistakes).
		tag selected by model -> cs (with 0.0033% of the mistakes).
		tag selected by model -> da (with 0.0697% of the mistakes).
		tag selected by model -> fc (with 0.0100% of the mistakes).
		tag selected by model -> nc (with 0.0896% of the mistakes).
		tag selected by model -> np (with 0.0199% of the mistakes).
		tag selected by model -> sp (with 0.0299% of the mistakes).
		tag selected by model -> vm (with 0.0199% of the mistakes).

	(original tag) pp: 
		tag selected by model -> aq (with 0.2521% of the mistakes).
		tag selected by model -> cc (with 0.0332% of the mistakes).
		tag selected by model -> cs (with 0.0166% of the mistakes).
		tag selected by model -> da (with 1.4431% of the mistakes).
		tag selected by model -> fc (with 0.1559% of the mistakes).
		tag selected by model -> fp (with 0.0199% of the mistakes).
		tag selected by model -> nc (with 0.3351% of the mistakes).
		tag selected by model -> np (with 0.1659% of the mistakes).
		tag selected by model -> p0 (with 0.0730% of the mistakes).
		tag selected by model -> sp (with 0.4578% of the mistakes).
		tag selected by model -> vm (with 0.7331% of the mistakes).

	(original tag) pr: 
		tag selected by model -> aq (with 0.0232% of the mistakes).
		tag selected by model -> cs (with 0.2853% of the mistakes).
		tag selected by model -> da (with 0.1725% of the mistakes).
		tag selected by model -> di (with 0.0033% of the mistakes).
		tag selected by model -> fc (with 0.0630% of the mistakes).
		tag selected by model -> fp (with 0.0332% of the mistakes).
		tag selected by model -> nc (with 0.3417% of the mistakes).
		tag selected by model -> np (with 0.0199% of the mistakes).
		tag selected by model -> rg (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.0299% of the mistakes).
		tag selected by model -> vm (with 0.0265% of the mistakes).

	(original tag) pt: 
		tag selected by model -> aq (with 0.0066% of the mistakes).
		tag selected by model -> cc (with 0.0033% of the mistakes).
		tag selected by model -> cs (with 0.0166% of the mistakes).
		tag selected by model -> da (with 0.1592% of the mistakes).
		tag selected by model -> fc (with 0.0299% of the mistakes).
		tag selected by model -> fp (with 0.0033% of the mistakes).
		tag selected by model -> nc (with 0.0597% of the mistakes).
		tag selected by model -> np (with 0.0663% of the mistakes).
		tag selected by model -> pr (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.0597% of the mistakes).
		tag selected by model -> vm (with 0.0299% of the mistakes).

	(original tag) px: 
		tag selected by model -> da (with 0.0398% of the mistakes).
		tag selected by model -> nc (with 0.0133% of the mistakes).
		tag selected by model -> sp (with 0.0033% of the mistakes).
		tag selected by model -> vm (with 0.0100% of the mistakes).

	(original tag) rg: 
		tag selected by model -> aq (with 1.1478% of the mistakes).
		tag selected by model -> cc (with 0.1161% of the mistakes).
		tag selected by model -> cs (with 0.0133% of the mistakes).
		tag selected by model -> da (with 2.0701% of the mistakes).
		tag selected by model -> di (with 0.0265% of the mistakes).
		tag selected by model -> fc (with 0.1990% of the mistakes).
		tag selected by model -> fp (with 0.0763% of the mistakes).
		tag selected by model -> nc (with 1.2009% of the mistakes).
		tag selected by model -> np (with 0.1791% of the mistakes).
		tag selected by model -> pr (with 0.0464% of the mistakes).
		tag selected by model -> sp (with 1.9274% of the mistakes).
		tag selected by model -> vm (with 0.8128% of the mistakes).

	(original tag) rn: 
		tag selected by model -> aq (with 0.2256% of the mistakes).
		tag selected by model -> cc (with 0.0166% of the mistakes).
		tag selected by model -> da (with 0.4479% of the mistakes).
		tag selected by model -> fc (with 0.1261% of the mistakes).
		tag selected by model -> fp (with 0.0265% of the mistakes).
		tag selected by model -> nc (with 0.3450% of the mistakes).
		tag selected by model -> np (with 0.1062% of the mistakes).
		tag selected by model -> pr (with 0.0166% of the mistakes).
		tag selected by model -> rg (with 0.2554% of the mistakes).
		tag selected by model -> sp (with 0.5606% of the mistakes).
		tag selected by model -> vm (with 0.4744% of the mistakes).

	(original tag) sp: 
		tag selected by model -> aq (with 0.0133% of the mistakes).
		tag selected by model -> cc (with 0.0066% of the mistakes).
		tag selected by model -> cs (with 0.0962% of the mistakes).
		tag selected by model -> da (with 1.8179% of the mistakes).
		tag selected by model -> fc (with 0.0962% of the mistakes).
		tag selected by model -> fp (with 0.1161% of the mistakes).
		tag selected by model -> nc (with 0.6701% of the mistakes).
		tag selected by model -> np (with 0.1725% of the mistakes).
		tag selected by model -> rg (with 0.0033% of the mistakes).
		tag selected by model -> vm (with 0.1692% of the mistakes).

	(original tag) un: 
		tag selected by model -> aq (with 0.0100% of the mistakes).
		tag selected by model -> da (with 0.0365% of the mistakes).
		tag selected by model -> fc (with 0.0033% of the mistakes).
		tag selected by model -> fe (with 0.0498% of the mistakes).
		tag selected by model -> fp (with 0.0133% of the mistakes).
		tag selected by model -> nc (with 0.0133% of the mistakes).
		tag selected by model -> np (with 0.0232% of the mistakes).
		tag selected by model -> pr (with 0.0066% of the mistakes).
		tag selected by model -> rg (with 0.0033% of the mistakes).
		tag selected by model -> sp (with 0.0464% of the mistakes).
		tag selected by model -> vm (with 0.0232% of the mistakes).

	(original tag) va: 
		tag selected by model -> aq (with 0.2554% of the mistakes).
		tag selected by model -> cc (with 0.0100% of the mistakes).
		tag selected by model -> cs (with 0.0100% of the mistakes).
		tag selected by model -> da (with 0.2986% of the mistakes).
		tag selected by model -> fc (with 0.1161% of the mistakes).
		tag selected by model -> fp (with 0.0332% of the mistakes).
		tag selected by model -> nc (with 0.3450% of the mistakes).
		tag selected by model -> np (with 0.0630% of the mistakes).
		tag selected by model -> pr (with 0.0066% of the mistakes).
		tag selected by model -> sp (with 0.4346% of the mistakes).
		tag selected by model -> vm (with 1.1976% of the mistakes).

	(original tag) vm: 
		tag selected by model -> aq (with 1.4829% of the mistakes).
		tag selected by model -> cs (with 0.0299% of the mistakes).
		tag selected by model -> da (with 3.8781% of the mistakes).
		tag selected by model -> di (with 0.0299% of the mistakes).
		tag selected by model -> fc (with 0.6005% of the mistakes).
		tag selected by model -> fp (with 0.2090% of the mistakes).
		tag selected by model -> nc (with 3.1150% of the mistakes).
		tag selected by model -> np (with 0.2919% of the mistakes).
		tag selected by model -> pr (with 0.0464% of the mistakes).
		tag selected by model -> rg (with 0.0299% of the mistakes).
		tag selected by model -> sp (with 3.8316% of the mistakes).

	(original tag) vs: 
		tag selected by model -> aq (with 0.5573% of the mistakes).
		tag selected by model -> cc (with 0.0365% of the mistakes).
		tag selected by model -> cs (with 0.0365% of the mistakes).
		tag selected by model -> da (with 0.5971% of the mistakes).
		tag selected by model -> di (with 0.0066% of the mistakes).
		tag selected by model -> fc (with 0.2322% of the mistakes).
		tag selected by model -> fp (with 0.0299% of the mistakes).
		tag selected by model -> nc (with 0.5839% of the mistakes).
		tag selected by model -> np (with 0.1062% of the mistakes).
		tag selected by model -> pr (with 0.0033% of the mistakes).
		tag selected by model -> rg (with 0.0199% of the mistakes).
		tag selected by model -> sp (with 1.1445% of the mistakes).
		tag selected by model -> vm (with 1.1578% of the mistakes).

	(original tag) zm: 
		tag selected by model -> aq (with 0.0232% of the mistakes).
		tag selected by model -> cs (with 0.0066% of the mistakes).
		tag selected by model -> da (with 0.0066% of the mistakes).
		tag selected by model -> fp (with 0.0066% of the mistakes).
		tag selected by model -> nc (with 0.1227% of the mistakes).
		tag selected by model -> np (with 0.0199% of the mistakes).
		tag selected by model -> sp (with 0.0100% of the mistakes).

	(original tag) zp: 
		tag selected by model -> aq (with 0.0033% of the mistakes).
		tag selected by model -> da (with 0.0033% of the mistakes).
		tag selected by model -> nc (with 0.2355% of the mistakes).
		tag selected by model -> np (with 0.0265% of the mistakes).
		tag selected by model -> sp (with 0.0033% of the mistakes).