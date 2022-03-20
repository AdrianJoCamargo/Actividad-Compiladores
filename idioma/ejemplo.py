 
class ejemplo():



    palabras=input('digite las palabras que conformaran el Alfabeto: ')
    ArrayPalabras=[]
    palabras2=input('digite las palabras que conformaran el Alfabeto#2: ')
    ArrayPalabras2=[]

    conjunto1=set(palabras.split(' '))
    conjunto2=set(palabras2.split(' '))

    print('la union entre A y B es: ',conjunto1|conjunto2)
    
'''

    for zz in range(0,len(palabras.split(' '))):
        ArrayPalabras.insert(zz,palabras.split(' ')[zz])

    for xx in range(0,len(ArrayPalabras)):
        print('->>>>>>>>>>>>>>>>>>>><',ArrayPalabras[xx])




'''

