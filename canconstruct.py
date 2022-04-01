def canconstruct(kata, list_kata, memo={}):
    if len(kata) == 0:
        return True
    elif memo.get(kata):
        return memo.get(kata)
    for word in list_kata:
        if len(kata) >= len(word) and word == kata[:len(word)]:
            can_it = canconstruct(kata[len(word):len(kata)], list_kata)
            if can_it:
                memo[kata] = True
                return True
    memo[kata] = False
    return False

print(canconstruct('skateboard',['bo','rd','ate','t','ska','sk','boar']))
