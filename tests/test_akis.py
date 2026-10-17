from itertools import islice,takewhile
from fibonacci import fibonacci
from yakit import yakit_gostergesi
from uzay_oyunu.oyun import travel


def test_fibonacci():
    g = fibonacci()
    assert [next(g),next(g),next(g)] == [0,1,1]

    assert list(islice(fibonacci(),12)) ==[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    assert list(takewhile(lambda x: x<100,fibonacci())) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    u = fibonacci()
    ilk_kontrol = list(islice(u,5)) 
    ikinci_kontrol = list(islice(u,5))
    assert ilk_kontrol != ikinci_kontrol

def test_yakit_gostergesi():
    sonuc = list(yakit_gostergesi(100,30))
    assert sonuc == [70,40,10,0]

def test_yakit_gostergesi_stop():
    g = yakit_gostergesi(20,20)
    assert next(g) == 0
    import pytest
    with pytest.raises(StopIteration):
        next(g)

def test_travel_yakit_bitti():
    galaksi = {"baglantilar": {"dunya": ["mars"]}}
    g = yakit_gostergesi(10, 10)
    next(g)

    assert travel(galaksi, "dunya", False, False, False, gosterge=g) is None