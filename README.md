# Hafta 4 - Odev Raporu ve Proje Dokumantasyonu

Bu proje; ozyineleme (recursion), dinamik programlama (lru_cache), fonksiyonel programlama araclari (map, filter, reduce, partial) ve uretecler (generators) kullanilarak gelistirilmis gorevleri ve testleri icermektedir.

---

## Proje Dosya Yapisi

* fibonacci.py: Fibonacci serisi ve altin oran hesaplamalari.
* rota.py: Ozyinelemeli rota sayaci ve @lru_cache ile optimize edilmis onbellekli rota sayaci.
* istatistik.py: Galaksi verisi uzerinde map, filter, reduce ve liste uretecleri ile yapilan veri analizi ve partial ile turetilen hizli_yolculuk fonksiyonu.
* bonus.py: zamanlayici ureteci ile mesgul bekleme (busy waiting) simulasyonu ve time.sleep analizi.
* tests/: Proje fonksiyonlarinin dogrulugunu denetleyen pytest test paketi (12 test).

---

## Gorev Ozetleri

### Gorev 1 - 3: Fibonacci, Rota ve Yakit Hesaplamalari
* Fibonacci sayilari ve altin oran yakinsamasi formulize edildi.
* Gezegenler arasi olasi rota kombinasyonlari ozyinelemeli olarak hesaplandi.
* Tum islevler pytest test paketinden basariyla gecti (12 passed).

### Gorev 4: Onbellekli Rota Sayaci Performans Karsilastirmasi

adim = 20 icin yapilan time.perf_counter() olcum sonuclari:

- Onbelleksiz Sure: 0.015363 saniye
- Onbellekli Sure: 0.000097 saniye
- Onbellek Bilgisi (cache_info): CacheInfo(hits=19, misses=41, maxsize=None, currsize=41)

Degerlendirme:
@lru_cache kullanimi sayesinde daha once hesaplanan durumlar hafizada tutulmus ve tekrarli ozyinelemeler engellenmistir. Bu sayede islem suresinde yaklasik 160 katlik bir performans artisi elde edilmistir.

### Gorev 5: Fonksiyonel Programlama Araclari (istatistik.py)
* Buyuk Harfli Gezegenler: map(str.upper, ...) ve [g.upper() for g in ...] yontemleriyle listelendi.
* En Az Iki Baglantili Gezegenler: filter(lambda ...) ve kosullu liste ureteci ile ayiklandi.
* Toplam Baglanti Sayisi: reduce(lambda x, y: x + y, ...) ve yerlesik sum() fonksiyonu ile 10 olarak hesaplandi.
* Hizli Yolculuk: functools.partial kullanilarak hiz=3 sabit parametreli hizli_yolculuk fonksiyonu turetildi.
* Okunabilirlik Degerlendirmesi: Python felsefesinde (PEP 20) liste uretecleri ve yerlesik sum() fonksiyonunun, lambda gerektiren fonksiyonel araclara gore daha yalin ve okunabilir oldugu belirtildi.

### Bonus Gorev (+10 Puan): Zamanlayici Ureteci ve Mesgul Bekleme (bonus.py)
* zamanlayici(aralik) ureteci kullanilarak 10 saniye boyunca her 2 saniyede "tik", her 5 saniyede "tak" yazdirildi.
* Mesgul Bekleme (Busy Waiting) vs time.sleep:
  * time.sleep, isletim sistemine sureci uyutmasini soyleyerek CPU kullanimini %0 seviyesine ceker ancak programi dondurur.
  * Mesgul bekleme ise while dongusunde araliksiz zaman kontrolu yaparak CPU'yu %100 yuk altinda tutar; fakat tek bir is parcaciginda birden fazla zamanlayicinin eszamanli gibi takip edilmesini saglar.

---

## Testleri Calistirma

Tum testleri calistirmak icin terminalde su komut yurutulebilir:

py -m pytest