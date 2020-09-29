#untuk permasalahan yang akan dipecahkan dalam kodingan ini dapat dilihat selengkapnya di 
#https://app.codility.com/programmers/lessons/1-iterations/binary_gap/


def BiggestBinaryGap(a):
    c = a
    d=[]
    while True:
        x=0
        while True:
            if 2**x > c:
                break
            x=x+1
        e = x
        d.append(e)
        if e==1 or e == 0:
            break
        c = c-(2**(e-1))
    w=d
    r=[]
    for i in range(len(w)-1):
        if w[i]>0 and w[i+1]>0 :
            c=(w[i]-w[i+1])-1
            r.append(c)

    if r==[] :
        e=0
        return e
    else:
        r.sort()
        e=r[len(r)-1]
        return e

#contoh
print(BiggestBinaryGap(97608))   
#hasilnya 2
