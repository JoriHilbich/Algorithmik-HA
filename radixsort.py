def radixsort(liste: list) -> list:
    '''
    this function sorts a list via radixsort
    '''
    if len(liste) <= 1:
        return liste
    
    for i in range(len(liste)): #integer to string in list
        liste[i] = str(liste[i])

    maxlen = 0

    for i in liste: #finds longest elementn in list
        if len(i) > maxlen:
            maxlen = len(i)

    for i in range(len(liste)): #adds '0' in front of all elements till all have len maxlen
        if len(liste[i]) < maxlen:
            for k in range(maxlen - len(liste[i])):
                liste[i] = '0' + liste[i]

    index = maxlen - 1 #index to iterate above every string of the list

    while index > -1:
        print(index)
        print(liste)
        partition =[[] for _ in range(10)] #to sort the relevant index of the strings

        for i in liste: #add the strings to one list of the partition decided by their number on index
            temp = int(i[index])
            partition[temp] += [i]

        for i in range(len(partition) - 1, 0, -1): #adds all lists of the partition together in first list(index 0)
            partition[i - 1] += partition[i]

        liste = partition[0] #aktualises the list
        index -= 1
    

    for i in range(len(liste)): #to remove the unnececerry '0'
        while liste[i][0] == '0':
            liste[i] = liste[i][1:]

    for i in range(len(liste)): #strings to integer in list
        liste[i] = int(liste[i])

    return liste

liste = [13, 1, 502, 172, 7777, 2]
print(radixsort(liste))

'''
Die laufzeit kommt von der länge der Zahlen nicht von der länge der Liste.
Da wir immer nur 10 verschiedene möglichkeiten haben die Elemente der Liste zu sortieren (Ziffern 0-9)
und diese deentsprechend in unsere Partition einfügen müssen wir immer nur nach 1er-Stellen, dann 10er-stellen,
dann hunderter-stellen und so wieter Sortieren.So ergibt sich die laufzeit O(nlog(n))
'''