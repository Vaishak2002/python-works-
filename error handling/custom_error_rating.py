def review(rating):

    if rating<0:

        raise Exception("too low")
    
    elif rating>10:

        raise Exception("too high")

    else:

        print("done !")

rating=int(input("enter the rating"))

try:

    review(rating)

except Exception as e:

    print(e)

print("hello")

print("hai")