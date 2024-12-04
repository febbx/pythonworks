#1 *  *  *
#2 *  *  *
#3 *  *  *
#4 *  *  *
#5 *  *  *
#6 *  *  *


# for row in range(1,7):

#     for col in range(1,4):

#         print("*",end="\t")

#     print()


#next
# $
# $ $
# $ $ $
# $ $ $ $
# $ $ $ $ $
# $ $ $ $ $ $

# for row in range(1,7):
#     for col in range(1,row+1):

#         print("$",end="\t")

#     print()


#next



for row in range(1,6):

    for col in range (5,row-1,-1):

        print("*",end="\t")
    print()