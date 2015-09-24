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


-------------------------------------------------------------------------------
EJERCICIO 5
-------------------------------------------------------------------------------