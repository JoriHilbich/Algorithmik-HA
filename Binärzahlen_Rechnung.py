def bin_inc(list: list) -> list:
    '''
    this function increments a binary number
    '''
    incList = []
    for i in range(len(list)):
        if list[i] == 0:
            incList.append(1)
            incList += list[i + 1:]
            break
        else:
            incList.append(0)
    if incList[len(list) - 1] == 0:
        incList.append(1)
    return incList

'''
Der Best-Case ist in jedem Fall, unabhängig der länge der Binärzahl, wenn die erste stelle der liste 0 ist, da diese dann einfach auf 1 gesetzt wird. Die laufzeit beträgt O(1), da eine feste Anzahl an Operationen durchgeführt wird.
Der Worst-Case ist, wenn die Liste keine 0 in sich hat. Dann wird ein mal komplett über die liste iteriert und am ende noch eine 1 angehängt. Dies entspricht einer linearen Laufzeit O(n) in der länge der eingegebenen Liste.
Der Average-Case beträgt O(n/2) in der länge der eingegebenen Liste, da an jeder position 50/50 eine 0 oder eine 1 steht. Deshalb ist es gleichwahrscheinlich das die erste 0 irgendwo steht und im schnitt ist das n/2.

Für das Programm aus 7.2.2 gelten die selben Worst- und Best-Case Szenarien.
'''

def count_till_same(list: list):
    tempList = [0]
    while tempList != list:
        tempList = bin_inc(tempList)
    return tempList


def bin_inc_mut(n): 
    i = 0
    while i < len(n) and n[i] == 1:
        n[i] = 0
        i = i + 1
    if i == len(n):
        n.append(1)
    else:
        n[i] = 1
    return n

def count_till_same_mut(list: list):
    tempList = [0]
    while tempList != list:
        tempList = bin_inc_mut(tempList)
    return tempList
    

#liste = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#count_till_same(liste)
#count_till_same_mut(liste)
'''
mit diesen beiden Tests habe ich wie in der Vorlesung die Laufzeit mehrmals im Terminal bestimmt und die Beiden Laufzeiten sind Quasi identisch. Ich gehe davon auß, dass die in Aufgabe 1 Programmierte Funktion nicht so Effizient Programmiert ist wie vorgesehen.
Zeiten für nicht Mutierend: 7,326; 7,351; 7,348
Zeiten für Mutierend: 7,401; 7,382; 7,345
Aus diesen Zeiten sehe ich keinen effizienten Zeitvorteil.
'''