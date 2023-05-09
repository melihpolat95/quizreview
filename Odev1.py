# Kullanıcıdan 4 soru al, sorunun dogru cevabını al ve kaydet. Daha sonra kullanıcıya soruları göster ve yanitlari al. En son buna göre puan hesapla ve göster.

sorular = []
siklar = []
dogrular = []
cevaplar = []
dogruSayisi = 0
i = 0
while i < 4:
    s = input("{}. Soruyu yaziniz: ".format(i+1))
    sorular.append(s)
    si = input("Siklari giriniz: ")
    siklar.append(si)
    dogru = input("Sorunun dogru cevabinin sikkini giriniz: ")
    dogrular.append(dogru)
    i += 1

print("***Simdi Sinav Zamani***")
k = 0
while k < 4:
    print(sorular[k])
    print(siklar[k])
    c = input("Cevabinizi yaziniz: ")
    cevaplar.append(c)
    if cevaplar[k] == dogrular[k]:
        print("Dogru!!!")
        dogruSayisi += 1
    else:
        print("Yanlis cevap")
    k += 1

puan = dogruSayisi*25
print("Puaniniz: " + puan)

