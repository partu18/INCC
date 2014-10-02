# coding=utf-8

import os

working_directory = os.getcwd()

#Images path's:
result_path = working_directory + '/../resultados/result.txt'
circle_image_path = working_directory+'/../imagenes/circle.png'
arrow_image_path = working_directory+'/../imagenes/arrow.png'
line_image_path = working_directory+'/../imagenes/line.png'


#Keys lists: 
RH_ARROWS_KEYLIST = ['right','left' ]
LH_ARROWS_KEYLIST = ['a','d']
RH_TAPPING_KEYLIST = ['return']
LH_TAPPING_KEYLIST = ['space']
NORM_DUAL_KEYLIST = ['space','left','right']
INV_DUAL_KEYLIST = ['return','a','d']



#Messages 
coverMessage = u"Trabajo Práctico N°1\n"\
				u"Introducción a la Neurociencia Congnitiva y Computacional\n"\
				u"Tema: Dual Task, Tapping.\n\n\n\n\n"\
				u"Alumnos:\n"\
				u"\t Abrevaya, Sofía\n"\
				u"\t Artuso, Pablo\n"\
				u"\t Belloli, Laouen\n"\
				u"\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t Presioná enter para continuar"





startMessage = u"\n Presioná Enter cuando lo estés para comenzar con el siguiente experimento"


presentationMessage =   u"GRACIAS! Por tu colaboración para nuestro proyecto!!\n\n" \
						u"El siguiente experimento está compuesto de 5 niveles distintos donde se realizarán distintas tareas, primero con una mano"\
						u" y luego con la otra. Cada nivel tendrá su explicación previa. El tiempo de duración de cada uno de ellos es"\
						u" aproximadamente 30 segundos. " + u"\n\n\n" + startMessage

endMessage = u"Finalizado"




def goodbyeMessage(id):
	return  u"Terminaste con el experimento. Muchas gracias por tu colaboración. Pedimos que por favor te acuerdes este Nro. de ID: "\
			+ str(id)+\
			u". Si bien el experimento es anónimo, vamos a entregar premios. Si llegás a ganar y QUERÉS retirarlo,"\
			u" cuando nombremos tu ID pasás a buscarlo. Si querés mantener el anonimato, puede optar por no levantarte y no retirar el premio.\n"\
			u"Nuevamente agradecemos tu colaboración.\n\n\n"\
			u"Abrevaya Sofía\n"\
			u"Artuso Pablo\n"\
			u"Belloli Laouen\n"





message1 = u"Arranquemos con el primer nivel!\n"\
			u"En la parte central de la pantalla se proyectará un círculo de color negro intermitentemente. Tu tarea en este nivel consiste en"\
			u" apretar con la mano derecha la tecla 'Enter' (-dibujo-) cada vez que aparezca dicho círculo en la pantalla, intentando ir al mismo"\
			u" ritmo que este.\n "\
			u"¡ ES MUY IMPORTANTE QUE SEA LA MANO DERECHA !" + "\n\n\n" + startMessage

	
message2 = u"Perfecto! Ahora, la consigna para esta tarea es la misma que para el anterior. La diferencias con el anterior son dos:\n"\
			u"- Vas a utilizar la mano izquierda en lugar de la derecha\n"\
			u"- Vas a apretar la tecla 'Barra espaciadora' en lugar del 'Enter'\n"\
			u"¡ ES MUY IMPORTANTE QUE SEA LA MANO IZQUIERDA !"	 + "\n\n\n" + startMessage		  


message3 = u"Bien! Pasamos al segundo nivel\n"\
			u"Este nivel es muy parecido al primero con una pequeña diferencia. Ahora en vez de aparecer un circulo negro, va a aparecer"\
			u"una flecha que puede apuntar o bien hacia la derecha o bien hacia la izquierda.\n"\
			u"Tu tarea nuevamente consiste en apretar con tu mano derecha la tecla 'flecha izquierda' (-dibujo-) o 'flecha derecha' (-dibujo-)"\
			u" dependiendo cual de ellas aparezca en la pantalla, intentando ir al mismo ritmo que las flechas\n"\
			u"¡ ES MUY IMPORTANTE QUE SEA LA MANO DERECHA !" + "\n\n\n" + startMessage

message4 = u"Bárbaro! Como bien hicimos entre el primero y el segundo experimento, ahora vamos a cambiar de mano. La consigna se mantiene (se apreta"\
			u" la flecha correspondiente proyectada en pantalla). Dado que la mano que vas a usar es la izquierda, las teclas que vas a utilizar son:\n"\
			u"- 'A' Para simular la 'flecha izquierda'\n"\
			u"- 'D' Para simular la 'flecha derecha'\n"\
			u" ¡ ES MUY IMPORTANTE QUE REVISES LA POSICIÓN DE TUS MANOS !"   + "\n\n\n" + startMessage

