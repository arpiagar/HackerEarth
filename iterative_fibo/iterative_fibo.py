def fibo(n):
    a = 0
    b = 1
    count  = 2
    
    if n ==0 or n==1:
        print n
        return n
    else:
        print a
        print b
        a = 1
        while count <= n:
            a,b = b,a+b
            print a
            count += 1
    return a
#fibo(0)
#fibo(1)
fibo(3)