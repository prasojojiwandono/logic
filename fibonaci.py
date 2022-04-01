def fib(n, memo={}):
    if memo.get(n):
        return memo.get(n)
    if n <=2 :
        return 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]

def fib2(n):
    if n <= 2:
        return 1
    a = 1
    b = 1
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
    return c


    

        

print(fib(995))

print(fib2(995))