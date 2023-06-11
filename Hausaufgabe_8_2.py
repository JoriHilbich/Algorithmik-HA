#Hausaufgabe 8.2
'''
Die Laufzeit hängt davon ab wie viele Elemente scih in einer conflict_list befinden. Sollten alle eintäge in der gleichen sein, dann beträgt die Laufzeit O(n) in der anzahl der keys. Wenn die Einträge gleichmäßig verteilt sind, dann beträgt die Laufzeit O(1). Also gehe ich im Average Case von einer Laufzeit von O(n/2) aus was einer Laufzeit von O(n) entspricht.

Es ist sinnvoll die Hashmap zu verkleinern, da es nach dem löschen eines keys zu einer sehr geringen füllrate der Hash-Map kommen kann. Dadurch wird unnötig viel Speicher gebraucht. Deshalb verkleinern wir.
'''

class HashMap():
    
    def __init__(self,size):
        self.size = 0   # number of element stored in the HasMap
        self.hash_list = []#
        for i in range(5):
            self.hash_list.append([])

    def __hash_code(str,size):
        '''
        copute hash_code for given string
        number between 0 an size-1
        '''
        code = 0
        for i in range(len(str)):
            code = (code + (ord(str[i]) * (i+1))) % size

        return code
    
    def __resize(self,new_size):
        '''
        auxiliary function to resize the array to given new_size
        '''
        old_hash_list = self.hash_list #
        self.size = 0
        self.hash_list = []
        for i in range(new_size):
            self.hash_list.append([])
        for conflict_list in old_hash_list:
            for key,value in conflict_list:
                self.insert(key,value)

    def insert(self, key, value):
        '''
        insert new key-value pair to given hashmap
        '''
        index =  HashMap.__hash_code(key,len(self.hash_list))
        conflict_list = self.hash_list[index]
        i = 0
        while i < len(conflict_list) and conflict_list[i][0] != key:
            i = i + 1

        if i == len(conflict_list):  # key not present
            conflict_list.append((key,value))
            self.size = self.size + 1
        else:                        # key found at index i
            conflict_list[i] = (key,value)
        if self.size / len(self.hash_list) > 0.7:
            self.__resize(len(self.hash_list)*2)

    def lookup(self,key):
        '''
        lookup the given key and returns the stored value
        in case the key is not present in the given hashmap
        the function returns None
        '''
        index =  HashMap.__hash_code(key,len(self.hash_list))
        conflict_list = self.hash_list[index]
        i = 0
        while i < len(conflict_list) and conflict_list[i][0] != key:
            i = i + 1
        if i == len(conflict_list):  # key not present
            return None
        else:                        # key found at index i
            return conflict_list[i][1]
        
    def delete(self, key):
        """
        Entfernt den angegebenen Schlüssel und den zugehörigen Wert aus der Hash Map.
        """
        index = HashMap.__hash_code(key, len(self.hash_list))
        conflict_list = self.hash_list[index]
        i = 0
        while i < len(conflict_list) and conflict_list[i][0] != key:
            i += 1
        if i < len(conflict_list):  # Schlüssel gefunden
            del conflict_list[i]
            self.size -= 1
            if self.size / len(self.hash_list) < 0.2:  # Verkleinern der Liste, wenn der Füllgrad zu niedrig ist
                self.__resize(len(self.hash_list) // 2)


map = HashMap(5)

keys = ['hallo','hi','hola','hey','toll','supi','yippi','los geht\'s']
        
for i in range(len(keys)):
    map.insert(keys[i],i)


print(map.hash_list)




