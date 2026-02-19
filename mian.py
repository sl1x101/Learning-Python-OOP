#object orientated programming in python

#create a class 

class Adventurer:
    def __init__(self,name,level): 
        self.name = name
        self.level = level
    def close_range(self):
        print(f"name: {self.name} level: {self.level}")
    def long_range(self):
        print(f"name:{self.name} level: {self.level}")
    def set_level (self,level): #modify method
        self.level = level
sword_man = Adventurer("Bod",20) 
sword_man.set_level(50)  
sword_man.close_range()


        