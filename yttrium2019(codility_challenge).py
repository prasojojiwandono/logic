#kodingan ini untuk menjawab tantangan dari situs codility dan nama tantangan yttrium 2019
#untuk lebih lengkap tentang soalnya bisa mengunjungi https://app.codility.com/programmers/task/different_characters/

def solution(S, K):
	a=[b for b in S]
	aw = 0
	ak = 0
	ko = 96 + K
	for i in range(len(a)):
		aw = aw + 1
		if ord(a[i])>ko :
			break
	for i in range(len(a)):
		ak = ak + 1
		if ord(a[len(a)-1-i]) > ko:
			break
	if ak+aw -2 >= len(a):
		return -1
	else :
		return len(a)-(ak+aw-2)
	

####contoh - contoh 

S = "abaacbca"
K = 2
a = solution(S,K)
print(a)
#hasilnya 3


S = "aabcabc"
K = 1
a = solution(S,K)
print(a)
#hasilnya 5


S = "zaaaa"
K = 1
a = solution(S,K)
print(a)
#hasilnya 1


S = "aaaa"
K = 2
a = solution(S,K)
print(a)
#hasilnya -1
