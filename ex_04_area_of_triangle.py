#area of triangle for all three sides are known
'''
s=(a+b+c)/2
area= square root of (s*(s-a)*(s-b)*(s-c))
'''

#a=3
#b=4
#c=5
'''
#user define parameters
a=float(input('Enter first side:'))
b=float(input('Enter second side:'))
c=float(input('Enter third side:'))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('Area of triangle is: ', area)
'''

#area of triangle for base and height are known
'''
area = 0.5*b*h
'''
'''
#b=5
#h=8

#user define parameters
b=float(input('Enter base side:'))
h=float(input('Enter height side:'))

area=0.5*b*h
print('Area of triangle is: ', area)
'''

#area of equilateral triangle
'''
b=a*a*a*a
area=(3*b/16)**0.5
'''
'''
#a=5

#user define parameters
a=float(input('Enter side:'))

b=a*a*a*a
area=(3*b/16)**0.5
print('Area of triangle is: ', area)
'''

#area of isoscles triangle
'''
area=((4*a*a-b*b)**0.5)*b/4
'''
#a=4
#b=5

#user define parameters
a=float(input('Enter equal side:'))
b=float(input('Enter base side:'))

area=((4*a*a-b*b)**0.5)*b/4
print('Area of triangle is: ', area)