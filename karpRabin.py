def main():
    y = "gcatcgcagagagtatacagtacg"
    x = "gcagagag"
    q=101
    d=256
    karprabin(x, y, d, q)

def karprabin(x, y, d, q):
    m=len(x)
    n=len(y)
    i=0
    j=0
    hx=0
    hy=0
    h=1
    
    for i in range(m-1):
        h=(h*d)%q
    
    for i in range(m):
        hx = (d*hx + ord(x[i]))%q
        hy = (d*hy + ord(y[i]))%q

    for i in range(n-m+1):
        if hx == hy:
            for j in range(m):
                if y[i+j] != x[j]:
                    break
            j=j+1
            if j==m:
                print(i)

        if i < n-m:
            hy=(d*(hy - ord(y[i])*h) + ord(y[i+m]))%q
            
            if hy < 0:
                hy=hy+q

main()