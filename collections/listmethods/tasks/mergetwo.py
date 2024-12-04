arr1=[1,2,3]
arr2=[4,5,6]

for i in range(0,len(arr2)):

    arr1.append(arr2[i])

arr1.sort()

print(arr1)
