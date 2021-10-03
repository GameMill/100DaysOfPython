def add(*args):
    num = 0
    for item in args:
        num += item
    return num


print(add(1,2,4,5))


def calculate(**kwargs):# bidmas
    value = 0
    if(kwargs.__contains__("add")):
        for item in kwargs["add"]:
            value += item
    if(kwargs.__contains__("multiply")):
        for item in kwargs["multiply"]:
            value *= item
    return value
print(calculate(add=(1,1),multiply=(2,2,2,2,2,2,2,2)))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Nissan",model="GT-R")
print(my_car.model)
my_car2 = Car(make = "Nissan")
print(my_car2.model)
