from google.cloud import datastore

from api.model.exception.model import EntityNotFoundException

from .model import MateriTilawah, materiTilawah_KIND


def getId(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        satu_hasil = client.get(client.key(materiTilawah_KIND, id))
        if satu_hasil != None:
            return MateriTilawah(id=satu_hasil.id,
                                 idTema=satu_hasil["idTema"],
                                 judul=satu_hasil["judul"],
                                 #   date_created=satu_hasil["date_created"],
                                 author=satu_hasil["author"],
                                 tema=satu_hasil["tema"],
                                 tulisan=satu_hasil["tulisan"],
                                 video=satu_hasil["video"]
                                 )
        else:
            return None


def cari(id):
    """
    Mengambil salah satu entitas pada kind PENINDAKLANJUT_KIND berdasarkan property id

    Parameter:
        + id : id Penindaklanjut

    Returns:
        + List dictionary salah satu penindaklanjut

    """
    if id is not None:
        # Buka koneksi ke datastore
        client = datastore.Client()
        # Minta dibuatkan key baru berdasarkan id
        key_materi = client.key(materiTilawah_KIND, id)
        # ambil hasil carinya berdasarkan key yang dibuat
        hasil = client.get(key_materi)
        # jika tidak ditemukan, bangkitkan exception
        if hasil is None:
            raise EntityNotFoundException(
                f"Tidak ada materi dengan id: {id}.")
        # buat list
        data_materi = []
        # buat objek penindaklanjut
        materi_tilawah = MateriTilawah(id=hasil.id,
                                       idTema=hasil["idTema"],
                                       judul=hasil["judul"],
                                       #   date_created=hasil["date_created"],
                                       author=hasil["author"],
                                       tema=hasil["tema"],
                                       tulisan=hasil["tulisan"],
                                       video=hasil["video"])
        # ubah format data ke dictionary dan append ke list
        data_materi.append(materi_tilawah)
        # kembalikan data penindaklanjut
        return data_materi


# def cari(id):

#     # cek parameter agar tidak kosong
#     if id is not None:
#         # Buka koneksi ke datastore
#         client = datastore.Client()
#         # Minta dibuatkan key baru berdasarkan id
#         key_materi_tilawah = client.key(materiTilawah_KIND, id)
#         # ambil hasil carinya berdasarkan key yang dibuat
#         hasil = client.get(key_materi_tilawah)
#         # jika tidak ditemukan, bangkitkan exception
#         if hasil is None:
#             raise EntityNotFoundException(
#                 f"Tidak ada materi dengan id: {id}.")
#         # buat list
#         data_materi = []
#         # buat objek materi
#         materi_tilawah = MateriTilawah(id=hasil.id,
#                                        idTema=hasil["idTema"],
#                                        judul=hasil["judul"],
#                                        #   date_created=hasil["date_created"],
#                                        author=hasil["author"],
#                                        tema=hasil["tema"],
#                                        tulisan=hasil["tulisan"],
#                                        video=hasil["video"])
#         # ubah format data ke dictionary dan append ke list
#         data_materi.append(materi_tilawah)
#         # kembalikan data materi
#         return data_materi


# def ubah(id, edit_tulisan):

#     # Buka koneksi ke datastore
#     client = datastore.Client()
#     # cari/filter data materi berdasar property id
#     key_materi_tilawah = client.key(materiTilawah_KIND, id)
#     #  ambil hasil carinya
#     hasil = client.get(key_materi_tilawah)
#     # jika tidak ditemukan, bangkitkan exception
#     if hasil is None:
#         raise EntityNotFoundException(f"Tidak ada materi dengan id: {id}.")
#     # Simpan
#     hasil.update(edit_tulisan)
#     client.put(hasil)
#     # kembalikan data materi
#     return MateriTilawah(id=hasil.id,
#                          idTema=hasil["idTema"],
#                          judul_tulisan=hasil["judul_tulisan"],
#                          #   date_created=hasil["date_created"],
#                          author=hasil["author"],
#                          judul_video=hasil["judul_video"],
#                          tema=hasil["tema"],
#                          tulisan=hasil["tulisan"],
#                          video=hasil["video"])


def ubah(id, edit_tulisan):
    # Buka koneksi ke datastore
    client = datastore.Client()
    # cari/filter data penindaklanjut berdasar property id
    key_materitilawah = client.key(materiTilawah_KIND, id)
    #  ambil hasil carinya
    hasil = client.get(key_materitilawah)
    # jika tidak ditemukan, bangkitkan exception
    if hasil is None:
        raise EntityNotFoundException(
            f"Tidak ada materi dengan id: {id}.")
    # Simpan
    hasil.update(edit_tulisan)
    client.put(hasil)
    # kembalikan data penindaklanjut
    return MateriTilawah(id=id,
                         idTema=hasil["idTema"],
                         judul_tulisan=hasil["judul_tulisan"],
                         #   date_created=hasil["date_created"],
                         author=hasil["author"],
                         judul_video=hasil["judul_video"],
                         tema=hasil["tema"],
                         tulisan=hasil["tulisan"],
                         video=hasil["video"])


def update(id, idTema, judul_tulisan, author, judul_video, video, tema, tulisan):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(materiTilawah_KIND, id))
        if entity != None and idTema == entity["idTema"].id:
            entity["judul_tulisan"] = judul_tulisan
            entity["author"] = author
            entity["judul_video"] = judul_video
            entity["tema"] = tema
            entity["tulisan"] = tulisan
            entity["video"] = video
            client.put(entity)
            return "sukses"
    else:
        return "gagal"
