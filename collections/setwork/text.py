text1="this is a test to remove duplicate words this test is simple"
words1=text1.split(" ")
# print(set(words))

text2="this simple test remove duplicate words"
words2=text2.split(" ")
print(set(text2).issubset(text1))