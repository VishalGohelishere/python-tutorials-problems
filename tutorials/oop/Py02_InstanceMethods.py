class Vehicle():
    #Class Methods/ Attributes

    #Here self is passed as an argument because instance is passed as first argument
    def type(self):     #Without self it throws an error
        print(self)
        print('I have a type')

car = Vehicle()
print(car)
car.type()