message5 = u"Perfecto! Llegamos al nivel 3.\n"\
			u"En este nivel vamos a combinar las dos tareas que veníamos realizando en los niveles anteriores. La pantalla va a estar dividida"\
			u" a la mitad porque una raya vertical de color negro. Del lado izquierdo de ésta aparecerá el círculo, mientras que del derecho"\
			u" apareceran las flechas. Tu tarea esta vez es apretar con la mano izquierda la 'Barra espaciadora' (-dibujo-) cada vez que el"\
			u" círculo aparece y con la mano derecha la 'flecha izquierda' o 'flecha derecha' (-dibujos-) (dependiendo de la dirección a la cual apunte)"\
			u" cada vez que alguna de éstas aparezca.\n"\
			u" ¡ ES MUY IMPORTANTE QUE REVISES LA POSICIÓN DE TUS MANOS !"   + "\n\n\n" + startMessage


message6 = u"Vamos muy bien.\n"\
			u"Ahora para no perder el hilo conductor, vamos a cambiar las manos de lugar. La mano derecha será la encarga de seguir el ritmo del"\
			u" círculo (que ahora aparecerá del lado derecho de la raya) presionando la tecla 'Enter'. Mientras que con las teclas 'A' y 'D'"\
			u" vas a tratar de seguirle el ritmo y la dirección a las flechas que serán expuestas del lado izquierdo de la raya."\
			u" ¡ ES MUY IMPORTANTE QUE REVISES LA POSICIÓN DE TUS MANOS !"   + "\n\n\n" + startMessage

message7 = u"Muy bien! Nivel 4."\
			u"En este nivel vamos a repetir lo que hiciste en el nivel 3. Es decir, el círculo y las flechas volverán a aparecer del"\
			u" lado izquierdo y derecho de la pantalla respectivamente y tratarás de seguirles el ritmo apretando la 'Barra espaciadora' o las "\
			u" flechas depende de lo que corresponda. La diferencia es que esta vez queremos que enfoques tu concentración"\
			u" en el círculo. Esto NO quiere decir que dejes de seguir el ritmo de las flechas. Simplemente nuestra prioridad es que trates de"\
			u" que no se te escape ningún círculo sin apretar la 'Barra espaciadora'.\n"\
			u" ¡ ES MUY IMPORTANTE QUE REVISES LA POSICIÓN DE TUS MANOS !"   + "\n\n\n" + startMessage


message8 = u"Bien!\n"\
			u"Nuevamente hagamos este ejercicio cambiando las teclas que vamos a presionar. Dado que el círculo estará de la derecha, tratarás"\
			u" de seguirle el ritmo presionando la tecla 'Enter', mientras que para las flechas utilizarás la mano izquierda y las telcas 'A' y 'D'."\
			u" No te olvides que el círculo es lo que más nos interesa!!\n"\
			u" ¡ ES MUY IMPORTANTE QUE REVISES LA POSICIÓN DE TUS MANOS !"   + "\n\n\n" + startMessage

message9 = u"Excelente!! Nivel 5, el último"\
			u"Al igual que hiciste en el anterior nivel, en donde pusiste tu mayor concentración en el círculo negro, ahora queremos que lo hagas"\
			u" sobre las flechas. Comenzando con la mano izquierda sobre la 'Barra espaciadora' para llevar el ritmo del círculo, y la mano derecha"\
			u" sobre las flechas para seguir el ritmo de ellas. Acordate que nos interesa que le presten mucha atención a las flechas!!\n"\
			u" ¡ ES MUY IMPORTANTE QUE REVISES LA POSICIÓN DE TUS MANOS !"   + "\n\n\n" + startMessage



message10  = u"Bárbaro!! Hemos llegado a la última tarea.\n"\
			  u"Como ya debés haber deducido, esta última tarea consiste seguir dándole la mayor atención a las flechas, pero que ahora"\
			  u" aparecerán del lado izquierdo de la pantalla, a través de la pulsación de las teclas 'A' y 'D' dependiendo de qué flecha aparezca"\
			  u" Recordá que NO queremos que dejes de seguir el ritmo del círculo, continúa aprentado 'Enter'"\
 			  u" ¡ ES MUY IMPORTANTE QUE REVISES LA POSICIÓN DE TUS MANOS !"   + "\n\n\n" + startMessage






messages = [message1,message2,message3,message4,message5,message6,message7,message8,message9,message10]

