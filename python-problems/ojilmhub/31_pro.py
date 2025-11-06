
son = int(input('a = '))

if son % 2 == 0 and son % 3 == 0 and son % 5 == 0:
    print('A')
elif son % 2 == 0 and son % 3 == 0:
    print('B')
elif son % 2 == 0 and son % 5 == 0:
    print('C')
elif son % 3 == 0 and son % 5 == 0:
    print('D')
elif son % 2 == 0 or son % 3 == 0 or son % 5 == 0:
    print('E')
else:
    print('N')