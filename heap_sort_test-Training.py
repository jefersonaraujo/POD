class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def delMin(self):
      retval = self.heapList[1]
      print(self.heapList[1])
      self.heapList[1] = self.heapList[self.currentSize]
      print(self.heapList[self.currentSize])
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def percDown(self,i):
      #print(self.currentSize)
      while (i * 2) <= self.currentSize:
          
          print("ENTROU WHILE", i*2 ," < = " , self.currentSize )
          print("PROCURANDO MC...")
          mc = self.minChild(i)          
          print("VALOR DA POSICAO DO MC = %d" %mc," =heapList[%d]" %self.heapList[mc])
          if self.heapList[i] > self.heapList[mc]:
          	  print("I=%d  |  MC=%d" %(i,mc))
          	  print("Entro no IF PERCDOWN self.heapList[i], > ,self.heapList[mc] POIS  ",self.heapList[i]," > ",self.heapList[mc])
          	  tmp = self.heapList[i]
          	  print("TMP RECEBE VALOR DA POSICAO de 'I' self.heapList[%d]" %self.heapList[i])
          	  print("self.heapList(i)[%d] = self.heapList(mc)[%d]" %(self.heapList[i],self.heapList[mc]))
          	  self.heapList[i] = self.heapList[mc]
          	  print("self.heapList(mc)[%d] = TMP[%d]" %(self.heapList[mc],tmp))
          	  self.heapList[mc] = tmp
              #print(self.heapList[mc])
          i = mc
          print("I AGORA eh =",i)

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
      	  print("Entrou primeiro IF !",i * 2 + 1," > ",self.currentSize ," VAI RETORNAR = ",i*2)
      	  return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
          	print("Entrou no Else depois IF !",self.heapList[i*2],"<", self.heapList[i*2+1]," VAI RETORNAR = ",i * 2)
          	return i * 2
          else:
          	print("Entrou no sub Else, VAI RETORNAR = ",i * 2 + 1)
          	return i * 2 + 1



    def buildHeap(self,alist):
      i = len(alist) // 2

     
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          print("WHILE %d > 0" %i )
          self.percDown(i)
          i = i - 1
          print(self.heapList)
          
          print("*************************************************")


    def toString(self):
        return self.heapList

bh = BinHeap()
bh.buildHeap([9, 8, 2, 1, 6, 5])

#print(bh.toString())

# print(bh.delMin())
# print(bh.toString())
# print(bh.delMin())
# print(bh.toString())
# print(bh.delMin())
# print(bh.toString())
# print(bh.delMin())
# print(bh.toString())
# print(bh.delMin())
