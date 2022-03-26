
from idioma import Idioma
import random
class Lenguaje(Idioma):
    def __init__(self,palabras,Npalabras,caracterMax):
        self.palabras=palabras
        self.Npalabras=Npalabras
        self.caracterMax=caracterMax
        self.palabraLeng=[]
        

        for i in range(0,Npalabras):
            if(caracterMax>1):
                aleatorio=random.randint(1,caracterMax-1)
                
            else:
                aleatorio=random.randint(1,caracterMax)

            self.generarPalabrasLenguaje(palabras,"",aleatorio,caracterMax)
       
      
        
      
        


    def generarPalabrasLenguaje(self,palabras,anterior,caracteresMax,auxP):
       
        if(caracteresMax==0):
                
            if anterior in self.palabraLeng:
                caracteresMax=auxP
                self.generarPalabrasLenguaje(palabras,"",caracteresMax,auxP)
            else:
                self.palabraLeng.insert(0,anterior)
            
        else:
            aleatorio=random.randint(0,len(palabras)-1)
            self.generarPalabrasLenguaje(palabras,anterior+palabras[aleatorio],caracteresMax-1,auxP)


    'aqui aplico el polimorfismo'
    def union(self,lenguaje2):
        conjunto1=set(self.palabraLeng)
        conjunto2=set(lenguaje2.getPalabrasDelLenguaje())
        return conjunto1 | conjunto2

    def getPalabrasDelLenguaje(self):
        return self.palabraLeng
    def concatenacion():
        return 0

    def potencia():
        return 0
    
    def inversa(self):
        aux=0
        inversa=[]
        Npalabras=len(self.palabraLeng)
        print(Npalabras)
        while aux<Npalabras:
            aux2=''
            nc=len(self.palabraLeng[aux])
            while nc>=1:
                print('->',+aux)
                lista=self.palabraLeng[aux][nc-1]
                aux2=aux2+lista
                nc-=1
            inversa.insert(aux,aux2)
            
            aux+=1

        'print(aux2)'
        return inversa
    

    def cardinalidad():
        return 0




'''palabra='aro','sala','acbd'
lenguaje=Lenguaje(palabra,3,1)
print(lenguaje.getPalabrasDelLenguaje())
print(lenguaje.inversa())
'''