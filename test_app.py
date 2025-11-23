#Tugas_RPL

#1. Ardiansyah N. Umar          F55124015
#2. Anggra Giovano Tapadongko   F55124023
#3. Chatrin Aurelia             F55124019
#4. Anisa Aulia Febrina         F55124005
#5. Atalya Victoria             F55124028

from app import tambah, kurang

def test_tambah():
    assert tambah(2, 3) == 5
    assert tambah(-1, 1) == 0

def test_kurang():
    assert kurang(10, 5) == 5