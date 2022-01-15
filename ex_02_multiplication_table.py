a=int(input("Enter Number Here :",))

if a==0:
    print ("Sorry")
elif a<0:
    print("Enter positive value")
else :
    print ("Multiplication Table of ", a, ":")
    for i in range(1,11):
        print (a ,"X", i, "=", a*i)