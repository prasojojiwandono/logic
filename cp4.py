#first recurring character

def solution(char):
    for x in range(len(char)-1):
        if char[x+1] in char[0:x+1]:
            return char[x+1]


char = 'kahdiuheofhrv'
dd = solution(char)
print(dd)