
## kitap = Kitap() ## __init__metodu
## print(kitap)  __str__ metodu
## len(kitap)   __len__ metodu
## del(kitap)  __del__ metodu

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür

    def __str__(self):
        return "isim: {}\nYazar: {}\nSayfa Sayısı {}\nTürü: {}\n".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)

    def __len__(self):
       return self.sayfa_sayısı

    def __del__(self):
        print("Kitap objesi siliniyor...........")



kitap = Kitap("istanbul hatırası","Ahmet Ümit",546,"Polisiye")

##print(kitap)

print(len(kitap))
del(kitap)