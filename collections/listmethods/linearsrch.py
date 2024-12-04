arr=[2,4,6,3,8,7]

srch_elmnt=int(input("enter the num:"))

is_present=False

for i in range(0,len(arr)):

    if arr[i]==srch_elmnt:

        is_present=True
        break
print(is_present)