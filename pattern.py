def calc(num1, c="x"):
    for k in range(0, num1):
        for j in range(0, 4):
            print(c.center(100, " "))
            c = c+"*"+"x"
        c = c[1:len(c)-5]
    for i in range(0, 2):
        print("*".center(100, " "))
    print(c.center(100, " "))


num1 = int(input("enter the height  of christmas tree:"))
calc(num1)
