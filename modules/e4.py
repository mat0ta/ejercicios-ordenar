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