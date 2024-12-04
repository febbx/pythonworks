users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]
rahul_followers=["rohit","kohli","rishab","rahul"]
sanju_followers=["sanju","rohit","kohli"]
#follow_suggestions=["sanju","pandya","siraj"]

# set_users=set(users)
# set_followers=set(rahul_followers)
# follow_suggestions=set_users.difference(set_followers)
# print(follow_suggestions)

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))
print(mutual_friends)