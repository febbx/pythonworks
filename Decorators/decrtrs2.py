def swap_dec(fn):

    def wrapper(n1,n2):

        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    
    return wrapper

def round_dec(fn):

    def wrapper(n1,n2):

        n1=round(n1)
        n2=round(n2)

        return fn(n1,n2)
    
    return wrapper

@round_dec
@swap_dec
def add_num(n1,n2):
    return n1+n2

@round_dec
@swap_dec

def subtraction(n1,n2):
    return n1-n2

@round_dec
@swap_dec

def division(n1,n2):
    return n1//n2

print(add_num(25.02,50.32))
print(subtraction(2.90,86.53))
print(division(10.9,2.4))