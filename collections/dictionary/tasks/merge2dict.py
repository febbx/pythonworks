# 2. Write a Python program to merge two dictionaries.
d1={"wottagirl": 180,"plum": 325}
d2={"deconstruct": 189,"dermaco":499}
merged={}
d1.update(d2)
merged=d1,d2
print(merged)