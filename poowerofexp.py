
base=int(input("Basse :"))
exp=int(input("Exponent :"))
def exponent(base,exp):
    po=1
    for i in range(exp):
        po=po*base
    print(base,"raises to the power of ",exp ,"is",po)
exponent(base,exp)        