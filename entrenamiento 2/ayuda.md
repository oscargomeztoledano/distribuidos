
				tipo	id
abrir				1		#	modo	tiempo
cerrar				2		#
estado				3		#
return_estado			4		#	estado
ack				5 		#
err				6		#


**Estas son las cadenas que tenemos que utilizar en el primer ejercicio**

para hacer este ejercicio se proporcionan ejemplos parecidos, hay que entender todos los ejercicios mirando los apuntes para luego poder entender los ejercicios gordos.


envelope{ 
	num tipo
	bytes msg
	}
	para hacerlo con un socket, hay que especificar un tipo de mensaje generico que tiene dentro los diferentes tipos de mensaje que hay que utilizar.
	
	si no hay que utilizar diversos sockets para cada acción, un total de 6 socket y ha dicho que lo mismo para este tipo de implementación hay tambien que utilizar hilos.
