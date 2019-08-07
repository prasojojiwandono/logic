#kodingan untuk mencari KPK (kelipatan persekutuan terkecil)

def cari_kpk(a):
	a.sort()
	b=len(a)
	c = a[b-1]
	d=0
	e=0
	while True:
		d = d + c
		e=0
		for i in a:
			if d%i == 0:
				e=e+1
			
		if e==len(a):
			return d
			break


#contoh , untuk mencari kpk dari 10,15 dan 24
b=[10,15,24]
a = cari_kpk(b)
print(a)

#hasilnya 120
