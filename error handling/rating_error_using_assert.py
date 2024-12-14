def review(rating):

    assert rating>0, "too low"

    assert rating in range(0,11),"too high"

    print("rated")

rating=int(input("enter the rating"))

try:

    review(rating)

except Exception as e:

    print(e)