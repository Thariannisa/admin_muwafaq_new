from datetime import datetime, timezone
# Nama kind untuk entity ini
USER_KIND = "user"


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
class User:

    def __init__(self, nama, email, password, date_created=None, id=None):
        # Default constructor
        self.id = id
        self.nama = nama
        self.email = email
        self.date_created = date_created
        self.password = password

    def ke_dictionary(self):
        # Ubah
        hasil = {}

        # Jika id None jangan buat key "id"
        if self.id != None:
            hasil["id"] = self.id

        hasil["nama"] = self.nama
        hasil["email"] = self.email
        local_time = datetime.now(timezone.utc).astimezone()
        hasil["date_created"] = local_time.isoformat()
        hasil["password"] = self.password

        return hasil
