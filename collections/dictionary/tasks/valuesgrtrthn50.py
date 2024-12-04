# 7. Write a Python program to filter a dictionary, keeping only items with values greater than 50 using dictionary comprehension.

score={"malu":40,"aswathy":50,"kareena":75,"vignesh":40,"ananthu":95}

filtered_scores={k:v for k,v in score.items() if v>50}

print(filtered_scores)