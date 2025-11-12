"""Collatzketma-ketligi butun son ustida quyidagi qoidalarni qayta-qayta bajarishdan hosil qilinadi.
agar son juft bo'lsa, sonni 2 ga bo'linadi
agar son toq bo'lsa, sonni 3 ga ko'paytirib 1 ni qo'shiladi
Collatz algoritmida barcha butun musbat sonlar uchun son doimo 1ga yetib boradi.
Ikkita butun sonlar kiritilganda, qaysi biri 1ga ertaroq yetishini aniqlovchi dastur tuzing."""

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

N, M = map(int, input('n m: ').split())

steps_N = collatz_steps(N)
steps_M = collatz_steps(M)

if steps_N < steps_M:
    print(N, steps_N)
elif steps_M < steps_N:
    print(M, steps_M)
else:
    print("2tasi ham teng 1ga", steps_N, "qadamda yetadi")
