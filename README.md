# Sistem Peminjaman Alat Laboratorium

## 1. Informasi Aplikasi

**Nama Aplikasi:** Sistem Peminjaman Alat Laboratorium

**Mata Kuliah:** Praktikum Pemrograman

**Bahasa Pemrograman:** Python

**Dikembangkan oleh:** Kelompok 1A

**Program Studi:** Pendidikan Teknik Informatika dan Komputer

**Universitas:** Universitas Sebelas Maret

## 2. Anggota Kelompok

1. **Daffa Radityatama** — K3525002
2. **Khalifah Ayu Anjani** — K3525009
3. **Nurul Hidayati** — K3525011
4. **Ahmad Malik Al Fatah** — K3525019
5. **Febri Ahmad Santoso** — K3525025

## 3. Deskripsi Sistem

Sistem Peminjaman Alat Laboratorium merupakan aplikasi berbasis Python yang dirancang untuk membantu pengelolaan inventaris peralatan laboratorium, data mahasiswa, serta transaksi peminjaman dan pengembalian alat. Aplikasi ini dikembangkan dengan menerapkan konsep Object-Oriented Programming (OOP) dan membagi program ke dalam beberapa modul agar kode lebih terstruktur, mudah dipahami, dan mudah dikembangkan.

Sistem ini memiliki beberapa fitur utama, yaitu:

* **Pengelolaan data mahasiswa:** Menambahkan, mengubah, menghapus, mencari, dan mengelola data mahasiswa yang terdaftar.
* **Pengelolaan inventaris alat:** Menambahkan, mengubah, menghapus, dan mencari peralatan berdasarkan kode, nama, atau kategori.
* **Pengelolaan kondisi dan ketersediaan alat:** Memantau kondisi alat, meliputi baik, rusak ringan, dan rusak berat, serta menentukan status ketersediaannya.
* **Transaksi peminjaman:** Mencatat transaksi peminjaman alat dengan batas maksimal dua transaksi aktif per mahasiswa dan lama peminjaman antara satu hingga tujuh hari.
* **Transaksi pengembalian:** Mencatat pengembalian setiap alat, tanggal pengembalian, kondisi alat, dan bukti pengembalian.
* **Perhitungan denda:** Menghitung denda keterlambatan dan denda berdasarkan kondisi alat ketika dikembalikan.
* **Pencatatan aktivitas:** Mencatat aktivitas pengelolaan data mahasiswa, inventaris, dan transaksi selama aplikasi berjalan.

Sistem juga menerapkan aturan bisnis untuk menjaga konsistensi data. Mahasiswa yang masih memiliki transaksi aktif tidak dapat dihapus. Alat yang masih dipinjam tidak dapat dihapus, sedangkan alat yang dikembalikan dalam kondisi rusak tidak langsung tersedia untuk dipinjam kembali.

## 4. Struktur Program

Struktur direktori proyek disusun sebagai berikut:

```text
sistem-peminjaman-alat-lab/
├── main.py
├── README.md
└── sistem_lab/
    ├── ActivityLog.py
    ├── Alat.py
    ├── AlatManager.py
    ├── LabManager.py
    ├── Mahasiswa.py
    ├── MahasiswaManager.py
    ├── Transaksi.py
    └── TransaksiManager.py
```

### Penjelasan File dan Modul

**`main.py`**

Merupakan file utama yang dijalankan untuk memulai aplikasi. File ini bertanggung jawab mengatur alur interaksi pengguna dan menggunakan kelas-kelas yang tersedia dalam package `sistem_lab`.

**`sistem_lab/ActivityLog.py`**

Mendefinisikan kelas `ActivityLog` untuk mencatat aktivitas beserta waktu pencatatannya dan menampilkan riwayat aktivitas tersebut.

**`sistem_lab/Alat.py`**

Mendefinisikan kelas `Alat` yang menyimpan informasi peralatan laboratorium, seperti kode, nama, kategori, kondisi, dan status ketersediaan.

