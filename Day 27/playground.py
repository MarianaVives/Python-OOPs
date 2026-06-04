#Using *Args to overload the method
def add_num(*args):
    sum = 0
    for n in args:
        print(n)
        sum+=n
    return sum

print(add_num(2,3,4,5))
print(add_num(2,3))

#Using **kwargs: many keyword args
#Arbitrary number of keyword arguments

def calculate(**kwargs):
    print(kwargs)#Dictionary {'add': 3, 'substract': 2, 'multiply': 5}
    for key, value in kwargs.items():
        print(key, value) #add 3 , substract 2, multiply 5
    print(kwargs["add"]) #3

calculate(add=3, substract=2, multiply=5)

def calculate_2(n, **kwargs):
    print(kwargs)
    n+=kwargs["add"]
    return n

print(calculate_2(2, add=3))


class Car:

    def __init__(self, **kw):
    #    self.make = kwargs["make"]
    #    self.model = kwargs["model"]
        self.make = kw.get("make")
        self.model= kw.get("model")
        self.color= kw.get("color")
my_car = Car(make="Suzuki", model="swift")
print(my_car.make)
