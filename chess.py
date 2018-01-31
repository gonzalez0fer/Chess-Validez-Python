#-------------------------------------------------------------------------------
#				,....,
#		      ,::::::<
#		    ,::/^\"``.
#		    ,::/, `   e`.
#			,::; |        '.
#			,::|  \___,-.  c) ####   #    #  ######   ####    ####
#			;::|     \   '-' #    #  #    #  #       #       #
#			;::|      \      #       ######  #####    ####    ####
#			;::|   _.=`\     #       #    #  #            #       #
#			`;:|.=` _.=`\    #    #  #    #  #       #    #  #    #
#			  '|_.=`   __\    ####   #    #  ######   ####    ####
#			   `\_..==`` /
# 				.'.___.-'.
#			   /          \
#			  ('--......--')
#			  /'--......--'\
#			  `"--......--"`
#
#--Fernando Gonzalez   carnet:08-10464
#--Bruno Colmenares    carnet:12-10551
#--Laboratorio de Algoritmos II
#--Grupo 9
#-------------------------------------------------------------------------------
import sys
import os


diccionario = {}

class Tablero:

	def __init__(self):
		self.tablero = [['#' for j in range (8)] for j in range (8)]

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

	def LOAD (self, archivo, nombre): #lee el archivo de la matriz y le 
	 								  #asigna nombre en un Diccionario
#	{Pre: archivo.contenido <> vacio and #archivo.contenido[i][j] = 8x8}

#
		file = open(archivo, "r")
		tableroTemporal = file.read().splitlines()
		self.tablero = []
		for line in tableroTemporal:
			self.tablero.append(list(line))
		diccionario[nombre] = self.tablero
		file.close()
#	{Post: Diccionario[nombre]= tablero(archivo.contenido)}

#
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

	def PRINT(self, nombre): #imprime el tablero
#	{Pre: nombre E Diccionario.claves}

#
		ESCRIBIR(archivo_salida, 'Tablero:' + ' ' + str(nombre))
		for i in range (0,8):
			ESCRIBIR(archivo_salida, ''.join(diccionario[nombre][i]))
		ESCRIBIR(archivo_salida, '--------')
#	{Post: archivo_salida.contenido ++ Diccionario[nombre]}
#
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

	def CHECK (self, origen, destino, nombre): #valida el movimiento de la pieza

#	{pre: origen/destino[i] E t.matriz[0<i<Max][j]  and origen/destino[j] E t.matriz[i][0<j<=Max] }

		orig = list(origen)
		dest = list(destino)  #convierto en listas origen y destino

		origcol = orig[0] #columna
		origfil = orig[1] #fila tomo elementos de las listas para posicionar
		destcolum = dest[0]#columna
		destfil= dest[1]#fila

		columnas = ['A','B','C','D','E','F','G','H']
		filas = ['8','7','6','5','4','3','2','1']
		
		for i in range(0,len(columnas)):

			if (columnas[i] == origcol):
				origencolumna = i

		for i in range(0,len(filas)):

			if (filas[i] == origfil):
				origenfila = i

		for i in range(0,len(columnas)): #columna destino

			if (columnas[i] == destcolum):
				destinocolumna = i

		for i in range(0,len(filas)): #fila destino

			if (filas[i] == destfil):
				destinofila = i


		if ((origcol in columnas) and (origfil in filas) and (destcolum in columnas) \
			and (destfil in filas) and (origenfila< 7) and (origenfila > 0)): 

			if (diccionario[nombre][origenfila][origencolumna] == 'P'):
				
				if (origenfila == 6 and (destinocolumna == origencolumna-2 \
					or destinocolumna == origencolumna+2)):
					return False

				elif (((origenfila == 6) and (destinofila == 4) and \
					(diccionario[nombre][5][destinocolumna] == '#') \
					and (diccionario[nombre][4][destinocolumna] == '#')) 
					or (origenfila == 6 and (destinofila == 5) and\
					 (diccionario[nombre][5][destinocolumna] =='#')) ):

					return True

				elif (origenfila != 6) and (destinofila != origenfila - 1):				
					return False 

				elif (origenfila != 6) and ((destinocolumna == origencolumna +1)\
				 or (destinocolumna == origencolumna -1)):
					if (diccionario[nombre][destinofila][destinocolumna]) == 'p':
						return True

					else:						
						return False 

				elif (origenfila != 6) and (destinocolumna != origencolumna +1) \
				and (destinocolumna != origencolumna -1):
					if (diccionario[nombre][destinofila][destinocolumna]) == '#':						
						return True 

					else:	
						return False 
				else:
					return False 


			elif(diccionario[nombre][origenfila][origencolumna] == 'p'):

				if (origenfila == 1 and (destinocolumna == origencolumna-2 or \
					destinocolumna == origencolumna+2)):			
					return False

				elif (((origenfila == 1) and (destinofila == 3) and \
					((diccionario[nombre][2][destinocolumna] == '#') and \
						(diccionario[nombre][3][destinocolumna] == '#')))
					or (origenfila == 1 and (destinofila == 2) and \
						(diccionario[nombre][2][destinocolumna] == '#')) ):				
					return True 

				elif (origenfila != 1) and (destinofila != origenfila + 1):					
					return False 

				elif (origenfila != 1) and ((destinocolumna == origencolumna +1)\
				 or (destinocolumna == origencolumna -1)):
					if (diccionario[nombre][destinofila][destinocolumna]) == 'P':						
						return True

					else:						
						return False

				elif (origenfila != 1) and (destinocolumna != origencolumna +1) \
				and (destinocolumna != origencolumna -1):
					if (diccionario[nombre][destinofila][destinocolumna]) == '#':
						return True

					else:					
						return False

				else:					
					return False 


			elif(diccionario[nombre][origenfila][origencolumna]== '#'):			
				return False 

		else:
			return False

