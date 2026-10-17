from itertools import islice,takewhile
from fibonacci import fibonacci

def test_fibonacci():
    g = fibonacci()
    assert [next(g),next(g),next(g)] == [0,1,1]

    assert list(islice(fibonacci(),12)) ==[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    assert list(takewhile(lambda x: x<100,fibonacci())) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    u = fibonacci()
    ilk_kontrol = list(islice(u,5)) 
    ikinci_kontrol = list(islice(u,5))
    assert ilk_kontrol != ikinci_kontrol
    