class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:

    def __init__(self, cakeFlavor, cakeFrosting):
        self.cakeFlavor = cakeFlavor
        self.cakeFrosting = cakeFrosting
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
class Diving:

    def __init__(self, diveCategory, numOfFlips, numOfTwists):
        self.diveCategory = diveCategory
        self.numOfFlips = numOfFlips
        self.numOfTwists = numOfTwists
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    dog1 = Dog("Charlotte" , 11)
    print(dog1.name, dog1.age)
    
    #and what about a new employee
    employee1 = Employee("Steve", 22204, "fruit")
    #how would we print out each of the variables from newEmployee?
    print(employee1.name, employee1.idNumber, employee1.department)
    
    #now create and print out a cake you make
    newCake = Cake("chocolate", "strawberry")
    print(newCake.cakeFlavor, newCake.cakeFrosting)
    
    
    #and now create another cake and print it out
    newCake2 = Cake("vanilla", "blueberry")
    print(newCake2.cakeFlavor, newCake2.cakeFrosting)
    
    
    #create a cat!
    cat1 = Cat("Pickles", 4, "short")
    #create another cat!
    cat2 = Cat("Charlie", 8, "long")
    #What would we put here to print out the result of breedGuess for cat1?
    catBreed = cat1.breedGuess()
    print(catBreed)
    
    #create a car!
    car1 = Car("Ford", 2020, "blue")
    #Now print out the function you made for car :)
    print(car1.model, car1.year, car1.color)

main()
