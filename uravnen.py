import math
a=-5;b=4;c=1# ax*x + bx +c =0

if a==0:
    if b!=0:
        print(f'x1=',-c/b)
    if b==0 and c==0:
        print('mnogo')
else:
    d = b*b - 4*a*c
    if d==0:
        x1=-b/(2*a)
        print(x1)
    elif d>0:
        x1=(-b-math.sqrt(d))/(2*a)
        x2=(-b+math.sqrt(d))/(2*a)
        print(f'diskr=',d,f'; korni=',x1,x2)
    elif d<0:
        print('no abc')

