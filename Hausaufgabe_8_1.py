#Hausaufgabe 8.1.1
'''
Wir würden die Liste mit einem Effizienten Sortieralgorythmus sortieren was einer laufzeit von O(n log(n)) entspricht. Dann müssen wir nur noch das Element der Liste an der Stelle (n-k) ausgeben.
'''

#Hausaufgabe 8.1.2
'''
Die Idee ist, dass wir die ersten k-Elemente der Liste in den Heap einfügen und danach jedes weitere Element der liste mit de an der ersten Stelle des heaps vergleichen. Ist das einzufügende Elemente größer als das an der stelle heap[0], so wird das kleinste Elemente extracted und das neue Elemente eingefügt. Dadurch Rutscht das k-größte Element an die stelle heap[0] und kann so zurückgegeben werden.

In der ersten Schleife werden k Elemente an der Heap angehängt. Da add eine Laufzeit von O(log(n)) in bezug auf die länge des Heaps, und da der Heap max die länge von k hat und wir k-Elemente einfügen, ist die Laufzeit der ersten Schleife O(k log(k)).
Da wir die Zweite schleife (n-k) mal durchlaufen (n = Länge der liste), und die die Funktionen 'extract_min' und 'add' die Laufzeit O(log(n)) im bezug auf die länge des Heaps haben, betägt die laufzeit hier O((n-k)log(k))
Da n > k ist die Laufzeit O(n log(k)) mit n = die länge der liste und k = k (im beispiel 4).
'''

class Heap():

    def __init__(self):
        self.heap = []

    def __heapify_up(self,i):
        parent_pos = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent_pos]:
            #swap(self.heap, i, parent_pos)
            self.heap[i], self.heap[parent_pos] =\
                self.heap[parent_pos], self.heap[i]
            self.__heapify_up(parent_pos)
        
    def __heapify_down(self,i):
        left = i * 2 + 1
        right = left + 1
        cont = True
        while cont and right < len(self.heap): # test wirh right, since we know 
                                      # that both subtrees exist in loop body 
            if self.heap[left]<self.heap[right]:
                min_pos = left
            else:
                min_pos = right
            if self.heap[i] > self.heap[min_pos]:
                #swap(self.heap, i, min_pos)
                self.heap[i], self.heap[min_pos] =\
                    self.heap[min_pos], self.heap[i]
                i = min_pos
                left = i * 2 + 1
                right = left + 1
            else:
                cont = False

        if cont and left < len(self.heap):
            if self.heap[i] > self.heap[left]:
                #swap(self.heap, i, left)
                self.heap[i], self.heap[left] =\
                    self.heap[left], self.heap[i]
        

    def add(self,v):
        self.heap.append(v)     # constant runtime
        self.__heapify_up(len(self.heap)-1)

    def get_min(self):
        return self.heap[0]

    def extract_min(self):
        if self.heap == []:
            return None
        elif len(self.heap) == 1:
            min = self.heap[0]
            self.heap = []
            return min
        else:
            min = self.heap[0]
            self.heap[0] = self.heap.pop() # important, since constant runtime
            self.__heapify_down(0)
            return min

    def __str__(self):
        def str_h(i):
            if i < len(self.heap):
                left_res  = str_h(i*2+1)
                right_res = str_h(i*2+2)
                return ('(' + left_res + ',' + str(self.heap[i]) + 
                        ',' + right_res + ')')
            else:
                return ''  
        
        return str_h(0)
    
    def k_biggest_elem(self, k, l):
        '''
        Method to search the k-largest element of a list
        '''
        for i in range(k): 
            self.add(l[i]) 
        
        for i in range(k, len(l)):
            if l[i] > self.heap[0]:
                self.extract_min()
                self.add(l[i])
        
        return self.get_min()



h = Heap()
l = [3,4,1,9,2,5] 
k = 4
print(h.k_biggest_elem(k, l))
