
class Hashmap:
    def __init__(self,size):
        self.size=size 
        self.map=[None]*size

    def get_hash(self,key):
        ascii_tot=0
        for obj in key:
            ascii_tot += ord(obj) 
        hashed = (ascii_tot*17)%self.size      
        return hashed

    def add(self,key,value):
        idx=self.get_hash(key)
        if self.map[idx] == None :
            self.map[idx]=[[key,value],]
        else:
            self.map[idx].append([key,value])

    def contains(self,key):
        idx=self.get_hash(key)
        x= dict(self.map[idx])
        y=x.keys()
        if key in y :
            return True
        else:
            return False       
    def find(self,key):
        idx=self.get_hash(key)
        x= dict(self.map[idx])
        for key, value in x.items():
            if key == key:
                return value


if __name__ == "__main__":  
    pass