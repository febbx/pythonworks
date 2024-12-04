lst1=["apple","mango","onion","potato",]
lst2=[100,200]


result={}

for i in range(0,len(lst2)):

    list_1_index=lst1[i]
    list_2_index=lst2[i]

    result[list_1_index]=list_2_index

balance_elemnts=lst1[len(lst2):]

for index,element in enumerate(balance_elemnts):

    result[element]=index+1

print(result)