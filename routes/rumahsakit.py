from flask import Blueprint, render_template
from models import Spesialis, Dokter, Pasien

hospital_bp = Blueprint('rumahsakit', __name__)

@hospital_bp.route('/rumahsakit', methods=['GET'])
def get_rumahsakit():

    total_patients = Pasien.query.count()
    total_doctors = Dokter.query.count()
    total_specialists = Spesialis.query.count()
    total_sick_patients = Pasien.query.filter_by(status='sick').count()
    total_recovered_patients = Pasien.query.filter_by(status='recovered').count()

    data = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_specialists': total_specialists,
        'total_sick_patients': total_sick_patients,
        'total_recovered_patients': total_recovered_patients
    }

    return render_template('dashboard.html', data=data)
