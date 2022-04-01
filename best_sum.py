def best_sum(target, list_number, memo={}):
    if memo.get(target):
        return list(memo.get(target))
    elif target == 0:
        return []
    elif target < 0:
        return None

    min_bs = None
    for number in list_number:
        remainder = target - number
        bs = best_sum(remainder, list_number, memo)
        if bs is not None:
            bs.append(number)
            if min_bs is None or len(bs) < len(min_bs):
                min_bs = bs

    memo[target] = tuple(min_bs)

    return min_bs

print(best_sum(18,[15,2,1]))
