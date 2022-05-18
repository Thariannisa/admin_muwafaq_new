import logging
from api.model.tilawah.model import MateriTilawah, materiTilawah_KIND
import datetime
import os
from xml.etree.ElementTree import dump

from flask import Flask, flash, jsonify, render_template, request, redirect
from flask import make_response
from api import model
from api.model.exception.model import EntityNotFoundException
from api.model.tilawah.atur import ubah, update
from form.forms import (
    AddTemaForm,
    KontenTulisanForm,
    KontenVideoForm,
)
from . import tilawah
from google.cloud import datastore
from google.cloud import storage
tilawah_KIND = "tilawah"
materiTilawah_KIND = "materi_tilawah"


@tilawah.route('/')
def maintilawah():
    client = datastore.Client()
    query = client.query(kind=tilawah_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idTema": data.id,
            "konten": data['konten'],
            "tema": data['tema']
        })
    return render_template('tilawah/index_tilawah.html', data=hasil_baru)


@tilawah.route('/tambahtema')
def addTema():
    form = AddTemaForm()
    return render_template('materi/tilawah/tema/add_tema.html', form=form)


@tilawah.route('/daftartema', methods=['POST'])
def daftartema():
    Tema = request.form['tema']
    jenis_konten = request.form['konten']

    hasil = {}

    hasil["tema"] = Tema
    hasil["konten"] = jenis_konten

    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(tilawah_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    # return render_template('modul/index_modul.html')
    # return hasil
    return redirect('/tilawah')


@tilawah.route('/detail_video/<int:idTema>')
def detailTemaVideo(idTema):
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiTilawah_KIND)
    query.add_filter("idTema", "=", idTema)
    hasil = query.fetch()
    res = client.get(client.key(tilawah_KIND, idTema))
    # if res == None:
    #     return "tidak ada"
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "video": data['video'],
            "author": data['author'],
            "idTema": data['idTema'],
            "tema": data['tema']
        })
    context = {
        "data": hasil_baru,
        "tema": res["tema"],
        "konten": res["konten"],
    }
    # return context
    return render_template('materi/tilawah/tema/tema_video.html', data=context)


@tilawah.route('/tambahvideo')
def addKontenVideo():
    form = KontenVideoForm()
    client = datastore.Client()
    query = client.query(kind=tilawah_KIND)
    hasil = query.fetch()
    hasil_tema = []
    for data in hasil:
        hasil_tema.append({
            "tema": data['tema'],
            "idTema": data.id
        })
    return render_template('materi/tilawah/tema/add_video.html', data=hasil_tema, form=form)


