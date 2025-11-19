import math

x1, y1 = map(int, input("(x1 y1): ").split())
x2, y2 = map(int, input("(x2 y2): ").split())

masofa = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Nuqtalar orasidagi masofa:", masofa)
