from google.cloud import datastore

from .model import USERS2_KIND, Users2

# Tambah Permintaan
#
# Tambah obejct Permintaan ke datastore.


def login(
        email,
        password,
):
    # Buat object hanya jika kedua data ada
    if email != None and password != None:
        # Buat object baru
        # Sambung ke datastore
        client = datastore.Client()

        # Buat query untuk meminta semua isi kind permintaan
        query = client.query(kind=USERS2_KIND)
        query.add_filter("email", "=", email)
        # Jalankan query
        satuHasil = list(query.fetch(limit=1))
        if satuHasil:
            data = satuHasil[0]

            hasilBaru = Users2(id=data.id,
                               nama=data["nama"],
                               email=data["email"],
                               date_created=data["date_created"],
                               image=data["image"],
                               kontak=data["kontak"],
                               password=data["password"],
                               )
            # Kembalikan list object permintaan
            return hasilBaru

    return None
# get by id


def register(
    nama,
    email,
    image,
    kontak,
    password,
    id=None,

):
    if nama != None and email != None and image != None and kontak != None and password != None:

        client = datastore.Client()
        dataUser = Users2(nama=nama, email=email, image=image,
                          kontak=kontak, password=password)

        userBaru = dataUser
        keyBaru = client.key(USERS2_KIND)

        entityBaru = datastore.Entity(key=keyBaru)
        dataDictionary = userBaru.ke_dictionary()
        dataDictionary['emailKonfirmasi'] = False
        entityBaru.update(dataDictionary)
        client.put(entityBaru)

        userBaru.id = entityBaru.id
        userBaru.date_created = entityBaru["date_created"]
        return userBaru


def getId(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        satu_hasil = client.get(client.key(USERS2_KIND, id))
        if satu_hasil != None:
            return Users2(id=satu_hasil.id,
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
        entity = client.get(client.key(USERS2_KIND, id))
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
        entity = client.get(client.key(USERS2_KIND, id))
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
        satu_hasil = client.get(client.key(USERS2_KIND, id))
        if satu_hasil != None:
            return satu_hasil
        else:
            return None
