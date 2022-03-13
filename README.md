<h1 align="center">Ejercicios de Ordenar</h1>
<p>Para realizar esta actividad he utilizado la herramienta <a href="https://replit.com/">Replit</a></p>
<p></p>
<p>El link del repositorio es el siguiente: <a href="https://github.com/mat0ta/ejercicios-ordenar/">ejercicios-ordenar</a></p>

***

<h2>Ejercicio 1. Ordenación por inserción dicotómica</h2>

Sea t una tabla de una sola línea (vector) de elementos de un tipo T que derivan de COMPARABLE, y que hay que ordenar en orden creciente. Cada elemento está insertado en su lugar dentro del resultado que se ha de obtener buscando su posición de inserción mediante el algoritmo dicotomía estudiado en el capítulo «Iteración».
La función empleada para crear dicho algoritmo es la siguiente:

```py
lista = [16, 36, 94, 103, 52, 2, 41, 77, 8, 10]
len_lista = len(lista)
lista_ordenada = []
pasos = 1

def ordenar():
  global pasos
  if len(lista_ordenada) == 0:
    lista_ordenada.append(min(lista))
    lista_ordenada.append(max(lista))
    lista.remove(max(lista))
    lista.remove(min(lista))
    ordenar()
  if len(lista_ordenada) == len_lista:
    print(lista_ordenada)
    return
  if len(lista) == 1:
    lista_ordenada.insert(len(lista_ordenada) // 2, lista[0])
    print(lista_ordenada)
    return
  lista_ordenada.insert(len(lista_ordenada) // 2, min(lista))
  lista_ordenada.insert(-(len(lista_ordenada) // 2), max(lista))
  lista.remove(max(lista))
  lista.remove(min(lista))
  if len(lista_ordenada) < len_lista:
    ordenar() 
    return

ordenar()
```

<h2>Ejercicio 2. Una ordenación topológica</h2>

Consideramos n tareas t1, t2… tn sometidas a las restricciones anteriores. Es decir, hay que terminar algunas tareas antes de poder empezar otras. Así, por ejemplo, primero tenemos que preparar los cimientos de una casa antes de montar las paredes y los tabiques. En el ejercicio siguiente se propone calcular una ordenación de tareas sometidas a restricciones de prioridad.
La función empleada para crear dicho algoritmo es la siguiente:

```py
import numpy

numeros = [[3,5], [7,20], [9,16], [1,6], [2, 4], [11, 8]]
solo_numeros = numpy.concatenate(numeros)
numeros_ordenados = []
prioridades = []
comparativa = 0

while comparativa != max(solo_numeros):
  for i in range(len(numeros)):
    if numeros[i][0] > numeros[i][1]:
      if numeros[i][0] - numeros[i][1] == comparativa:
        prioridades.append(i)
    else: 
      if numeros[i][1] - numeros[i][0] == comparativa:
        prioridades.append(i)
  comparativa = comparativa + 1

comparativa = 0

while len(numeros_ordenados) < len(solo_numeros):
  temp_list = []
  for i in range(len(prioridades)):
    if len(numeros[prioridades[i]]) == 2:
      temp_list.append(numeros[prioridades[i]][0])
      temp_list.append(numeros[prioridades[i]][1])
    elif len(numeros[prioridades[i]]) == 1:
      temp_list.append(numeros[prioridades[i]][0])
  for i in range(len(prioridades)):
    if len(numeros[prioridades[i]]) == 1 or len(numeros[prioridades[i]]) == 2:
      if numeros[prioridades[i]][0] == min(temp_list):
        numeros_ordenados.append(min(temp_list))
        numeros[prioridades[i]].remove(min(temp_list))
      elif len(numeros[prioridades[i]]) == 2 and numeros[prioridades[i]][1] == min(temp_list):
        numeros_ordenados.append(min(temp_list))
        numeros[prioridades[i]].remove(min(temp_list))

print(numeros_ordenados)
```

<h2>Ejercicio 3. Completar las especificaciones</h2>

La sección «Algunos algoritmos simples» ha usado un predicado está_explorado que no se ha especificado completamente. En particular, hemos escrito: «cada componente de t\[inicio] está colocado después de la serie más grande de componentes de la que es el max». El ejercicio siguiente propone completar esta especificación. Es un problema difícil.
La función empleada para crear dicho algoritmo es la siguiente:

```py
import random

lista = []
lista_segmentada = []
h = 1
j_safe = 0
guardado = False

def completarEspecificaciones():
  global lista
  longitud = int(input('Introduce la longitud de la lista: '))
  for i in range(longitud):
    lista.append(random.randint(0, 50))
  print(lista)
  segmentar()

def segmentar():
  global lista,lista_segmentada,h,j_safe,guardado
  for j in range(len(lista)):
    print(j, j_safe, h)
    if guardado == False:
      j_safe = j
      guardado = True
    if lista[j_safe] > lista[h]:
      print('no añadido')
      h += 1
      continue
    else:
      print('añadido')
      lista_segmentada.append(lista[j_safe:h+1])
      guardado = False
  print(lista_segmentada)


completarEspecificaciones()
```
