from csmodel.eval import *


ev = Eval()




print(ev('+', 10, 20))

assert ev('+', 10, 20) == 30

print(ev('-', 10, 20))

assert ev('-', 10, 20) == -10

#FOLLOWS TEST:

print(ev('->', True, False))
print(ev('->', True, True))
print(ev('->', False, False))
print(ev('->', False, True))

print(ev('->', True, bool))
print(ev('->', False, bool))
print(ev('->', bool, True))
print(ev('->', bool, False))
print(ev('->', bool, bool))

# in test:


assert ev('in', 4, {2,3,4,5})

assert ev('in', 4, int)

assert ev('in', 4, 4)

assert ev('in', True, bool) 

assert ev('in', False, bool) 

assert ev('in', int, int) 

assert ev('in', bool, bool) 

assert  ev('in', {True, False}, bool)

assert  ev('in', {True, False}, {True, False})

assert  ev('in',  False, {True, False})



assert ev('in', int, int) 

assert  ev('in', {1,2,3,5,6}, int)

assert  ev('in', {2,3,5}, {1,2,3,5,6})




assert not ev('in', 4, {2,3,5})

assert not ev('in', 4, float)

assert not ev('in', 4, 3)

assert not ev('in', bool, False)

assert not ev('in', False, int)
# python returns isinstance (False, int) is True


assert  not ev('in',  False, { True})

assert not ev('in', {1,2,3.3,5,6}, int)

assert  not ev('in', {2,3,5}, {1,2,3,4})

