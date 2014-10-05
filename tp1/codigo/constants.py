# coding=utf-8

import os

working_directory = os.getcwd()

#data structure
dual_tasks_TF = ["D", "DT", "DA"]
dual_tasks_AF = ["D", "DA", "DT"]

#Images path's:
result_path = working_directory + '/../resultados/{}.data'
circle_image_path = working_directory+'/../imagenes/circle.png'
arrow_image_path = working_directory+'/../imagenes/arrow.png'
line_image_path = working_directory+'/../imagenes/line.png'
enter_image_path = working_directory+'/../imagenes/enter.jpg'
space_image_path = working_directory+'/../imagenes/space.jpg'
arrows_image_path = working_directory+'/../imagenes/arrows.jpeg'
ad_image_path = working_directory+'/../imagenes/ad.jpg'


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





startMessage = u"\n ¿Estás listo? Presioná Enter cuando lo estés para comenzar con el siguiente experimento"


presentationMessage =   u"Muchas gracias por colaborar para nuestro proyecto.\n\n" \
						u"El siguiente experimento está compuesto de 5 niveles distintos donde se realizarán distintas tareas, primero con una mano"\
						u" y luego con la otra. Cada nivel tendrá su explicación previa. El tiempo de duración del experimento es aproximadamente"\
						u" entre 5 y 8 minutos. Si bien es totalmente anónimo, al finalizar te asignaremos un número. Estaremos dando premios para los que"\
						u" mejor resultados obtengan, por lo tanto este número será tu identificador. En el caso que aún ganando un premio quieras"\
						u" conservar el anonimato, simplemente ignorá nuestro llamado al ganador. \n\n\n" + startMessage

endMessage = u"Finalizado"




def goodbyeMessage(id):
	return  u"¡Muy bien! terminaste con el experimento. Tu identificador para recibir premios es %(ID)i .\n" \
			u"Muchas gracias por tu colaboración.\n\n\n"\
			u"Abrevaya Sofía\n"\
			u"Artuso Pablo\n"\
			u"Belloli Laouen\n" % {'ID':id}





message1 = u"Arranquemos con el primer nivel.\n"\
			u"En la parte central de la pantalla se va a proyectar un círculo de color negro intermitentemente. Tu tarea, en este nivel, consiste en"\
			u" apretar con la mano derecha la tecla 'Enter' cada vez que aparezca dicho círculo en la pantalla, intentando ir al mismo"\
			u" ritmo que este.\n\n"\
			u"Teclas a utilizar: \n"\
			u"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Mano Derecha \n\n\n\n\n\n"\
			"\n\n\n" + startMessage

	
message2 = u"¡Perfecto! La consigna para esta tarea es similar a la anterior. La diferencias son dos:\n"\
			u"- Vas a utilizar la mano izquierda en lugar de la derecha\n"\
			u"- Vas a apretar la tecla 'Barra espaciadora' en lugar de 'Enter'\n\n"\
			u"Teclas a utilizar: \n"\
			u"Mano izquierda \n\n\n\n\n\n"\
			"\n\n\n" + startMessage

message3 = u"¡Bien! Pasamos al segundo nivel.\n"\
			u"Este nivel es muy parecido al primero. Ahora en vez de aparecer un circulo negro, va a aparecer"\
			u"una flecha que puede apuntar o bien hacia la derecha o bien hacia la izquierda.\n"\
			u"Tu tarea nuevamente consiste en apretar con tu mano derecha la tecla 'flecha izquierda' (-dibujo-) o 'flecha derecha' (-dibujo-)"\
			u" dependiendo cual de ellas aparezca en la pantalla, intentando ir al mismo ritmo que las flechas\n\n"\
			u"Teclas a utilizar: \n"\
			u"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Mano Derecha \n\n\n\n\n\n"\
			"\n\n\n" + startMessage


message4 = u"¡Bárbaro! Como bien hicimos entre el primero y el segundo experimento, ahora vamos a cambiar de mano. La consigna se mantiene (se apreta"\
			u" la flecha correspondiente proyectada en pantalla). Dado que la mano que vas a usar es la izquierda, las teclas que vas a utilizar son:\n"\
			u"- 'A' cuando aparezca la flecha que apunta hacia la izquierda.\n"\
			u"- 'D' cuando aparezca la flecha que apunta hacia la derecha.\n\n"\
			u"Teclas a utilizar: \n"\
			u"Mano izquierda \n\n\n\n\n\n"\
			"\n\n\n" + startMessage



