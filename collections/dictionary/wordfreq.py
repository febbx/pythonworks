# text="ABBAABCCDE"
# character_frequency={ch:text.count(ch) for ch in text}
# print(character_frequency)

#print non recursive elements
# non_recursive={ch:text for ch in text if text.count(ch)<2}#dict comp chythal it'll show the count.
# print(non_recursive)

    # non_recursive_character=[k for k,v in character_frequency.items() if v==1] #list comprehension is used , vaalues mathy count vnda.
    # print(non_recursive_character)

words=["hello","hai","hello","this","is","hai","is","is"]
word_frequency={w:words.count(w) for w in words}
print(word_frequency)
# recursive_words=[k for k,v in word_frequency.items() if v>1]
# print(recursive_words)

    #display non recursive words
    # non_recursive_words=[k for k,v in word_frequency.items() if v==1]
    # print(non_recursive_words)

#most recursive
most_recursive_words=[k for k,v in word_frequency.items() if v>2]
print(most_recursive_words)