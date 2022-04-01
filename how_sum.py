def how_sum(target, list_number, memo={}):
    if target ==  0:
        return 1
    elif target < 0 :
        return 0
    elif memo.get(target):
        return memo.get(target)
    x = 0
    for n in list_number:
        remainder = target - n
        x = x + how_sum(remainder, list_number)
    if x > 0:
        memo[target] = x

    return x

def how_sum2(target, list_number):
    if target == 0:
        return []
    elif target < 0:
        return None
    
    for n in list_number:
        remainder = target - n
        res = how_sum2(remainder, list_number)
        if res is not None:
            res.insert(len(res),n)
            
            return res
    return None

print(how_sum(17,[1,15]))
print(how_sum2(17,[15,1]))