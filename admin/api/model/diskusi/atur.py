from google.cloud import datastore

from api.model.exception.model import EntityNotFoundException

from .model import Diskusi, diskusi_KIND


def getId(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        satu_hasil = client.get(client.key(diskusi_KIND, id))
        if satu_hasil != None:
            return Diskusi(id=satu_hasil.id,
                           platform=satu_hasil["platform"],
                           link=satu_hasil["link"],
                           keterangan=satu_hasil["keterangan"],
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
        key_materi = client.key(diskusi_KIND, id)
        # ambil hasil carinya berdasarkan key yang dibuat
        hasil = client.get(key_materi)
        # jika tidak ditemukan, bangkitkan exception
        if hasil is None:
            raise EntityNotFoundException(
                f"Tidak ada diskusis dengan id: {id}.")
        # buat list
        data_diskusi = []
        # buat objek penindaklanjut
        platform_diskusi = Diskusi(id=hasil.id,
                                   platform=hasil["platform"],
                                   link=hasil["link"],
                                   keterangan=hasil["keterangan"])
        # ubah format data ke dictionary dan append ke list
        data_diskusi.append(platform_diskusi)
        # kembalikan data penindaklanjut
        return data_diskusi


def ubah(id, edit_tulisan):
    # Buka koneksi ke datastore
    client = datastore.Client()
    # cari/filter data penindaklanjut berdasar property id
    key_platformdiskusi = client.key(diskusi_KIND, id)
    #  ambil hasil carinya
    hasil = client.get(key_platformdiskusi)
    # jika tidak ditemukan, bangkitkan exception
    if hasil is None:
        raise EntityNotFoundException(
            f"Tidak ada materi dengan id: {id}.")
    # Simpan
    hasil.update(edit_tulisan)
    client.put(hasil)
    # kembalikan data penindaklanjut
    return Diskusi(id=id,
                   platform=hasil["platform"],
                   link=hasil["link"],
                   keterangan=hasil["keterangan"])


def update(id, platform, keterangan, link, ubah_diskusi):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(diskusi_KIND, id))
        if entity != None:
            entity["platform"] = platform
            entity["keterangan"] = keterangan
            entity["link"] = link
            entity.update(ubah_diskusi)
            client.put(entity)
            return "sukses"
    else:
        return "gagal"
