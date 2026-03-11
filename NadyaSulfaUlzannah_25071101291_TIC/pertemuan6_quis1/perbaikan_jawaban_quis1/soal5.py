import soal1
import soal2
import soal3
import soal4


def main():
    inventaris = []

    skema_komisi = (
        (100000000, 10),
        (50000000, 5),
        (20000000, 2),
        (0, 0)
    )

    while True:
        print("=== PyGadget Hub ===")
        print("1. Tambah Gadget")
        print("2. Daftar Inventaris")
        print("3. Update Stok")
        print("4. Cek Komisi")
        print("5. Keluar")

        menu = input("Pilih menu: ")
        print()

        if menu == "1":
            merk = input("Masukkan merk: ")
            tipe = input("Masukkan tipe: ")
            harga = int(input("Masukkan harga: "))
            sn = input("Masukkan SN: ")

            gadget = soal1.registrasi_gadget(merk, tipe, harga, sn)

            if gadget:
                inventaris.append(gadget)
                print("Gadget berhasil ditambahkan!")

        elif menu == "2":
            if len(inventaris) == 0:
                print("Inventaris masih kosong.")
            else:
                print("=== Daftar Inventaris ===")
                for g in inventaris:
                    print(f"Merk : {g['merk']}")
                    print(f"Tipe : {g['tipe']}")
                    print(f"Harga: {g['harga']}")
                    print(f"SN   : {g['sn']}")
                    print(f"Stok : {g.get('stok', 0)}")
                    print()

        elif menu == "3":
            sn_target = input("Masukkan SN gadget: ")
            tambah = int(input("Masukkan jumlah stok tambahan: "))
            soal3.update_stok(inventaris, sn_target, tambah)

        elif menu == "4":
            nama_sales = input("Masukkan Nama Sales: ")
            total_penjualan = int(input("Masukkan Total Penjualan: "))

            persen = soal4.hitung_komisi(total_penjualan, skema_komisi)
            komisi = total_penjualan * persen / 100

            print("\n=== Rincian Komisi ===")
            print(f"Nama Sales      : {nama_sales}")
            print(f"Total Penjualan : {total_penjualan}")
            print(f"Persen Komisi   : {persen}%")
            print(f"Nominal Komisi  : {komisi}")

        elif menu == "5":
            print("Terima kasih telah menggunakan PyGadget Hub!")
            break

        else:
            print("Menu tidak valid.")

        print("\n============================\n")


if __name__ == "__main__":
    main()