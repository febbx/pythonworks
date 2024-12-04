num1=[-2,1,1]
closest=0
closest_value=sorted(num1, key=lambda x: (abs(x),-x))[0]
print(closest_value)