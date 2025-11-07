"""(Vending Machine - Kioska)2 ta musbatintegersonlarNvaMni o'qing:N (1~3)tanlangan ichimlik turini anglatadi, vaM(100 ga karrali son) to'langan summani anglatadi. Tanlangan ichimlik nomi va qaytimlar sonini chop eting.
Qaytim500yoki100sumliklar. Mashina4tadan ortiq100sumlik qaytarmaydi.
Qaytimlar chop etilganda avval 500 keyin 100 sumliklar chop etiladi. Orasi bitta bo'sh katak bilan ajratiladi"""

N = int(input("Ichimlikni kiriting (1-3): "))
M = int(input("To‘langan summani: "))

if N == 1:
    ichimlik = "Americano"
    narx = 500
elif N == 2:
    ichimlik = "Caffe Latte"
    narx = 400
elif N == 3:
    ichimlik = "Lemon Tea"
    narx = 300
else:
    print("Xato raqam kiritildi")
    exit()
qaytim = M - narx
qaytim_500 = qaytim // 500
qaytim = qaytim % 500
qaytim_100 = qaytim // 100
if qaytim_100 > 4:
    qaytim_100 = 4

print(ichimlik)
print(qaytim_500, qaytim_100)
