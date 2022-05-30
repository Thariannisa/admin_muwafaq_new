from flask import redirect, render_template, request

from api.model.admin import model
from api import model
from api.model.diskusi.model import Diskusi, diskusi_KIND
from . import diskusi
from google.cloud import datastore
from form.forms import (
    AddDiskusiForm
)
diskusi_KIND = "DISKUSI"


@diskusi.route('/')
def maindiskusi():

    client = datastore.Client()
    query = client.query(kind=diskusi_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "idPlatform": data.id,
            "link": data['link'],
            "platform": data['platform'],
            "keterangan": data['keterangan']
        })
    return render_template('diskusi/index_diskusi.html',  data=hasil_baru, title="Diskusi")


@diskusi.route('/tambahplatform')
def addPlatform():
    form = AddDiskusiForm()
    return render_template('diskusi/create_diskusi.html', form=form, title="tambah diskusi")


@diskusi.route('/daftarplatform', methods=['POST'])
def daftarPlatform():

    Platform = request.form['platform']
    Link = request.form['link']
    Keterangan = request.form['keterangan']

    hasil = {}

    hasil["platform"] = Platform
    hasil["link"] = Link
    hasil["keterangan"] = Keterangan

    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(diskusi_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    # return render_template('modul/index_modul.html')
    # return hasil
    return redirect('/diskusi')


@diskusi.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(diskusi_KIND, id))
        if entity != None:
            client.delete(entity)
            return redirect('/diskusi')
    else:
        return "gagal"


@diskusi.route('/edit_diskusi/<int:id>',  methods=["GET", "POST"])
def edit_diskusi(id):

    # Lakukan pencarian berdasar id
    try:
        cari_diskusi = model.diskusi.atur.cari(id)
    except:

        return f"Gagal mencari diskusi dengan id: {id}.", 400
    # Pastikan berhasil
    if cari_diskusi is None:
        # return render_template('materi/tilawah/tema/edit_Tulisan2.html/', form=form, data=cari_materi)
        # return cari_materi
        return f"Gagal mencari diskusi dengan id: {id}.", 400
    # Load template
    # parameter title dikirim untuk mengisi nilai variabel title di template
    return render_template('diskusi/edit_diskusi.html/', data=cari_diskusi)


@diskusi.route('/updatediskusi/<int:id>', methods=["POST"])
def ubah_diskusi(id):
    client = datastore.Client()
    key = client.key(diskusi_KIND, id)
    entity = datastore.Entity(key=key)
    entity.update({
        'link': request.form['link'],
        'platform': request.form['platform'],
        'keterangan': request.form['keterangan'],
    })
    client.put(entity)

    # data = MateriMawaris.update(id,
    #                             # request.form['idTema'],
    #                             request.form['judul_tulisan'],
    #                             # request.form['author'],
    #                             # request.form['judul_video'],
    #                             request.form['tema'],
    #                             request.form['tulisan'],
    #                             # request.form['video']
    #                             )

    return redirect('/diskusi')
