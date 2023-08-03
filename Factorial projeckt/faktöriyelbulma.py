print("""*********************
FAKTORİYEL BULMA

ÇIKIŞ YAPMAK İÇİN 'P' YE BASIN
*********************""")

while True:
    sayi = input("Bir sayı girin:")
    if (sayi == 'p'):
        print("Çıkış yapılıyor")
        break

    sayi = int(sayi)
    faktoriyel = 1
    for i in range(2,sayi +1):
        faktoriyel *= i

    print("Faktoriyel:",faktoriyel)




