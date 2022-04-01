import ipdb
def check_anagram(kata1, kata2):
    if len(kata1) != len(kata2):
        return False
    kata1 = [i for i in kata1]
    kata2 = [i for i in kata2]
    len_kata = len(kata1)
    for x in range(len_kata):
        first_word = kata1[0]
        if first_word in kata2:
            kata1.remove(first_word)
            kata2.remove(first_word)
        else:     
            return False
    return True

def check_anagram2(kata1, kata2):
    if len(kata1) != len(kata2):
        return False
    for k1 in kata1:
        if not(k1 in kata2):
            return False
    return True

def check_anagram3(kata1,kata2):
    if len(kata1) != len(kata2):
        return False
    return sorted(kata1) == sorted(kata2)

print(check_anagram3('danger','garden'))
