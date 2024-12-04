text="ABBACD"

for ch in text:
    text_dic={}

for ch in text:
    if ch in text_dic:
        text_dic[ch]+=1

    else:
        text_dic[ch]=1
        
print(text_dic)

#first recursive character