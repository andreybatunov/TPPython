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

@validate_args
def summa(a, b):
    return a + b

@validate_args
def hello():
    return "hello"

@validate_args
def square(a):
    return a**2
summa(12, 12) # Too many arguments
hello() # Not enough arguments
square(2.2) # Wrong types
square(-2) # Negative argument
        