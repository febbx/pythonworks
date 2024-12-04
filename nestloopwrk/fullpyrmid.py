# for i in range(1,6):

#     print('   ' *  (5-i),end='  ')

#     print( ' * ' * (2*i-1))

for row in range(1,8):

    for sp in range(1,8-row):

        print("   ",end="")

    for col in range(1,row+1):

        print(" *    ",end="")

    print()