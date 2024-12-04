# 8. Given a sentence, count the frequency of each word using a dictionary.

words=["welcome to ootty nice to meet you"]
word_count={}
for ch in words:
    print(ch)
word_frequency={w:words.count(w) for w in words}
print(word_frequency)