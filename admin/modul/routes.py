from form.forms import AddModulForm
from flask import flash, jsonify, render_template, request, redirect
import os
import datetime
from . import modul
from google.cloud import storage
from google.cloud import datastore


MODUL_KIND = "MODUL"


@modul.route('/')
def mainModul():
    client = datastore.Client()
    query = client.query(kind=MODUL_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "judul": data['judul'],
            "PDF": data['PDF'],

        })
    return render_template('modul/index_modul.html', data=hasil_baru)


@modul.route('/tambahmodul')
def addModul():
    form = AddModulForm()
    return render_template('modul/createmodul.html', form=form)


@modul.route('/daftarmodul', methods=['POST'])
def daftarmodul():

    Judul = request.form['judul']
    PDF = uploadPDF(request)
    # if PDF == None:
    #     return ""
    # # (
    # #         jsonify(
    # #         ),
    # #         400,
    # #     )

    hasil = {}

    # hasil["tema"] = Tema
    hasil["judul"] = Judul
    hasil["PDF"] = PDF

    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(MODUL_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    # return render_template('modul/index_modul.html')
    # return hasil
    return redirect('/modul')


def uploadPDF(request):
    form = AddModulForm()
    uploaded_file = request.files.get("PDF")
    if not uploaded_file:
        return ""
    try:
        split = os.path.splitext(uploaded_file.filename)
        if split[1] not in [".pdf"]:
            return None

        # check size
        read = uploaded_file.read()
        size = len(read)
        if size >= 4000000:  # 4 mb
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


@modul.route('/edit_modul/<int:id>', methods=['GET'])
def edit(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(MODUL_KIND, id))
        if entity is not None:
            client.put(entity)
            return render_template('modul/editmodul.html')


@modul.route('/update/<int:id>', methods=['PUT'])
def update(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(MODUL_KIND, id))
        if entity is not None:
            client.put(entity)
            return redirect('/modul')


@modul.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(MODUL_KIND, id))
        if entity != None:
            client.delete(entity)
            return redirect('/modul')
    else:
        return "gagal"
