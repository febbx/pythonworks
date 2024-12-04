# text="malayalam"
# #indx:012345678
# #leng:123456789
    # length=len(text)-1
    # reversed_str=""

# for i in range(length,-1,-1):
#     reversed_str+=text[i]
# print(reversed_str)


text="hellopython"
index=text.index("o")
reversed_text=text[text.index("o")-1::-1]
balance_text=text[text.index("o"):]
result=reversed_text+balance_text
print(result)