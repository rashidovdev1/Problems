"""uumiy markazga ega bolgan ikkita aylana raduisi berilgan. R1 R2 (R1>R2)
ularnig yuzalari S1 va S2 ularning ayirmasi S3 aniqlansin
S1 = pi * R1 S2 = pi*R2 S3 = pi*(R1-R2)"""

import math

R1 = float(input("R1 = "))
R2 = float(input("R2 = "))

if R1 > R2:
    S1 = math.pi * R1**2
    S2 = math.pi * R2**2
    S3 = math.pi * (R1**2 - R2**2)

    print("Katta aylana yuzi:", round(S1, 2))
    print("Kichik aylana yuzi:", round(S2, 2))
    print("Yuzalar ayirmasi:", round(S3, 2))
else:
    print("R1 R2 dan katta bo‘lishi kerak!")
