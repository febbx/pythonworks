text="this is a simple programming question to find word with maximum characters"

#split text to words
words=text.split(" ") #['this', 'is', 'asimple', 'programming', 'question', 'to', 'find', 'word', 'with', 'maximum', 'characters']

# def get_length(w):
#     return len(w)
# print(max(words,key=get_length)) o/p=programming

# srt_wrds=sorted(words,key=get_length,reverse=True) #op appears as per the length of the words(count of words,largest number of words to smallest in num)
# print(srt_wrds)
# ['programming', 'characters', 'question', 'maximum', 'simple', 'this', 'find', 'word', 'with', 'is', 'to', 'a']

#most recursive character
def get_count(w):
    return words.count(w)

frequent_word=max(words,key=get_count)
print(frequent_word)
