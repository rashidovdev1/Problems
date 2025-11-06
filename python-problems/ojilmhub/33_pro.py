"""Sonni topo'yinida avval javob sifatida bitta son kiritiladi. Shu sonni taxmin qilib topish uchun 2 marta imkoniyat beriladi.
1 - taxmindayoq javob to'g'ri topilsa,YORVORDIZdeb chop etiladi vao'yin tugaydi.
1 - taxminda javob to'g'ri topilmasa va taxmin javobdan kichik bo'lsa,YUQORIGAdeb, katta bo'lsaPASTGAdeb chop etiladi vao'yin davom etadi.
2 - taxminda javob to'g'ri topilsa,YORVORDIZdeb chop etiladi vao'yin tugaydi.
2 - taxminda javob to'g'ri topilmasa va taxmin javobdan kichik bo'lsa,YUQORIGAdeb, katta bo'lsaPASTGAdeb chop etiladi vao'yin tugaydi."""

n = int(input('Javob (n): '))
m = int(input('1-taxmin: '))

if m == n:
    print('YORVORDIZ')
else:
    if m < n:
        print('YUQORIGA')
    else:
        print('PASTGA')
    m = int(input('2-taxmin: '))

    if m == n:
        print('YORVORDIZ')
    else:
        if m < n:
            print('YUQORIGA')
        else:
            print('PASTGA')
        print('YUTKAZDING UKA')






