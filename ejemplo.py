from asyncio.windows_events import NULL
from cmath import sin
import random
from xml.etree.ElementPath import prepare_parent 









class ejemplo():

    cadena=['ana','sex']
   
    aux2=''
    perra='peste'
    nc=''
    
    aux=0
    
    
    

    while aux<2:
        nc=len(cadena[aux])
        while nc>=1:
            print('->',+aux)
            lista=list(cadena[aux][nc-1])
            aux2=aux2+str(lista)
            nc-=1
        aux+=1

        print(aux2)





        
        
        


    '''
     ''  palabras=input('digite las palabras que conformaran el Alfabeto: ')
    palabras=palabras.split(' ')
    CerrEstrella=[] 
    Npalabras=input('digite el numero de palabras que se generaran: ')
    caracterMax=int(input('digite el numero de caracteres maximo que podrá tener cada palabra'))
    tamaño=len(palabras)
    
    tamañoArray=int(len(palabras))
    guardar=''
    vaciar=""
    for i in range(0,int(Npalabras)):
        
            
        
        for z in range(1,random.randint(1,caracterMax)):
            guardar+=palabras[random.randint(0,tamañoArray-1)]

        
        CerrEstrella.insert(i+1,guardar)
        guardar=''
        


    sinRepetidos=set(CerrEstrella)
    sinRepetidos=list(sinRepetidos)
    sinRepetidos.insert(0,chr(955))

    print(sinRepetidos)
    print('-------------------------------------------Repetidos')
    print('repetidos: ',CerrEstrella)      
    -------------------------------------------------------------------
     palabras=input('digite las palabras que conformaran el Alfabeto: ')
    ArrayPalabras=[]
    palabras2=input('digite las palabras que conformaran el Alfabeto#2: ')
    ArrayPalabras2=[]

    conjunto1=set(palabras.split(' '))
    conjunto2=set(palabras2.split(' '))

    print('la union entre A y B es: ',conjunto1|conjunto2)
    '''
'''

    for zz in range(0,len(palabras.split(' '))):
        ArrayPalabras.insert(zz,palabras.split(' ')[zz])

    for xx in range(0,len(ArrayPalabras)):
        print('->>>>>>>>>>>>>>>>>>>><',ArrayPalabras[xx])




'''

