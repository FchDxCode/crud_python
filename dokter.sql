-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Waktu pembuatan: 29 Bulan Mei 2024 pada 01.02
-- Versi server: 8.0.30
-- Versi PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dokter`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_dokter`
--

CREATE TABLE `tb_dokter` (
  `kd_dokter` char(3) NOT NULL,
  `nama_dokter` varchar(35) NOT NULL,
  `kd_spesialis` char(3) NOT NULL,
  `telepon` varchar(15) NOT NULL,
  `sex` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `tb_dokter`
--

INSERT INTO `tb_dokter` (`kd_dokter`, `nama_dokter`, `kd_spesialis`, `telepon`, `sex`) VALUES
('D01', 'Dr. Boi Trimayo', 'UMM', '08111111111', 'P'),
('D04', 'Dr. umar', 'JTG', '08444444444', 'P'),
('D05', 'Dr. Ibrahim', 'KDG', '08555555555', 'P'),
('D06', 'Dr. aji', 'SRF', '08666666666', 'P'),
('D07', 'Dr. ridwan', 'MAT', '08777777777', 'P'),
('D08', 'Dr. fajar', 'ANK', '08888888888', 'P'),
('D09', 'Dr. mory', 'UMM', '08999999999', 'P'),
('D10', 'Dr. serly', 'BDH', '08000000000', 'W'),
('D12', 'Dr. bayhaqi', 'BDH', '08202020202', 'P'),
('D13', 'Dr.rina', 'ANK', '08303030303', 'W'),
('D14', 'Dr.agus', 'UMM', '0840404040404', 'P'),
('D15', 'Dr. andin', 'KDG', '0850505050505', 'W'),
('D16', 'Dr. labala', 'BDH', '0860606060606', 'P'),
('D17', 'Dr. fauzi', 'BDH', '0870707070707', 'P'),
('D18', 'Dr.Raihan alif', 'BDH', '0894247284783', 'L');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_jaga`
--

CREATE TABLE `tb_jaga` (
  `kd_dokter` char(3) NOT NULL,
  `hari` varchar(15) NOT NULL,
  `jam_mulai` time NOT NULL,
  `jam_selesai` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `tb_jaga`
--

INSERT INTO `tb_jaga` (`kd_dokter`, `hari`, `jam_mulai`, `jam_selesai`) VALUES
('99D', '2024-05-16', '23:26:00', '20:29:00'),
('SSD', '2024-05-02', '07:15:00', '07:17:00');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_pasien`
--

CREATE TABLE `tb_pasien` (
  `kd_pasien` int NOT NULL,
  `nama_pasien` varchar(255) NOT NULL,
  `alamat_pasien` varchar(255) NOT NULL,
  `umur_pasien` int NOT NULL,
  `sex` char(1) NOT NULL,
  `telepon` int NOT NULL,
  `spesialis` varchar(255) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `tb_pasien`
--

INSERT INTO `tb_pasien` (`kd_pasien`, `nama_pasien`, `alamat_pasien`, `umur_pasien`, `sex`, `telepon`, `spesialis`, `status`) VALUES
(1, 'deks', 'indo', 11, 'P', 2131, 'dalam', ''),
(2, 'Jane Smith', 'Jl. Percobaan No. 456', 25, 'F', 85678901, 'Gigi', '');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_spesialis`
--

CREATE TABLE `tb_spesialis` (
  `kd_spesialis` char(3) NOT NULL,
  `spesialis` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `tb_spesialis`
--

INSERT INTO `tb_spesialis` (`kd_spesialis`, `spesialis`) VALUES
('ANK', 'Anak'),
('BDH', 'Bedah1'),
('DLM', 'Penyakit Dalam'),
('GIG', 'Gigi'),
('JTG', 'Jantung'),
('KDG', 'Kandung'),
('KLT', 'Kulit'),
('MAT', 'Mata'),
('SRF', 'Saraf'),
('UMM', 'Dokter Umum');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tb_dokter`
--
ALTER TABLE `tb_dokter`
  ADD PRIMARY KEY (`kd_dokter`);

--
-- Indeks untuk tabel `tb_jaga`
--
ALTER TABLE `tb_jaga`
  ADD PRIMARY KEY (`kd_dokter`);

--
-- Indeks untuk tabel `tb_pasien`
--
ALTER TABLE `tb_pasien`
  ADD PRIMARY KEY (`kd_pasien`);

--
-- Indeks untuk tabel `tb_spesialis`
--
ALTER TABLE `tb_spesialis`
  ADD PRIMARY KEY (`kd_spesialis`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
