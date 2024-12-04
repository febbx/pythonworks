#given an integer array nums of size n, return the number with the value closed to 0 in nums.if there are multiple answers,return the number with the largest value.
# #input:nums=[-4,-2,1,4,8]
#output=1

num1=[-4,-2,1,4,8]
closest=0
closest_value=sorted(num1, key=lambda x: (abs(x),-x))[0]
print(closest_value)