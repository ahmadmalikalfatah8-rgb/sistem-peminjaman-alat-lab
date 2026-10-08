from .Mahasiswa import Mahasiswa

class MahasiswaManager:
    """Mengelola penyimpanan dan operasi data mahasiswa."""
    def __init__(self, log=None):
        self.data = {}  # nim -> Mahasiswa
        self.log = log

    def tambah(self, nim, nama, no_hp):
        if not nim or not nama:
            raise ValueError("NIM dan nama tidak boleh kosong.")
        if nim in self.data:
            raise ValueError(f"NIM {nim} sudah terdaftar.")
        mhs = Mahasiswa(nim, nama, no_hp)
        self.data[nim] = mhs
        if self.log:
            self.log.catat(f"Mahasiswa {nim} ditambahkan")
        return mhs

    def edit(self, nim, nama=None, no_hp=None):
        mhs = self.get(nim)
        if nama:
            mhs.nama = nama
        if no_hp:
            mhs.no_hp = no_hp
        if self.log:
            self.log.catat(f"Mahasiswa {nim} diubah")
        return mhs

    def hapus(self, nim):
        mhs = self.get(nim)
        del self.data[nim]
        if self.log:
            self.log.catat(f"Mahasiswa {nim} dihapus")
        return mhs

    def cari(self, kata):
        kata = kata.lower()
        return [m for m in self.data.values()
                if kata in m.nim.lower() or kata in m.nama.lower()]

    def get(self, nim):
        if nim not in self.data:
            raise ValueError(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
        return self.data[nim]