def main():
    y = "gcatcgcagagagtatacagtacg"
    n = len(y)
    x = "gcagagag"
    m = len(x)
    bruteForce(x, m, y, n)

def bruteForce(x, m, y, n):
    for i in range(n - m + 1):
        j = 0
        while j < m and x[j] == y[i + j]:
                j = j + 1
        if j >= m:
            print(i)
main()