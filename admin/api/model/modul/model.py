from datetime import datetime, timezone
# Nama kind untuk entity ini
MODUL_KIND = "MODUL"


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
class Modul:

    def __init__(self, judul, PDF,   id=None):
        # Default constructor
        self.id = id
        self.judul = judul
        self.PDF = PDF

    def ke_dictionary(self):
        # Ubah
        hasil = {}

        # Jika id None jangan buat key "id"
        if self.id != None:
            hasil["id"] = self.id
        hasil["judul"] = self.judul
        hasil["PDF"] = self.PDF

        return hasil
