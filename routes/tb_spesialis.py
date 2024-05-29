from flask import Blueprint, request, jsonify, render_template
from extensions import db
from models import Spesialis

spesialis_bp = Blueprint('spesialis', __name__)

@spesialis_bp.route('/spesialis', methods=['GET'])
def get_spesialis():
    all_spesialis = Spesialis.query.all()
    return render_template('spesialis_pages.html', spesialis=all_spesialis)

@spesialis_bp.route('/spesialis', methods=['POST'])
def add_spesialis():
    data = request.form
    new_spesialis = Spesialis(
        kd_spesialis = data['kd_spesialis'],
        spesialis = data['spesialis']
    )
    db.session.add(new_spesialis)
    db.session.commit()
    return jsonify({"message": "Spesialis added successfully"})

@spesialis_bp.route('/spesialis/<kd_spesialis>', methods=['PUT'])
def update_spesialis(kd_spesialis):
    data = request.form
    spesialis = Spesialis.query.filter_by(kd_spesialis=kd_spesialis).first()
    if spesialis:
        spesialis.spesialis = data['spesialis']
        db.session.commit()
        return jsonify({"message": "Spesialis updated successfully"})
    return jsonify({"message": "Spesialis not found"}), 404

@spesialis_bp.route('/spesialis/<kd_spesialis>', methods=['DELETE'])
def delete_spesialis(kd_spesialis):
    spesialis = Spesialis.query.filter_by(kd_spesialis=kd_spesialis).first()
    if spesialis:
        db.session.delete(spesialis)
        db.session.commit()
        return jsonify({"message": "Spesialis deleted successfully"})
    return jsonify({"message": "Spesialis not found"}), 404
