orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]
order_summary={}

for ord in orders:

    if ord in order_summary:

        order_summary[ord]+=1

    else:
        
        order_summary[ord]=1

print(order_summary)