from .ActivityLog import ActivityLog
from .MahasiswaManager import MahasiswaManager
from .AlatManager import AlatManager
from .TransaksiManager import TransaksiManager
from .Alat import KONDISI_BAIK

class LabManager:
    """Koordinator utama sistem laboratorium untuk aturan bisnis lintas domain."""
    MAKS_TRANSAKSI_AKTIF = 2   # Aturan 2
    MAKS_HARI_PINJAM = 7

    def __init__(self):
        self.log = ActivityLog()
        self.mhs_mgr = MahasiswaManager(self.log)
        self.alat_mgr = AlatManager(self.log)
        self.trx_mgr = TransaksiManager()

    def hapus_mahasiswa(self, nim):
        mhs = self.mhs_mgr.get(nim)
        if mhs.aktif_meminjam:
            raise ValueError("Mahasiswa masih memiliki transaksi aktif, tidak dapat dihapus.")
        return self.mhs_mgr.hapus(nim)

    def hapus_alat(self, kode):
        if self.trx_mgr.is_alat_dipinjam(kode):
            raise ValueError("Alat masih tercatat dalam transaksi aktif, tidak dapat dihapus.")
        return self.alat_mgr.hapus(kode)

    def buat_transaksi(self, nim, daftar_kode, lama_hari=7):
        mhs = self.mhs_mgr.get(nim)
        if len(mhs.status_mahasiswa) >= self.MAKS_TRANSAKSI_AKTIF:
            raise ValueError("Mahasiswa sudah memiliki 2 transaksi aktif.")
        if not 1 <= lama_hari <= self.MAKS_HARI_PINJAM:
            raise ValueError("Lama peminjaman harus 1-7 hari.")
        daftar_kode = list(dict.fromkeys(daftar_kode))
        if not daftar_kode:
            raise ValueError("Pilih minimal satu alat.")

        for kode in daftar_kode:
            alat = self.alat_mgr.get(kode)
            if alat.status_alat != "tersedia":
                raise ValueError(f"Alat {kode} ({alat.nama}) tidak tersedia (status: {alat.status_alat}).")

        trx = self.trx_mgr.buat_peminjaman(nim, daftar_kode, lama_hari)
        mhs.status_mahasiswa.append(trx.id)
        for kode in daftar_kode:
            self.alat_mgr.get(kode).status_alat = "tidak tersedia"
            self.log.catat(f"{self.alat_mgr.get(kode).nama} ({kode}) dipinjam dalam {trx.id}")
        self.log.catat(f"Transaksi {trx.id} dibuat untuk {nim}")
        return trx

    def kembalikan_alat(self, id_trx, kode, kondisi, tanggal=None):
        trx, bukti_kembali = self.trx_mgr.catat_pengembalian(id_trx, kode, kondisi, tanggal)
        alat = self.alat_mgr.get(kode)
        alat.kondisi = kondisi    # Aturan 5: hanya 'baik' yang jadi tersedia
        alat.status_alat = "tersedia" if kondisi == KONDISI_BAIK else "tidak tersedia"
        self.log.catat(f"{alat.nama} ({kode}) dikembalikan, kondisi {kondisi} [{bukti_kembali.id}]")

        if not trx.aktif:
            self.mhs_mgr.get(trx.nim).status_mahasiswa.remove(id_trx)
            self.log.catat(f"Transaksi {id_trx} selesai")
        return trx

    def alat_dipinjam(self):
        return [a for a in self.alat_mgr.data.values() if self.trx_mgr.is_alat_dipinjam(a.kode)]