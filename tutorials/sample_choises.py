import random as r 


arr = [x for x in range(10)]

ch = r.sample(arr, 7)

print(ch)


ch = r.choices(arr, k=7)

print(ch)