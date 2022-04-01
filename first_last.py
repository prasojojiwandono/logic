def first_last(number, list_number):
    first = list_number.index(number)
    len_list = len(list_number)
    list_number.reverse()
    last = len_list - list_number.index(number) - 1
    return [first, last]

print(first_last(5,[2,4,5,5,5,5,5,7,9,9]))
