# π ning qiymati:3.14
# Raduisirbo'lgan doiraning uzunligi: L = 2πr
# Doiraning yuzi formulasi: S = πr^2

import math

L = float(input('yoz: '))
r = L/(2*math.pi)
S = math.pi*r**2
print(round(S))