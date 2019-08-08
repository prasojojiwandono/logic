#kodingan ini untuk melatih logic programming
#untuk soal yang akan diselesaikan bisa dilihat di tautan berikut:
#https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

def solution(A):
	A.sort()
	if min(A) == 1 :
		pass
	else:
		return 0
	for i in range(len(A)):
		if i > 0 and A[i]!=A[i-1]+1:
			return 0
	return 1
	

#contoh

a=[1,1,1,3,4,5]
print(solution(a))
#hasilnya 0


b=[1,2,3,4,5]
print(solution(b))
#hasilnya 1

