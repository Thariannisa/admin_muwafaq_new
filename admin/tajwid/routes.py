import datetime
import os
from api import model
from api.model.tajwid.model import MateriTajwid, materiTajwid_KIND, tajwid_KIND
from xml.etree.ElementTree import dump
from flask import flash, jsonify, render_template, request, redirect
from api.model.admin.check_login import check_login
from form.forms import (
    EditTulisanForm,
    KontenTulisanForm,
    KontenVideoForm,
)
from . import tajwid
from google.cloud import datastore
from google.cloud import storage


@tajwid.route('/')
@check_login
def maintajwid(datatajwid):
    client = datastore.Client()
    query = client.query(kind=tajwid_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idTema": data.id,
            "konten": data['konten'],
            "tema": data['tema']
        })
    return render_template('materi/tajwid/index_tajwid.html', data=hasil_baru)


@tajwid.route('/tambahtema')
def addTema():
    return render_template('materi/tajwid/tema/add_tema.html')


@tajwid.route('/daftartema', methods=['POST'])
def daftartema():
    Tema = request.form['tema']
    jenis_konten = request.form['konten']
    hasil = {}
    hasil["tema"] = Tema
    hasil["konten"] = jenis_konten
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(tajwid_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    return redirect('/tajwid')


@tajwid.route('/detail_video/<int:idTema>')
def detailTemaVideo(idTema):
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiTajwid_KIND)
    query.add_filter("idTema", "=", idTema)
    hasil = query.fetch()
    res = client.get(client.key(tajwid_KIND, idTema))
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
        "konten": res["konten"]
    }
    return render_template('materi/tajwid/tema/tema_video.html', data=context)


@tajwid.route('/tambahvideo')
def addKontenVideo():
    form = KontenVideoForm()
    client = datastore.Client()
    query = client.query(kind=tajwid_KIND)
    hasil = query.fetch()
    hasil_tema = []
    for data in hasil:
        hasil_tema.append({
            "tema": data['tema'],
            "idTema": data.id
        })
    return render_template('materi/tajwid/tema/add_video.html', data=hasil_tema, form=form)


@tajwid.route('/daftarvideo', methods=['POST'])
def daftarKontenVideo():
    Tema = request.form['idTema']
    client = datastore.Client()
    query = client.query(kind=tajwid_KIND)
    query.add_filter("tema", "=", Tema)
    data1 = list(query.fetch())
    Judul = request.form['judul']
    author = request.form['author']
    Video = uploadVideo(request)
    idTema = str(data1[0].id)
    hasil = {}
    hasil["judul"] = Judul
    hasil["author"] = author
    hasil['tulisan'] = ""
    hasil["tema"] = Tema
    hasil["idTema"] = int(idTema)
    hasil["video"] = Video
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(materiTajwid_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    return redirect('/tajwid/detail_video/' + idTema)


@tajwid.route('/tambahpembahasan')
def addKontenTulisan():
    form = KontenTulisanForm()
    client = datastore.Client()
    query = client.query(kind=tajwid_KIND)
    hasil = query.fetch()
    hasil_tema = []
    for data in hasil:
        hasil_tema.append({
            "tema": data['tema'],
            "idTema": data.id
        })
    return render_template('materi/tajwid/tema/add_Tulisan.html', data=hasil_tema, form=form)


@tajwid.route('/daftartulisan', methods=['POST'])
def daftarKontenTulisan():
    Tema = request.form['idTema']
    # return Tema
    client = datastore.Client()
    query = client.query(kind=tajwid_KIND)
    query.add_filter("tema", "=", Tema)
    data1 = list(query.fetch())
    Judul = request.form['judul']
    Tulisan = request.form['tulisan']
    idTema = str(data1[0].id)
    hasil = {}
    hasil["judul"] = Judul
    hasil["tulisan"] = Tulisan
    hasil['author'] = ""
    hasil['video'] = ""
    hasil["tema"] = Tema
    hasil["idTema"] = int(idTema)
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(materiTajwid_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    flash("Your materi has been added!", "success")
    return redirect('/tajwid/detail_tulisan/' + idTema)


@tajwid.route('/detail_tulisan/<int:idTema>')
def detailTemaTulisan(idTema):
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    query = client.query(kind=materiTajwid_KIND)
    query.add_filter("idTema", "=", idTema)
    hasil = query.fetch()
    res = client.get(client.key(tajwid_KIND, idTema))
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
    return render_template('materi/tajwid/tema/tema_tulisan.html', data=context)


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


@tajwid.route('/deletekontenvideo/<int:id>/<int:idTema>', methods=['GET', 'POST'])
def deleteKontenVideo(id, idTema):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(materiTajwid_KIND, id))
        if entity != None:
            client.delete(entity)
            return redirect('/tajwid/detail_video/' + str(idTema))
    else:
        return "gagal"


@tajwid.route('/deletekontentulisan/<int:id>/<int:idTema>', methods=['GET', 'POST'])
def deleteKontenTulisan(id, idTema):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(materiTajwid_KIND, id))

        if entity != None:
            client.delete(entity)
            return redirect('/tajwid/detail_tulisan/' + str(idTema))
    else:
        return "gagal"


