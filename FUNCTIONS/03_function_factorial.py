def fact(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    print(fact)

n=int(input("enter the number"))
fact(n)