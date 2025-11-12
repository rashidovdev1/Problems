# Ikki sonni EKUBini topadigan dastur tuzing.

N, M = map(int, input("2 ta sonni kiriting: ").split())

while M != 0:
    N, M = M, N % M
print(N)


