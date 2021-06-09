from lrucache import LRUCache
import time


def timer(func):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def lrucache(func):
    cache = LRUCache(5)
    def wrapper(*args, **kargs):
        key = str(args)
        result = cache.get(key)

        if result == -1:
            result = func(*args, **kargs)
            cache.set(key, result)

        return result

    return wrapper



@lrucache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n-2)



@timer
def timeFibonacci():
    for i in range(1000):
        fib(i)
    print(f"Fibonacci {i+ 1} = {fib(i+1)}")


timeFibonacci()


