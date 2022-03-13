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