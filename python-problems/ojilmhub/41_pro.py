"""Berilgan sondan keyingi tub sonni topadigan dastur tuzing.
agarNsoni tub bo'lsa o'zini chop eting
agarNtub bo'lmasa, undan keyingi tub sonni chop eting"""

n = int(input("Sonni kiriting: "))

def tubmi(x):
    if x < 2:
        return False
    else:
        for j in range(2, int(x**0.5)+1):
            if x % j == 0:
                return False
    return True

if tubmi(n):
    print(n)
else:
    i = n + 1
    while not tubmi(i):
        i += 1
    print(i)

# n or ndan keyingi tub
# n = int(input("N ni kiriting: "))
#
# tub = True
# if n < 2:
#     tub = False
# else:
#     for j in range(2, int(n**0.5)+1):
#         if n % j == 0:
#             tub = False
#             break
#
# if tub is True:
#     print(n)
# else:
#     i = n + 1
#     while True:
#         tub = True
#         if i < 2:
#             tub = False
#         else:
#             for j in range(2, int(i**0.5)+1):
#                 if i % j == 0:
#                     tub = False
#                     break
#         if tub:
#             print(i)
#             break
#         i += 1

# #N sonidan keyingi 1-tub son
# n = int(input("N ni kiriting: "))
#
# i = n + 1
# while True:
#     tub = True
#     if i >= 2:
#         for j in range(2, int(i**0.5) + 1):
#             if i % j == 0:
#                 tub = False
#                 break
#     else:
#         tub = False
#
#     if tub:
#         print(i)
#         break
#     i += 1




