
class HashTable():
  def __init__(self):
    self.max = 100  
    self.arr =[None for i in range(self.max)] 
  
  def hash_key(self,key):# method for finding the hash key using ASCII 
    h = 0 # this is varialbe for saving the sum
    for char in key:
      h += ord(char) #ord - will convert each character in the key to the ASCII value 
        #print(h%self.max)
        
    return h % self.max # assuming that 100 will the size of the list so we are calculating mod using 100
  def __setitem__(self,key,value): #this method will add an item to a hash map. And it takes in a key-value pair
    h=self.hash_key(key) # we get the hash_key method convert the key using ASCII to a number and store it in h.
    self.arr[h]=value  # h which is the key is then = value
  def __getitem__(self,key):  # this method get the key
    h=self.hash_key(key)
    #print(self.arr[h])
    return self.arr[h]

  def __delitem__ (self, key): 
    h=self.hash_key(key) #get the hash key
    self.arr[h]=None  #Then in your array set that particular element to be none

t = HashTable() 
#val=t.hash_key('march 6')
#keep = t.add('march 6',130)
#t.get('march 6') #Display the value
#take = t.get('march 6')
t['march 6'] =130
t['march 17'] =  20
print(t['march 6'])
print(t['march 17'])
del t['march 17']
#print(take)#Display the value
#print(val) #Displaying the position of the key
print(t.arr)
