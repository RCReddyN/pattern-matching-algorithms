def main():
    y = input()
    n = len(y)
    x = input()
    m = len(x)
    morrisPratt(x,m,y,n)


def morrisPratt(x, m, y, n):
    i=0
    j=0
    mpNext = [0 for i in range(m+1)]
    preMorrisPratt(x, m, mpNext)
    while j < n:
        while i > -1 and x[i] != y[j]:
            i=mpNext[i]
        i=i+1
        j=j+1
        if i >= m:
            print(j-i)
            i = mpNext[i]

def preMorrisPratt(x, m, mpNext):
    i=0
    j=-1
    mpNext[0]=-1
    while i < m:
        while j>-1 and x[i] != x[j]:
            j = mpNext[j]
        mpNext[i] = j
        i=i+1
        j=j+1
    print(mpNext)
main()