from time import *

def validate_args(func):
    def wrapped_func(*args, **kwargs):
        if len(args) < 1:
            print("Not enough arguments")
        elif len(args) > 1:
            print("Too many arguments")
        elif not isinstance(args[0], int):
            print("Wrong types")
        elif args[0] < 0:
            print("Negative argument")
            
        value = func(*args, **kwargs)
        return value
    return wrapped_func

def timer(func):
    def wrapped_func(*args, **kwargs):
        start_at = time()
        result = func(*args, **kwargs)
        end_at = time()
        print(f'Функция проработала {round(end_at - start_at, 4)} секунд')
        return result
    return wrapped_func

def memoize(func):
    cache = {}
    def wrapped_func(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        cache[args] = result
        return result
    return wrapped_func

@validate_args
@timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@memoize
@validate_args
@timer
def fibonacci_memoize(n):
    if n < 2:
        return n
    return fibonacci_memoize(n - 1) + fibonacci_memoize(n - 2)

fibonacci(10) # Функция проработала 0.7556 секунд
print("\n")
fibonacci_memoize(10) # Функция проработала 0.0313 секунд

