def grid_traveler(m, n, memo={}):
    if m == 1 and n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    elif memo.get(f'{str(m)},{str(n)}'):
        return memo.get(f'{str(m)},{str(n)}')
    elif memo.get(f'{str(n)},{str(m)}'):
        return memo.get(f'{str(n)},{str(m)}')
    else:
        memo[f'{str(m)},{str(n)}'] = grid_traveler(m-1,n) + grid_traveler(m, n-1)
        return memo[f'{str(m)},{str(n)}']

print(grid_traveler(18,18))