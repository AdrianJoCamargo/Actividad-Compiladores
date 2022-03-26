'''hay que validar que hayan alfabetos antes de poder hacer 
union, interseccion y demas'''

from array import array
from asyncio.windows_events import NULL
from pickle import TRUE
from alfabeto import Alfabeto
from lenguaje import Lenguaje
import random
alfabeto1=''
alfabeto2=''
palabras=''
palabras2=''

lenguaje1=''
lenguaje2=''

   

   

def crearAlfabetos():
    global alfabeto1
    global alfabeto2
    alfabeto1=Alfabeto()
    alfabeto2=Alfabeto()
    global palabras
    global palabras2

    palabras=input('digite las palabras que conformaran el primer Alfabeto: ')
    palabras2=input('digite las palabras que conformaran el Alfabeto#2: ')

    '''el esplit se encarga de separar por espacios 
    las palabras que ingresemos, y las guarda como en una lista'''
    palabras=palabras.split(' ')
    palabras2=palabras2.split(' ')
    
    

def unionAlfabetos():
    print('UNION:')
    print(alfabeto1.union(palabras,palabras2))


def diferenciaAlfabetos():
    while True:
            
        print('elija una opción: ')
        print('1.A diferencia de B: ')
        print('2.B diferencia de A:')
        print('3.Atras' )
        eleccion=int(input())

        if(eleccion==1):
            print('DIFERENCIA:')
            print(alfabeto1.diferencia(palabras,palabras2))
        if(eleccion==2):    
            print('DIFERENCIA:')
            print(alfabeto1.diferencia(palabras2,palabras))
        if(eleccion==3):
            break


def interseccionAlfabetos():
    print('interseccion:')
    if(len(alfabeto1.interseccion(palabras,palabras2))):
        print(alfabeto1.interseccion(palabras,palabras2))
    else:
        print('no hay elementos comunes entre los 2 alfabetos')


def menuCerraduraDeEstrella(alfabeto,palabras):
    
        Npalabras=int(input('digite el numero de palabras que se generaran: '))
        caracterMax=int(input('digite el numero de caracteres maximo que podrá tener cada palabra'))
        print('cerradura de estrella: ')
        array=alfabeto.cerraduraDeEstrella(palabras,Npalabras,caracterMax)
        print(array)
        array.clear()
    
        

def cerraduraDeestrellaAlfabeto():

    while True:
        print('elija a que alfabeto le quiere aplicar la cerradura de estrella: ')
        print('1. Alfabeto A=',palabras)
        print('2. Alfabeto B=',palabras2)
        print('3.Atras')
        opc=int(input())


        if(opc==1):
            menuCerraduraDeEstrella(alfabeto1,palabras)
            
        if(opc==2):
            menuCerraduraDeEstrella(alfabeto2,palabras2)
        if(opc==3):
            break







def generarLenguajes(palabras):
    
   
    global lenguaje1
    global lenguaje2
 
    Npalabras=int(input('digite el numero de palabras que tendrán los lenguajes: '))
    caracterMax=int(input('digite el numero maximo de caracteres que podrá tener cada palabra'))
    
    lenguaje1=Lenguaje(palabras,Npalabras,caracterMax)
    lenguaje2=Lenguaje(palabras,Npalabras,caracterMax)

    ' mostrarLenguajes()'
    
 


def menuDeLenguaje():
     while True:
        print('elija a que alfabeto con el que quiere crear los 2 lenguajes: ')
        print('1. Alfabeto A=',palabras)
        print('2. Alfabeto B=',palabras2)
        print('3.Atras')
        
        opc=int(input())
        if(opc==1):
            generarLenguajes(palabras)
            
        if(opc==2):
            generarLenguajes(palabras2)
        if(opc==3):
            break

def mostrarLenguajes():
    print(lenguaje1.getPalabrasDelLenguaje())
    print(lenguaje2.getPalabrasDelLenguaje())

def unionDeLenguajes():
    mostrarLenguajes()
    print('->>>>>>>>>>>>>>>>>>><',lenguaje1.union(lenguaje2))

def menuInversa():
    
    print('a que lenguaje desea calcularle la inversa:')
    print('1.A=',lenguaje1.getPalabrasDelLenguaje())
    print('2.B=',lenguaje2.getPalabrasDelLenguaje())
    print('3.atras')
        

def inversaLenguaje():
    while TRUE:
       
        menuInversa()
        opc=int(input())
        
        if(opc==1):
            print('inversa del lenguaje A: ',lenguaje1.inversa())
        if(opc==2):
            print('inversa del lenguaje B: ',lenguaje2.inversa())
        if(opc==3):
            break
        print('\n')
   
def menuDiferenciaDeLenguajes():
    print('lenguaje A=',lenguaje1.getPalabrasDelLenguaje())
    print('lenguaje B=',lenguaje2.getPalabrasDelLenguaje())
    print('1.diferencia de A-B')
    print('2.diferencia de B-A')
    print('3.atras')
    print('\n')
def diferenciaDeLenguajes():
    while True:
        menuDiferenciaDeLenguajes()
        opc=int(input())
        if(opc==1):
           print('diferencia A-B:') 
           diferencia=lenguaje1.diferencia(lenguaje1.getPalabrasDelLenguaje(),lenguaje2.getPalabrasDelLenguaje())
        if(opc==2):
            print('diferencia B-A:') 
            diferencia=lenguaje2.diferencia(lenguaje2.getPalabrasDelLenguaje(),lenguaje1.getPalabrasDelLenguaje())
    
        if (opc==3):
            break
        print(diferencia)
    

def imprimirOpcionesDeLenguajeDeMenu():
    print('1.calcular la Union entre lenguajes')
    print('2.Calcular la diferencia entre lenguajes')
    print('3.Calcular la intersección entre lenguajes')
    print('4.Calcular la concatenación entre lenguajes')
    print('5.Calcular la potencia de un lenguaje. El usuario determinará la potencia del lenguaje. ')
    print('6.Calcular la inversa de un lenguaje')
    print('7.Calcular la cardinalidad de un lenguaje.')
    print('8.atras')

def opcionesDeLenguajeMenu():
    while True:
        imprimirOpcionesDeLenguajeDeMenu()
        opc=int(input())
        if(opc==1):
            unionDeLenguajes()
        if(opc==2):
            diferenciaDeLenguajes()
        if(opc==6):
            inversaLenguaje()
        if(opc==8):
            break


def mostrarMenu():
    print('menu')
    print('elija el numero dependiendo de lo que desea hacer: ')
    print('1.ingresar los alfabetos')
    print('2.realizar la union de los alfabetos')
    print('3.realizar la diferencia de los alfabetos')
    print('4.realizar la interseccion de los alfabetos')
    print('5.realizar cerradura de estrella')
    print('6.Generar el lenguaje')
    print('7.opciones de lenguaje: ')
    print('8.salir')
    
    return int(input())

def menu():
    
    while True:
        opc=mostrarMenu()
        if (opc==1):
            crearAlfabetos()
        if(opc==2):
            unionAlfabetos()
        if(opc==3):
            diferenciaAlfabetos()
        if(opc==4):
            interseccionAlfabetos()
        if(opc==5):
            cerraduraDeestrellaAlfabeto()
        if(opc==6):
            menuDeLenguaje()
        if(opc==7):
            opcionesDeLenguajeMenu()
        if(opc==8):
            break
       

class main():

    menu()    
    




