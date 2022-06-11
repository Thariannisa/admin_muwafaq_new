from google.cloud import datastore

from api.model.exception.model import EntityNotFoundException

from .model import Modul, MODUL_KIND


def getId(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        satu_hasil = client.get(client.key(MODUL_KIND, id))
        if satu_hasil != None:
            return Modul(id=satu_hasil.id,
                         judul=satu_hasil["judul"],
                         PDF=satu_hasil["PDF"],
                         )
        else:
            return None


def cari(id):

    if id is not None:
        # Buka koneksi ke datastore
        client = datastore.Client()
        # Minta dibuatkan key baru berdasarkan id
        key_modul = client.key(MODUL_KIND, id)
        # ambil hasil carinya berdasarkan key yang dibuat
        hasil = client.get(key_modul)
        # jika tidak ditemukan, bangkitkan exception
        if hasil is None:
            raise EntityNotFoundException(
                f"Tidak ada modul dengan id: {id}.")
        # buat list
        data_modul = []
        # buat objek modul
        upload_modul = Modul(id=hasil.id,
                             judul=hasil["judul"],
                             PDF=hasil["PDF"])
        # ubah format data ke dictionary dan append ke list
        data_modul.append(upload_modul)
        # kembalikan data penindaklanjut
        return data_modul


def ubah(id, edit_tulisan):
    # Buka koneksi ke datastore
    client = datastore.Client()
    # cari/filter data penindaklanjut berdasar property id
    key_getmodul = client.key(MODUL_KIND, id)
    #  ambil hasil carinya
    hasil = client.get(key_getmodul)
    # jika tidak ditemukan, bangkitkan exception
    if hasil is None:
        raise EntityNotFoundException(
            f"Tidak ada materi dengan id: {id}.")
    # Simpan
    hasil.update(edit_tulisan)
    client.put(hasil)
    # kembalikan data penindaklanjut
    return Modul(id=id,
                 judul=hasil["judul"],
                 PDF=hasil["PDF"])


def update(id, judul, PDF, ubah_modul):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(MODUL_KIND, id))
        if entity != None:
            entity["judul"] = judul
            entity["PDF"] = PDF
            entity.update(ubah_modul)
            client.put(entity)
            return "sukses"
    else:
        return "gagal"
