"""harorat0dan past bo'lsa,ichkarida oynadeb habar yuboriladi.
harorat0va40orasida bo'lsatashqarida o'ynadeb habar yuboriladi.
harorat40dan yuqori bo'lsaichkarida o'ynadeb habar yuboriladi """

gradus = int(input('harorat: '))
if gradus < 0:
    print('ichkarida oyna')
elif gradus >= 0 and gradus < 40:
    print('tashqarida oyna')
else:
    print('ichkarida oyna')