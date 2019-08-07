#kodingan ini tentang bilangan prima

#function untuk mencari bilangan prima kurang dari suatu integer (N)

def prima(N):
	a=[2]
	for i in range(N):
		if i > 1:
			q=0
			for b in a:
				if i % b == 0:
					q=1
				if b>(N**(0.5))+1:
					break
			if q==0:
				a.append(i)
	return a
  
#contoh ingin mencari bilangan prima kurang dari seratus
bil_prima_kurang_dari_100 = prima(N)
print(bil_prima_kurang_dari_100)
#hasilnya [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]



###############################################

#function untuk mencari apakah suatu integer N merupakan bilangan prima

def apakah_prima(N):
	a=[2]
	if N <=1 :
		print ('bukan bilangan prima')
	if N==2:
		print('bilangan prima')
	u = 0
	for i in range(N+1):
		if i > 1:
			q=0
			for b in a:
				if b>(N**(0.5))+2:
					print(str(N)+' adalah bilanga prima')
					u=1
					break
				if i % b == 0:
					q=1
					break
				if N % b == 0:
					print(str(N)+' bukan bilangan prima karena bisa dibagi '+str(b))
					u = 1
					break

			if q==0:
				a.append(i)
			if u == 1:
				break
        
#contoh untuk mengetes apakah 69997 adalah bilangan prima

apakah_prima(69997)

#hasilnya 69997 adalah bilanga prima



#contoh lagi untuk mengetes apakah 82307983 adalah bilangan prima

apakah_prima(82307983)

#hasilnya 82307983 bukan bilangan prima karena bisa dibagi 1483
