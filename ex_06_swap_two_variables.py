#x=5
#y=10

#user defined data
x=int(input("Enter value of X:", ))
y=float(input("Enter value of Y:", ))

#print ('Value of X is: {}'.format(x),'\nValue of Y is: {}'.format(y))

a=x
x=y
y=a
print ('Value of X after swapping is: {}'.format(x),'\nValue of Y after swapping is: {}'.format(y))