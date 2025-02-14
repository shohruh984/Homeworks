import time
import random

class decorator_1:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time 
        print(f"{self.func.__name__} call executed in {execution_time:.4f} sec")

from task1 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i**2)

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [i**2 for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "__main__": 
    func()
    funx()
    func()
    funx()
    func()
