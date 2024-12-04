text="The quick brown fox jumps over the lazy dog"

text_seq=("The quick brown fox jumps over the lazy dog")

alphabet_seq=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

is_pangram=True

for ch in alphabet_seq:

    if ch not in text:
        is_pangram=False

        break

print(is_pangram)