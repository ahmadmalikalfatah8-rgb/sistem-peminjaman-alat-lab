class ActivityLog:
    def __init__(self):
        self.entries = []  

    def catat(self, pesan):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.entries.append({"waktu": waktu, "pesan": pesan})

    def tampilkan(self):
        if not self.entries:
            print("Belum ada aktivitas.")
            return
        for e in self.entries:
            print(f"[{e['waktu']}] {e['pesan']}")