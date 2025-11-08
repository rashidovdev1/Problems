"""Nta son o'qing va ularni kublari yig'indisini chop eting.
Birinchi qatorNsoni kiritiladi(2≤N≤10)
Ikkinchi qatordaNta butun sonlar(−50≤SONLAR≤50)
KiritilganNta sonlarni kublari yig'indisini chop eting."""
import math
x = int(input('x = '))

jami = []
for i in range(x):
    son = int(input('son = '))
    son3 = pow(son, 3)
    jami.append(son3)

print(sum(jami))