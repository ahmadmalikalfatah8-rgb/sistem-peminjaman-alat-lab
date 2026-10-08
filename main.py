from datetime import date

from labmanager import LabManager


# ======================================================================
# MENU INTERAKTIF
# ======================================================================

def input_angka(prompt, default=None):
    teks = input(prompt).strip()
    if not teks and default is not None:
        return default
    if not teks.isdigit():
        raise ValueError("Input harus berupa angka.")
    return int(teks)


def tampil_daftar(daftar, kosong="Data tidak ditemukan."):
    if not daftar:
        print(kosong)
    for item in daftar:
        print(item)


def data_awal(lab):
    """Data contoh agar program mudah diuji (Skenario 1)."""
    lab.mhs_mgr.tambah("M001", "Andi", "0811111111")
    lab.mhs_mgr.tambah("M002", "Budi", "0822222222")
    lab.alat_mgr.tambah("A001", "Kamera Digital", "perangkat multimedia")
    lab.alat_mgr.tambah("A002", "Tripod", "perangkat multimedia")
    lab.alat_mgr.tambah("A003", "Kabel LAN", "perangkat jaringan")
    lab.alat_mgr.tambah("A004", "Laptop", "perangkat komputasi")
    lab.alat_mgr.tambah("A005", "Multimeter", "elektronika")


def menu_mahasiswa(lab):
    print("\n[Kelola Mahasiswa] 1.Tambah 2.Edit 3.Hapus 4.Cari 5.Tampilkan semua")
    p = input("Pilih: ").strip()
    if p == "1":
        lab.mhs_mgr.tambah(input("NIM: ").strip(), input("Nama: ").strip(),
                           input("No HP: ").strip())
    elif p == "2":
        lab.mhs_mgr.edit(input("NIM: ").strip(),
                         input("Nama baru (kosong=tetap): ").strip(),
                         input("No HP baru (kosong=tetap): ").strip())
    elif p == "3":
        lab.hapus_mahasiswa(input("NIM: ").strip())
    elif p == "4":
        tampil_daftar(lab.mhs_mgr.cari(input("Kata kunci (NIM/nama): ").strip()))
    elif p == "5":
        tampil_daftar(lab.mhs_mgr.data.values(), "Belum ada mahasiswa.")
    else:
        print("Pilihan tidak valid.")
        return
    if p in ("1", "2", "3"):
        print("Berhasil.")


def menu_alat(lab):
    print("\n[Kelola Alat] 1.Tambah 2.Edit 3.Hapus 4.Cari 5.Tampilkan semua")
    p = input("Pilih: ").strip()
    if p == "1":
        print("Kategori yang ada:", ", ".join(sorted(lab.alat_mgr.kategori)))
        print("(Ketik kategori baru jika belum ada.)")
        lab.alat_mgr.tambah(input("Kode: ").strip(), input("Nama: ").strip(),
                            input("Kategori: ").strip())
    elif p == "2":
        lab.alat_mgr.edit(input("Kode: ").strip(),
                          input("Nama baru (kosong=tetap): ").strip(),
                          input("Kategori baru (kosong=tetap): ").strip())
    elif p == "3":
        lab.hapus_alat(input("Kode: ").strip())
    elif p == "4":
        tampil_daftar(lab.alat_mgr.cari(input("Kode / sebagian nama / kategori: ").strip()))
    elif p == "5":
        tampil_daftar(lab.alat_mgr.data.values(), "Belum ada alat.")
    else:
        print("Pilihan tidak valid.")
        return
    if p in ("1", "2", "3"):
        print("Berhasil.")


def buat_transaksi(lab):
    nim = input("NIM peminjam: ").strip()
    print("Alat tersedia:")
    tampil_daftar(lab.alat_mgr.alat_tersedia(), "(tidak ada alat tersedia)")
    kode = input("Kode alat (pisahkan dengan koma): ").split(",")
    kode = [k.strip() for k in kode if k.strip()]
    lama = input_angka("Lama pinjam (1-7 hari, default 7): ", default=7)
    trx = lab.buat_transaksi(nim, kode, lama)
    print("Transaksi berhasil dibuat:")
    print(trx)


def proses_pengembalian(lab):
    id_trx = input("ID transaksi: ").strip().upper()
    trx = lab.trx_mgr.get_transaksi(id_trx)
    belum = trx.alat_belum_kembali()
    if not belum:
        print("Semua alat pada transaksi ini sudah dikembalikan.")
        return
    print("Alat belum kembali:", ", ".join(belum))
    kode = input("Kode alat yang dikembalikan (pisahkan koma): ").split(",")
    for k in [x.strip() for x in kode if x.strip()]:
        kondisi = input(f"Kondisi {k} (baik/rusak ringan/rusak berat): ").strip().lower()
        tgl_str = input("Tanggal kembali (YYYY-MM-DD, kosong=hari ini): ").strip()
        tgl = date.fromisoformat(tgl_str) if tgl_str else None
        try:
            lab.kembalikan_alat(id_trx, k, kondisi, tgl)
            print(f"{k} berhasil dikembalikan.")
        except ValueError as e:
            print(f"Gagal untuk {k}: {e}")
    print(lab.trx_mgr.transaksi[id_trx])


MENU = """
===== SISTEM PEMINJAMAN PERALATAN LAB =====
 1. Kelola data mahasiswa
 2. Kelola data alat
 3. Buat transaksi peminjaman
 4. Tampilkan transaksi
 5. Proses pengembalian alat
 6. Cari transaksi berdasarkan mahasiswa
 7. Tampilkan alat yang tersedia
 8. Tampilkan alat yang sedang dipinjam
 9. Tampilkan alat yang rusak
10. Tampilkan riwayat peminjaman mahasiswa
11. Log aktivitas
 0. Keluar
"""


def main():
    lab = LabManager()
    if input("Muat data contoh? (y/n): ").strip().lower() == "y":
        data_awal(lab)

    while True:
        print(MENU)
        pilihan = input("Pilih menu: ").strip()
        try:
            if pilihan == "1":
                menu_mahasiswa(lab)
            elif pilihan == "2":
                menu_alat(lab)
            elif pilihan == "3":
                buat_transaksi(lab)
            elif pilihan == "4":
                print("\n--- DAFTAR TRANSAKSI PEMINJAMAN ---")
                tampil_daftar(lab.trx_mgr.transaksi.values(), "Belum ada transaksi peminjaman.")
                if lab.trx_mgr.pengembalian:
                    print("\n--- BUKTI TRANSAKSI PENGEMBALIAN ---")
                    tampil_daftar(lab.trx_mgr.pengembalian)
            elif pilihan in ("6", "10"):
                nim = input("NIM mahasiswa: ").strip()
                tampil_daftar(lab.trx_mgr.transaksi_mahasiswa(nim), "Mahasiswa belum pernah meminjam.")
            elif pilihan == "5":
                proses_pengembalian(lab)
            elif pilihan == "7":
                tampil_daftar(lab.alat_mgr.alat_tersedia(), "Tidak ada alat tersedia.")
            elif pilihan == "8":
                tampil_daftar(lab.alat_dipinjam(), "Tidak ada alat yang sedang dipinjam.")
            elif pilihan == "9":
                tampil_daftar(lab.alat_mgr.alat_rusak(), "Tidak ada alat rusak.")
            elif pilihan == "11":
                lab.log.tampilkan()
            elif pilihan == "0":
                print("Terima kasih.")
                break
            else:
                print("Menu tidak valid.")
        except ValueError as e:
            print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()