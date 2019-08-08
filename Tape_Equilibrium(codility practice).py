#kodingan ini untuk melatih logic programming
#untuk melihat masalah yang akan disolusikan, bisa ke tautan berikut : 
#https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/


def TapeEquilibrium(b):
	c=[]
	d=0
	e=[]
	f=0
	for i in range(len(b)-1):
		d=d+b[i]
		f=f+b[len(b)-1-i]
		c.append(d)
		e.append(f)
	e.reverse()
	g=[]
	for i in range(len(c)):
		g.append(abs(c[i]-e[i]))
	return(min(g))
	
#contoh ada array [4, 5, 4, -9, 4, -7, 7, 2, -1, 2]
arr = [4, 5, 4, -9, 4, -7, 7, 2, -1, 2]
result = TapeEquilibrium(arr)
print(result)

#hasilnya 3
