#  turishi kerak bo'lgan vaqtni anglatuvchi ikki butun sonlarSvaM(0 ≤ S ≤ 23, 0 ≤ M ≤ 59).

s = int(input('soat = '))
m = int(input('minut = '))

print(s, end=' ')
print(m)
if s == 0:
    s = 24
daq = s * 60 + m
print(daq)
clock = (daq - 45) % 60
clock1 = (daq - 45) // 60
print(clock1, end=' ')
print(clock)
