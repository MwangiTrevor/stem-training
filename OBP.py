class Dog :
    def __init__(self, no_of_eyes, color):
        self.no_of_eyes=no_of_eyes
        self.color=color
    def barking (self):
        print ("woof woof") 
    def eats (self):
         print ("pork stake")
german_shephered = Dog(no_of_eyes=2, color="grey")    
Dodger = Dog(no_of_eyes=1, color="white")
Dobber_man = Dog(2, "brown")

print(german_shephered.color, german_shephered.no_of_eyes)
print(Dobber_man.color)
Dobber_man. barking()
Dobber_man. eats()
german_shephered.eats()
Dodger.eats()