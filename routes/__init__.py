from flask import Blueprint

from .tb_spesialis import spesialis_bp
from .tb_dokter import dokter_bp
from .tb_jaga import jaga_bp
from .tb_pasien import pasien_bp
from .rumahsakit import hospital_bp

def register_blueprints(app):
    app.register_blueprint(spesialis_bp)
    app.register_blueprint(dokter_bp)
    app.register_blueprint(jaga_bp)
    app.register_blueprint(pasien_bp)
    app.register_blueprint(hospital_bp)
