text="ABAABBBC"
#most recursive char
def get_count(ch):
    return text.count(ch)
most_freq_ch=max(text,key=get_count)
print(most_freq_ch)

#least recursive char
def get_count(ch):
    return text.count(ch)
least_freq_ch=min(text,key=get_count)
print(least_freq_ch)

#most recursive
#non recursive