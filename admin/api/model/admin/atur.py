# from google.cloud import datastore
from google.cloud import datastore
from .model import Admin, admin_KIND


def LoginAdmin(
    email,
    password,
):
    if email != None and password != None:

        client = datastore.Client()
        queri = client.query(kind=admin_KIND)
        queri.add_filter("email", "=", email)

        satuHasil = list(queri.fetch(limit=1))
        if satuHasil:
            data = satuHasil[0]
            return data
        return None


# def login(
#         email,
#         password,
# ):
#     # Buat object hanya jika kedua data ada
#     if email != None and password != None:
#         # Buat object baru
#         # Sambung ke datastore
#         client = datastore.Client()

#         # Buat query untuk meminta semua isi kind permintaan
#         query = client.query(kind=admin_KIND)
#         query.add_filter("email", "=", email)
#         # Jalankan query
#         satuHasil = list(query.fetch(limit=1))
#         if satuHasil:
#             data = satuHasil[0]
#             # Cek bahwa sudah konfirmasi email
#             # if not data['emailKonfirmasi']:
#             #     return "email belum di konfirmasi"
#             hasilBaru = Admin(id=data.id,
#                               email=data["email"],
#                               password=data["password"],
#                               )
#             # Kembalikan list object permintaan
#             return hasilBaru

#     return None
