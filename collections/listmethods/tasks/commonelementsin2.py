arr1=[2,3,4,5,6]

arr2=[9,4,1,2,5,8]

arr1.sort()
arr2.sort()
p1=0
p2=0
while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        print(arr2[p2])
        p1+=1
        p2+=1

    elif arr1[p1]<arr2[p2]:
        p1+=1

    elif arr1[p1]>arr2[p2]:
        p2+=1