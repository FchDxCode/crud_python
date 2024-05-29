from flask import Blueprint, request, jsonify, render_template
from extensions import db
from models import Jaga

jaga_bp = Blueprint('jaga', __name__)

@jaga_bp.route('/jaga', methods=['GET'])
def get_jaga():
    all_jaga = Jaga.query.all()
    return render_template('jaga_pages.html', jaga=all_jaga)

@jaga_bp.route('/jaga', methods=['POST'])
def add_jaga():
    data = request.form
    new_jaga = Jaga(
        kd_dokter = data['kd_dokter'],
        hari = data['hari'],
        jam_mulai = data['jam_mulai'],
        jam_selesai = data['jam_selesai']
    )
    db.session.add(new_jaga)
    db.session.commit()
    return jsonify({"message": "Jaga added successfully"})

@jaga_bp.route('/jaga/<kd_dokter>/<hari>', methods=['PUT'])
def update_jaga(kd_dokter, hari):
    data = request.form
    jaga = Jaga.query.filter_by(kd_dokter=kd_dokter, hari=hari).first()
    if jaga:
        jaga.jam_mulai = data['jam_mulai']
        jaga.jam_selesai = data['jam_selesai']
        db.session.commit()
        return jsonify({"message": "Jaga updated successfully"})
    return jsonify({"message": "Jaga not found"}), 404

@jaga_bp.route('/jaga/<kd_dokter>/<hari>', methods=['DELETE'])
def delete_jaga(kd_dokter, hari):
    jaga = Jaga.query.filter_by(kd_dokter=kd_dokter, hari=hari).first()
    if jaga:
        db.session.delete(jaga)
        db.session.commit()
        return jsonify({"message": "Jaga deleted successfully"})
    return jsonify({"message": "Jaga not found"}), 404
