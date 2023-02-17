class Hashtable:
    def __init__ (self,size=7):
        self.data_map=[None]*size

    def __hash(self,key):
        my_hash=0
        for letters in key:
            my_hash=(my_hash+ord(letters)*23)%len(self.data_map)
        return hash

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)
    
my_hash_table=Hashtable()
my_hash_table.print_table()
