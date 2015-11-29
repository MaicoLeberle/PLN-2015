-------------------------------------------------------------------------------
EJERCICIO 2
-------------------------------------------------------------------------------

Procesar el corpus de entrenamiento, y computar toda la información necesaria 
posteriormente, requirió entre otros detalles:
	* Agregar símbolos de inicio y fin a cada oración.
	* Crear distintos defaultdicts (a saber, self.counts, self.word_counts, 
	  etc.) para ir procesando la información necesaria para ejecutar los
	  métodos de la clase.
	* Por una comodidad de código, opté por incluir a self.probs y 
	  self.sorted_probs en esta clase, para su posterior utilización en 
	  conjunto con la clase NGramGenerator.
	* A su vez, esta clase hereda de EvaluatingClass para posteriormente poder
	  realizar las evaluaciones (perplexity, etc.) pertinentes.


-------------------------------------------------------------------------------
EJERCICIO 3
-------------------------------------------------------------------------------

Aquí, simplemente cree una clase que contiene un objeto de tipo NGram (a saber,
self.model). 
Además, en self.generate_token genero una variable aleatoria entre 0.0 y 1.0 y 
de ahí genero un token. Puedo hacer esto pues los valores en self.probs suman 
1.0. Luego, con esos tokens generados voy generando las oraciones.
Comando a utilizar para generar oraciones:

	python3 languagemodeling/scripts/generate.py -i <file> -n <number>

, donde <file> es el nombre del archivo cuyo contenido es producto de ejecutar
pickle.dump y <number> es el número de oraciones a generar. Si se procedió a 
entrenar <file> con languagemodeling/scripts/train.py, entonces conviene no 
hacerlo con la opción de línea de comandos --testing, para aprovechar todo el 
corpus.
Aprovecho aquí para aclarar cómo utilizar languagemodeling/scripts/train.py:
	
	python3 languagemodeling/scripts/train.py -o <output file> -m <model> 
		-n <n> [--testing]

, donde <model> es alguno de ngram, addone, interpolated, backoff, <n> indica
el orden del modelo, y la opción --testing indica que se utilizará sólo el 90%
del corpus para entrenar el modelo (en lugar del 100%)
A continuación, las oraciones generadas de esta manera.

Unigramas:
	* Lightning question him open school say . 
	* her pay Corps in.
	* Buddha matched if the the brightly on counseling between Corps not 
	  Reformation the understanding chairman intervals.
	* Their his.

Bigramas:
	* Mills deliberately simplify the Russian nihilist.
	* I've reached 32-degrees-F all men at least afford to what few people `` 
	  white every letter , then chuck capacity in its leaders of talk to be 
	  weatherproof refrigeration.
	* A project is not merely pick of Science In classical defense of life.
	* His point out.

Trigramas:
	* The commission had issued an appeal for Patchen.
	* The pets were chosen as her subsequent disinclination to assume they'll 
	  decide he didn't know we'd be pretty difficult to compose himself.
	* It was too young and ripening , you know.
	* Hegel's profound admiration for our town's worthiest charities.

Cuatrigramas:
	* This cooling does not change the probabilities much , and who is able to
	  create a nine-state regional group in a collective effort to attract new 
	  employees , hiring and training them , extra overtime , and defective 
	  work performed by the new generation of Europeans began to discover the 
	  crowning virtue that completes this company's collective personality.
	* Most people would have to produce a cumulative effect.
	* The pale blob of the woman disappeared.
	* Experiments are often composed of several repetitions of the five-round 
	  experiment.


-------------------------------------------------------------------------------
EJERCICIO 4
-------------------------------------------------------------------------------

Esta clase es igual de simple que NGram. La única diferencia es que 
self.cond_prob agrega el suavizado add-one.

Valores perplexity obtenidos con esta clase:

  Valor de N   |   Perplexity  |
--------------------------------
       1       |     1042      |
--------------------------------
       2       |     2250      |
