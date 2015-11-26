-------------------------------------------------------------------------------
EJERCICIO 1
-------------------------------------------------------------------------------

Aquí se implementó la evaluación de los modelos implementados por la cátedra, 
mediante los métodos de evaluación (precision, recall y F1) propuestos por 
Michael Collins en sus videolectures.
Los resultados de evaluar los modelos Flat, RBranch y LBranch (sólo las oraciones 
que no exceden la longitud 20) son:

* Flat - Labeled:
	- Precision: 99.93% 
  	- Recall: 14.57% 
  	- F1: 25.43%

* Flat - Unlabeled:
	- Precision: 100.00% 
	- Recall: 14.58% 
	- F1: 25.45% 


* RBranch - Labeled:
	- Precision: 8.81% 
	- Recall: 14.57% 
	- F1: 10.98% 

* RBranch - Unlabeled:
	- Precision: 8.87% 
	- Recall: 14.68% 
	- F1: 11.06% 


* LBranch - Labeled:
	- Precision: 8.81% 
	- Recall: 14.57% 
	- F1: 10.98% 

* LBranch - Unlabeled:
	- Precision: 14.71% 
	- Recall: 24.33% 
	- F1: 18.33% 


-------------------------------------------------------------------------------
EJERCICIO 2
-------------------------------------------------------------------------------

Se implementa aquí el algoritmo CKY para parsear una oración, tomando como base
 para dicho parseo una PCFG binarizada de NLTK. Se siguen las indicaciones de 
Collins a la hora de implementar el algoritmo, y se optó por devolver la 2-upla
 (float('-inf'), None), siguiendo lo implementado en los tests.
Además, se agregó un caso de test que corresponde con la siguiente oración 
sintácticamente ambigua: "el periodista habló a la persona con el micrófono". 
Se puede apreciar que esta oración es ambigua, viendo que quien porta el 
micrófono puede ser el periodista o la persona. El modo de evaluar este caso de
 test es análogo al otro caso de test presentado por la cátedra.


-------------------------------------------------------------------------------
EJERCICIO 3
-------------------------------------------------------------------------------

Se implementa un modelo que recibe oraciones parseadas en su constructor, y 
que encapsula a un CKYParser (implementado en el ejercicio 2). Además, se 
deslexicalizó cada una de las producciones de la gramática subyacente, antes 
de ser pasadas como parámetro al CKYParser.
Con respecto al método parse, si se encuentra un parseo para la oración ya 
tageada (i.e., cada una de las palabras de la oración, junto a las etiquetas de
 Part-Of-Speech correspondientes) pasada como parámetro, entonces devolver el 
árbol. En caso de no encontrar un parseo válido, se devuelve el árbol llano 
como se explica en los comentarios del código. Se eligió esta forma de 
representar el no haber hallado un parseo apropiado al seguir las indicaciones
(implícitas) de los casos de test sobre cómo se debería resolver esta 
situación.

Los resultados encontrados al evaluar el modelo UPCFG fueron:

* Tiempo de evaluación: 4m12.278s.
* Labeled:
	- Precision: 67.90% 
	- Recall: 64.34% 
	- F1: 66.07% 
* Unlabeled:
	- Precision: 71.89% 
	- Recall: 68.12% 
	- F1: 69.96%


-------------------------------------------------------------------------------
EJERCICIO 4
-------------------------------------------------------------------------------

Para realizar este ejercicio, no fue necesario agregar mucho al código ya 
existente. Simplemente se agregó un parámetro (cuyo valor por defecto es None)
que establece el orden de markovización horizontal que se ha de implementar. 
Además, se debió incrementar las funcionalidades de parsing/scripts/train.py 
para poder entrenar modelos de este tipo.

A continuación, se detallan (y contrastan) los resultados de evaluar un modelo 
UPCFG con markovización horizontal de orden 0, 1, 2 y 3:

* N=0:
	- Tiempo de evaluación: 1m34.777s.
	- Labeled:
		. Precision: 68.27% 
		. Recall: 65.76% 
		. F1: 66.99% 
	- Unlabeled:
		. Precision: 70.16% 
		. Recall: 67.58% 
		. F1: 68.84%

* N=1:
	- Tiempo de evaluación: 2m5.748s.
	- Labeled:
		. Precision: 70.79% 
  		. Recall: 67.45% 
  		. F1: 69.08%
	- Unlabeled:
		. Precision: 73.32% 
  		. Recall: 69.86% 
  		. F1: 71.55% 

* N=2:
	- Tiempo de evaluación: 3m10.241s.
	- Labeled:
		. Precision: 70.41% 
  		. Recall: 66.35% 
  		. F1: 68.32% 
	- Unlabeled:
		. Precision: 73.78% 
  		. Recall: 69.52% 
  		. F1: 71.58%

* N=3:
	- Tiempo de evaluación: 3m42.027s.
	- Labeled:
		. Precision: 68.63% 
  		. Recall: 64.91% 
  		. F1: 66.72%
	- Unlabeled:
		. Precision: 72.54% 
  		. Recall: 68.61% 
  		. F1: 70.52%