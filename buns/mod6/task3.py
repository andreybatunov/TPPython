def is_armstrong(number):
    digitals = [int(i) for i in str(number)]
    degree = len(digitals)
    sum_ = 0
    for digit in digitals:
        sum_ += digit**degree
    return True if sum_ == number else False

def get_armstrong_generator():
    for i in range(10, 115132219018763992565095597973971522401):
        if is_armstrong(i):
            yield i
            
armstrong_generator = get_armstrong_generator()

def get_armstrong_numbers():
    return next(armstrong_generator)

for i in range(8):
    print(get_armstrong_numbers(), end=' ') # 153 370 371 407 1634 8208 9474 54748 
    
        
    