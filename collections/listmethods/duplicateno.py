# find the duplicate nos

arr=[1,2,2,2,1,4,5,6,9,8]

arr.sort()

duplicate_numbers=[]

for i in range(0,len(arr)-1):
     
     j=i+1
     
     if arr[j]-arr[i]==0:
         
         if arr[i] not in duplicate_numbers:
              
              duplicate_numbers.append(arr[i])
              
print(duplicate_numbers)