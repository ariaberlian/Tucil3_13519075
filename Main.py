from pencariJalur import kamusBeban
from visualiasiGraph import membuatGraph

while True:
    kamus = kamusBeban
    arrayNodes = [nodes for nodes in kamus]
    # List nama tempat
    print("Tempat-Tempat: ")
    num = 1
    for i in arrayNodes:
        print(f"{num}. {i}")
        num += 1
    # Input tempat awal
    tempatAwal = str(input("Tempat Awal: "))
    while (tempatAwal not in arrayNodes):
        print("Tempat awal tidak ditemukan")
        tempatAwal = str(input("Tempat Awal: "))
    # Input tempat akhir
    tempatAkhir = str(input("Tempat Akhir: "))
    while (tempatAkhir not in arrayNodes):
        print("Tempat akhir tidak ditemukan")
        tempatAkhir = str(input("tempat Akhir: "))
    # Membentuk graph
    membuatGraph(tempatAwal, tempatAkhir)
    break
