#untuk permasalahan yang akan dipecahkan dalam kodingan ini dapat dilihat selengkapnya di 
#https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/


def solution(A):
    if len(A) ==1:
        return A[0]
    A.sort()
    p=0
    
    for i in range(len(A)):
        if i==0 :
            p=1
        if i>0:
            if A[i]==A[i-1]:
                p=p+1
            else:
                if p%2==1:
                    return A[i-1]
                else:
                    p=1
    return A[len(A)-1]


# contoh
a=[1,2,3,4,5,1,6,5,4,6,3]                
print(solution(a))   
#hasilnya 2
