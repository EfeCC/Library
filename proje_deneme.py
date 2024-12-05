import time

from kütüphane import *

print("""

Kütüphane programına hoş geldiniz.
*****************************

1-Kitapları göster
2-Kitap sorgulama
3-Kitap ekle
4-Kitap sil
5-Baskı yükselt
6-Çıkmak için 'q' ya basın.

*****************************



""")
kütüphane = Kütüphane()

while True:
    işlem = input("İşlem: ")
    if işlem == 'q':
        time.sleep(1)
        print("Program sonlandırılıyor...")
        break
    elif işlem == "1":
        kütüphane.kitapları_goster()

    elif işlem == "2":
        isim = input("Hangi kitabı istiyorsunuz ?")
        print("Kitap sorgulanıyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)

    elif işlem == "3":
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı: "))
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor...")
        time.sleep(1)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")
    elif işlem == "4":
        islem = input("Hangi kitabı silmek istiyorsunuz ?")
        cevap = input("Emin misiniz ? (E/H)")
        if cevap == "E":
            print("Kitap siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi.")

    elif işlem == "5":
        isim = input("Hangi kitabın baskını yükseltmek istiyorsunuz ?")
        print("Baskı yükseltiliyor...")
        kütüphane.baskı_yükselt(isim)
        time.sleep(2)
        print("Baskı yükseltildi.")
    else:
        print("Geçersiz işlem!")

