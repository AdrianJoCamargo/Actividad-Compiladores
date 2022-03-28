
from array import array



from idioma import Idioma
import random
class Lenguaje(Idioma):
    
    '''def __init__(self,palabras,Npalabras,caracterMax):
        self.palabras=palabras
        self.Npalabras=Npalabras
        self.caracterMax=caracterMax
        self.palabraLeng=[]
        self.resultadoPotencia=[]
        

        for i in range(0,Npalabras):
            if(caracterMax>1):
                aleatorio=random.randint(1,caracterMax-1)
                
            else:
                aleatorio=random.randint(1,caracterMax)

            self.generarPalabrasLenguaje(palabras,"",aleatorio,caracterMax)
        self.__ponerLanda__()'''

    def __init__(self):
        self.palabraLeng=[]
        self.resultadoPotencia=[]
        self.contadorUniversal=0
        self.palabraLeng.insert(0,'ab')
        self.palabraLeng.insert(1,'ac')
      
    def __ponerLanda__(self):
        self.palabraLeng.insert(0,chr(955))
        

    
        


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
        aux=self.getPalabrasDelLenguajeSinLanda()
        aux2=lenguaje2.getPalabrasDelLenguajeSinLanda()
        conjunto1=set(aux)
        conjunto2=set(aux2)
        resultado=((conjunto1 | conjunto2))
        resultado.add(chr(955))
        
        return resultado

    def getPalabrasDelLenguaje(self):
        return self.palabraLeng


    def getPalabrasDelLenguajeSinLanda(self):
        aux=0
        sinLanda=[]
        'para eliminar el landa hay que poner el rango en 1'
        for xx in range(0,len(self.palabraLeng)):
            sinLanda.insert(aux,self.palabraLeng[xx])
            aux+=1
        return sinLanda
    


    'preguntar si hay que colocar el landa en la concatenacion'
    def concatenacion(self,lenguaje2):
        array=[]
        cont=0
        obtenerArray=lenguaje2.getPalabrasDelLenguajeSinLanda()
        for i in range(1,len(self.getPalabrasDelLenguaje())):
            
            aux=self.palabraLeng[i]
            size=len(obtenerArray)
            
            for x in range(0,size):
                aux2=aux+obtenerArray[x]
                array.insert(cont,aux2)
                cont+=1
            
        return array

    def __ponerPrimeros__(self):
        cont=0
        for i in self.palabraLeng:
            self.resultadoPotencia.insert(cont,i)
            cont+=1
        

    
    ' palabra=AB,Npotencia=2,indice=0'
    
                                                   
    '''def __potenciaRecursiva__(self,anterior,palabras,indice,cont,potencia,aux):
        Npalabras=pow(len(palabras),potencia)
        if(self.contadorUniversal<Npalabras):
            array=self.getPalabrasDelLenguajeSinLanda()
            if(cont==potencia):
                '=["AB",AC'
                'cont=2  ultimo=0 aux=1  indice=1 potencia=2 anterior=ABAC'
                
                self.resultadoPotencia.insert(aux,anterior)
                self.contadorUniversal+=1
                anterior=array[indice] 
                ultimo=indice   
                aux+=1
                cont=0
                indice+=1
                if(self.contadorUniversal==Npalabras-1):
                    self.__potenciaRecursiva__(array[len(array)-1],palabras,indice,cont+1,potencia,aux)
                else:
                    self.__potenciaRecursiva__(anterior,palabras,indice,cont+1,potencia,aux)
            
           

            if(indice==len(array)):
                indice=0
                self.__potenciaRecursiva__(anterior+array[indice],palabras,indice,cont+1,potencia,aux)
            else:
                self.__potenciaRecursiva__(anterior+array[indice],palabras,indice,cont+1,potencia,aux)
        
                

      '''
    'resultadoPotencia=AB,AC'
    'anterior=AB   Npalabras=2 contador=0 Ncaracteres=0 aux=1 contador2=0'
    def __potenciaRecursiva__(self,anterior,palabras,Npalabras,contador,Ncaracteres,aux,contador2):
        if(Npalabras!=0):
            if(Ncaracteres==0):
                self.resultadoPotencia.insert(contador,anterior)
                Ncaracteres=aux
                self.__potenciaRecursiva__("",palabras,Npalabras-1,contador+1,Ncaracteres,aux,contador2+1)
            else:
                
                self.__potenciaRecursiva__(anterior+palabras[contador2],palabras,Npalabras,contador,Ncaracteres-1,aux,contador2)
            

    def __calcNpalabras__(self,Npotencia,palabras):
        return pow(len(palabras),Npotencia)

    def potencia(self,Npotencia):
        
        if(not Npotencia==0):
            ''' self.__ponerPrimeros__()'''
            palabras=self.getPalabrasDelLenguajeSinLanda()
            print('sin landa:',palabras)
            'Npalabras es el numero de palabras que se generaran'
            
    

            for xx in range(0,Npotencia):
                print(xx+1)
                Npalabras=self.__calcNpalabras__(xx+1,palabras)
                
                self.__potenciaRecursiva__("",palabras,Npalabras,0,xx,xx,0)


        '''else:
            self.resultadoPotencia.insert(0,chr(955))'''
            

        return self.resultadoPotencia
    
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
    

    def cardinalidad(self):

        return len(self.getPalabrasDelLenguaje())







l1=Lenguaje()
print('lenguaje1=',l1.getPalabrasDelLenguaje())
print('potencia:')
print(l1.potencia(3))

'''palabra='A','B','C'
palabra2='er','o','imos'
l1=Lenguaje(palabra,3,1)
lenguaje=Lenguaje(palabra2,3,1)
print('lenguaje1=',l1.getPalabrasDelLenguaje())
print('potencia:')
print(l1.potencia(2))
'''
'''print('lenguaje1=',l1.getPalabrasDelLenguaje())
print('lenguaje2=',lenguaje.getPalabrasDelLenguaje())
print('union:',l1.union(lenguaje))'''
'''print('lenguaje1=',l1.getPalabrasDelLenguaje())
    print('lenguaje2=',lenguaje.getPalabrasDelLenguaje())
    print(l1.concatenacion(lenguaje))
'''
