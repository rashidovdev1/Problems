"""Berilgan sondan keyingi tub sonni topadigan dastur tuzing.
agarNsoni tub bo'lsa o'zini chop eting
agarNtub bo'lmasa, undan keyingi tub sonni chop eting"""

#N sonidan keyingi 1-tub son
n = int(input("N ni kiriting: "))

i = n + 1
while True:
    tub = True
    if i >= 2:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                tub = False
                break
    else:
        tub = False

    if tub:
        print(i)
        break
    i += 1


