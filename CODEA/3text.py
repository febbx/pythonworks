text="hello world hai everyone welcome to the world"

words=text.split(" ")

most_freq_word={w:words.count(w) for w in words}

print(max(most_freq_word))