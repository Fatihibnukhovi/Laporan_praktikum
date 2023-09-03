from operator import *
a = 1
b = 5.0
print('a = {}'.format(a))
print('b = {}'.format(b))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(a, b): {}'.format(func.__name__, func(a, b))) 
