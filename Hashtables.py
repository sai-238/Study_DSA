class HashTable:
    
    def __init__(self):
        #based on the load factor we may change the size of the data structure
        #( Dynamic resizing)
        self.capacity = 10
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def insert(self, key, value):

        # we have to find a valid location for the value (data)
        index = self.hash_function(key)

        # there may be a collision which means that the index is already occupied
        # while we do not find an empty array slot
        while self.keys[index] is not None:
            # sometimes we have to update the value if the key is already present 
            if self.keys[index] == key:
                self.values[index] = value
                return

            # do linear probing (try the next slot in the array)
            # because we may increment the index such that we are outside the range of the array
            index = (index + 1) % self.capacity 

        # we have found an empty slot 
        # so we insert the data
        self.keys[index] = key   
        self.values[index] = value

    def get(self, key):

        # we have to find a valid location for the value (data)
        index = self.hash_function(key)

        while self.keys[index] is not None:
            # this is when we find the item we are looking for 
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity

        # the given key value pair is not present in the hash table
        return None

    # hash value (index of the array) based on the key
    def hash_function(self, key):

        hash_sum = 0
        
        for letter in key:
            hash_sum += ord(letter) 
        
        return hash_sum % self.capacity 
    

table = HashTable()

table.insert("Adam", 23)
table.insert("Kevin", 45)
table.insert("Daniel", 34)

print(table.hash_function("Adam"))
print(table.get("Kevin"))
print(table.get("Dan"))