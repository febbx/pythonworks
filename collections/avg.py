expenses=[100,200,300,400,500]

sum=0
avg=0

count=len(expenses)

for exp in expenses:

    sum+=exp

avg=sum//count

print(avg)