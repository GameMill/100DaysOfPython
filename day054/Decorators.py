
def add(n1,n2):
    return n1 + n2;
    
def subtract(n1,n2):
    return n1 - n2;
    
def multiply(n1,n2):
    return n1 * n2;
    
def devide(n1,n2):
    return n1 / n2;
    

#Function are first-class object, can be passed around as arguments e.g. int/scripng/float etc.
def calculate(calc_function, n1, n2):
    return calc_function(n1,n2);


result = calculate(devide,6,2)
print(result)

# Nested Functions
def  outer_function():
    print("I`m outer")
    def  nested_function():
        print("I`m Inner")
    
    return nested_function


# Function can be returned from other functions

inner_function = outer_function()
inner_function()


# Python Decorator Function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")


say_hello()
say_bye()
say_greeting()