from typing import List

n = int(input())
check = 0

while n:
    n -= 1
    m, c = [int(x) for x in input().split()]
    mou = {str(x): [] for x in range(m)}
    moni: List[int] = [int(x) for x in input().split()]

    if check:
        print()

    for i in moni:
        noman = i % m
        mou[str(noman)].append(int(i))

    for i in mou:
        print('%d -> ' % int(i), end='')
        for j in mou[i]:
            print('%d -> ' % j, end='')
        print('\\')

    check = 1
