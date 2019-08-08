#ini kodingan untuk melatih logic programming
#untuk soal bisa dilihat di tautan berikut:
#https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/


def CariMax(A):
	max_ending = max_slice=0
	for a in range(len(A)):
		max_ending=max(0,max_ending+A[a])
		max_slice=max(max_slice,max_ending)
	return max_slice


#contoh 
Arr = [-1,-2,-1,3,4,-20,-6,1,21,4,-8,20,-90,-10,-2,4,8]
print(CariMax(Arr))

#hasilnya 38
