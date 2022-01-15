a=float(input("Enter First number here : ",))
b=float(input("Enter Second number here : ",))
c=float(input("Enter Third number here : ",))
if (a>b) and (a>c):
    print("The largest number is : ", a)
elif (b>a) and (b>c):
    print("The largest number is : ", b)
elif (a==b==c) :
    print("The numbers are equal")
else :
    print("The largest number is : ", c)