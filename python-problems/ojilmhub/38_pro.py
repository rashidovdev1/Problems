"""3ta son o'qing. Agar shu sonlarPifagorsonlari bo'lsa,truedeb chop eting. Aks holdafalsedeb chop eting.
_Pifagor_sonlari deb2ta sonning kvadratlari yig'indisi3-sonkvadratiga teng bo'lgan sonlarga aytiladi.a,b va c
Pifagor sonlari bo'lishi uchun ular quyidagi shartlardan birini qoniqtirishi kerak"""

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
    print('True')
else:
    print('False')