@tilawah.route('/daftarvideo', methods=['POST'])
def daftarKontenVideo():
    Tema = request.form['idTema']
    # return Tema
    client = datastore.Client()
    query = client.query(kind=tilawah_KIND)
    query.add_filter("tema", "=", Tema)
    data1 = list(query.fetch())
    Judul = request.form['judul']
    author = request.form['author']
    Video = uploadVideo(request)
    idTema = str(data1[0].id)
    # return idTema
    if Video == None:
        return ""
    hasil = {}
    hasil["judul"] = Judul
    hasil["author"] = author
    hasil['tulisan'] = ""
    hasil["tema"] = Tema
    hasil["idTema"] = int(idTema)
    hasil["video"] = Video
    if Video == None:
        return ""
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(materiTilawah_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    return redirect('/tilawah/detail_video/' + idTema)
# return render_template('modul/index_modul.html')
    # return hasil
# return render_template('materi/tilawah/tema/detail_tema_video.html', data=entity_baru)
# return render_template('materi/tilawah/tema/add_konten_video.html')


# def daftarKontenVideo():

#     idTema = request.form['idTema']


@tilawah.route('/tambahpembahasan')
def addKontenTulisan():
    form = KontenTulisanForm()
    client = datastore.Client()
    query = client.query(kind=tilawah_KIND)
    hasil = query.fetch()
    hasil_tema = []
    for data in hasil:
        hasil_tema.append({
            "tema": data['tema'],
            "idTema": data.id
        })
    return render_template('materi/tilawah/tema/add_Tulisan.html', data=hasil_tema, form=form)


@tilawah.route('/daftartulisan', methods=['POST'])
def daftarKontenTulisan():

    Tema = request.form['idTema']
    # return Tema
    client = datastore.Client()
    query = client.query(kind=tilawah_KIND)
    query.add_filter("tema", "=", Tema)
    data1 = list(query.fetch())
    Judul = request.form['judul']
    Tulisan = request.form['tulisan']
    idTema = str(data1[0].id)
    # return idTema

    hasil = {}
    hasil["judul"] = Judul
    hasil["tulisan"] = Tulisan
    # hasil['judul_video'] = ""
    hasil['author'] = ""
    hasil['video'] = ""
    hasil["tema"] = Tema
    hasil["idTema"] = int(idTema)

    # hasil["konten"] = Jenis_konten
    # hasil["video"] = Video

    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(materiTilawah_KIND)

    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    # return render_template('modul/index_modul.html')
    # return hasil
    flash("Your materi has been added!", "success")
    return redirect('/tilawah/detail_tulisan/' + idTema)


@tilawah.route('/detail_tulisan/<int:idTema>')
def detailTemaTulisan(idTema):
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiTilawah_KIND)
    query.add_filter("idTema", "=", idTema)
    hasil = query.fetch()

    res = client.get(client.key(tilawah_KIND, idTema))

    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "tulisan": data['tulisan'],
            "idTema": data['idTema'],
            "tema": data['tema']
        })
    context = {

        "data": hasil_baru,
        "tema": res["tema"],
        "konten": res["konten"]
    }
    # return (context)
    return render_template('materi/tilawah/tema/tema_tulisan.html', data=context)


# @tilawah.route('/detail_pembahasan/<int:id>')
# def detailTulisan(id):
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     query = client.query(kind=materiTilawah_KIND)
#     hasil = query.fetch()

#     # res = client.get(client.key(mawaris_KIND,))

#     hasil_baru = []
#     for data in hasil:
#         hasil_baru.append({
#             "id": data.id,
#             "judul_tulisan": data['judul_tulisan'],
#             "tulisan": data['tulisan'],

#         })
#     # expectedResult = [d for d in hasil_baru if d['id'] == id][0]
#     # return str(hasil_baru)
#     # return redirect('/mawaris/detail/' + id, data=hasil_baru)
#     return render_template('materi/tilawah/tema/detail_tulisan.html', data=hasil_baru)


def uploadVideo(request):
    uploaded_file = request.files.get("video")

    if not uploaded_file:
        return ""
    try:
        split = os.path.splitext(uploaded_file.filename)
        if split[1] not in [".mp4"]:
            return None

        # check size
        read = uploaded_file.read()
        size = len(read)
        if size >= 40000000:  # 40 mb
            return None
        # Create a Cloud Storage client.
        gcs = storage.Client()
        # Get the bucket that the file will be uploaded to.
        bucket = gcs.get_bucket("ta-fahmil.appspot.com")
        # Create a new blob and upload the file's content.
        dt = str(datetime.datetime.now())
        blob = bucket.blob(split[0] + dt + split[1])
        blob.upload_from_string(read, content_type=uploaded_file.content_type)
        blob.make_public()

        # The public URL can be used to directly access the uploaded file via HTTP.
        return str(blob.public_url)
    except:

        return ""


@tilawah.route('/deletekontenvideo/<int:id>/<int:idTema>', methods=['GET', 'POST'])
def deleteKontenVideo(id, idTema):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(materiTilawah_KIND, id))

        if entity != None:
            client.delete(entity)
            return redirect('/tilawah/detail_video/' + str(idTema))
    else:
        return "gagal"


@tilawah.route('/deletekontentulisan/<int:id>/<int:idTema>', methods=['GET', 'POST'])
def deleteKontenTulisan(id, idTema):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(materiTilawah_KIND, id))

        if entity != None:
            client.delete(entity)
            return redirect('/tilawah/detail_tulisan/' + str(idTema))
    else:
        return "gagal"


