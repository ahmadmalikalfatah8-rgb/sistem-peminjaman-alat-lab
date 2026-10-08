from .Alat import Alat, KONDISI_BAIK, KONDISI_VALID

class AlatManager:
    """Mengelola inventaris peralatan dan kategori laboratorium."""
    def __init__(self, log=None):
        self.data = {}  # kode -> Alat
        self.kategori = {"perangkat komputasi", "perangkat jaringan",
                         "perangkat multimedia"}
        self.log = log

    def tambah(self, kode, nama, kategori, kondisi=KONDISI_BAIK):
        if not kode or not nama or not kategori:
            raise ValueError("Kode, nama, dan kategori tidak boleh kosong.")
        if kode in self.data:
            raise ValueError(f"Kode alat {kode} sudah ada.")
        if kondisi not in KONDISI_VALID:
            raise ValueError("Kondisi tidak valid.")
        kategori = kategori.lower()
        if kategori not in self.kategori:
            self.kategori.add(kategori)
            if self.log:
                self.log.catat(f"Kategori baru '{kategori}' ditambahkan")
        alat = Alat(kode, nama, kategori, kondisi)
        self.data[kode] = alat
        if self.log:
            self.log.catat(f"Alat {kode} ({nama}) ditambahkan")
        return alat

    def edit(self, kode, nama=None, kategori=None):
        alat = self.get(kode)
        if nama:
            alat.nama = nama
        if kategori:
            alat.kategori = kategori.lower()
            self.kategori.add(alat.kategori)
        if self.log:
            self.log.catat(f"Alat {kode} diubah")
        return alat

    def hapus(self, kode):
        alat = self.get(kode)
        del self.data[kode]
        if self.log:
            self.log.catat(f"Alat {kode} dihapus")
        return alat

    def cari(self, kata):
        """Cari berdasarkan kode, sebagian nama, atau kategori."""
        kata = kata.lower()
        return [a for a in self.data.values()
                if kata in a.kode.lower() or kata in a.nama.lower()
                or kata in a.kategori.lower()]

    def get(self, kode):
        if kode not in self.data:
            raise ValueError(f"Alat dengan kode {kode} tidak ditemukan.")
        return self.data[kode]

    def alat_tersedia(self):
        return [a for a in self.data.values() if a.status_alat == "tersedia"]

    def alat_rusak(self):
        return [a for a in self.data.values() if a.kondisi != KONDISI_BAIK]