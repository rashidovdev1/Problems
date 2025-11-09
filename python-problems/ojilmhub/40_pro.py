"""Berilgan son biror boshqa sonni faktoriali yoki yo'qligini aniqlaydigan dastur tuzing.
AgarNbiror boshqaxsonning faktoriali bo'lsatruedeb, aks holdafalsechop eting.
"""
x = int(input("Sonni kiriting: "))
n = 1
fakt = 1

while fakt < x:
    n += 1
    fakt *= n

if fakt == x:
    print(f"{x} bu {n}! faktoriali True")
else:
    print("False bu faktoriali emas")