#Bitta musbatintson o'qing. Bu son sekundlar (seconds)ni anglatadi.
# Shu sekundlarni hours:minutes:seconds formatida chop eting.

son = int(input('sekund : '))
#hours:minutes:seconds

soat = son // 3600
minut = (son % 3600) // 60
sekond = son % 60

print(f"{soat}:{minut}:{sekond}")