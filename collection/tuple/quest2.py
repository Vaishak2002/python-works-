users=["kohli","rohith","siraj","rishabh","sanju","pandya"]

rahul_folloers=["rohith","kohli","rishabh","rahul"]

sanju_followers=["sanju","rohith","kohli"]

user_set=set(users)

rahul_folloers_set=set(rahul_folloers)

follow_suggestions=user_set.difference(rahul_folloers_set)

print(follow_suggestions)

common=rahul_folloers_set.intersection(set(sanju_followers))

print(common) 