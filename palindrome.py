def palindrome(a):
    return a==a[::-1]
a=input("enter a string:")
if palindrome(a):
    print("it is palindrome")
else:
    print("it is not")    