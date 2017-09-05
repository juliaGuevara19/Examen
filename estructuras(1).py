import numpy as np
import math
class dinamico():
    def __init__(self):
        self.espacio=1
        self.tam=0
        self.arreglo= np.empty(self.espacio, dtype=int)
        
    def __len__(self):
        return self.tam
        
    def add(self,nuevo):
        if self.tam<self.espacio:
            self.arreglo[self.tam]=nuevo
            self.tam+=1
        else:
            self.espacio*=2
            newA=np.empty(self.espacio, dtype=int)
            for i in range(self.tam):
                newA[i]=self.arreglo[i]
            newA[self.tam]=nuevo
            self.tam+=1
            self.arreglo=newA 
            
    def __str__(self):
        print("Espacio: {0}\t Elementos: {1}".format(self.espacio,self.tam))
        return "-".join([str(x) for x in self.arreglo[:self.tam]])
        
    def __getitem__(self,pos):
        if 0<=pos<self.tam:
            return self.arreglo[pos]
        else:
            raise IndexError
            
    def deleteLast(self):
        self.tam-=1
        if self.tam<=(self.espacio/2):
            self.espacio*= (3/4)
            self.espacio=math.floor(self.espacio)
            newA=np.empty(self.espacio, dtype=int)   
            for i in range(self.tam):
                newA[i]=self.arreglo[i]
            self.arreglo=newA
        
    def deleteFirst(self):
        if self.tam<=(self.espacio/2):
           self.espacio*=(3/4)
           self.espacio=math.floor(self.espacio)
        newB=np.empty(self.espacio, dtype=int)
        for i in range(1,self.tam):
           newB[i-1]=self.arreglo[i]
        self.tam-=1
        self.arreglo=newB
       
    def removeLast(self):
        if self.tam==0: return
        self.tam=self.tam-1
        if self.tam>self.espacio/2: return
        else: 
            self.espacio=int(.75*self.espacio)
            newA=np.empty(self.espacio, dtype=int)
            for i in range(self.tam):
                newA[i]=self.arreglo[i]
            
    
            