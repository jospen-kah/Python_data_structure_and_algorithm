class Myclass: 
    def __init__(self, name, age):
        self.name  = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
cls1 = Myclass("jos", 13)
print(cls1)


