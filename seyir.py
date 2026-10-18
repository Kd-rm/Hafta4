def satirlari_oku(yol):
    """Dosyadaki satirlari bosluk ve yorumlari eleyerek uretir."""
    with open(yol,"r",encoding="utf-8") as dosya:
        for satir in dosya :
            temiz = satir.strip()
            if not temiz or temiz.startswith("#"):
                continue
            yield temiz

def ayristir(satirlar):
    """Metin satirlarini kaynak, hedef ve yakit demeti olarak uretir."""
    for satir in satirlar :
        kaynak, sag = satir.split("->")
        kaynak = kaynak.strip()
        hedef , yakit = sag.strip().split()

        yield (kaynak,hedef,int(yakit))

def uzun_yolculuklar(kayitlar,esik):
    """Esik degerinden buyuk olan yakit seferlerini suzer."""
    for kaynak,hedef,yakit in kayitlar:
        if yakit > esik :
            yield (kaynak,hedef,yakit)

if __name__ == "__main__":
    toplam = sum(y for _, _, y in ayristir(satirlari_oku("veri/seyir.txt")))
    print("Toplam Yakıt:", toplam)
    kayitlar = ayristir(satirlari_oku("veri/seyir.txt"))
    uzunlar = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    print("Uzun Yolculuklar:", uzunlar)