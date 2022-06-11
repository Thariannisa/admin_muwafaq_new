from google.cloud import datastore
from google.cloud import storage
import re
from datetime import datetime, timezone
# Nama kind untuk entity ini
admin_KIND = "ADMIN"

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


class Admin:

    def __init__(self, nama, email, password, id=None):
        # Default constructor
        self.id = id
        self.email = email
        self.password = password
        self.nama = nama

    def ke_dictionary(self):
        # Ubah
        hasil = {}

        # Jika id None jangan buat key "id"
        if self.id != None:
            hasil["id"] = self.id
        hasil["email"] = self.email
        hasil["nama"] = self.nama
        hasil["password"] = self.password

        return hasil


# def LoginAdmin(
#     email,
#     password,
# ):
#     if email != None and password != None:

#         client = datastore.Client()
#         queri = client.query(kind=admin_KIND)
#         queri.add_filter("email", "=", email)

#         satuHasil = list(queri.fetch(limit=1))
#         if satuHasil:
#             data = satuHasil[0]
#             return data
#         return None