@tilawah.route('/deletetema/<int:id>', methods=['GET', 'POST'])
def deleteTema(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(tilawah_KIND, id))
        if entity != None:
            client.delete(entity)
            return redirect('/tilawah')
    else:
        return "gagal"


#


# @tilawah.route('/edit_tulisan/<int:id>/<int:idTema>', methods=['GET', 'POST'])
# def edit_tulisan(id, idTema):
#     form = KontenTulisanForm()
#     client = datastore.Client()
#     # cari/filter data operator berdasar property id
#     key_materi_tilawah = client.key(materiTilawah_KIND, id)
#     #  ambil hasil carinya
#     hasil = client.get(key_materi_tilawah)

#     if hasil:
#         materi_baru = hasil
#         return render_template('materi/tilawah/tema/edit_Tulisan.html/', form=form, data=materi_baru)
#         # return materi_baru
#         # return redirect('/tilawah/detail_tulisan/' + id)
#     # else:
#         # return "tes data salah", 400

#     # # Periksa parameter sudah benar
#     if materi_baru is None:
#         return "Data materi baru tidak ada!", 400
#     if "judul" not in materi_baru:
#         return "Salah data! Property judul tidak ada.", 400
#     if "tulisan" not in materi_baru:
#         return "Salah data! Property tulisan tidak ada.", 400
#     if "tema" not in materi_baru:
#         return "Salah data! Property tema tidak ada.",
#     if "idTema" not in materi_baru:
#         return "Salah data! Property idTema tidak ada.", 400

#     cari_materi = model.tilawah.atur.cari(id)

#     if len(cari_materi) == 1:
#         cari_materi = cari_materi[0]

#         cari_materi["judul"] = cari_materi["judul"]
#         cari_materi["tulisan"] = cari_materi["tulisan"]
#         # cari_materi["judul_video"] = cari_materi[""]
#         # cari_materi["author"] = cari_materi[""]
#         # cari_materi["video"] = cari_materi[""]
#         cari_materi["tema"] = cari_materi["tema"]
#         cari_materi["idTema"] = cari_materi["idTema"]

#         del cari_materi["id"]
#     try:
#         hasil = ubah(id, materi_baru)
#     except EntityNotFoundException:
#         return f"Tidak ada materi dengan id: {id}.", 400
#     # except:
#     #     return f"Gagal mengubah materi dengan id: {id}.", 400

#     # except ValueError as ve:
#     #     # print(ve)
#     #     logging.error(ve)

#        # Pastikan berhasil
#     if hasil is None:
#         # set flash message
#         flash('Gagal mengubah data materi')
#         # direct ke laman tambah materi
#         return render_template('materi/tilawah/tema/edit_Tulisan.html' + id)

#     # set flash message
#     flash('Data materi berhasil diubah')
#     # direct ke halaman daftar materi
#     return redirect('/tilawah/detail_tulisan/' + idTema)


# def uploadImage(request):
#     uploaded_file = request.files.get("gambar")
#     if not uploaded_file:
#         return ""
#     try:
#         split = os.path.splitext(uploaded_file.filename)
#         if split[1] not in [".jpg", ".jpeg"]:
#             return None

#         # check size
#         read = uploaded_file.read()
#         size = len(read)
#         if size >= 4000000:  # 4 mb
#             return None
#         # Create a Cloud Storage client.
#         gcs = storage.Client()

#         # Get the bucket that the file will be uploaded to.
#         bucket = gcs.get_bucket("ta-fahmil.appspot.com")
#         # Create a new blob and upload the file's content.

#         dt = str(datetime.datetime.now())
#         blob = bucket.blob(split[0] + dt + split[1])
#         blob.upload_from_string(read, content_type=uploaded_file.content_type)
#         blob.make_public()
#         # The public URL can be used to directly access the uploaded file via HTTP.
#         return str(blob.public_url)
#     except:
#         return ""


# @tilawah.route('/edit_tulisan/<int:id>/<int:idTema>', methods=['GET', 'POST'])
# def edit_tulisan(id, idTema):
#     form = KontenTulisanForm()

#     cari_materi = model.tilawah.atur.cari(id)

