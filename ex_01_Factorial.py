'''
factorial of n =
1*2*3*............*(n-1)*n
'''

a=int(input("Enter Number Here :",))
fact=1
if a<0:
    print ("Factorial does not exist")
elif a==0:
    print ("Factorial is 1")
else:
    for i in range(1, (a+1)):
        fact=fact*i
    print ("Factorial of ", a, "is", fact)