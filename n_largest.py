import heapq
def n_largest(n, list_number):
    list_number.sort()
    len_list = len(list_number)
    return list_number[len_list - n]

print(n_largest(3,[2,43,53,255,443,234,25,234324,253]))


