def fib(number):
    n1 = 0
    n2 = 1
    for x in range(number):
        yield n1
        temp = n1
        n1 = n2
        n2 = temp + n2
    
for i in fib(20):
    print(i)