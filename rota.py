from functools import lru_cache
import time 

baglantilar = {
    "dünya": ["mars","venüs"],
    "mars": ["dünya","jüpiter"],
    "venüs": ["dünya"],
    "jüpiter":["mars"],
}

def rota_sayaci(baglantilar):
    """Baglanti haritasina gore onbellekli rota sayisi fonksiyonu dondurur."""

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen,adim):
        """Verilen gezegenden tam adim yolculuk yapan rota sayisini hesaplar."""
        if adim == 0 :
            return 1
        return sum(rota_sayisi(h , adim-1) for h in baglantilar[gezegen])
    return rota_sayisi

def rota_sayisi_onbelleksiz(gezegen,adim):
    if adim == 0:
        return 1
    return sum(rota_sayisi_onbelleksiz(h,adim-1) for h in baglantilar[gezegen])

basla = time.perf_counter()
rota_sayisi_onbelleksiz("dünya", 20)
sure_onbelleksiz = time.perf_counter() - basla

say = rota_sayaci(baglantilar)
basla = time.perf_counter()
say("dünya", 20)
sure_onbellekli = time.perf_counter() - basla

print(f"Önbelleksiz süre : {sure_onbelleksiz:.6f} saniye")
print(f"Önbellekli süre  : {sure_onbellekli:.6f} saniye")
print(f"Cache bilgisi    : {say.cache_info()}")

print("3 adim  :", say("dünya", 3))
print("10 adim :", say("dünya", 10))
print("40 adim :", say("dünya", 40))