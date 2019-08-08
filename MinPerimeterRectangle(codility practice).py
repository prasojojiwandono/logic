#ini kodingan untuk melatih logic programming
#untuk soal bisa dilihat di tautan berikut :
#https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/min_perimeter_rectangle/


def solution(N):
	# write your code in Python 3.6
	if N ==0:
		return 0 
	a=[]
	u = 0
	for i in range(N+1):
		if i>0 :
			if N % i==0 and i <= N**(0.5):
				a.append(i)
			if i>N**(0.5):
				u = 1
				break
		if u==1:
			break
	b = len(a)
	c = a[len(a)-1]
	perimeter = (c+(N/c))*2
	return int(perimeter)


# contoh inputnya adalah 30
luas = 30
keliling_terkecil = solution(luas)
print(keliling_terkecil)

#hasilnya 22
   
   
   
 