#     if len(cari_materi) == 1:
#         cari_materi = cari_materi[0]
#         cari_materi["judul"] = cari_materi["judul"]
#         cari_materi["tulisan"] = cari_materi["tulisan"]
#         cari_materi["judul_video"] = cari_materi[""]
#         cari_materi["author"] = cari_materi[""]
#         cari_materi["video"] = cari_materi[""]
#         cari_materi["tema"] = cari_materi["tema"]
#         cari_materi["idTema"] = cari_materi["idTema"]

#         del cari_materi["id"]
#     try:
#         cari_materi = model.tilawah.atur.cari(id)
#     except:
#         return f"Gagal mencari materi dengan id: {id}.", 400

#     # Pastikan berhasil
#     if cari_materi is None:
#         # set flash message
#         flash('Gagal mengubah data operator')
#         # direct ke laman tambah operator
#         return render_template('materi/tilawah/tema/edit_Tulisan2.html/', form=form, data=cari_materi)

#     # set flash message
#     flash('Data operator berhasil diubah')
#     # direct ke halaman daftar operator
#     return redirect('/tilawah/detail_tulisan/' + idTema)


@tilawah.route('/edit_tulisan/<int:id>/<int:idTema>', methods=['GET', 'POST'])
def edit_tulisan(id, idTema):
    form = KontenTulisanForm()
    # Lakukan pencarian operator berdasar id
    try:
        cari_materi = model.tilawah.atur.cari(id)
    except:
        return f"Gagal mencari materi dengan id: {id}.", 400
    # Pastikan berhasil
    if cari_materi is None:
        # return render_template('materi/tilawah/tema/edit_Tulisan2.html/', form=form, data=cari_materi)
        return f"Gagal mencari materi dengan id: {id}.", 400
    # Load template
    # parameter title dikirim untuk mengisi nilai variabel title di template
    return render_template('materi/tilawah/tema/edit_Tulisan2.html/', form=form, data=cari_materi)
    # return redirect('/tilawah/detail_tulisan/' + str(idTema))
    # if cari_materi is None:
    #     # set flash message
    #     # flash('Gagal mengubah data operator')
    #     # direct ke laman tambah operator
    #     return render_template('materi/tilawah/tema/edit_Tulisan2.html/', form=form, data=cari_materi)

    # # set flash message
    # flash('Data operator berhasil diubah')
    # # direct ke halaman daftar operator
    # return redirect('/tilawah/detail_tulisan/' + str(idTema))


@tilawah.route('/ubah_tulisan', methods=["POST"])
def ubah_tulisan(id, idTema):

    data = MateriTilawah.update(id,
                                # request.form['idTema'],
                                request.form['judul_tulisan'],
                                # request.form['author'],
                                # request.form['judul_video'],
                                request.form['tema'],
                                request.form['tulisan'],
                                # request.form['video']
                                )

    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(materiTilawah_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(data)
    # Simpan entity ke datastore
    client.put(entity_baru)
    # return redirect('/tilawah/detail_video/' + idTema)

    return redirect('/tilawah/detail_tulisan/' + str(idTema))


# @tilawah.route('/update/<int:id>/<int:idTema>', methods=["GET"])
# def update(id, idTema):

#     data = MateriTilawah.update(id,
#                                 request.form['idTema'],
#                                 request.form['judul_tulisan'],
#                                 # request.form['author'],
#                                 # request.form['judul_video'],
#                                 request.form['tema'],
#                                 request.form['tulisan'],
#                                 # request.form['video']
#                                 )
#     client = datastore.Client()
#     # Minta dibuatkan Key/Id baru untuk object baru
#     key_baru = client.key(materiTilawah_KIND)
#     # Minta dibuatkan entity di datastore memakai key baru
#     entity_baru = datastore.Entity(key=key_baru)
#     # Simpan object Permintaan ke entity baru
#     entity_baru.update(data)
#     # Simpan entity ke datastore
#     client.put(entity_baru)
#     # return redirect('/tilawah/detail_video/' + idTema)

#     return redirect('/tilawah/detail_tulisan/' + str(idTema))
