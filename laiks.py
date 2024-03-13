import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        sakuma_laiks = time.time()
        function()
        beigu_laiks = time.time()
        print(f"Funkcijas {function.__name__} darbības ātrums ir {beigu_laiks-sakuma_laiks} sekundes.")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()