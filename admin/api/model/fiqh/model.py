from datetime import datetime, timezone
# Nama kind untuk entity ini
materiFiqh_KIND = "MATERI_FIQH"
fiqh_KIND = "FIQH"


class MateriFiqh:

    def __init__(self, idTema, author, judul, tema, tulisan, video,   id=None):
        # Default constructor
        self.id = id
        self.idTema = idTema
        self.author = author
        self.judul = judul
        self.tema = tema
        self.tulisan = tulisan
        self.video = video

    def ke_dictionary(self):
        # Ubah
        hasil = {}

        # Jika id None jangan buat key "id"
        if self.id != None:
            hasil["id"] = self.id
        hasil["idTema"] = self.idTema
        hasil["author"] = self.author
        hasil["judul"] = self.judul
        hasil["tema"] = self.tema
        hasil["tulisan"] = self.tulisan
        hasil["video"] = self.video

        return hasil
