while True:
    try:
        abul = float(input())
        hasan = float(input())
        frnd = hasan / 2
        total = 3.14 * frnd * frnd
        alt = abul / (frnd * frnd * 3.14)
        print('ALTURA = %.2f' % alt)
        print('AREA = %.2f' % total)

    except EOFError:
        break