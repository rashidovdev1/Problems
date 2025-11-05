# 3 burchak a va b katet, gipo va pere ?
import math

a = int(input("a: "))
b = int(input("b: "))

gipo = math.sqrt(a * a + b * b)
print(f'gipo = {gipo}')
pere = a + b + gipo
print(f'pere = {pere}')