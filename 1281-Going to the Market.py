n: int = int(input())
while n:
    n -= 1
    noman = {}
    genjam = 0.0

    m: int = int(input())
    while m:
        m -= 1
        item, valor = input().split()
        noman[item] = float(valor)

    p: int = int(input())
    while p:
        p -= 1
        item, nm = input().split()
        genjam += noman[item] * int(nm)

    print('R$ %.2f' % genjam)