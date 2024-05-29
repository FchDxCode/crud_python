from extensions import db

class Spesialis(db.Model):
    __tablename__ = 'tb_spesialis'
    kd_spesialis = db.Column(db.String(3), primary_key=True)
    spesialis = db.Column(db.String(35))

class Dokter(db.Model):
    __tablename__ = 'tb_dokter'
    kd_dokter = db.Column(db.String(3), primary_key=True)
    nama_dokter = db.Column(db.String(35))
    kd_spesialis = db.Column(db.String(3), db.ForeignKey('tb_spesialis.kd_spesialis'))
    telepon = db.Column(db.String(15))
    sex = db.Column(db.String(1))

class Jaga(db.Model):
    __tablename__ = 'tb_jaga'
    kd_dokter = db.Column(db.String(3), db.ForeignKey('tb_dokter.kd_dokter'), primary_key=True)
    hari = db.Column(db.String(15), primary_key=True)
    jam_mulai = db.Column(db.Time)
    jam_selesai = db.Column(db.Time)

class Pasien(db.Model):
    __tablename__ = 'tb_pasien'
    kd_pasien = db.Column(db.String(3), primary_key=True)
    nama_pasien = db.Column(db.String(35))
    alamat_pasien = db.Column(db.String(255))
    umur_pasien = db.Column(db.Integer)
    sex = db.Column(db.String(1))
    telepon = db.Column(db.String(15))
    spesialis = db.Column(db.String(35))
    status = db.Column(db.String(10))
