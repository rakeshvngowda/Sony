def decor(func):
    def inner(x, y):
        if y == 0:
            print('cannot divide by zero')
        else:
            return func(x, y)
    return inner()
  
@decor  
def div(a, b):
    print(a / b)
    
# closure
def outer():
    x = 10
    def inner():
        print(x)
    return inner

    
    