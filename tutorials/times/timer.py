import time 

# i dont like this mess : 

def timed(num_times = 100):
    def decorator(func):    
        def wrapper(*args, **kwargs):
            max_time, min_time = 0.0, float("inf")
            for _ in range(num_times):
                start_time = time.perf_counter()
                value = func(*args, **kwargs)
                end_time = time.perf_counter()
                run_time = end_time - start_time
                min_time = min(min_time, run_time)
                max_time = max(max_time, run_time)
            return min_time, max_time
        return wrapper
    return decorator

@timed()
def spend_time():
    x = 0
    for i in range(1000*1000):
        x += i*i
    return x 

min_time, max_time = spend_time()

print(min_time, max_time)
                
            
         

    