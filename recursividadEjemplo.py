import random 


arrayPalabras=[]
def estaRepetido(alfabeto,cadena):
    aux=False
    for z in alfabeto:
        if(z==cadena):
            aux=True
        break

    return aux        


def unirCaracteresCE(alfabeto,anterior,caracterMax):
    if(caracterMax==0):
        arrayPalabras.insert(0,anterior)

    else:
        
        aleatorio=random.randint(0,len(alfabeto)-1)
        
        unirCaracteresCE(alfabeto,anterior+alfabeto[aleatorio],caracterMax-1)

def generarPalabras(alfabeto,Npalabras,caracterMax):

    for i in range(0,Npalabras):
        aleatorio=random.randint(1,caracterMax)
        unirCaracteresCE(alfabeto,"",aleatorio)



class  cerraduraKleene():
    
    palabras=input('digite las palabras que conformaran el Alfabeto: ')
    palabras=palabras.split(' ')
    CerrEstrella=[]
    Npalabras=input('digite el numero de palabras que se generaran: ')
    caracterMax=int(input('digite el numero de caracteres maximo que podrá tener cada palabra'))
    tamaño=len(palabras)


    generarPalabras(palabras,int(Npalabras),caracterMax)

    for z in arrayPalabras:
    
        print('->>>>>>>>>><',z)
    