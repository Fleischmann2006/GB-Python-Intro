class ZeroDiv(Exception):
    def __str__(self):
        return 'Zero division error!'


while True:
    try:
        a, b = int(input('Enter dividend: ')), int(input('Enter divisor: '))

        if b == 0:
            raise ZeroDiv
    except (ValueError, ZeroDiv) as er:
        print(er)
    else:
        print(round(a / b, 2))
        break

    print('Try again!')
