"""2 tamusbat sonva bittaoperatordan iborat tenglamani o'qing va natijasini chop eting.
Inputquyidagiketma-ketlikda kiritladi:integer,operator,integer
Inputprobel(bosh katak -space) bilan ajratilsin.
Operatorlar '+' yoki '-' bo'la oladi holos. Boshqa operatorlar kiritilmaydi"""

son1 = int(input('son1 : '))
operator = (input())
son2 = int(input('son2 : '))

if operator == '+':
    print(son1 + son2)
elif operator == '-':
    print(son1 - son2)
elif operator == '*':
    print(son1 * son2)
elif operator == '/':
    if son2 != 0:
        print(son1 / son2)
    else:
        print('0ga bolma')