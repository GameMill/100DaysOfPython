
def logger_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"You called {function.__name__}({str(args)[1:-1]})")

        print(f"It returned: {function(*args)}") 
    return wrapper

@logger_decorator
def a_function(n1,n2,n3):
    return n1+n2+n3
    
a_function(1,2,3)