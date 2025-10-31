# Kiritilgan sonning har bir xonasi orasiga!belgisi bilan chop eting.
#Bitta butun sonN(1 ≤ N ≤ 99999)
#100 - 0!0!1!0!0

N = input("Son kiriting: ")
N = N.zfill(5)
natija = "!".join(N)
print(natija)

# N.zfill(5) - bu metod son uzunligini 5 ta belgigacha to‘ldiradi, boshiga 0 lar qo‘yadi.
# "!".join(N) - har bir raqam orasiga ! qo‘yadi.
