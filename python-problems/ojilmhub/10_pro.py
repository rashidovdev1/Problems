# Dastlabki 10 taFibonaccisonlarini chop eting.
# Fibonacci son = avvalgi 2 ta Fibonacci sonlar yig'indisi

a, b = 0, 1
print(a, b, end=' ')

for i in range(8):
    c = a + b
    print(c, end=' ')
    a = b
    b = c