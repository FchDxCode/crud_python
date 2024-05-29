from flask import Blueprint, request, jsonify, render_template
from extensions import db
from models import Dokter

dokter_bp = Blueprint('dokter', __name__)

@dokter_bp.route('/dokter', methods=['GET'])
def get_dokter():
    all_dokter = Dokter.query.all()
    return render_template('dokter_pages.html', dokter=all_dokter)

@dokter_bp.route('/dokter', methods=['POST'])
def add_dokter():
    data = request.form
    new_dokter = Dokter(
        kd_dokter = data['kd_dokter'],
        nama_dokter = data['nama_dokter'],
        kd_spesialis = data['kd_spesialis'],
        telepon = data['telepon'],
        sex = data['sex']
    )
    db.session.add(new_dokter)
    db.session.commit()
    return jsonify({"message": "Dokter added successfully"})

@dokter_bp.route('/dokter/<kd_dokter>', methods=['PUT'])
def update_dokter(kd_dokter):
    data = request.form
    dokter = Dokter.query.filter_by(kd_dokter=kd_dokter).first()
    if dokter:
        dokter.nama_dokter = data['nama_dokter']
        dokter.kd_spesialis = data['kd_spesialis']
        dokter.telepon = data['telepon']
        dokter.sex = data['sex']
        db.session.commit()
        return jsonify({"message": "Dokter updated successfully"})
    return jsonify({"message": "Dokter not found"}), 404

@dokter_bp.route('/dokter/<kd_dokter>', methods=['DELETE'])
def delete_dokter(kd_dokter):
    dokter = Dokter.query.filter_by(kd_dokter=kd_dokter).first()
    if dokter:
        db.session.delete(dokter)
        db.session.commit()
        return jsonify({"message": "Dokter deleted successfully"})
    return jsonify({"message": "Dokter not found"}), 404
