'''
The roots of quadratic equation ax**2+bx+c=0 are
m = (-b + ((b**2) - (4*a*c))**0.5) / (2*a)
n = (-b - ((b**2) - (4*a*c))**0.5) / (2*a)
'''
#type one (solution in format of i and j)
'''
import cmath
#a=1
#b=5
#c=6

#user define parameters
a=float(input('Enter a from equation ax**2+bx+c=0:'))
b=float(input('Enter b from equation ax**2+bx+c=0:'))
c=float(input('Enter c from equation ax**2+bx+c=0:'))

d=(b**2) - (4*a*c)
m = (-b-cmath.sqrt(d))/(2*a)
n = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(m,n))
'''

#type second format int
#a=1
#b=5
#c=6

#user define parameters
a=float(input('Enter a from equation ax**2+bx+c=0:'))
b=float(input('Enter b from equation ax**2+bx+c=0:'))
c=float(input('Enter c from equation ax**2+bx+c=0:'))

d=(b**2) - (4*a*c)
m = (-b-(d**0.5))/(2*a)
n = (-b+(d**0.5))/(2*a)
print(m,n)