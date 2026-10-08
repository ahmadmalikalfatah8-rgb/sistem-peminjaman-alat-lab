class Mahasiswa:
    def __init__(self, nim, nama, no_hp):
        self.nim = nim
        self.nama = nama
        self.no_hp = no_hp
        self.status_mahasiswa = []

    @property
    def aktif_meminjam(self):
        return len(self.status_mahasiswa) > 0

    def __str__(self):
        status = "Aktif meminjam" if self.aktif_meminjam else "Tidak meminjam"
        return f"{self.nim} | {self.nama} | {self.no_hp} | {status}"