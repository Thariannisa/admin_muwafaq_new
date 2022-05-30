from datetime import datetime, timezone
# Nama kind untuk entity ini
latihan_KIND = "latihan"

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


class Latihan:

    def __init__(self, pertanyaan, pilihan1, pilihan2, pilihan3, pilihan4, jawaban,   id=None):
        # Default constructor
        self.id = id
        self.pertanyaan = pertanyaan
        self.pilihan1 = pilihan1
        self.pilihan2 = pilihan2
        self.pilihan3 = pilihan3
        self.pilihan4 = pilihan4
        self.jawaban = jawaban

    def ke_dictionary(self):
        # Ubah
        hasil = {}

        # Jika id None jangan buat key "id"
        if self.id != None:
            hasil["id"] = self.id
        hasil["pertanyaan"] = self.pertanyaan
        hasil["pilihan1"] = self.pilihan1
        hasil["pilihan2"] = self.pilihan2
        hasil["pilihan3"] = self.pilihan3
        hasil["pilihan4"] = self.pilihan4
        hasil["jawaban"] = self.jawaban

        return hasil
