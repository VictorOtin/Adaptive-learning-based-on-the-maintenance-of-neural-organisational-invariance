# Aprendizaje adaptativo basado en el mantenimiento de invarianzas organizacionales neuronales

## Resumen
Un artículo de la revista Scientific Reports [1] propone un mecanismo de aprendizaje que genera comportamientos adaptativos, en entornos sencillos, buscando los puntos críticos, que son las transiciones de fase comentadas anteriormente.

La primera parte del trabajo consiste en acercar el funcionamiento del algoritmo al de los sistemas biológicos reales. Esto se consigue sustituyendo la red neuronal finita del mismo por una red infinita. En la segunda parte se replica el algoritmo con la nueva arquitectura y se comprueban sus resultados no solo en los mismos entornos, sino también en uno mas complejo. Estos entornos son: Un robot, un péndulo con una barra articulada y una serpiente que aprender a avanzar.

En todos los entornos se observa que, simplemente buscando estos puntos críticos, los agentes generan comportamientos interesantes sin haber sido programados para ello. Además, la complejidad de su comportamiento aumenta a medida que se aumenta el tamaño de las redes neuronales.

## Código
En este proyecto se han subido diferentes partes del código utilizado para la realización del trabajo fin de máster. Los siguientes entornos han sido analizados: Mountain Car, Acrobot y Swimmer.

## Referencias
En este proyecto se ha tomado como referencia un artículo publicado en la revista Scientific Reports, cuyo código y parte de los resultados obtenidos se pueden consultar en el siguiente repositorio: [1] https://github.com/MiguelAguilera/Adaptation-to-criticality-through-organizational-invariance
