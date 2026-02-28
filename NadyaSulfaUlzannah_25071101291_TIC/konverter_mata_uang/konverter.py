from kurs import Kurs   # mengambil dictionary Kurs dari file kurs.py

def idr_mata_uang(jumlah_idr, kode_mata_uang):  # konversi dari rupiah ke mata uang asing
    if kode_mata_uang in Kurs:                  # mengecek apakah mata uang yang dimasukkan ada pada dictionary Kurs
        return jumlah_idr / Kurs[kode_mata_uang]  # jika mata uang ada maka akan dilakukan operasi
    return None     # jika mata uang tidak ada kembalikan None

def mata_uang_idr(jumlah, kode_mata_uang): # konversi dari mata uang asing ke rupiah
    if kode_mata_uang in Kurs:      # mengecek apakah mata uang yang dimasukkan ada pada dictionary Kurs
        return jumlah * Kurs[kode_mata_uang]   # jika mata uang ada maka akan dilakukan operasi 
    return None     # jika mata uang tidak ada kembalikan None