# Nama kind untuk entity ini
PERMINTAAN_KIND = "permintaan"


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
class Permintaan:
    def __init__(self, nama, ulang, id=None):
        # Default constructor
        self.id = id
        self.nama = nama
        self.ulang = ulang


    def ke_dictionary(self):
        # Ubah
        hasil = {}

        # Jika id None jangan buat key "id"
        if self.id != None:
            hasil["id"] = self.id

        hasil["nama"] = self.nama
        hasil["ulang"] = self.ulang

        return hasil
        