**`sistem_lab/AlatManager.py`**

Mengelola data inventaris peralatan laboratorium. Modul ini menyediakan fungsi untuk menambah, mengubah, menghapus, mencari, serta menyaring alat berdasarkan status ketersediaan dan kondisi kerusakannya.

**`sistem_lab/LabManager.py`**

Berfungsi sebagai koordinator utama sistem. Modul ini menghubungkan pengelolaan mahasiswa, inventaris, dan transaksi, sekaligus menerapkan aturan bisnis peminjaman dan pengembalian alat.

**`sistem_lab/Mahasiswa.py`**

Mendefinisikan kelas `Mahasiswa` yang menyimpan NIM, nama, nomor telepon, dan status transaksi peminjaman aktif.

**`sistem_lab/MahasiswaManager.py`**

Mengelola data mahasiswa melalui fungsi penambahan, pengubahan, penghapusan, pencarian, dan pengambilan data berdasarkan NIM.

**`sistem_lab/Transaksi.py`**

Mendefinisikan kelas dasar `Transaksi` serta kelas turunan `Peminjaman` dan `Pengembalian`. Modul ini mengelola representasi transaksi, status peminjaman, pencatatan pengembalian alat, dan informasi denda.

**`sistem_lab/TransaksiManager.py`**

Mengelola pembuatan transaksi peminjaman, pencatatan pengembalian, penyimpanan riwayat transaksi, pemeriksaan alat yang masih dipinjam, serta pembuatan nomor transaksi secara berurutan.

## 5. Cara Menjalankan Aplikasi

### 5.1 Prasyarat

Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki:

* Python 3 yang telah terpasang.
* Terminal atau Command Prompt.
* Git apabila ingin mengunduh repository menggunakan Git.

Berdasarkan modul yang tersedia, aplikasi menggunakan pustaka standar Python sehingga tidak memerlukan instalasi dependensi eksternal untuk bagian kode tersebut.

### 5.2 Mengunduh Repository

Unduh proyek menggunakan perintah berikut:

```bash
git clone <URL_REPOSITORY>
```

Ganti `<URL_REPOSITORY>` dengan URL repository GitHub kelompok.

Setelah proses selesai, masuk ke direktori proyek:

```bash
cd sistem-peminjaman-alat-lab
```

### 5.3 Memastikan Struktur Folder

Pastikan file `main.py` berada di direktori utama proyek, sedangkan seluruh modul pengelolaan sistem berada di dalam folder `sistem_lab/`.

### 5.4 Menjalankan Aplikasi

Jalankan aplikasi dengan tombol play di VSC atau melalui terminal dari direktori utama proyek menggunakan perintah:

```bash
python main.py
```

Khusus pengguna Windows, jika perintah `python` tidak dikenali, gunakan:

```bash
py main.py
```

File `main.py` harus berisi kode untuk menjalankan aplikasi dan mengimpor modul dari package `sistem_lab`. Sebagai contoh, apabila kelas `LabManager` digunakan, import dapat ditulis sebagai berikut:

```python
from sistem_lab.LabManager import LabManager
```

Sesuaikan perintah import dengan kelas yang digunakan pada `main.py`.

## 6. Pembagian Kontribusi Anggota

**1. Daffa Radityatama — K3525002**

Bertanggung jawab dalam pengembangan Mahasiswa.py dan Alat.py

**2. Khalifah Ayu Anjani — K3525009**

Bertanggung jawab dalam pengembangan MahasiswaManager.py dan AlatManager.py

**3. Nurul Hidayati — K3525011**

Bertanggung jawab dalam pengembangan Transaksi.py

**4. Ahmad Malik Al Fatah — K3525019**

Bertanggung jawab dalam pengembangan LabManager.py dan ActivityLog.py

**5. Febri Ahmad Santoso — K3525025**

Bertanggung jawab dalam pengembangan SistemTransaksi.py

---