#  1 dan 31 gacha n son

#7
# Sun Mon Tue Wed Thu Fri Sat
#   7   8   9  10  11  12  13

week = 'Sun Mon Tue Wed Thu Fri Sat'
n = int(input('n = '))

print(week)
for i in range(n, n + 7):

    kun = i if i <= 31 else i - 31
    print(f"{kun:>3}", end=' ')