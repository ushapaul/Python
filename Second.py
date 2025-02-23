class node:
    def _init_(self, d):
        self.data = d
        self.next = None
class LL:
    def _init_(self):
        self.head = None
    
    def add_node(self, val):
        new_node = node(val)
        if(self.head == None):
            self.head = new_node
        else:
            traveller = self.head
            while(traveller.next != None):
                traveller = traveller.next
            traveller.next = new_node
    
    def traverse(self):
        traveller = self.head
        while(traveller.next != None):
            print(traveller.data)
            traveller = traveller.next       
        print(traveller.data)
    def delete_node(self):
        traveller = self.head
        prev = self.head
        while(traveller.next != None):
            prev = traveller
            traveller = traveller.next
            
        prev.next = None
        

LL1 = LL()
LL1.add_node(3)
LL1.add_node(8)
LL1.add_node(6)
LL1.add_node(1)
LL1.traverse()
LL1.delete_node()
LL1.traverse()
