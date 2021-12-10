import time


def timer_decorator(function):
    """Decorator add a timer to the function to see how long it takes"""
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(end_time - start_time)
    return wrapper_function

@timer_decorator
def fast_function():
    for i in range(10000000):
        i * i

@timer_decorator    
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()