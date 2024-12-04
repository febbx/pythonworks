text="this is a simple pythonprogram that print most recursive word.this program is simple"

words=text.split()

word_frequency={w:words.count(w) for w in words}

most_recursive_word=max(word_frequency, key=word_frequency.get)

print(most_recursive_word)