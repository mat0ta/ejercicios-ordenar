import sys
sys.path.insert(1, './modules')
from modules import e1, e2, e3

array_ejercicios = {
  1: 'e4.ordenar()',
  2: 'e5.iniciar()',
  3: 'e6.completarEspecificaciones()',
}

if __name__ == "__main__":
  start = input('Bienvenido a la plataforma de ejercicios de ordenar. Por favor, introduzca el número del ejercicio que quiere probar (1 a 3) o introduzca 0 para salir: ')
  while int(start) >= 1 and int(start) <= 3:
    eval(str(array_ejercicios[int(start)]))
    start = input('Por favor, introduzca el número del ejercicio que quiere probar (1 a 3) o introduzca 0 para salir: ')