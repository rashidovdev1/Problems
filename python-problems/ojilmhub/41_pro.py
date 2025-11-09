"""Berilgan sondan keyingi tub sonni topadigan dastur tuzing.
agarNsoni tub bo'lsa o'zini chop eting
agarNtub bo'lmasa, undan keyingi tub sonni chop eting"""

#N sonidan 1ta oldingi tub son
n = int(input("N gacha tub sonlar: "))
x = 0
for i in range(2, n):
    tub = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            tub = False
    if tub:
        x = i
print(x)
