prev=0
curr=1
print(prev)
print(curr)

for i in range(1,6):
    next=prev+curr
    prev=curr
    curr=next
    print(next)