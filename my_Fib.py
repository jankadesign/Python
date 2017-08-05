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
 a = [0,1]
 a.append(a[i-2]+a[i-1] for i in range(2,n))
 print a

fib2(10)
