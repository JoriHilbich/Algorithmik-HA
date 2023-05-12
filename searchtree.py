import random

class SearchTree():

    '''
    Class implementing search trees, without balancing
    '''

    def __init__(self):
        '''
        construct an empty search tree
        '''
        self.empty = True
        self.height = 0

    def _update_height(self):
        '''
        auxiliary function for updating the height of a node.
        '''
        self.height = max(self.left.height, self.right.height) + 1

    def insert(self,v):
        '''
        inserts the given value v into the searchtree
        returns False, if value already occurs, otherwise True 
        '''
        if self.empty:
            self.value = v
            self.left = SearchTree()
            self.right = SearchTree()
            self.empty = False
            self.height = 1
            return True
        elif v == self.value:
            return False
        elif v < self.value:
            result = self.left.insert(v)
            self._update_height()
            return result
        else:
            result = self.right.insert(v)
            self._update_height()
            return result

    def elem(self,v):
        '''
        checks whether v occurs in th search tree
        '''
        if self.empty:
            return False
        elif v == self.value:
            return True
        elif v < self.value:
            return self.left.elem(v)
        else:
            return self.right.elem(v)
        
    def elem_iter(self,v):
        '''
        iterative version of elem
        '''
        st = self
        while not st.empty and v != self.value:
            if v < self.value:
                st = st.left
            else:
                st = st.right
        return not st.empty
    
    def delete(self, v):
        '''
        deletes the the value v and replaces it with the largest variable from left side
        '''
        if v == self.value:
            if self.left.empty and self.right.empty:
                self.value = SearchTree()
                self._update_height()
            elif self.left.empty:
                temptree = self.right
                self.value = temptree
                self._update_height()
            else:
                tempvalue = self.left.delete_largest()
                print(tempvalue)
                self.value = tempvalue
                self._update_height

        elif v < self.value:
            self.left.delete(v)
        else:
            self.right.delete(v)

    def delete_largest(self):
        '''
        deleats the largest value and returns ist
        '''
        if self.right.empty and self.right.empty: #if left and right are empty return value
            tempvalue = self.value
            self.value = SearchTree()
            self.empty = True
            self.height = 0
            self._update_height()
            print(tempvalue)
            return tempvalue
        elif self.right.empty:
            tempvalue = self.value
            temptree = self.left
            self.value = temptree
            self._update_height()
            return tempvalue
        else:
            return self.right.delete_largest()


    def __str__(self):
        '''
        nice string representation of a search tree, mainly usefull for
        debugging purposes'''
        if self.empty:
            return '_'
        elif self.left.empty and self.right.empty:
            return str(self.value)
        else:
            return ('(' + str(self.left) + ',' + str(self.value) + '[' + str(self.height) + ']' + ',' + str(self.right) + ')')
                    
        
def rand_list(n):
    res = []
    for i in range(n):
        res.append(random.randint(1,n*10))
    return res

#l = [4,7,2,9,8,1,3,2]
n = 2000

l = rand_list(n)
st = SearchTree()
st.insert(22)
st.insert(12)
st.insert(7)
st.insert(3)
st.insert(9)
st.insert(420)
st.delete(12)
print(st)




