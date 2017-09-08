def fib(n):
    a = [0,1]
    for i in range (2,n):
        a.append(a[i-2]+a[i-1])
    print a

def fib1(n):
    a, b = 0, 1
    while b <= n :
        a, b = a + b, a
        print b

def fib2(n):
    s = (2,3,6,1,8)
    #a = (n for n in range(0, n + 1))
    for i in s :
        print i

def fib3(n) :
    print [a[0] + a[1] for a in [[b, b+1] for b in range(n)]]

fib3(10)
