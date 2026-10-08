from datetime import date, timedelta
from .Transaksi import Peminjaman, Pengembalian
from .Alat import KONDISI_VALID

class TransaksiManager:
    """Mengelola riwayat transaksi peminjaman dan pengembalian."""
    def __init__(self):
        self.transaksi = {}      # id_trx -> Peminjaman
        self.pengembalian = []   # list of Pengembalian
        self._no_transaksi = 0
        self._no_pengembalian = 0

    def buat_peminjaman(self, nim, daftar_kode, lama_hari=7):
        self._no_transaksi += 1
        id_trx = f"T{self._no_transaksi:03d}"
        hari_ini = date.today()
        trx = Peminjaman(id_trx, nim, daftar_kode, hari_ini,
                         hari_ini + timedelta(days=lama_hari))
        self.transaksi[id_trx] = trx
        return trx

    def catat_pengembalian(self, id_trx, kode, kondisi, tanggal=None):
        trx = self.get_transaksi(id_trx)
        if kondisi not in KONDISI_VALID:
            raise ValueError("Kondisi harus: baik / rusak ringan / rusak berat.")
        if kode not in trx.items:
            raise ValueError(f"Alat {kode} tidak ada di transaksi {id_trx}.")
        if trx.items[kode]["dikembalikan"]:
            raise ValueError(f"Alat {kode} sudah dikembalikan.")
        tanggal = tanggal or date.today()
        if tanggal < trx.tanggal:
            raise ValueError("Tanggal pengembalian tidak boleh sebelum tanggal pinjam.")

        # 1. Catat pengembalian item pada transaksi peminjaman
        trx.catat_pengembalian(kode, kondisi, tanggal)

        # 2. Buat objek transaksi pengembalian (Subclass Transaksi)
        self._no_pengembalian += 1
        id_kembali = f"R{self._no_pengembalian:03d}"
        terlambat = tanggal > trx.batas_kembali
        hari_terlambat = (tanggal - trx.batas_kembali).days if terlambat else 0
        denda = max(0, hari_terlambat * 5000)

        bukti_kembali = Pengembalian(
            id_kembali, id_trx, trx.nim, kode, kondisi, tanggal, terlambat, denda
        )
        self.pengembalian.append(bukti_kembali)
        return trx, bukti_kembali

    def is_alat_dipinjam(self, kode):
        for trx in self.transaksi.values():
            if trx.aktif and kode in trx.alat_belum_kembali():
                return True
        return False

    def transaksi_mahasiswa(self, nim):
        return [t for t in self.transaksi.values() if t.nim == nim]

    def get_transaksi(self, id_trx):
        if id_trx not in self.transaksi:
            raise ValueError(f"Transaksi {id_trx} tidak ditemukan.")
        return self.transaksi[id_trx]