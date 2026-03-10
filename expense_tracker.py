import datetime
import statistics

def main():
    transaksi = []
    
    print("=== Program Pencatat Keuangan Sederhana ===")
    
    while True:
        print("\nMenu:")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Semua Transaksi")
        print("3. Analisis Statistik")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama pengeluaran: ")
            try:
                jumlah = float(input("Masukkan jumlah (Rp): "))
                waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                item = {
                    "nama": nama,
                    "jumlah": jumlah,
                    "waktu": waktu
                }
                transaksi.append(item)
                print(f"Berhasil menambahkan: {nama}")
            except ValueError:
                print("Error: Harap masukkan angka yang valid untuk jumlah.")
                
        elif pilihan == '2':
            print("\n--- Riwayat Transaksi ---")
            if not transaksi:
                print("Belum ada transaksi.")
            else:
                for i, t in enumerate(transaksi, 1):
                    print(f"{i}. [{t['waktu']}] {t['nama']}: Rp{t['jumlah']:,.2f}")
                    
        elif pilihan == '3':
            print("\n--- Analisis Statistik ---")
            if len(transaksi) < 1:
                print("Data tidak cukup untuk analisis.")
            else:
                daftar_jumlah = [t['jumlah'] for t in transaksi]
                
                total = sum(daftar_jumlah)
                rata_rata = statistics.mean(daftar_jumlah)
                maksimum = max(daftar_jumlah)
                
                print(f"Total Pengeluaran: Rp{total:,.2f}")
                print(f"Rata-rata: Rp{rata_rata:,.2f}")
                print(f"Pengeluaran Tertinggi: Rp{maksimum:,.2f}")
                print(f"Jumlah Transaksi: {len(transaksi)}")
                
        elif pilihan == '4':
            print("udah out ya bolo")
            break
        else:
            print("Pilihan ga ada breee. pilih yang lain yaww.")

if __name__ == "__main__":
    main()
