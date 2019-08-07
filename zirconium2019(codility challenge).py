#ini kodingan untuk menjawab tantangan dari situs codility 
#untuk lebih lengkap tentang soalnya bisa mengunjungi https://app.codility.com/programmers/task/dream_team/



def solution(A, B, F):
	# write your code in Python 3.6
	C=[]
	for i in range(len(A)):
		C.append(A[i]-B[i])
	D=[]
	v=0
	N = C.copy()
	x = [A,B,N]
	C.sort(reverse = True)
	
	for i in range(F):
		u = x[2].index(C[i])
		v=v+x[0][u]
		
		for t in range(3):
			del x[t][u]
	
	for i in x[1]:
		v = v+i
		
	return v


#contoh
r = solution([7, 1, 4, 4], [5, 3, 4, 3], 2)
print(r)
