a=int(input("Enter number here : ",))
b=False
if a>1:
    for i in range(2,a):
        if (a%i)==0:
            b=True
            break
if b:
    print (a, "is not a prime number")
else:
    print (a,"is a prime number")
