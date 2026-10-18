from functools import partial, reduce

galaksi = {
    "baglantilar": {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "sirius", "orion"],
        "sirius": ["dünya", "centauri", "orion"],
        "orion": ["centauri", "sirius"],
        "kara_delik": [],
    }
}

def buyuk_harfli_map(gezegenler):
    """map() kullanarak tüm gezegen adlarını büyük harfe çevirir."""
    return list(map(str.upper, gezegenler))


def buyuk_harfli_liste(gezegenler):
    """Liste üreteci kullanarak tüm gezegen adlarını büyük harfe çevirir."""
    return [g.upper() for g in gezegenler]

def iki_baglantili_filter(baglantilar):
    """filter() kullanarak en az iki komşusu olan gezegenleri döndürür."""
    return list(filter(lambda g: len(baglantilar[g]) >= 2, baglantilar))

def iki_baglantili_liste(baglantilar):
    """Liste üreteci kullanarak en az iki komşusu olan gezegenleri döndürür."""
    return [g for g in baglantilar if len(baglantilar[g]) >= 2]

def toplam_baglanti_reduce(baglantilar):
    """reduce() kullanarak tüm gezegenlerin bağlantı sayılarını toplar."""
    uzunluklar = [len(b) for b in baglantilar.values()]
    return reduce(lambda x, y: x + y, uzunluklar, 0)


def toplam_baglanti_sum(baglantilar):
    """sum() kullanarak tüm gezegenlerin bağlantı sayılarını toplar."""
    return sum(len(b) for b in baglantilar.values())

def yolculuk(baslangic, hedef, hiz=1):
    """Belirtilen iki gezegen arasında verilen hızla rota oluşturur."""
    return f"{baslangic} -> {hedef} rotası (hız: {hiz})"

hizli_yolculuk = partial(yolculuk, hiz=3)

if __name__ == "__main__":
    gezegenler = list(galaksi["baglantilar"].keys())
    baglanti_haritasi = galaksi["baglantilar"]

# Soru 1
    print("map ile    :", buyuk_harfli_map(gezegenler))
    print("liste ile  :", buyuk_harfli_liste(gezegenler))

    # Soru 2
    print("filter ile :", iki_baglantili_filter(baglanti_haritasi))
    print("liste ile  :", iki_baglantili_liste(baglanti_haritasi))

    # Soru 3
    print("reduce ile :", toplam_baglanti_reduce(baglanti_haritasi))
    print("sum ile    :", toplam_baglanti_sum(baglanti_haritasi))

    # Soru 4
    print("hızlı yolculuk:", hizli_yolculuk("dünya", "mars"))