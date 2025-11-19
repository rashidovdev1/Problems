x1, y1 = map(int, input("A nuqta koordinatalarini kiriting: ").split())
x2, y2 = map(int, input("C nuqta koordinatalarini kiriting: ").split())

uzunlik = abs(x2 - x1)
kenglik = abs(y2 - y1)

perimetr = 2 * (uzunlik + kenglik)
yuza = uzunlik * kenglik

print("Perimetr:", perimetr)
print("Yuza:", yuza)
