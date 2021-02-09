

def  until(iterable, fn, fn_alter, args_before, args_after,return_break, return_end):
    
    for item in iterable: 
        if fn_alter(fn(*args_before, item, *args_after)):
            return return_break
    return return_end


def and_all(iterable,fn,args_before = [], args_after = []):
    
    return until(iterable,fn,lambda x : not x ,args_before, args_after,False, True )


def or_all(iterable,fn,args_before = [], args_after = []):
    
    return until(iterable,fn,lambda x : x ,args_before, args_after,True, False )
    
    
    
arr = [1,2,3,4,5]


print(or_all(arr, lambda x: x < 0))
print(or_all(arr, lambda x: x < 4))
print(and_all(arr, lambda x: x > 0))
print(and_all(arr, lambda x: x < 4))




