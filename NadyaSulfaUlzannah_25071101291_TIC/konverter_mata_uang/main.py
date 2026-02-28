from kurs import Kurs   # mengambil dictionary Kurs dari file kurs.py
from konverter import idr_mata_uang, mata_uang_idr  # mengambil fungsi konversi dari file konverter.py 
from tabulate import tabulate   # mengambil library tabulate untuk membuat tabel

def tampilkan_kurs():       # fungsi untuk menampilkan tabel Kurs
    data = []       # membuat list kosong untuk menyimpan data tebel
    for kode, nilai in Kurs.items():    # melakukan perulangan untuk setiap isi dictionary Kurs
        data.append([kode, f"{nilai:,.0f}".replace(",", ".")])  # menambahkan data ke dalam list

    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))    # menampilkan tabel dengan format grid 

def rupiah(angka):  # fungsi untuk memformat angka rupiah 
    return f"{angka:,.0f}".replace(",", ".")

def main():     # menjalankan program uatama
    print("=== KONVETER MATA UANG ===")     # menampilkan judul program
    tampilkan_kurs()    # memanggil fungsi untuk menampilkan tabel

    i = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()   # upper() = mengubah huruf jadi kapital
    j = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))

    if i == "IDR" and j in Kurs:    # jika dari IDR ke mata uang asing
        hasil = idr_mata_uang(jumlah, j)
        print(f"{rupiah(jumlah)} = {hasil: .2f} {j}")   # menampilkan hasil dengan 2 angka desimal

    elif j == "IDR" and i in Kurs:  # jika dari mata uang asing ke IDR
        hasil = mata_uang_idr(jumlah, i)
        print(f"{jumlah: .2f} {i} = Rp {rupiah(hasil)}")    # menampilkan hasil

    else:       # jika salah input maka akan menampilkan konversi tidak valid
        print("Konversi tidak valid")

if __name__ == "__main__":  # code dijalankan jika file main.py di jalankan langsung
    main()