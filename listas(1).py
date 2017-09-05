from time import sleep

class nodo():
    def __init__(self,valor):
        self.value=valor
        self.next=None
        
    def get_value(self):
        return self.value
        
    def get_next(self):
        return self.next 
        
    def set_value(self,valor):
        self.value=valor
        
    def set_next(self, siguiente):
        self.next=siguiente
        
class lista1():
    def __init__(self):
        self.head=None
        
    def get_head(self):
        return self.head
        
    def set_head(self, cabeza):
        self.head=cabeza
        
    def is_empty(self):
        return self.head==None
        
    def add(self,valor):
        eslabon=nodo(valor)
         #sleep(0.1)
        eslabon.next=self.head
        self.head=eslabon
        
    def __len__(self):
        contador=0
        explorador= self.head
        while explorador!= None:
            contador+=1
            explorador=explorador.next
        return contador
        
    def __getitem__(self,pos):
        if self.__len__()<pos:
            raise IndexError
        explorador=self.head
        for i in range(pos):
            explorador=explorador.next
        return explorador.value
        
    def add_last(self, valor):
        eslabon =nodo(valor)
        explorador =self.head
        if explorador == None:
            self.head=eslabon
        else:
            while explorador.next!=None:
                #sleep(0.1)
                explorador=explorador.next
            explorador.next=eslabon
            
    def remove_last(self):
        explorador =self.head
        while explorador.next.next!=None:
            explorador=explorador.next
        explorador.set_next(None)