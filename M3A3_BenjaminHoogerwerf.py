# creates the parent class
class Vehicle:
    vType = ""

# creates the child class
class Automobile(Vehicle):
    aYear = 0
    aMake = ""
    aModel = ""
    aDoors = 0
    aRoof = ""

# creates an Automobile object
test = Automobile()

# gathers user input for all of the "test" object's attributes
test.vType = input("What kind of vehicle is this? ")
test.aYear = int(input("What year was it made? "))
test.aMake = input("What's its make? ")
test.aModel = input("What's its model? ")
test.aDoors = int(input("Does it have 2 or 4 doors?" ))
test.aRoof = input("Does it have a solid roof or a sun roof? ")

# prints user input in an easy-to-read list as output
print(f"Vehicle type: {test.vType}\nYear: {test.aYear}\nMake: {test.aMake}\nModel: {test.aModel}\nNumber of doors: {test.aDoors}\nType of roof: {test.aRoof}")