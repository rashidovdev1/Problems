"""Bitta belgi (char)ni o'qing va quyidagicha chop eting.
Katta harfni kichigiga yoki kichigini kattasiga o'girib chop eting.
Agar kiritilgan belgiharfbolmasa, "none" deb chop eting."""

harf = input(': ')

if harf.isdigit():
    print("none")
else:
    if harf.islower():
        print(f"{harf.upper()}")
    elif harf.isupper():
        print(harf.lower())
    else:
        print('Harf emas')