# custom error handling using "assert" 
# here the 'error message' is 'called' after the 'condition given becomes false'

def poll(age):

    assert age>18, "invalid age"

    print("voted")

try:

    poll(14)

except Exception as e:

    print(e)
