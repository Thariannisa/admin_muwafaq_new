from google.cloud import datastore

from api.model.exception.model import EntityNotFoundException


from .model import Latihan, latihan_KIND


def getId(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        satu_hasil = client.get(client.key(latihan_KIND, id))
        if satu_hasil != None:
            return Latihan(id=satu_hasil.id,
                           pertanyaan=satu_hasil["pertanyaan"],
                           pilihan1=satu_hasil["pilihan1"],
                           pilihan2=satu_hasil["pilihan2"],
                           pilihan3=satu_hasil["pilihan3"],
                           pilihan4=satu_hasil["pilihan4"],
                           jawaban=satu_hasil["jawaban"],
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
        key_materi = client.key(latihan_KIND, id)
        # ambil hasil carinya berdasarkan key yang dibuat
        hasil = client.get(key_materi)
        # jika tidak ditemukan, bangkitkan exception
        if hasil is None:
            raise EntityNotFoundException(
                f"Tidak ada diskusis dengan id: {id}.")
        # buat list
        data_latihan = []
        # buat objek penindaklanjut
        objek_latihan = Latihan(id=hasil.id,
                                pertanyaan=hasil["pertanyaan"],
                                pilihan1=hasil["pilihan1"],
                                pilihan2=hasil["pilihan2"],
                                pilihan3=hasil["pilihan3"],
                                pilihan4=hasil["pilihan4"],
                                jawaban=hasil["jawaban"])
        # ubah format data ke dictionary dan append ke list
        data_latihan.append(objek_latihan)
        # kembalikan data penindaklanjut
        return data_latihan


def ubah(id, edit_tulisan):
    # Buka koneksi ke datastore
    client = datastore.Client()
    # cari/filter data penindaklanjut berdasar property id
    key_objeklatihan = client.key(latihan_KIND, id)
    #  ambil hasil carinya
    hasil = client.get(key_objeklatihan)
    # jika tidak ditemukan, bangkitkan exception
    if hasil is None:
        raise EntityNotFoundException(
            f"Tidak ada materi dengan id: {id}.")
    # Simpan
    hasil.update(edit_tulisan)
    client.put(hasil)
    # kembalikan data penindaklanjut
    return Latihan(id=id,
                   pertanyaan=hasil["pertanyaan"],
                   pilihan1=hasil["pilihan1"],
                   pilihan2=hasil["pilihan2"],
                   pilihan3=hasil["pilihan3"],
                   pilihan4=hasil["pilihan4"],
                   jawaban=hasil["jawaban"])


def update(id, pertanyaan, pilihan1, pilihan2, pilihan3, pilihan4, jawaban, ubah_latihan):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(latihan_KIND, id))
        if entity != None:
            entity["pertanyaan"] = pertanyaan
            entity["pilihan1"] = pilihan1
            entity["pilihan2"] = pilihan2
            entity["pilihan3"] = pilihan3
            entity["pilihan4"] = pilihan4
            entity["jawaban"] = jawaban
            entity.update(ubah_latihan)
            client.put(entity)
            return "sukses"
    else:
        return "gagal"
