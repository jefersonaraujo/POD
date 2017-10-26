import random
import string
import time

def generationName():
    size = random.randint(3,18)
    chars = []
    chars.extend([i for i in string.ascii_lowercase])
    user = ''
    alt = random.uniform(0,3)


    for i in range(size):
        user += chars[random.randint(0,  len(chars) - 1)]

    return user,alt


class HashMap(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self.data = []

        for i in range(self.size):
            self.slots.append([])
            self.data.append([])

    def hashfunction(self,key):
        hash = 0
        for char in str(key):
            hash += ord(char)

        return hash % self.size
        #return key%self.size



    def _find(self, key):
        hashvalue = self.hashfunction(key)

        index = 0
        found = False
        for item in self.slots[hashvalue]:
            if key == item:
                found = True
                break

            index = index + 1

        return found, index

    def remove(self, key):
        result = None
        hashvalue = self.hashfunction(key)

        found, index = self._find(key)
        if found:
            self.slots[hashvalue].pop(index)
            result = self.data[hashvalue].pop(index)

        return result

    def get(self, key):
        result = None
        hashvalue = self.hashfunction(key)

        found, index = self._find(key)
        if found:
            result = self.data[hashvalue][index]

        return result

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def put (self, key, data):
        hashvalue = self.hashfunction(key)

        if key not in self.slots[hashvalue]:
            self.slots[hashvalue].append(key)
            self.data[hashvalue].append(data)
        else:
            index = 0
            for item in self.slots[hashvalue]:
                if key == item:
                    break
                index = index + 1

            self.data[hashvalue][index] = data


def gera_nome():
        caracters = 'abcdefghijlmnopqrstuwvxz'
        senha = ''
        for char in xrange(tamanho):
                senha += choice(caracters)
        return  senha

# print (gera_senha())
print(gera_nome())


H=HashMap(10)
print(H.slots)

# H["Joao"]="1.72"
# H["Alfredo"]="1.80"
# H["Jeferson"]="1.68"
# print(H.slots)
# print(H.data)
# print("A altura de Joao %s e", H["Joao"])
# print("A altura de Alfredo %s e", H["Joao"])
# print("A altura de Jeferson %s e", H["Joao"])