message5 = u"¡Perfecto! Llegamos al nivel 3.\n"\
			u"En este nivel vamos a combinar las dos tareas que veníamos realizando en los niveles anteriores. La pantalla va a estar dividida"\
			u" a la mitad por una raya vertical de color negro. Del lado izquierdo de ésta aparecerá el círculo, mientras que del derecho"\
			u" aparecerán las flechas. Tu tarea esta vez es apretar con la mano izquierda la 'Barra espaciadora' (-dibujo-) cada vez que el"\
			u" círculo aparece y con la mano derecha la 'flecha izquierda' o 'flecha derecha' (-dibujos-) (dependiendo de la dirección a la cual apunte)"\
			u" cada vez que alguna de éstas aparezca.\n\n"\
			u"Teclas a utilizar: \n"\
			u"Mano izquierda \t\t\t\t\t\t Mano Derecha \n\n\n\n\n\n"\
			"\n\n\n" + startMessage



message6 = u"Vamos muy bien.\n"\
			u"Ahora para no perder el hilo conductor, vamos a cambiar las manos de lugar. La mano derecha será la encarga de seguir el ritmo del"\
			u" círculo (que ahora aparecerá del lado derecho de la raya) presionando la tecla 'Enter'. Mientras que con las teclas 'A' y 'D'"\
			u" vas a tratar de seguirle el ritmo y la dirección a las flechas que serán expuestas del lado izquierdo de la raya.\n\n"\
			u"Teclas a utilizar: \n"\
			u"Mano izquierda \t\t\t\t\t\t Mano Derecha \n\n\n\n\n\n"\
			"\n\n\n" + startMessage


message7 = u"¡Muy bien! Nivel 4."\
			u"En este nivel vamos a repetir lo que hiciste en el nivel 3. Es decir, el círculo y las flechas volverán a aparecer del"\
			u" lado izquierdo y derecho de la pantalla respectivamente y tratarás de seguirles el ritmo apretando la 'Barra espaciadora' o las "\
			u" flechas depende de lo que corresponda. La diferencia es que esta vez queremos que enfoques tu concentración"\
			u" en el círculo. Esto NO quiere decir que dejes de seguir el ritmo de las flechas. Simplemente nuestra prioridad es que trates de"\
			u" que no se te escape ningún círculo sin apretar la 'Barra espaciadora'.\n\n"\
			u"Teclas a utilizar: \n"\
			u"Mano izquierda \t\t\t\t\t\t Mano Derecha \n\n\n\n\n\n"\
			"\n\n\n" + startMessage


message8 = u"¡Bien!\n"\
			u"Nuevamente hagamos este ejercicio cambiando las teclas que vamos a presionar. Dado que el círculo estará de la derecha, tratarás"\
			u" de seguirle el ritmo presionando la tecla 'Enter', mientras que para las flechas utilizarás la mano izquierda y las telcas 'A' y 'D'."\
			u" No te olvides que el círculo es lo que más nos interesa.\n\n"\
			u"Teclas a utilizar: \n"\
			u"Mano izquierda \t\t\t\t\t\t Mano Derecha \n\n\n\n\n\n"\
			"\n\n\n" + startMessage


message9 = u"¡Excelente! Nivel 5, el último.\n"\
			u"Al igual que hiciste en el anterior nivel, en donde pusiste tu mayor concentración en el círculo negro, ahora queremos que lo hagas"\
			u" sobre las flechas. Comenzando con la mano izquierda sobre la 'Barra espaciadora' para llevar el ritmo del círculo, y la mano derecha"\
			u" sobre las flechas para seguir el ritmo de ellas. Acordate que nos interesa que le presten mucha atención a las flechas.\n\n"\
			u"Teclas a utilizar: \n"\
			u"Mano izquierda \t\t\t\t\t\t Mano Derecha \n\n\n\n\n\n"\
			"\n\n\n" + startMessage


message10  = u"¡Bárbaro! Hemos llegado a la última tarea.\n"\
			  u"Como ya debés haber deducido, esta última tarea consiste seguir dándole la mayor atención a las flechas, pero que ahora"\
			  u" aparecerán del lado izquierdo de la pantalla, a través de la pulsación de las teclas 'A' y 'D' dependiendo de qué flecha aparezca"\
			  u" Recordá que NO queremos que dejes de seguir el ritmo del círculo, continúa aprentado 'Enter'\n\n"\
			u"Teclas a utilizar: \n"\
			u"Mano izquierda \t\t\t\t\t\t Mano Derecha \n\n\n\n\n\n"\
			"\n\n\n" + startMessage





messagesCEF = [message1,message2,message3,message4,message5,message6,message7,message8,message9,message10]
messagesAEF = [message1,message2,message3,message4,message5,message6,message9,message10,message7,message8]

