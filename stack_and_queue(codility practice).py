#kodingan ini dibuat untuk menjadi latihan logic programming
#untuk masalah yang akan diselesaikan bisa di lihat di tautan berikut : 
#https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/


def solution(S):
    # write your code in Python 3.6
    contain =[['(','{','['],[')','}',']']]
    n=(len(S))/2
    t=[]
    for i in range(int(n)+1):
        t.append('')
    if S=='':
        return 1
    if len(S)%2 ==1:
        return 0
    if S[0] not in contain[0] :
        return 0
    if S[len(S)-1] not in contain[1]:
        return 0
    x = contain[0].index(S[0])
    u = contain[1].index(S[len(S)-1])
    if u!=x:
        return 0
    
    lastindex=0
    counter=0
    z=0
    for i in range(len(S)):
        if i == 0:
            t[0]=S[i]
            lastindex=i
            counter = counter+1    
        else:
            if S[i] in contain[0]:
                lastindex=counter-1
                t[lastindex+1]=S[i]
                counter=counter+1
            else:
                lastindex=counter-1
                if lastindex <0 :
                    z=1
                    return 0 
                    break
                w = contain[1].index(S[i])
                r = contain[0].index(t[lastindex])
                
                if w!=r:
                    z=1
                    return 0
                    break
                t[lastindex]=''
                counter=counter-1
        if z == 1:
            break
    
    if t[0]!='' :
        return 0
    if z==1:
        return 0
    else:
        return 1

##contoh
S='{}(){{}}{{(())}}'


print(solution(S))
