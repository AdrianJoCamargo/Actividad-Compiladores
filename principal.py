'''hay que validar que hayan alfabetos antes de poder hacer 
union, interseccion y demas'''

from array import array
from asyncio.windows_events import NULL
from alfabeto import Alfabeto
from lenguaje import Lenguaje
import random
alfabeto1=''
alfabeto2=''
palabras=''
palabras2=''
palabraLeng=[]
'''def añadirPalabrasAlAlfabeto(palabras,palabras2,alfabeto1,alfabeto2):'''
lenguajes=[]
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


def generarPalabrasLenguaje(palabras,anterior,caracteresMax,auxP):
    global palabraLeng
    if(caracteresMax==0):
            
        if anterior in palabraLeng :
            caracteresMax=auxP
            generarPalabrasLenguaje(palabras,"",caracteresMax,auxP)
        else:
            palabraLeng.insert(0,anterior)
        
    else:
        aleatorio=random.randint(0,len(palabras)-1)
        generarPalabrasLenguaje(palabras,anterior+palabras[aleatorio],caracteresMax-1,auxP)


def ponerLandaLenguaje():
    palabraLeng.insert(0,chr(955))

def generarLenguajes(palabras):
    
    global palabraLeng
    global lenguaje1
    global lenguaje2
    global lenguajes
    Npalabras=int(input('digite el numero de palabras que tendrán los lenguajes: '))
    caracterMax=int(input('digite el numero maximo de caracteres que podrá tener cada palabra'))
    
    for zz in range(0,2):
        palabraLeng=[]    
        for i in range(0,Npalabras):

            aleatorio=random.randint(1,caracterMax-1)
            generarPalabrasLenguaje(palabras,"",aleatorio,caracterMax)
    
        ponerLandaLenguaje()
        lenguajes.insert(zz,palabraLeng)
    
    'para acceder a el lenguaje 1=lenguajes[0] y para el lenguaje 2 es: lenguajes[2]'
    lenguaje1=Lenguaje()
    lenguaje2=Lenguaje()


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
    print(lenguajes[0])
    print(lenguajes[1])

def unionDeLenguajes():
    mostrarLenguajes()
    print('->>>>>>>>>>>>>>>>>>><',lenguaje1.union(lenguajes[0],lenguajes[1]))

def menuInversa():
    print('a que lenguaje desea calcularle la inversa:')
    print('1.A=',lenguaje1)
    print('2.B=',lenguaje2)

def inversaLenguaje():
    menuInversa()
    opc=input()
    while True:
        if(opc==1):
            print(lenguaje1.inversa())
        
        

    
    



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
    




