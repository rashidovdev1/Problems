# Ikkita butun son kiriting. Kattasini kichigiga bo'lib,natija va qoldiqni chop eting.

a = int(input('a = '))
b = int(input('b = '))

if a > b:
    natija = a // b
    qoldiq = a % b
    print(natija)
    print(qoldiq)
else:
    natija = b // a
    qoldiq = b % a
    print(natija)
    print(qoldiq)