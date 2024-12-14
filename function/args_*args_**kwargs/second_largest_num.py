
def second_largest(*args):

    sorted_num=sorted(args,reverse=True)

    return sorted_num[1]

print(second_largest(10,20,30,40,50))


