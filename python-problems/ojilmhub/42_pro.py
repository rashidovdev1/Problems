

n = int(input("robot soni: "))
harakatlar = list(map(int, input("xarakatlar: ").split()))

x, y = 0, 0
yonalish = 0

for step in harakatlar:
    if yonalish == 0:
        y += step
    elif yonalish == 1:
        x += step
    elif yonalish == 2:
        y -= step
    elif yonalish == 3:
        x -= step
    yonalish = (yonalish + 1) % 4

print(x, y)
