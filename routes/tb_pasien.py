from flask import Blueprint, request, jsonify, render_template
from extensions import db
from models import Pasien

pasien_bp = Blueprint('pasien', __name__)

@pasien_bp.route('/pasien', methods=['GET'])
def get_pasien():
    all_pasien = Pasien.query.all()
    return render_template('pasien_pages.html', pasien=all_pasien)

@pasien_bp.route('/pasien', methods=['POST'])
def add_pasien():
    data = request.form
    new_pasien = Pasien(
        kd_pasien=data['kd_pasien'],
        nama_pasien=data['nama_pasien'],
        alamat_pasien=data['alamat_pasien'],
        umur_pasien=data['umur_pasien'],
        sex=data['jenis_kelamin'],
        telepon=data['telepon'],
        spesialis=data['spesialis']
    )
    db.session.add(new_pasien)
    db.session.commit()
    return jsonify({"message": "Pasien added successfully"})

@pasien_bp.route('/pasien/<kd_pasien>', methods=['PUT'])
def update_pasien(kd_pasien):
    data = request.form
    pasien = Pasien.query.filter_by(kd_pasien=kd_pasien).first()
    if pasien:
        pasien.nama_pasien = data['nama_pasien']
        pasien.alamat_pasien = data['alamat_pasien']
        pasien.umur_pasien = data['umur_pasien']
        pasien.sex = data['jenis_kelamin']
        pasien.telepon = data['telepon']
        pasien.spesialis = data['spesialis']
        db.session.commit()
        return jsonify({"message": "Pasien updated successfully"})
    return jsonify({"message": "Pasien not found"}), 404

@pasien_bp.route('/pasien/<kd_pasien>', methods=['DELETE'])
def delete_pasien(kd_pasien):
    pasien = Pasien.query.filter_by(kd_pasien=kd_pasien).first()
    if pasien:
        db.session.delete(pasien)
        db.session.commit()
        return jsonify({"message": "Pasien deleted successfully"})
    return jsonify({"message": "Pasien not found"}), 404
