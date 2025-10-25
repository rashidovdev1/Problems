# Birthday is mm-dd. | Birthday is 03-05.

oy = int(input('oy = '))
kun = int(input('kun = '))

while True:
    if (oy <= 12) and (kun <= 31):
        if (oy < 10) and (kun < 10):
            print(f"Birthday is 0{oy}-0{kun}.")
        elif (oy >= 10) and (kun >= 10):
            print(f"Birthday is {oy}-{kun}.")
        elif (oy < 10) and (kun >= 10):
            print(f"Birthday is 0{oy}-{kun}.")
        else:
            print(f"Birthday is {oy}-0{kun}.")
        break

    elif (oy <= 12) and (kun > 31):
        print("Kun 31 dan katta bo'lishi mumkin emas!")
        kun = int(input('Kun = '))
        continue

    elif (oy > 12) and (kun <= 31):
        print("Oy 12 dan katta bo'lishi mumkin emas!")
        oy = int(input('Oy = '))
        continue

    else:
        print("Oy va kun noto‘g‘ri kiritilgan!")
        oy = int(input('Oy = '))
        kun = int(input('Kun = '))
        continue

# oy = 01
# kun = 01

# oy = 11
# kun = 11

# oy = 01
# kun = 11

# oy = 11
# kun = 01

# oy = 13
# kun = 32