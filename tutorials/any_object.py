

class Any(object):
    def __init__(self, **_dict):
        self.__dict__.update(_dict)
        
    def __str__(self):
        return str(self.__dict__)
        
        

a = Any(whatever = 17, k = 6)


b = Any(doors= 10, windows = 2)


print(a)
print(b)





