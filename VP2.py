

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



H=HashMap(10)
print(H.slots)

H["Joao"]="1.72"
print(H.slots)
print(H.data)
print(H["Joao"])
