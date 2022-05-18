from flask import redirect, render_template, request
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
    return render_template('diskusi/index_diskusi.html',  data=hasil_baru)


@diskusi.route('/tambahplatform')
def addPlatform():
    form = AddDiskusiForm()
    return render_template('diskusi/create_diskusi.html', form=form)


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

# @diskusi.route('/edit/<int:id>')
# def edit(id):
#     return render_template('/diskusi/edit_diskusi.html')
# # def update(id):
# #     # data = request.get_json()
# #     data = diskusi.update(
# #         id,
# #         data["platform"],
# #         data["link"],
# #     )
# # return data, 200
# # update


# @diskusi.route('/update/<int:id>', methods=['POST'])
# def update(id):
#     # Buat object hanya jika kedua data ada
#     if id != None:
#         # Sambung ke datastore
#         client = datastore.Client()
#         entity = client.get(client.key(diskusi_KIND, id))
#         if entity != None:
#             entity["platform"],
#             entity["link"],

#             client.put(entity)
#             return redirect('/diskusi')
