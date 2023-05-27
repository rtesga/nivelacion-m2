#version 2
import numpy as np
import os
import time  # time es util para hacer una pausa entre las iteraciones para poder ver correctamente la evolucion del juego
#el juego de la vida es un juego de 0 jugadores
# representa celulas , una celula viva esta representada con el valor 1 y una celula muerta se representa con el valor 0
# el juego representa una matrix de celula de tamamo size_y*size_x
# a cada iteracion del juego se genera una nueva matrix que depende del estado (matrix) anterior
# las reglas de generacion de la nueva matrix son las siguientes y depende de cada celula y sus vecinos
# *1 si una celula viva tiene 1 o menos celulas vecinas vivas, muere al siguiente turno por aburrimiento social
# *2 si una celula viva tiene 2 celulas vecinas vivas, vive en el siguiente turno
# *3 si una celula viva tiene 3 o mas vecinas vivas , muere en el situigente turno  por sobrepoblacion
# *4 si una celula muerta tiene 2 vecinos vivos , vive en el siguiente turno por reproduccion de los vecinos

size_x = 20
size_y = 20
iteraciones = 50  #vamos a jugar 50 iteraciones del juego y imprimir cada una
#Primero creamos una matrix aleatorioa de 0 y 1 con 50% de probabilidades
matrix = np.random.randint(0, 2, (size_y, size_x))
print(matrix)
print(matrix[1:4, 1:4])
#aqui definimos las iteraciones del juego
for iteracion in range(iteraciones):
  #creamos una matrix nueva vacias que vamos a llenar dependiendo de las celulas de la matrix en curso
  matrix_nueva = np.zeros((size_y, size_x))

  # recorremos la matrix por lienas y columnas con un ciclo anidadado( doble for)
  # ojo! evitamos los bordes para no salirse del rango de la matrix cuando bucamos los valores de los vecinos
  for linea in range(1, size_y - 1):
    for columna in range(1, size_x - 1):
      #tomamos los valores de los vecinos:
      #vecino_top_left = matrix[linea - 1, columna - 1]
      #vecino_top = matrix[linea - 1, columna ]
      #vecino_top_right = matrix[linea -1, columna + 1]
      #vecino_left = matrix[linea , columna - 1]
      #vecino_right = matrix[linea , columna + 1]
      #vecino_down_left = matrix[linea + 1, columna - 1]
      #vecino_down = matrix[linea + 1, columna]
      #vecino_down_right = matrix[linea + 1, columna  + 1]

      #Calculamos la cantidad de vecinos vivos
      #vecinos_vivos = vecino_top_left + vecino_top + vecino_left + vecino_right + vecino_down_left + vecino_down + vecino_down_right
      #Calcular los vecinos vivos se puede hacer en menos lineas ocupando las funciones de numpy
      #tomamos el sub array de 3x3 alrededor del pixel en curos
      sub_array = matrix[linea - 1:linea + 1 + 1, columna - 1:columna + 1 + 1]
      #calculamos la suma del sub array menos el valor del pixel central... y nos da la suma de los vecinos
      vecinos_vivos = np.sum(sub_array) - matrix[linea, columna]
      #en una sola linea seria vecinos_vivos = np.sum(matrix[linea-1:linea+1+1,columna-1: columna +1+1])-matrix[linea,columna]

      #regla 1 si una celula viva tiene 1 o menos celulas vecinas vivas, muere al siguiente turno por aburrimiento social
      #if matrix[linea,columna]== 1 and vecinos_vivos <2:
      #  matrix_nueva[linea,columna]=0
      #regla 2 si una celula viva tiene 2 celulas vecinas vivas, vive en el siguiente turno
      #elif matrix[linea,columna]== 1 and vecinos_vivos ==2:
      #  matrix_nueva[linea,columna]=1
      #regla 3 si una celula viva tiene 3 o mas vecinas vivas , muere en el situigente turno  por sobrepoblacion
      #elif matrix[linea,columna]== 1 and vecinos_vivos >2:
      #  matrix_nueva[linea,columna]=0
      #regla 4 si una celula muerta tiene 2 vecinos vivos , vive en el siguiente turno por reproduccion de los vecinos
      #elif matrix[linea,columna]== 0 and vecinos_vivos ==2:
      #  matrix_nueva[linea,columna]=1

      #las reglas se pueden simplificar a solo las celulas que tienen 2 vecinos vivos estan vivas al siguiente turno
      if (vecinos_vivos == 2):
        matrix_nueva[linea, columna] = 1

  #ahora que terminamos recorrer la matix y creamos la matix nueva, remplazamos la matrix por la nueva para la isguiente iteracion
  matrix = matrix_nueva
  #imprimimos la matrix
  os.system('clear')
  time.sleep(0.2)
  print(matrix)
  time.sleep(0.2)

#esperamos un poco  (0.2s) para poder ver la evolucionen pantalla sin que sea demasiado rapido
