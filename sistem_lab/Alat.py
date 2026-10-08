KONDISI_BAIK = "baik"
KONDISI_RINGAN = "rusak ringan"
KONDISI_BERAT = "rusak berat"
KONDISI_VALID = (KONDISI_BAIK, KONDISI_RINGAN, KONDISI_BERAT)

class Alat:
    def __init__(self, kode, nama, kategori, kondisi=KONDISI_BAIK):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.kondisi = kondisi
        self.status_alat = "tersedia" if kondisi == KONDISI_BAIK else "tidak tersedia"

    def __str__(self):
        return (f"{self.kode} | {self.nama} | {self.kategori} | "
                f"kondisi: {self.kondisi} | status: {self.status_alat}")