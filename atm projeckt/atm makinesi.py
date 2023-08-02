print("****************\nATM'MİZE HOŞGELDİNİZ\n****************")

print("""
YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN;

BAKİYE SORGULAMA:1
PARA YATIRMA:2
PARA ÇEKME:3
""")
sys_sifre = "123456"
giris_hakki = 3
bakiye = 1000

while giris_hakki > 0:
    sifre = input("Şifrenizi girin:")
    if sifre != sys_sifre:
        print("YANLIŞ ŞİFRE GİRDİNİZ TEKRAR DENEYİN")
        giris_hakki -= 1
        if giris_hakki == 0:
            print("ÇOK FAZLA YANLIŞ ŞİFRE GİRDİĞİNİZ İÇİN\nKART İADESİ YAPILIYOR")
            exit()
    else:
        print("Giriş yapılıyor")
        break

while True:
    islem = input("\nYAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN (Çıkmak için 'E' ye basın):")
    if islem == "1":
        print("Bakiyeniz {} TL'dir".format(bakiye))
    elif islem == "2":
        miktar = int(input("Yatırmak istediğiniz miktarı girin:"))
        bakiye += miktar
    elif islem == "3":
        miktar = int(input("Çekmek istediğiniz miktarı girin:"))
        if bakiye - miktar < 0:
            print("Geçersiz miktar\nBakiyeniz {} TL dir".format(bakiye))
        else:
            bakiye -= miktar
    elif islem == "E":
        print("ÇIKIŞ YAPILIYOR\nTEKRAR BEKLERİZ")
        break
    else:
        print("Geçersiz işlem")
