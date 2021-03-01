from csmodel.eval import *


ev = Eval()


print(ev('with', 2,4))

print(ev('with', bool,4))

print(ev('with', False,4))

# boolean checks:

print(ev('with', bool,False))

print(ev('with', False,bool))

print(ev('with', False,True))


print(ev('with', True,True))


# set checks :

print(ev('with', {2,3},10))

print(ev('with', {2,3},2))

print(ev('with', {2,3,4},{4,5,6}))

print(ev('with',10, {2,3}))

print(ev('with',2 , {2,3}))


# check that original sets do not change :
a = {2,3,4}

b = {4,5,6}

print(ev('with',a , b ))

print(ev('with',2 , b ))

print(ev('with',b, 10 ))

print(ev('with',5, a ))

print(ev('with',a, 12 ))


assert a == {2,3,4}
assert b == {4,5,6}
