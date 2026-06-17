#using a try and except
try:
    numb=int(input("enter a number: "))
    print("the number entered is", numb)
#using value error
except ValueError as ex:
    print("Exception", ex)
    