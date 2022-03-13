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