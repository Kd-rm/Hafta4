import time


def zamanlayici(aralik):
    """Belirtilen aralık dolduğunda True, dolmadığında False üreten meşgul bekleme üreteci."""
    hedef = time.perf_counter() + aralik
    while True:
        simdi = time.perf_counter()
        if simdi >= hedef:
            hedef = simdi + aralik
            yield True
        else:
            yield False

if __name__ == "__main__":
    # 2 saniyelik ve 5 saniyelik üreteçleri başlatıyoruz
    zamanlayici_tik = zamanlayici(2)
    zamanlayici_tak = zamanlayici(5)

    baslangic = time.perf_counter()
    toplam_sure = 10

    print("Zamanlayıcı başlatıldı (10 saniye)...")

    # 10 saniye boyunca aralıksız döner
    while time.perf_counter() - baslangic <= toplam_sure:
        # 2 saniye dolduysa 'tik' bas
        if next(zamanlayici_tik):
            gecen = time.perf_counter() - baslangic
            print(f"[{gecen:.2f}s] tik")

        # 5 saniye dolduysa 'tak' bas
        if next(zamanlayici_tak):
            gecen = time.perf_counter() - baslangic
            print(f"[{gecen:.2f}s] tak")