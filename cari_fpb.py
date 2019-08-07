#ini kodingan untuk mencari FPB (faktor persekutuan terbesar)

def cari_fpb(a):
	#a=[20,30,40]
	a.sort()
	b = len(a)
	c = a[0]
	d=0
	while True:
		d= 0
		for i in a:
			if i%c==0:
				d=d+1
				
		if d==len(a):
			return c
			break
		
		c = c - 1
		
		if c==0 :
			return 'ga ada hasil'
			break


#contoh untuk mencari FPB antara 40,60,80 dan 75
x=[40,60,80,75]
y=cari_fpb(x)
print(y)

#hasilnya adalah 5
