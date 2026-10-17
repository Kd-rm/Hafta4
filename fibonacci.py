from itertools import islice,takewhile

def fibonacci():
    a,b = 0,1

    while True:
        yield a
        a,b = b,a + b
g = fibonacci()
print(next(g))
print(next(g))
print(next(g))

u = fibonacci()

print(list(islice(u,12)))
print(list(islice(u,12)))
print(list(takewhile(lambda x: x<100,fibonacci())))