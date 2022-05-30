from datetime import datetime, timezone
# Nama kind untuk entity ini
diskusi_KIND = "DISKUSI"


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
class Diskusi:

    def __init__(self, platform, keterangan, link,   id=None):
        # Default constructor
        self.id = id
        self.platform = platform
        self.keterangan = keterangan
        self.link = link

    def ke_dictionary(self):
        # Ubah
        hasil = {}

        # Jika id None jangan buat key "id"
        if self.id != None:
            hasil["id"] = self.id
        hasil["platform"] = self.platform
        hasil["keterangan"] = self.keterangan
        hasil["link"] = self.link

        return hasil
