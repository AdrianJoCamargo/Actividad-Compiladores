'''hay que validar que hayan alfabetos antes de poder hacer 
union, interseccion y demas'''

from alfabeto import Alfabeto
alfabeto1=''
alfabeto2=''
palabras=''
palabras2=''
'''def añadirPalabrasAlAlfabeto(palabras,palabras2,alfabeto1,alfabeto2):'''
   

   

   

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
    
    
def mostrarMenu():
    print('menu')
    print('elija el numero dependiendo de lo que desea hacer: ')
    print('1.ingresar los alfabetos')
    print('2.realizar la union de los alfabetos')
    print('3.realizar la diferencia de los alfabetos')
    print('4.realizar la interseccion de los alfabetos')
    print('5.salir')
    
    return int(input())

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
            break
       
        
        

class main():

    menu()    
    



