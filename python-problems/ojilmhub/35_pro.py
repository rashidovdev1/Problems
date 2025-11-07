"""Strike-Ballo'yinida 3 ta sonni taxmin qilib topish kerak.
Taxminlar ichidagistrikevaballnechta ekanini topadigan dastur tuzing.
strike- son bir xil ustunda taxmin qilib topilsa
ball- son boshqa ustunda taxmin qilib topilsa"""

x = int(input('1-son: '))
y = int(input('2-son: '))
z = int(input('3-son: '))
sonlar = [x, y, z]

a = int(input('1-taxmin: '))
b = int(input('2-taxmin: '))
c = int(input('3-taxmin: '))
taxmin = [a, b, c]

S, B = 0, 0
for t in range(3):
    if taxmin[t] == sonlar[t]:
        S += 1
    elif taxmin[t] in sonlar:
        B += 1
print(f'{S}S{B}B')



