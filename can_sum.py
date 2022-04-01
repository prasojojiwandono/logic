def can_sum(target, list_number, memo={}):
    if target == 0:
        return True
    if target < 0 :
        return False
    if memo.get(target):
        return memo.get(target)
    for n in list_number:
        remainder = target - n
        if can_sum(remainder, list_number) == True:
            memo[target] = True
            return True
    memo[target] = False
    return False
    
print(can_sum(345,[3,31,5,7,8,2,21]))