#	{Post: {post: caso blancas...respuesta==(%exists i,j | 0<i,j<=t.Max | 
#(((origen[i] == 6) and (destino[i] == 4)and(diccionario[nombre][5][j] == '#')
#and (diccionario[nombre][4][j] == '#')) or (origen[i] == 6 and (destino[i] == 5)
#and (diccionario[nombre][5][j] =='#') or (%exists i,j | 0<i,j<=t.Max | (origen[i] != 6) 
#and ((destino[j] == origen[j] +1) or (destino[j] == origen[j] -1)) 
#and(diccionario[nombre][destino[i]][destino[j]]) =='p' or 
#(%exists i,j | 0<i,j<=t.Max |  (origen[i] != 6) and (destino[j] != origen[j] +1) 
#and (destino[j] != origen[j] -1): and(diccionario[nombre][destino[i]][destino[j]]) == '#'
#analogamente caso negras}
 
 
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
 
	def MOVE (self, origen, destino, nombre): #mueve la pieza si check es valid

#	{pre: Check.respuesta == True}


		orig = list(origen)
		dest = list(destino)  #convierto en listas origen y destino

		origcol = orig[0] #columna
		origfil = orig[1] #fila -- tomo elementos de las listas para posicionar
		destcolum = dest[0]#columna
		destfil= dest[1]#fila

		columnas = ['A','B','C','D','E','F','G','H']
		filas = ['8','7','6','5','4','3','2','1']
		
		for i in range(0,len(columnas)):

			if (columnas[i] == origcol):
				origencolumna = i

		for i in range(0,len(filas)):

			if (filas[i] == origfil):
				origenfila = i

		for i in range(0,len(columnas)): #columna destino

			if (columnas[i] == destcolum):
				destinocolumna = i

		for i in range(0,len(filas)): #fila destino

			if (filas[i] == destfil):
				destinofila = i

		if ((origcol in columnas) and (origfil in filas) and \
			(destcolum in columnas) and (destfil in filas)):

			respuesta = self.CHECK(origen, destino, nombre)

			tablilla = diccionario[nombre]


			if (tablilla[origenfila][origencolumna] == 'P' and respuesta == True):

				tablilla[origenfila][origencolumna]='#'

				if (tablilla[destinofila][destinocolumna] == '#'):
					tablilla[destinofila][destinocolumna] ='P'

				elif (tablilla[destinofila][destinocolumna] == 'p'):
					tablilla[destinofila][destinocolumna]='P'

			elif (tablilla[origenfila][origencolumna] == 'p' and respuesta ==True):

				tablilla[origenfila][origencolumna]='#'

				if (tablilla[destinofila][destinocolumna] == '#'):
					tablilla[destinofila][destinocolumna]='p'
				elif (tablilla[destinofila][destinocolumna] == 'p'):
					tablilla[destinofila][destinocolumna]='p'
			else:
				pass

		else:

			ESCRIBIR(archivo_salida, 'INVALID')

