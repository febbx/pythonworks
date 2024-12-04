# 9. Write a dictionary comprehension to convert all the values in a dictionary to their absolute values.

name=["feby","joyal","nissy","godson"]

age=[22,24,23,25]

abs_values={name[i]:age[i] for i in range(len(name))}

print(abs_values)