@tajwid.route('/deletetema/<int:id>', methods=['GET', 'POST'])
def deleteTema(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(tajwid_KIND, id))
        if entity != None:
            client.delete(entity)
            return redirect('/tajwid')
    else:
        return "gagal"


@tajwid.route('/edit_tulisan/<int:id>/<int:idTema>',  methods=["GET", "POST"])
def edit_tulisan(id, idTema):
    form = KontenTulisanForm()
    # Lakukan pencarian materi berdasar id
    try:
        cari_materi = model.tajwid.atur.cari(id)
    except:

        return f"Gagal mencari materi dengan id: {id}.", 400
    # Pastikan berhasil
    if cari_materi is None:
        # return render_template('materi/tajwid/tema/edit_Tulisan2.html/', form=form, data=cari_materi)
        # return cari_materi
        return f"Gagal mencari materi dengan id: {id}.", 400
    # Load template
    # parameter title dikirim untuk mengisi nilai variabel title di template
    return render_template('materi/tajwid/tema/edit_Tulisan.html/', form=form, data=cari_materi)


@tajwid.route('/updatetulisan/<int:id>/<int:idTema>', methods=["POST"])
def ubah_tulisan(id, idTema):
    Tema = request.form['idTema']
    client = datastore.Client()
    query = client.query(kind=tajwid_KIND)
    query.add_filter("tema", "=", Tema)
    data1 = list(query.fetch())
    Judul = request.form['judul']
    Tulisan = request.form['tulisan']
    idTema = str(data1[0].id)
    hasil = {}
    hasil["judul"] = Judul
    hasil["tulisan"] = Tulisan
    hasil['author'] = ""
    hasil['video'] = ""
    hasil["tema"] = Tema
    hasil["idTema"] = int(idTema)
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key = client.key(materiTajwid_KIND, id)
    # Minta dibuatkan entity di datastore memakai key baru
    entity = datastore.Entity(key=key)
    # Simpan object Permintaan ke entity baru
    entity.update(hasil)
    # Simpan entity ke datastore
    client.put(entity)
    return redirect('/tajwid/detail_tulisan/' + str(idTema))


@tajwid.route('/edit_video/<int:id>/<int:idTema>',  methods=["GET", "POST"])
def edit_video(id, idTema):
    form = KontenVideoForm()
    # Lakukan pencarian materi berdasar id
    try:
        cari_materi = model.tajwid.atur.cari(id)
    except:

        return f"Gagal mencari materi dengan id: {id}.", 400
    # Pastikan berhasil
    if cari_materi is None:
        # return render_template('materi/tajwid/tema/edit_Tulisan2.html/', form=form, data=cari_materi)
        # return cari_materi
        return f"Gagal mencari materi dengan id: {id}.", 400
    # Load template
    # parameter title dikirim untuk mengisi nilai variabel title di template
    return render_template('materi/tajwid/tema/edit_video.html/', form=form, data=cari_materi)


@tajwid.route('/updatevideo/<int:id>/<int:idTema>', methods=["POST"])
def ubah_video(id, idTema):
    Tema = request.form['idTema']
    client = datastore.Client()
    query = client.query(kind=tajwid_KIND)
    query.add_filter("tema", "=", Tema)
    data1 = list(query.fetch())
    Judul = request.form['judul']
    author = request.form['author']
    Video = uploadVideo(request)
    idTema = str(data1[0].id)
    hasil = {}
    hasil["judul"] = Judul
    hasil["author"] = author
    hasil['tulisan'] = ""
    hasil["tema"] = Tema
    hasil["idTema"] = int(idTema)
    hasil["video"] = Video
    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key = client.key(materiTajwid_KIND, id)
    # Minta dibuatkan entity di datastore memakai key baru
    entity = datastore.Entity(key=key)
    # Simpan object Permintaan ke entity baru
    entity.update(hasil)
    # Simpan entity ke datastore
    client.put(entity)
    return redirect('/tajwid/detail_video/' + idTema)
