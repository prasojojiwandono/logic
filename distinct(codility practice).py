#kodingan ini untuk melatih logic programming
#untuk soal bisa dilihat di https://app.codility.com/programmers/lessons/6-sorting/distinct/


def solution(A):
	n=0
	b = set(A)
	for i in b:
		n=n+1
	return n
  
 #contoh 
 arr = [-10, 4, 2, 1, 1, -6, -4, 1, 4, -3, 0, 3, -9, 7, 3, 6, -5, -10, 7, -3]
 print(solution(arr))
 
 #hasilnya 13
