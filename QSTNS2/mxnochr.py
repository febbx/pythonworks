text="this is a simple question return word with maximum number of characters"

words=text.split()

def get_length(word):

    return len(word)

print(max(words,key=get_length))