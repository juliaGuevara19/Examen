from time import sleep

class nodo():
    def __init__(self,valor):
        self.value=valor
        self.next=None
        self.last=None
        
    def get_value(self):
        return self.value
        
    def get_next(self):
        return self.next 
        
    def get_last(self):
        return self.last
    
    def set_value(self,valor):
        self.value=valor
        
    def set_next(self, siguiente):
        self.next=siguiente
    
    def set_last(self, anterior):
        self.last=anterior
        
class lista():
    
    def __init__(self):
        self.lider= nodo('Lider')
        self.cabus =nodo('Cabus')
        self.lider.next=self.cabus
        self.cabus.last=self.lider
        #para ahcerlo circular
        self.lider.last =self.cabus
        self.cabus.next=self.lider
        
    def is_empty(self):
        return self.lider.next is self.cabus
    def add(self,valor):
        newNodo=nodo(valor)
        newNodo.next=self.lider.next
        newNodo.last=self.lider
        self.lider.next.last=newNodo
        self.lider.next=newNodo
       
    def remove(self):
        if self.lider.next is not self.cabus:
            self.lider.next=self.lider.next.next
            self.lider.next.last=self.lider
    def __len__(self):
        contador=0
        explorador= self.lider
        while explorador is not self.cabus:
            contador+=1
            explorador=explorador.next
        return contador 
    
    def __getitem__(self,pos):
        if self.__len__()<pos:
            raise IndexError
        explorador=self.lider.next
        for i in range(pos):
            explorador=explorador.next
        return explorador.value
        
   # def add_last(self, valor):
    #    eslabon =nodo(valor)
       # explorador =self.head
     #   if explorador == None:
   #         self.head=eslabon
     #   else:
      #      while explorador.next!=None:
                #sleep(0.1)
       #         explorador=explorador.next
        #    explorador.next=eslabon