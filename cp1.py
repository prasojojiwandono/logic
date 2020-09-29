'''
you're given 2 array and an integer c,
each array have same number of item,
and inside both array consist whole number,
find (a,b), whereas a is item of the first array,
and b is the item of second array, that a + b have
the value that equal to c , if a + b does not equal to c
find the closest result to c , example
array_a = [3,7,17,10,20,13,1]
array_b = [30,15,12,6,11,-5,9]
c =  21
then result is (10,11)
write a function that satisfy the problem above
def solution([array_a],[array_b],c):
    # your code
    return (a,b)
'''


def solution(array_a, array_b, c):
    array_a.sort()
    array_b.sort()

    for x in range(len(array_a)):
        add_value = array_a[x] + array_b[x]
        if add_value >= c:
            if x > 0:
                if add_value == c:
                    return (array_a[x],array_b[x])

                y = x
                selisih = pow(10,20)
                arr = [0,0,selisih]
                while y >= 0:
                    # ke kiri
                    add_value2 = array_a[y-1] + array_b[x]
                    arr2 = [array_a[y-1], array_b[x], abs(c - add_value2)]
                    arr_mix =[arr, arr2]
                    if abs(c - add_value2) != selisih:
                        selisih = min(abs(c - add_value2),selisih)
                        arr = [x for x in arr_mix if x[2] == selisih][0]

                    # ke atas
                    add_value2 = array_a[x] + array_b[y-1]
                    arr2 = [array_a[x], array_b[y-1], abs(c - add_value2)]
                    arr_mix = [arr, arr2]
                    if abs(c - add_value2) != selisih:
                        selisih = min(abs(c - add_value2), selisih)
                        arr = [x for x in arr_mix if x[2] == selisih][0]

                    y -= 1

                y = x - 1
                while y < len(array_a)-1:
                    #ke kanan
                    add_value2 = array_a[y + 1] + array_b[x]
                    arr2 = [array_a[y + 1], array_b[x], abs(c - add_value2)]
                    arr_mix = [arr, arr2]
                    if abs(c - add_value2) != selisih:
                        selisih = min(abs(c - add_value2),selisih)
                        arr = [x for x in arr_mix if x[2] == selisih][0]

                    #ke bawah

                    add_value2 = array_a[x] + array_b[y + 1]
                    arr2 = [array_a[x], array_b[y+1], abs(c - add_value2)]
                    arr_mix = [arr, arr2]
                    if abs(c - add_value2) != selisih:
                        selisih = min(abs(c - add_value2), selisih)
                        arr = [x for x in arr_mix if x[2] == selisih][0]

                    y+=1

                return (arr[0], arr[1])

            else:
                if add_value == c:
                    return (array_a[x], array_b[x])

                y = 0
                while y < len(array_a):
                    # ke kanan
                    add_value2 = array_a[y + 1] + array_b[x]
                    arr2 = [array_a[y + 1], array_b[x], abs(c - add_value2)]
                    arr_mix = [arr, arr2]
                    if abs(c - add_value2) != selisih:
                        selisih = min(abs(c - add_value2), selisih)
                        arr = [x for x in arr_mix if x[2] == selisih][0]

                    # ke bawah

                    add_value2 = array_a[x] + array_b[y + 1]
                    arr2 = [array_a[x], array_b[y + 1], abs(c - add_value2)]
                    arr_mix = [arr, arr2]
                    if abs(c - add_value2) != selisih:
                        selisih = min(abs(c - add_value2), selisih)
                        arr = [x for x in arr_mix if x[2] == selisih][0]

                    y += 1

                return (arr[0], arr[1])
        elif x == len(array_a)-1:
            return (array_a[x],array_b[x])



array_a = [3,7,17,10,20,13,1]
array_b = [30,15,12,6,11,-5,9]
c = 21
x = solution(array_a, array_b, c)
print(x)

from random import  randint,randrange

jangkauan = 10000
array_p = [randrange(-10000,10000,1) for i in range(jangkauan)]
array_q = [randrange(-10000,10000,1) for i in range(jangkauan)]
r = randint(-10000,10000)
s = solution(array_p,array_q,r)

print(s)




