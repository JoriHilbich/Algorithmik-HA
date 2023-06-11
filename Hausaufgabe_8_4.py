#Hausaufgabe 8.4
#zusammenarbeit mit Gruppe HD und Gruppe AF

class max_heap():
    '''
    a class wich constucts a max_heap out of a list and sorts it
    '''
    def __init__(self, l):
        self.heap = l
        self.list_length = len(l)

    def list_to_maxheap(self):
        '''
        method to turn a list into a max heap
        '''
        for i in range(self.list_length // 2 - 1, -1, -1):
            self.heapify_up(i)

    def heapify_up(self, i):
        '''
        this Method tests if a small value is above a bigger one and changes it if it is so.
        '''
        parent_node = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        #Überprüfe, ob linker Kindknoten größer, als Elternknoten:
        if left_child < self.list_length and self.heap[left_child] > self.heap[parent_node]:
            parent_node = left_child

        #Überprüfe, ob rechter Kindknoten größer, als (neuer) Elternknoten:
        if right_child < self.list_length and self.heap[right_child] > self.heap[parent_node]:
            parent_node = right_child

        #Ggf. tausche größtes Kind mit Elternknoten & mache rekursiven aufruf,
        #falls Knoten unter betrachtetem Teilbaum größer sind:
        if parent_node != i:
            self.heap[i], self.heap[parent_node] = self.heap[parent_node], self.heap[i]
            self.heapify_up(parent_node)

    def heap_sort(self):
        '''
        Method to sort a list
        '''
        for i in range(self.list_length - 1, -1, -1):
            '''
            we remember where the list is sorted and where not and does heapify up to get the 
            '''
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0] #like the extract_min function from heap.py out of the VL but we change them and dont delete. So the biggest Element is infront of the Sorted part and the sorted part gets one bigger.
            self.list_length -= 1
            self.heapify_up(0)

            




l = [6, 2, 4, 7, 2, 8, 34, 4, 77, 77, 87, 65, 65, 43, 45, 56, 67, 78, 34, 44, 55, 66, 77, 88, 99, 100, 200, 2333, 23232, 342243, 2323, 232324, 2]
heap = max_heap(l)
heap.list_to_maxheap()
heap.heap_sort()
print(l)