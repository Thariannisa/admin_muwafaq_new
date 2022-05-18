from google.cloud import datastore

from .model import Users, USERS_KIND

# Tambah Permintaan
#
# Tambah obejct Permintaan ke datastore.


def tambah(
        nama,
        email,
        kontak,
        password,
):
    # Buat object hanya jika kedua data ada
    if nama != None and email != None and kontak != None and password != None:
        # Buat object baru
        permintaan_baru = Users(nama=nama, email=email,
                                kontak=kontak, password=password, )

        # Sambung ke datastore
        client = datastore.Client()
        # Minta dibuatkan Key/Id baru untuk object baru
        key_baru = client.key(USERS_KIND)
        # Minta dibuatkan entity di datastore memakai key baru
        entity_baru = datastore.Entity(key=key_baru)
        # Simpan object Permintaan ke entity baru
        entity_baru.update(permintaan_baru.ke_dictionary())
        # Simpan entity ke datastore
        client.put(entity_baru)

        # Kembalikan object Permintaan yang baru disimpan dengan id yang diberikan
        # return Users(id=entity_baru.id,
        #                   nama=entity_baru["nama"],
        #                   email=entity_baru["email"],
        #                   jenis_kelamin=entity_baru["jenis_kelamin"],
        #                   date_created=entity_baru["date_created"])
        permintaan_baru.id = entity_baru.id
        permintaan_baru.date_created = entity_baru["date_created"]
        return permintaan_baru


# Ambil daftar Permintaan
#
# Ambil semua entity Permintaan yang ada di datastore.

def daftar():
    # Sambung ke datastore
    client = datastore.Client()

    # Buat query untuk meminta semua isi kind permintaan
    query = client.query(kind=USERS_KIND)
    # Jalankan query
    hasil = query.fetch()
    print(hasil)
    # print(hasil[0]["nama"])
    # Ambil setiap entity yang dikembalikan query dan jadikan list dari
    # object Permintaan.
    daftar_permintaan = []
    for satu_hasil in hasil:
        satu_permintaan = Users(id=satu_hasil.id,
                                nama=satu_hasil["nama"],
                                email=satu_hasil["email"],
                                date_created=satu_hasil["date_created"],
                                image=satu_hasil["image"],
                                kontak=satu_hasil["kontak"],
                                password=satu_hasil["password"]
                                )
        daftar_permintaan.append(satu_permintaan)

    # Kembalikan list object permintaan
    return daftar_permintaan

# get by id


def getId(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        satu_hasil = client.get(client.key(USERS_KIND, id))
        if satu_hasil != None:
            return Users(id=satu_hasil.id,
                         nama=satu_hasil["nama"],
                         email=satu_hasil["email"],
                         date_created=satu_hasil["date_created"],
                         image=satu_hasil["image"],
                         kontak=satu_hasil["kontak"],
                         password=satu_hasil["password"]
                         )
        else:
            return None

# update


def update(
        id,
        nama,
        email,
        image,
        kontak,
        password,
):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(USERS_KIND, id))
        if entity != None:
            entity["nama"] = nama
            entity["email"] = email
            entity["image"] = image
            entity["kontak"] = kontak
            entity["password"] = password
            client.put(entity)
            return "sukses"
        else:
            return "gagal"

# delete


def delete(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(USERS_KIND, id))
        if entity != None:
            client.delete(entity)
            return "sukses"
        else:
            return "gagal"


# get by id to userEntity
def getUserEntityById(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        satu_hasil = client.get(client.key(USERS_KIND, id))
        if satu_hasil != None:
            return satu_hasil
        else:
            return None