--------------------------------
       3       |     10703     |
--------------------------------
       4       |     13660     |
--------------------------------


-------------------------------------------------------------------------------
EJERCICIO 5
-------------------------------------------------------------------------------

Aquí implementé un script para cargar un modelo desde un archivo (idealmente, 
se trata de un modelo entrenado con languagemodeling/scripts/train.py, 
utilizando el 90% nltk.corpus.brown) y evaluarlo sobre el test set que consiste
 del último 10% de nltk.corpus.brown.
El uso de este script es

	python3 languagemodeling/scripts/eval.py -i <file>

, donde <file> contiene el modelo entrenado (y guardado vía pickle.dump).

Además, en languagemodeling/ngram.py implementé la clase EvaluatingClass, la 
cual contiene los cálculos para log-probability, cross-entropy y perplexity. 
De esta clase heredan las distintas clases de este práctico que requieren ser
evaluadas.


-------------------------------------------------------------------------------
EJERCICIO 6
-------------------------------------------------------------------------------

Aquí se implementa el modelado de lenguajes con suavizado por interpolación. El
 procesamiento de las oraciones del corpus de entrenamiento es más o menos 
similar al de las previas clases, con el detalle de que ahora se deben 
contabilizar en self.counts no sólo los n-gramas y (n-1)-gramas, sino todos los
k-gramas con el mismo final, con 0 <= k <= n. Es decir, dado una tupla de 
longitud n, ngram, se deben contabilizar en self.counts a ngram, ngram[1:], 
ngram[2:], ..., ().
Además, se utiliza sólo el 90% del training corpus (es decir, el 90% del 90% de
 nltk.corpus.brown, si se entrena con languagemodeling/scripts/train.py) para 
entrenar el modelo, y 10% del training corpus (10% del 90% de nltk.corpus.brown,
 análogamente) se utiliza como held-out data para calcular el parámetro gamma 
vía barrido. Se busca el gamma que maximiza la log-likelihood del held-out set.
A su vez, __init__ tiene un parámetro extra, addone, que indica si el 
procesamiento de las probabilidades de unigramas debe hacerlo un modelo 
AddOneNGram o uno NGram. 

Valores perplexity obtenidos con esta clase:

  Valor de N   |   Perplexity  |
--------------------------------
       1       |     1026      |
--------------------------------
       2       |      419      |
--------------------------------
       3       |      961      |
--------------------------------
       4       |      932      |
--------------------------------


-------------------------------------------------------------------------------
EJERCICIO 7
-------------------------------------------------------------------------------

Aquí se implementa el modelado de lenguajes con suavizado por Back-Off con 
Discounting. El procesamiento de las oraciones del corpus de entrenamiento es 
similar al de InterpolatedNGram, con la diferencia de que es preciso agregar 
cada sub-k-grama, con 0 <= k <= n, en la oración.
También se utiliza aquí un modelo de AddOneNGram o de NGram para el cálculo de
probabilidades de los unigramas, y barrido para calcular el parámetro beta del
modelo. Aquí también se busca el beta que maximiza la log-likelihood del 
held-out set.
Dicho beta se calcula con el 10% final del corpus de entrenamiento (10% del 90%
 de nltk.corpus.brown, si se entrena vía languagemodeling/scripts/train.py). 
Pero el barrido para beta es un tanto más complicado que para el gamma del 
ejercicio anterior. Es preciso realizar memoization a medida que se van 
computando las probabilidades condicionales (self.cond_prob), para evitar 
recomputarlas, lo cual es sumamente costoso. Dicha memoization se realiza en 
self.__q_D, self.__A, self.__alpha y self.__denom. 

Valores perplexity obtenidos con esta clase:

  Valor de N   |   Perplexity  |
--------------------------------
       1       |     1513      |
--------------------------------
       2       |            |
--------------------------------
       3       |            |
--------------------------------
       4       |            |
--------------------------------