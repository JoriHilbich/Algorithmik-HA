def empty_queue():
    '''
    constructs an empty queue
    '''
    empty_elem = {}
    return {'head' : empty_elem, 'end' : empty_elem}

def enqueue(value,queue):
    '''
    adds value to queue (FIFO-Order)
    '''
    old_end = queue['end']
    old_end['value'] = value
    empty_elem = {}
    old_end['next'] = empty_elem
    queue['end'] = empty_elem
    
def top(queue):
    '''
    returns value of oldest element in the queue, without removing
    returns None if queue is empty
    '''
    if queue['head'] == {}:
        return None
    else:
        return queue['head']['value']
       
def dequeue(queue):
    '''
    removes oldest element from the queue and returns its value
    returns None if queue is empty
    '''
    if queue['head'] == {}:
        return None
    else:
        result = queue['head']['value']
        queue['head'] = queue['head']['next']
        return result

def list_to_queue(liste: list, queue):
    '''
    converts a list to a queue
    '''
    for i in liste:
        enqueue(i, queue)

def queue_to_list(queue) -> list:
    '''
    converts a queue to a list
    '''
    liste = []
    while queue['head'] != {}:
        liste.append(dequeue(queue))
    return liste

def undequeue(value, queue: dict):
    '''
    puts an object at the reedingend
    '''
    liste = queue_to_list(queue)
    liste2 = [value] + liste
    list_to_queue(liste2, queue)

def dedequeue(queue):
    '''
    removes an object from the queue
    '''
    liste = queue_to_list(queue)
    liste.pop()
    list_to_queue(liste, queue)


q = empty_queue()
enqueue(42,q)
enqueue(73,q)
enqueue(55,q)
undequeue(5, q)
dedequeue(q)
a = queue_to_list(q)
print(a)
list_to_queue(a, q)
print(dequeue(q))
print(dequeue(q))
print(dequeue(q))
print(dequeue(q))