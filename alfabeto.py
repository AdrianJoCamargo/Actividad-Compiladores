from idioma import Idioma
import random

class Alfabeto(Idioma):
    
    def __init__(self):
        self.arrayCerraduraEstrella=[]
        self.auxP=0
    
    
    def  __unirCaracteresCE__(self,palabras,anterior,caracteresMax):

        
        if(caracteresMax==0):
            
            if anterior in self.arrayCerraduraEstrella:
                caracteresMax=self.auxP
                self.__unirCaracteresCE__(palabras,"",caracteresMax)
            else:
                self.arrayCerraduraEstrella.insert(0,anterior)
        
        else:
            aleatorio=random.randint(0,len(palabras)-1)
            self.__unirCaracteresCE__(palabras,anterior+palabras[aleatorio],caracteresMax-1)
      
    def __ponerLanda__(self):
        
        self.arrayCerraduraEstrella.insert(0,chr(955))
    def __generarPalabras__(self,palabras,Npalabras,caracteresMax):
       
        for i in range(0,Npalabras):
    
            aleatorio=random.randint(1,caracteresMax-1)
            self.__unirCaracteresCE__(palabras,"",aleatorio)
        
        self.__ponerLanda__()    
           

    def cerraduraDeEstrella(self,palabras,Npalabras,caracterMax):
    
        self.auxP=caracterMax

        self.__generarPalabras__(palabras,int(Npalabras),caracterMax)

        '''for i in self.arrayCerraduraEstrella:
            print(i)'''
        return self.arrayCerraduraEstrella
       
    



'''pera=Alfabeto()
aux=['A','B','C']
pera.cerraduraDeEstrella(aux,10,5)

'''
