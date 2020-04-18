def main():
    y = input()
    n = len(y)
    x = input()
    m = len(x)
    knuthmorrisPratt(x,m,y,n)


def knuthmorrisPratt(x, m, y, n):
    i=0
    j=0
    kmpNext = [0 for i in range(m+1)]
    preKnuthMorrisPratt(x, m, kmpNext)
    while j < n:
        while i > -1 and x[i] != y[j]:
            i=kmpNext[i]
        i=i+1
        j=j+1
        if i >= m:
            print(j-i)
            i = kmpNext[i]
            
def preKnuthMorrisPratt(x, m, kmpNext):
    i = 0
    j = -1
    kmpNext[0] = -1
    while i < m:
        while j > -1 and x[i] != x[j]:
            j = kmpNext[j]
        j = j + 1
        if x[i] == x[j]:
            kmpNext[i] = kmpNext[j]
        else:
            kmpNext[i] = j
        i = i + 1
    print(kmpNext)
main()