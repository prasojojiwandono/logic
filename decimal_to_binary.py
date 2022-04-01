def d_to_b(number):
    b_list = []
    while number > 0:
        b_list.append(number%2)
        number = number//2
    b_list.reverse()
    return b_list

print(d_to_b(16))
