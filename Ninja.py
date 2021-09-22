class Ninja:
    def __init__(self, fName, lname, pet, treats, pet_food):
        self.first_name=fName
        self.last_name=lname
        self.pet = pet
        self.treats=treats
        self.pet_food=pet_food
    
    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()
    
    def bathe(self):
        self.pet.noise()