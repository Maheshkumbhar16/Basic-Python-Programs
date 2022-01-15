'''
Fibonacci sequence is the integer sequence of
0,1,1,2,3,5,8,........
The first 2 terms are 0,1. All other terms obtain by adding the preceding two terms.
the nth term is the sum of (n-1) and (n-2)
'''

a= int(input("Enter the number of terms :",))
num1=0
num2=1
count=0

if a<=0:
    print("Enter positive Integer")
elif a==1:
    print("Fibonacci sequence upto", a, "is\n", num1)
else :
    print("Fibonacci sequence:") 
    while count < a:
        print(num1)
        num=num1+num2
        num1=num2
        num2=num
        count +=1
        #print (num)