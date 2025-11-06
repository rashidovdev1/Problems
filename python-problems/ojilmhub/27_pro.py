#  turishi kerak bo'lgan vaqtni anglatuvchi ikki butun sonlarSvaM(0 ≤ S ≤ 23, 0 ≤ M ≤ 59).

S, M = map(int, input("Soat va minutni kiriting: ").split())

total = S * 60 + M

total -= 45

if total < 0:
    total += 24 * 60

S = total // 60
M = total % 60

print(S, M)

