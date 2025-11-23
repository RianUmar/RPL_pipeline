from app import tambah, kurang

def test_tambah():
    assert tambah(2, 3) == 5
    assert tambah(-1, 1) == 0

def test_kurang():
    assert kurang(10, 5) == 5