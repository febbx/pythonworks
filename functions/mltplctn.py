def multiplication_table(number,n):

    for i in range(1,n+1):

        j=i*number

        print(f"{i} * {number} = {j}")

multiplication_table(3,20)