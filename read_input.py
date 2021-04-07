import os
from collections import defaultdict
from os.path import dirname, abspath

kamusKoordinat = defaultdict(dict)


def membaca_input():
    directory = dirname(abspath(__file__))
    namaFile = str(input("Nama File tanpa ekstensi: "))
    lokasiFile = os.path.join(directory, 'test\\' + namaFile + '.txt')
    f = open(lokasiFile, "r")

    kamusBeban = defaultdict(dict)

    # Mendapatkan list dari seluruh tempat, PENTING !
    listNodes = f.readline().replace("\n", "").split(" ")
    jumlahNodes = len(listNodes)

    # Parsing koordinat
    contents = f.readlines()
    arrayKoordinatMentah = contents[:contents.index("MATRIKS\n")]
    for koordinatTempat in arrayKoordinatMentah:
        namaNode = koordinatTempat.replace("\n", "").split(" ")
        kamusKoordinat[namaNode[0]]["lat"] = int(namaNode[1])
        kamusKoordinat[namaNode[0]]["lng"] = int(namaNode[2])

    # Parsing matriks
    MATRIKS = []
    arrayMatriksMentah = contents[contents.index("MATRIKS\n") + 1:]
    for elem in arrayMatriksMentah:
        elemenAdjacency = elem.replace("\n", "").split(" ")
        elemenAdjacency = list(map(int, elemenAdjacency))
        MATRIKS.append(elemenAdjacency)

    # Parsing bobot
    for ortu in range(jumlahNodes):
        for anak in range(jumlahNodes):
            if (MATRIKS[ortu][anak] == 1):
                kamusBeban[listNodes[ortu]][listNodes[anak]] = jarakEuclidian(listNodes[ortu], listNodes[anak])
    return kamusBeban


def jarakEuclidian(start, end):
    return round(((kamusKoordinat[start]["lat"] - kamusKoordinat[end]["lat"]) ** 2 + (
                kamusKoordinat[start]["lng"] - kamusKoordinat[end]["lng"]) ** 2) ** (0.5), 3)
