'''
in this problem you are given a mapping like
a = '1'
b = '2'
c = '3'
......
z = '26'
and you are given a string that only contain positif integer.
create the function that find the possible number of ways
that the string can map to the alphabet.
for example
string of integer = '12345'
possible mapping to alphabet are 'abcde' or 'lcde' or 'awde'
so there 3 possible mapping to alphabet,
therefore the answer is 3

def solution(string_of_integer):
    #your code
'''


def helper(data, k, memo):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == '0':
        return 0
    if memo[k] != None:
        return memo[k]
    result = helper(data, k-1, memo)
    if k>=2 and int(data[s:s+2]) <= 26:
        result += helper(data, k-2, memo)
    memo[k] = result
    return result

def num_ways(data):
    memo = [None] * (len(data) + 1)
    return helper(data,len(data), memo)


print(num_ways('1321321'))
#result 12


