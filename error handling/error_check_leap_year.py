def is_leap_year(year):

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        return True
    
    else:

        return False
    
def test_if_leapyear():

    assert is_leap_year(2024)==True,"non century year check failed"

    assert is_leap_year(2025)==False,"invalid noncentury check failed"

    assert is_leap_year(2000)==True,"century year check failed"

    assert is_leap_year(1900)==False,"invalid centuary year check failed"

    assert is_leap_year(-2029)==False,"invalid year check failed"

try:

    test_if_leapyear()

    print("test case passed")

except Exception as e:

    print("test failed",e)