#kodingan ini untuk melatih logic programming
#untuk melihat masalah yang akan diselesaikan , bisa mengunjungi tautan berikut :
#https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/


def solution(A):
	if max(A)<=0:
		return 1
	b=set(A)
	c=[]
	for i in b:
		c.append(i)
	c.sort()
	if 1 not in c:
		return 1
	d=[r for r in c if r>0]
	d.sort()
	if max(d) == len(d):
		return max(d)+1
	for i in range(max(d)):
		if d[i]!=i+1:
			return i+1
			
#contoh 
A = [1, 3, 6, 4, 1, 2]
print(solution(A))

#hasilnya 5
