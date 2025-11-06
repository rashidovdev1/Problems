"""Yil berilganda, agar u kabisa yili bo'lsa,1ni, aks holda0ni chop etadigan dastur tuzing.
Kabisa yili - bu 4 ga bo'linadi, lekin 100 ga bo'linmaydi, ammo 400 ga bo'linadi.
Masalan, 2012 yil kabisa yili, chunki u 4 ga bo'linadi, 100 ga bo'linmaydi.1900 yil kabisa yili emas,
chunki u 100 ga bo'linadi, ammo 400 ga bo'linmaydi. 2000 yil kabisa yili, chunki u 400 ga bo'linadi."""

kabisa = int(input('kabisa: '))

if (kabisa % 4 == 0 and kabisa % 100 != 0) or (kabisa % 400 == 0):
    print(1)
else:
    print(0)