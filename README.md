# LAB-EQUIP — Sistem Peminjaman Peralatan Laboratorium

Sistem informasi berbasis Python untuk mengelola data mahasiswa, inventaris peralatan laboratorium, serta transaksi peminjaman dan pengembalian alat secara terintegrasi.

---

## 👥 Anggota Kelompok

| NIM      | Nama Anggota         |
| K3525002 | Daffa Radityatama    |
| K3525009 | Khalifah Ayu Anjani  |
| K3525011 | Nurul Hidayati       |
| K3525019 | Ahmad Malik Al Fatah |
| K3525025 | Febri Ahmad Santoso  |

---

## 📝 Deskripsi Sistem

**LAB-EQUIP** dirancang untuk mempermudah tata kelola laboratorium dalam mencatat pergerakan inventaris dan peminjaman alat oleh mahasiswa. 

**Fitur Utama:**
- **Kelola Data Mahasiswa**: Penambahan, pembaruan, penghapusan, dan pencarian data mahasiswa.
- **Kelola Inventaris Alat**: Manajemen unit alat laboratorium beserta pencatatan kondisi (baik, rusak ringan, rusak berat) dan kategorinya.
- **Peminjaman Alat**: Batas peminjaman 1–7 hari dengan batasan maksimal 2 transaksi aktif per mahasiswa.
- **Pengembalian & Denda**: Perhitungan denda otomatis untuk pengembalian yang terlambat serta denda untuk alat yang mengalami kerusakan.
- **Log Aktivitas**: Pencatatan riwayat setiap aksi sistem secara *real-time*.

---

## 📁 Struktur Program

Proyek ini dipisah menjadi beberapa modul berdasarkan kelas dan fungsinya untuk menerapkan prinsip pemisahan tanggung jawab (*Separation of Concerns*):

```text
lab-system/
│
├── ActivityLog.py          # Class untuk pencatatan log aktivitas
├── Alat.py                 # Model data Alat & konstanta kondisi
├── AlatManager.py          # Manager untuk mengelola inventaris alat
├── LabManager.py           # Facade / Koordinator utama aturan bisnis antar-manager
├── Mahasiswa.py            # Model data Mahasiswa
├── MahasiswaManager.py     # Manager untuk mengelola data mahasiswa
├── Transaksi.py            # Superclass Transaksi & Subclass (Peminjaman, Pengembalian)
├── TransaksiManager.py     # Manager untuk mengelola siklus transaksi peminjaman/pengembalian
└── main.py                 # Main script & antarmuka menu interaktif (CLI)