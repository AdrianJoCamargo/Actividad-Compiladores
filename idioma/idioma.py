


class Idioma():
    

    
            
    def union(self,array1,array2):
        conjunto1=set(array1)
        conjunto2=set(array2)
        return conjunto1 | conjunto2

    def diferencia(self,array1,array2):
        conjunto1=set(array1)
        conjunto2=set(array2)
        return conjunto1-conjunto2

    def interseccion(self,array1,array2):
        conjunto1=set(array1)
        conjunto2=set(array2)
        return conjunto1&conjunto2 
        
    