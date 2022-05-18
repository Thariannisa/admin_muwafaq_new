from flask import Blueprint, jsonify, request, escape, make_response, url_for, render_template
# from .token import generate_confirmation_token, confirm_token
# from aplikasi.views.auth.email import send_email
import json
import jwt
# from ..componentRespon.responTemplate import templateRespon
from werkzeug.security import generate_password_hash, check_password_hash
from api.model import users2 as us
import datetime


users2 = Blueprint("users2", __name__, url_prefix="/api/users2")


@users2.route('/login', methods=['POST', 'GET'])
def login():
    # Pastikan parameter dalam JSON
    if request.is_json:
        # Ambil parameter
        permintaan_baru = request.get_json()
    # elif request.form:
    #     permintaan_baru = request.form
    else:
        return jsonify({"success": False,
                        "result": {},
                        "message": "Parameter salah",
                        "code": 415}), 415

    if permintaan_baru is None:
        return jsonify({
            "success": False,
            "result": {},
            "message": "Parameter salah",
            "code": 400
        }), 400
    if "email" not in permintaan_baru.keys() or "password" not in permintaan_baru.keys():
        return jsonify({
            "success": False,
            "result": {},
            "message": "Parameter salah",
            "code": 400
        }), 400

    email = escape(permintaan_baru["email"].strip())
    hasil = us.login(email, permintaan_baru["password"])

    if hasil:

        if isinstance(hasil, (str)):
            # return jsonify(False, {}, 400, hasil), 400
            return jsonify({"success": False, "result": {}, "message": hasil, "code": 400}), 400
        suksesLogin = check_password_hash(
            hasil.password, permintaan_baru["password"])
        if suksesLogin:
            token = jwt.encode(
                {
                    "id": hasil.id,
                    "nama": hasil.nama,
                    "email": hasil.email,
                    # "kontak": hasil.kontak,
                    "image": hasil.image,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                },
                "thisisthesecretkey",
                algorithm="HS256",
            )
            hasilJson = json.loads(json.dumps(hasil.__dict__))
            hasilJson["token"] = token
            return jsonify({
                "success": True,
                "result": hasilJson,
                "message": "sukses login!",
                "code": 200
            })
    return jsonify({
        "success": False,
        "result": {},
        "message": "email atau password salah!",
        "code": 400
    }), 400


@users2.route('/register', methods=['POST', 'GET'])
def register():
    # Pastikan parameter dalam JSON
    if request.is_json:
        # Ambil parameter
        parameter_baru = request.get_json()
    else:
        return jsonify(
            {
                "success": False,
                "result": {},
                "message": "Parameter salah",
                "code": 415
            }
        ), 415
    parameters = ["nama", "email", "password", "kontak", ]
    if parameter_baru is None:
        return jsonify({
            "success": False,
            "result": {},
            "message": "Parameter salah",
            "code": 400
        }), 400
    for parameter in parameters:
        if parameter not in parameter_baru.keys():
            return jsonify({"success": False,
                            "result": {},
                            "message": "Parameter salah",
                            "code": 400
                            }), 400
    if len(parameter_baru["password"]) < 7:
        return jsonify({
            "success": False,
            "result": {},
            "message": "Password harus lebih dari 6 karakter",
            "code": 400
        }), 400
        # False, {}, 400, "Password harus lebih dari 6 karakter"), 400,)
    # if not isinstance(request.json["kontak"], (int)):
    #     return (jsonify(False, {}, 400, "kontak"), 400, )
    # if us.checkEmailExists(request.json["email"]):
    #     return jsonify(False, {}, 400, "Email sudah ada!"), 400
    # dafault untuk user

    image = "https://adipurwa.desa.id/wp-content/uploads/2018/12/default-staff-1.png"

    if parameter_baru is None:
        return jsonify(False, {}, 400, "Parameter salah"), 400

    # id = parameter_baru["id"]
    nama = escape(parameter_baru["nama"].strip())
    email = request.json["email"]
    kontak = request.json["kontak"]
    password = generate_password_hash(
        request.json["password"], method="sha256")

    hasil = us.register(nama, email, image, kontak, password,)

    if hasil is None:
        return jsonify(False, {}, 400, "Gagal menambah data!"), 400
    if isinstance(hasil, (str)):
        return jsonify(True, {}, 400, hasil), 400
    # return jsonify(True, {}, 200, "sukses mendaftar"), 400
    return jsonify({
        "success": True,
        "result": {},
        "message": "sukses mendaftar",
        "code": 200}
    ), 400

# # krm email kalau berhasil simpan ke db
#     token = generate_confirmation_token(email),
#     confirm_url = url_for('confirm_email', token=token, _external=True)
#     template = render_template(
#         'email/emailKonfirmasi.html', linkKonfirmasi=confirm_url)
#     send_email(email, "muwafaq : Konfirmasi email anda", template)

#     return (jsonify(True, {}, 400, "Sukses Mendaftar"), 400,)


@users2.route('/daftar/<int:id>', methods=["GET"])
def getId(id):
    daftara = us.getId(id)

    if daftara != None:
        return json.loads(json.dumps(daftara.__dict__)), 200
    else:
        return {"error": "not found data"}, 200


@ users2.route('/update/<int:id>', methods=["PUT"])
def update(id):

    permintaan_baru = request.get_json()
    nama = escape(permintaan_baru["nama"].strip())
    data = us.update(
        id,
        nama,
        request.json['email'],
        request.json['image'],
        request.json['kontak'],
        request.json['password'])

    return data, 200


@ users2.route('/delete/<int:id>', methods=["DELETE"])
def delete(id):

    data = us.delete(id)

    return data, 200
