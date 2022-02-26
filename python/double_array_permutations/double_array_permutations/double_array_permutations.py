# given a smaller string and a bigger string
# find all permutations of the smaller string
# in the larger string


def creatDict(s):
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return d

def compareDicts(d1, d2):
    for i in d1:
        if i in d2.keys():
            if d1[i] != d2[i]:
                return False
        else:
            return False
    return True




lilStr = "abbc";
bigStr = "abbcababcbabbac"


lilDict = creatDict(lilStr)

strLen = len(lilStr)

for i in range(len(bigStr) - strLen):
    s = bigStr[i: i + strLen]
    d = creatDict(s)
    if compareDicts(lilDict, d):
        print(str(i) + ": " + s)





    
