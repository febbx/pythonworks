arr=[10,20,25,30,40,50]

search_element=int(input("enter the num:"))


low=0
upp=len(arr)-1

while(low<=upp):
    
    mid=(low+upp)//2

    if search_element==arr[mid]:
        is_present=True
        break

    elif search_element<arr[mid]:
        upp=mid-1

    elif search_element>arr[mid]:
        low=mid+1

print(is_present)