# {post: Diccionario[nombre]= Diccionario0 [origen[i]>>destino[i]] [origen[j]>>destino[j]]}

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

	def CHECKTHREAT(self, jugador, nombre): #comprueba amenaza en blancas o negras

#	{Pre: (jugador = P  v  jugador = p) and %exist i: 0<i< #Diccionario :
#    Diccionario[i] = tab}

		if (jugador == 'P'):
			esta=False
			ciclo=False
			while ciclo==False:
				for i in range (7, 0, -1):
					for j in range (1, 7):

						if ((diccionario[nombre][i][j]== 'P') and \
							(diccionario[nombre][i-1][j+1] == 'p' or \
								diccionario[nombre][i-1][j-1] == 'p')):

							esta = True
							ciclo = True
							break
						if i==6 and j==6:
							ciclo=True
							break
						else:
							pass
	
			for i in range(7, 0, -1):
				if (((diccionario[nombre][i][0]== 'P') and \
					(diccionario[nombre][i-1][1] == 'p')) or \
				((diccionario[nombre][i][7]== 'P') and \
					(diccionario[nombre][i-1][6] == 'p'))):
					esta=True
					break
			if esta:
				ESCRIBIR(archivo_salida,'YES')
			else:
				ESCRIBIR(archivo_salida,'NO')

		elif (jugador == 'p'):
			esta=False
			ciclo=False
			while ciclo==False:
				for i in range (0, 7):
					for j in range (1, 7):
						if ((diccionario[nombre][i][j]== 'p') and \
							(diccionario[nombre][i+1][j+1] == 'P' or \
								diccionario[nombre][i+1][j-1] == 'P')):
							esta = True
							ciclo = True
							break
						if i==6 and j==6:
							ciclo=True
							break
						else:
							pass
	
			for i in range(6,-1,-1):
				if (((diccionario[nombre][i][0]== 'p') and \
					(diccionario[nombre][i-1][1] == 'P')) or \
				((diccionario[nombre][i][7]== 'p') and \
					(diccionario[nombre][i+1][6] == 'P'))):
					esta=True
					break
	
			if esta:
				ESCRIBIR(archivo_salida,'YES')
			else:
				ESCRIBIR(archivo_salida,'NO')

#	{Post: esta == (Diccionario[nombre][i][j]= P and Diccionario[nombre][i+1][j+1 o j-1] = P)) 
#or (Diccionario[nombre][i][j]= P and Diccionario[nombre][i-1][j+1 o j-1] = p) }
 
#

###############################################################################
#                                                                             #
#                            MAIN PROGRAM                                     #
#                                                                             #
###############################################################################

def LLAMADOS(tab, archivo_entrada, archivo_salida): #toma el archivo de entrada
                                                    #y llama las funciones
                                                    #asignando parametros

	arch = open(archivo_entrada,'r')
	linea = arch.readline()
	lista = linea.split()
	while (linea !=""):
		
		if lista != []:
			if (lista[0] == 'LOAD'):
				tab.LOAD(lista[1], lista[2])

			elif (lista[0] == 'CHECK' and lista[1]=='THREAT'):
				tab.CHECKTHREAT(lista[2], lista[3])

			elif (lista[0] == 'CHECK'):
				respuesta = (tab.CHECK(lista[1], lista[2], lista[3]))
				if respuesta == True:
					ESCRIBIR(archivo_salida,'VALID')
				else:
					ESCRIBIR(archivo_salida,'INVALID')

			elif (lista[0] == 'PRINT'):
				tab.PRINT(lista[1])

			elif (lista[0] == 'MOVE'):
				tab.MOVE (lista[1], lista[2], lista[3])
		linea = arch.readline()
		lista = linea.split()

def ESCRIBIR (archivo_salida,string): #hace la escritura del archivo de texto

	arch = open(archivo_salida,'a')
	arch.write(string + '\n')
	arch.close()

def parseArgs(args): #comprueba si se estan metiendo justamente 2 parametros 
                     #en el terminal.

    msg = "Error en la linea de comando:\nchess.py <arch_entrada> <arch_salida>"
    if len(args) != 3:
        print(msg)
        sys.exit(1)

    return str(args[1]), str(args[2])



if __name__=="__main__":

    archivo_entrada,archivo_salida = parseArgs(sys.argv)
    tab = Tablero()
    if os.path.exists(archivo_salida): #remueve el archivo por cada corrida
	    os.remove(archivo_salida)      #para que cree un archivo nuevo y no 
                                       #agregue lineas
    LLAMADOS(tab,archivo_entrada,archivo_salida)

