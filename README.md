# Hafta 4 - Ödev Raporu

## Görev 4 - Önbellekli Rota Sayacı Performans Karşılaştırması

`adim = 20` için yapılan `time.perf_counter()` ölçüm sonuçları:

- **Önbelleksiz Süre:** 0.015363 saniye
- **Önbellekli Süre:** 0.000097 saniye
- **Önbellek Bilgisi (`cache_info`):** CacheInfo(hits=19, misses=41, maxsize=None, currsize=41)

### Değerlendirme
`@lru_cache` kullanımı sayesinde daha önce hesaplanan durumlar hafızada tutulmuş ve tekrarlı özyinelemeler engellenmiştir. Bu sayede işlem süresinde yaklaşık 160 katlık bir performans artışı elde edilmiştir.