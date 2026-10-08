from .Alat import KONDISI_BAIK, KONDISI_RINGAN, KONDISI_BERAT

class Transaksi:
    """Superclass / Base class untuk seluruh transaksi laboratorium."""
    def __init__(self, id_transaksi, nim, tanggal):
        self.id = id_transaksi
        self.nim = nim
        self.tanggal = tanggal

    def __str__(self):
        return f"[{self.id}] NIM: {self.nim} | Tanggal: {self.tanggal}"


class Peminjaman(Transaksi):
    """Subclass Transaksi untuk peminjaman alat laboratorium."""
    def __init__(self, id_transaksi, nim, daftar_kode, tanggal_pinjam, batas_kembali):
        super().__init__(id_transaksi, nim, tanggal_pinjam)
        self.batas_kembali = batas_kembali
        self.items = {
            kode: {"dikembalikan": False, "kondisi": None,
                   "tanggal_kembali": None, "terlambat": False, "denda": 0}
            for kode in daftar_kode
        }

    @property
    def status(self):
        jumlah_kembali = sum(1 for i in self.items.values() if i["dikembalikan"])
        if jumlah_kembali == 0:
            return "dipinjam"
        if jumlah_kembali < len(self.items):
            return "sebagian dikembalikan"
        return "selesai"

    @property
    def aktif(self):
        return self.status != "selesai"

    def alat_belum_kembali(self):
        return [k for k, i in self.items.items() if not i["dikembalikan"]]

    def catat_pengembalian(self, kode, kondisi, tanggal, tarif_denda_telat=1000):
        item = self.items[kode]

        denda_telat = 0
        item["dikembalikan"] = True
        item["kondisi"] = kondisi
        item["tanggal_kembali"] = tanggal
        if tanggal > self.batas_kembali:
            item["terlambat"] = True
            hari_terlambat = (tanggal - self.batas_kembali).days
            denda_telat = hari_terlambat * tarif_denda_telat
        else:
            item["terlambat"] = False

        denda_kondisi = 0
        if kondisi == KONDISI_RINGAN:
            denda_kondisi = 25000
        elif kondisi == KONDISI_BERAT:
            denda_kondisi = 50000

        item["denda"] = denda_telat + denda_kondisi

    def __str__(self):
        baris = [f"Transaksi Peminjaman {self.id} | NIM: {self.nim} | Status: {self.status.upper()}",
                 f"  Pinjam: {self.tanggal} | Batas kembali: {self.batas_kembali}"]
        for kode, i in self.items.items():
            if i["dikembalikan"]:
                info_tambahan = []
                if i["terlambat"]:
                    info_tambahan.append("TERLAMBAT")
                if i["kondisi"] != KONDISI_BAIK:
                    info_tambahan.append(f"KONDISI {i['kondisi'].upper()}")

                if info_tambahan or i["denda"] > 0:
                    status_str = f" ({' & '.join(info_tambahan)} | TOTAL DENDA: Rp {i['denda']:,})"
                else:
                    status_str = "(Tepat Waktu & Kondisi Baik)"
                baris.append(
                    f"  - {kode}: dikembalikan {i['tanggal_kembali']}, "
                    f"kondisi {i['kondisi']}{status_str}")
            else:
                baris.append(f"  - {kode}: masih dipinjam")
        return "\n".join(baris)


class Pengembalian(Transaksi):
    """Subclass Transaksi untuk pencatatan berita acara pengembalian alat."""
    def __init__(self, id_kembali, id_peminjaman, nim, kode_alat, kondisi, tanggal_kembali, terlambat=False, denda=0):
        super().__init__(id_kembali, nim, tanggal_kembali)
        self.id_peminjaman = id_peminjaman
        self.kode_alat = kode_alat
        self.kondisi = kondisi
        self.terlambat = terlambat
        self.denda = denda

    def __str__(self):
        telat_info = (
            f" | Terlambat: Ya (Denda: Rp {self.denda:,})" 
            if self.terlambat 
            else " | Tepat Waktu"
        )
        return (
            f"Transaksi Pengembalian {self.id} (Ref Pinjam: {self.id_peminjaman}) | "
            f"NIM: {self.nim} | Alat: {self.kode_alat} | "
            f"Kondisi: {self.kondisi}{telat_info} | Tanggal: {self.tanggal}")

TransaksiPeminjaman = Peminjaman
TransaksiPengembalian = Pengembalian
