from datetime import datetime, timezone
# Nama kind untuk entity ini
materiMawaris_KIND = "materi_mawaris"
mawaris_KIND = "mawaris"


# Class Permintaan
#
# Deklarasi object yang akan disimpan padda datastor.
#
# Property:
#   * nama: isian nama yang diisi pada form
#   * ulang: isian ulang yang diisi pada form
#   * id: ID yang dibangkitkan oleh Datastore
#
# Method:
#   * __init__: Default constructor
#   * ke_dictionary: Ubah object ke Dictionary agar bisa di serialkan dan simpan
class MateriMawaris:

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
