s = input()

def nrcs(s):
    count = [0  for i in range(256)]
    l=0
    max = 0
    for i in range(len(s)):
        if count[ord(s[i])] == False:
            count[ord(s[i])] = True
            if(max < (i-l+1)):
                max = i-l+1
        else:
            l=i-1
    return max
print(nrcs(s))

