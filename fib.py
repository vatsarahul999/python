def fib(n):
    a = 0
    b = 1
    n = n - 1
    while(n > 0):
        b = a + b
        a = b - a
        n = n - 1
    return b


print fib(1)
print fib(2)
print fib(3)
print fib(4)
