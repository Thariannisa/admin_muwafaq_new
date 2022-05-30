import csv
import datetime
import os
from xml.etree.ElementTree import dump
from flask import flash, jsonify, render_template, request, redirect
from api.model.latihan import model
from api import model
from api.model.latihan.model import Latihan, latihan_KIND
from form.forms import AddLatihanForm
from . import latihan
from google.cloud import datastore
from google.cloud import storage
latihan_KIND = "latihan"


@latihan.route('/')
def mainlatihan():
    client = datastore.Client()
    query = client.query(kind=latihan_KIND)
    hasil = query.fetch()
    hasil_baru = []
    for data in hasil:
        hasil_baru.append({
            "id": data.id,
            "pertanyaan": data['pertanyaan'],
            "pilihan1": data['pilihan1'],
            "pilihan2": data['pilihan2'],
            "pilihan3": data['pilihan3'],
            "pilihan4": data['pilihan4'],
            "jawaban": data['jawaban'],


        })
    return render_template('latihan/index_latihan.html', data=hasil_baru, title="Latihan")


@latihan.route('/tambahlatihan')
def addLatihan():
    form = AddLatihanForm()
    return render_template('latihan/add_latihan.html', form=form, title="tambah latihan")


@latihan.route('/daftarlatihan', methods=['POST'])
def daftarlatihan():
    Pertanyaan = request.form['pertanyaan']
    Pilihan1 = request.form['pilihan1']
    Pilihan2 = request.form['pilihan2']
    Pilihan3 = request.form['pilihan3']
    Pilihan4 = request.form['pilihan4']
    Jawaban = request.form['jawaban']

    hasil = {}

    hasil["pertanyaan"] = Pertanyaan
    hasil["pilihan1"] = Pilihan1
    hasil["pilihan2"] = Pilihan2
    hasil["pilihan3"] = Pilihan3
    hasil["pilihan4"] = Pilihan4
    hasil["jawaban"] = Jawaban

    if Jawaban == "pilihan1":
        hasil["jawaban"] = Pilihan1
    elif Jawaban == "pilihan2":
        hasil["jawaban"] = Pilihan2
    elif Jawaban == "pilihan3":
        hasil["jawaban"] = Pilihan3
    elif Jawaban == "pilihan4":
        hasil["jawaban"] = Pilihan4

    client = datastore.Client()
    # Minta dibuatkan Key/Id baru untuk object baru
    key_baru = client.key(latihan_KIND)
    # Minta dibuatkan entity di datastore memakai key baru
    entity_baru = datastore.Entity(key=key_baru)
    # Simpan object Permintaan ke entity baru
    entity_baru.update(hasil)
    # Simpan entity ke datastore
    client.put(entity_baru)
    # return render_template('modul/index_modul.html')
    # return hasil

    return redirect('/latihan')


@latihan.route('/deletelatihan/<int:id>', methods=['GET', 'POST'])
def deleteLatihan(id):
    # Buat object hanya jika kedua data ada
    if id != None:
        # Sambung ke datastore
        client = datastore.Client()
        entity = client.get(client.key(latihan_KIND, id))
        if entity != None:
            client.delete(entity)
            return redirect('/latihan')
    else:
        return "gagal"


@latihan.route('/edit_latihan/<int:id>',  methods=["GET", "POST"])
def edit_latihan(id):

    # Lakukan pencarian berdasar id
    try:
        cari_latihan = model.latihan.atur.cari(id)
    except:
        # return cari_latihan
        return f"Gagal mencari latihan dengan id: {id}.", 400
    # Pastikan berhasil
    if cari_latihan is None:
        # return render_template('materi/tilawah/tema/edit_Tulisan2.html/', form=form, data=cari_materi)
        # return cari_materi
        return f"Gagal mencari latihan dengan id: {id}.", 400
    # Load template
    # parameter title dikirim untuk mengisi nilai variabel title di template
    return render_template('latihan/edit_latihan.html/', data=cari_latihan)


@latihan.route('/updatelatihan/<int:id>', methods=["POST"])
def ubah_latihan(id):
    Pertanyaan = request.form['pertanyaan']
    Pilihan1 = request.form['pilihan1']
    Pilihan2 = request.form['pilihan2']
    Pilihan3 = request.form['pilihan3']
    Pilihan4 = request.form['pilihan4']
    Jawaban = request.form['jawaban']

    hasil = {}

    hasil["pertanyaan"] = Pertanyaan
    hasil["pilihan1"] = Pilihan1
    hasil["pilihan2"] = Pilihan2
    hasil["pilihan3"] = Pilihan3
    hasil["pilihan4"] = Pilihan4
    hasil["jawaban"] = Jawaban

    if Jawaban == "pilihan1":
        hasil["jawaban"] = Pilihan1
    elif Jawaban == "pilihan2":
        hasil["jawaban"] = Pilihan2
    elif Jawaban == "pilihan3":
        hasil["jawaban"] = Pilihan3
    elif Jawaban == "pilihan4":
        hasil["jawaban"] = Pilihan4

    client = datastore.Client()
    key = client.key(latihan_KIND, id)
    entity = datastore.Entity(key=key)
    entity.update(hasil)

    client.put(entity)

    return redirect('/latihan')
