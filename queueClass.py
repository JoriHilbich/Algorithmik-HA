class ListElem():
     def __init__(self):
         '''
         construct an empty list elem
         '''
         self.empty = True

     def fill(self,value):
         '''
         fill list elem with value and pointer to a new empty list elem
         '''
         self.empty = False
         self.value = value
         self.next = ListElem()
         return self.next

class Queue():

    def __init__(self):     
        '''
        constructs an empty queue
        '''
        empty_elem = ListElem()
        self.head = empty_elem
        self.end = empty_elem

    def enqueue(self,value):
        '''
        adds value to queue (FIFO-Order)
        '''
        self.end = self.end.fill(value)
    
    def top(self):
        '''
        returns value of oldest element in the queue, without removing
        returns None if queue is empty
        '''
        if self.head.empty:
            return None
        else:
            return self.head.value
       
    def dequeue(self):
        '''
        removes oldest element from the queue and returns its value
        returns None if queue is empty
        '''
        if self.head.empty:
            return None
        else:
            result = self.head.value
            self.head = self.head.next
            return result
        
    def list_to_queue(self, liste: list):
        '''
        converts a list to a queue
        '''
        for i in liste:
            self.enqueue(i)
    
    def queue_to_list(self) -> list:
        '''
        converts a queue to a list
        '''
        liste = []
        while not self.head.empty:
            liste.append(self.dequeue())
        return liste
    
    def undequeue(self, value):
        '''
        puts an object at the reedingend
        '''
        liste = self.queue_to_list()
        liste2 = [value] + liste
        self.list_to_queue(liste2)

    def dedequeue(self):
        '''
        removes an object from the queue
        '''
        liste = self.queue_to_list()
        liste.pop()
        self.list_to_queue(liste)

q = Queue()
#q.enqueue(42)
#q.enqueue(73)
q.list_to_queue([1, 2, 3])
#print(q.dequeue())
#q.enqueue(55)
q.undequeue(4)
q.dedequeue()
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())


