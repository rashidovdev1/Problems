"""Ikkita son qabul qiling. Agar sonlarning qaysidir biri ikkinchisini kvadratiga teng bo'lsa,
shu sonlarni ko'paytma shaklida yozing. Aks holdanonechop eting."""

a = int(input('a = '))
b = int(input('b = '))

if a == b*b:
    print(f'{b}*{b}={a}')
elif b == a*a:
    print(f'{a}*{a}={b}')
else:
    print('none')
