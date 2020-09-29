'''
imagine there is a staircase that have N step,
where N is whole positif integer.
and you are given an array x that consist some positif integer,
and that array represent the number of step that you allow to move.
find the number of possible ways of move in staircase.
for example
there a staircase that have 4 step,
and you are give array [1, 3] , meaning you can only go to staircase 1 step
or 3 step
the number of possible ways of move in staircase is 3.
because
first move is you go to step1, and then step2, and then step3, and then step4 (you move 1 step each time)
second move is you go to step1, and then step4 (because you move 1step and then 3step)
third move is you go to step3, and then step4 (because you move 3step and then 1step)
'''

def helper(n, x, memo):
    if n == 1 or n == 0:
        return 1
    if memo[n] != None:
        return memo[n]
    total = 0
    for i in x:
        if n-i >= 0:
            total += helper(n-i, x, memo)
    memo[n] = total
    return total

def num_ways(n, x):
    memo = [None] * (n+1)
    return helper(n, x, memo)

x = [1,3,5]
num_way_to_move = num_ways(10,x)
print(num_way_to_move)