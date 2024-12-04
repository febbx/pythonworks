# is_perfect_number(number)

def perfect_number(number):

    total=0

    for i in range (1,number):
        
        if number%i==0:
    
            total=total+i

            return "perfect" if total==number else"not perfect"
    
print(perfect_number(6))