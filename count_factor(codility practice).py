#kodingan ini untuk melatih logic programming
#untuk soal bisa dilihat di tautan berikut:
#https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/

def solution(N):
	# write your code in Python 3.6
		# write your code in Python 3.6
	if N ==1:
		return 1
	if N ==2:
		return 2
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
	hasil = 2 * b
	if N%(N**(0.5))==0:
		return hasil-1
	else:
		return hasil
		
		
#contoh, untuk mengetahui banyak faktor dari 24
faktor24= solution(24)
print(faktor(24))

##hasilnya 8 , dan memang faktor dari 24 ada sebanyak 8 yaitu --> 1,2,3,4,6,8,12,24
