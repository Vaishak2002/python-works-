s1={10,20,40,50,70}

s2={10,20,30,60,80}


inter_set=s1.intersection(s2)  # intersection

print(inter_set)

union_set=s1.union(s2)  # union

print(union_set)

difference_set=s1.difference(s2)  # difference

print(difference_set)

#remove method

s1.remove(50)  # removes obj 50 from set s1

print(s1)