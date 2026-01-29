-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 22, 2026 at 05:09 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `raport_raditya`
--

-- --------------------------------------------------------

--
-- Table structure for table `raditya_absensi`
--

CREATE TABLE `raditya_absensi` (
  `ID_Absen_Raditya` int(10) NOT NULL,
  `Keterangan_Raditya` enum('Sakit','Izin','Alfa') NOT NULL,
  `Jumlah_Raditya` int(10) NOT NULL,
  `NIS_Raditya` int(10) DEFAULT NULL,
  `Semester_Raditya` int(1) DEFAULT NULL,
  `Tahun_Ajaran_Raditya` year(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `raditya_guru`
--

CREATE TABLE `raditya_guru` (
  `ID_Guru_Raditya` int(10) NOT NULL,
  `Nama_Guru_Raditya` varchar(50) NOT NULL,
  `ID_Mapel` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `raditya_guru`
--

INSERT INTO `raditya_guru` (`ID_Guru_Raditya`, `Nama_Guru_Raditya`, `ID_Mapel`) VALUES
(1, 'Harry Potter', 10),
(2, 'Hermione Granger', 7),
(3, 'Ronald Wèasley', 1),
(4, 'Mikasa Ackerman', 3);

-- --------------------------------------------------------

--
-- Table structure for table `raditya_kelas`
--

CREATE TABLE `raditya_kelas` (
  `ID_Kelas_Raditya` int(10) NOT NULL,
  `Jurusan_Raditya` enum('Mekatronika','Teknik Permesinan','Teknik Kimia Industri','Pengembangan Perangkat Lunak dan Gim','Desain Komunikasi Visual','Animasi') NOT NULL,
  `Tingkat_Raditya` enum('X','XI','XII') NOT NULL,
  `ID_Guru_Raditya` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `raditya_kelas`
--

INSERT INTO `raditya_kelas` (`ID_Kelas_Raditya`, `Jurusan_Raditya`, `Tingkat_Raditya`, `ID_Guru_Raditya`) VALUES
(1, 'Mekatronika', 'X', 1),
(2, 'Pengembangan Perangkat Lunak dan Gim', 'XI', 2),
(3, 'Desain Komunikasi Visual', 'X', 3),
(4, 'Animasi', 'XI', 4);

-- --------------------------------------------------------

--
-- Table structure for table `raditya_mapel`
--

CREATE TABLE `raditya_mapel` (
  `ID_Mapel_Raditya` int(10) NOT NULL,
  `Nama_Mapel_Raditya` varchar(50) NOT NULL,
  `KKM_Raditya` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `raditya_mapel`
--

INSERT INTO `raditya_mapel` (`ID_Mapel_Raditya`, `Nama_Mapel_Raditya`, `KKM_Raditya`) VALUES
(1, 'English ', 80),
(2, 'Japanese', 80),
(3, 'Francè', 85),
(4, 'Mathematics', 78),
(5, 'Biology', 85),
(6, 'Physic', 85),
(7, 'Chemistery', 85),
(8, 'Music', 80),
(9, 'Art', 80),
(10, 'History', 80),
(11, 'Sport', 80);

-- --------------------------------------------------------

--
-- Table structure for table `raditya_nilai`
--

CREATE TABLE `raditya_nilai` (
  `ID_Nilai_Raditya` int(10) NOT NULL,
  `NIS_Raditya` int(10) NOT NULL,
  `ID_Mapel_Raditya` int(10) NOT NULL,
  `Nilai_Tugas_Raditya` int(10) NOT NULL,
  `Nilai_UTS_Raditya` int(10) NOT NULL,
  `Nilai_UAS_Raditya` int(10) NOT NULL,
  `Nilai_Akhir_Raditya` int(3) NOT NULL,
  `Deskripsi_Raditya` text NOT NULL,
  `Semester_Raditya` int(10) NOT NULL,
  `Tahun_Ajaran_Raditya` year(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `raditya_nilai`
--

INSERT INTO `raditya_nilai` (`ID_Nilai_Raditya`, `NIS_Raditya`, `ID_Mapel_Raditya`, `Nilai_Tugas_Raditya`, `Nilai_UTS_Raditya`, `Nilai_UAS_Raditya`, `Nilai_Akhir_Raditya`, `Deskripsi_Raditya`, `Semester_Raditya`, `Tahun_Ajaran_Raditya`) VALUES
(4, 10243309, 6, 100, 100, 100, 100, '', 1, '2026'),
(6, 10243309, 5, 100, 100, 100, 100, '', 1, '2026'),
(7, 10243309, 7, 100, 100, 100, 100, '', 1, '2026'),
(8, 10243309, 1, 100, 100, 100, 100, '', 1, '2026'),
(9, 10243309, 3, 100, 100, 100, 100, '', 1, '2026'),
(10, 10243309, 10, 100, 100, 100, 100, '', 1, '2026'),
(11, 10243309, 2, 100, 100, 100, 100, '', 1, '2026'),
(12, 10243309, 4, 100, 100, 100, 100, '', 1, '2026'),
(13, 10243309, 8, 100, 100, 100, 100, '', 1, '2026'),
(14, 10243309, 11, 100, 100, 100, 100, '', 1, '2026'),
(15, 10243309, 9, 100, 100, 100, 100, '', 1, '2026'),
(16, 10243312, 9, 100, 100, 100, 100, '', 1, '2026'),
(17, 10243312, 5, 100, 100, 100, 100, '', 1, '2026'),
(18, 10243312, 7, 100, 100, 100, 100, '', 1, '2026'),
(19, 10243312, 1, 100, 100, 100, 100, '', 1, '2026'),
(20, 10243312, 3, 100, 100, 100, 100, '', 1, '2026'),
(21, 10243312, 10, 100, 100, 100, 100, '', 1, '2026'),
(22, 10243312, 2, 100, 100, 100, 100, '', 1, '2026'),
(23, 10243312, 4, 100, 100, 100, 100, '', 1, '2026'),
(24, 10243312, 8, 100, 100, 100, 100, '', 1, '2026'),
(25, 10243312, 6, 100, 100, 100, 100, '', 1, '2026'),
(26, 10243312, 11, 100, 100, 100, 100, '', 1, '2026'),
(27, 10243310, 9, 100, 100, 100, 100, '', 1, '2026'),
(28, 10243310, 5, 100, 100, 100, 100, '', 1, '2026'),
(29, 10243310, 7, 100, 100, 100, 100, '', 1, '2026'),
(30, 10243310, 1, 100, 100, 100, 100, '', 1, '2026'),
(31, 10243310, 10, 100, 100, 100, 100, '', 1, '2026'),
(32, 10243310, 3, 100, 100, 100, 100, '', 1, '2026'),
(33, 10243310, 2, 100, 100, 100, 100, '', 1, '2026'),
(34, 10243310, 4, 100, 100, 100, 100, '', 1, '2026'),
(35, 10243310, 8, 100, 100, 100, 100, '', 1, '2026'),
(36, 10243310, 6, 100, 100, 100, 100, '', 1, '2026'),
(37, 10243310, 11, 100, 100, 100, 100, '', 1, '2026'),
(38, 10243313, 9, 100, 100, 100, 100, '', 1, '2026'),
(39, 10243313, 5, 100, 100, 100, 100, '', 1, '2026'),
(40, 10243313, 7, 100, 100, 100, 100, '', 1, '2026'),
(41, 10243313, 1, 100, 100, 100, 100, '', 1, '2026'),
(42, 10243313, 3, 100, 100, 100, 100, '', 1, '2026'),
(43, 10243313, 10, 100, 100, 100, 100, '', 1, '2026'),
(44, 10243313, 2, 100, 100, 100, 100, '', 1, '2026'),
(45, 10243313, 4, 100, 100, 100, 100, '', 1, '2026'),
(46, 10243313, 8, 100, 100, 100, 100, '', 1, '2026'),
(47, 10243313, 6, 100, 100, 100, 100, '', 1, '2026'),
(49, 10243313, 11, 100, 100, 100, 100, '', 1, '2026'),
(50, 10243311, 9, 100, 100, 100, 100, '', 1, '2026'),
(51, 10243311, 5, 100, 100, 100, 100, '', 1, '2026'),
(52, 10243311, 7, 100, 100, 100, 100, '', 1, '2026'),
(53, 10243311, 1, 100, 100, 100, 100, '', 1, '2026'),
(54, 10243311, 3, 100, 100, 100, 100, '', 1, '2026'),
(55, 10243311, 10, 100, 100, 100, 100, '', 1, '2026'),
(56, 10243311, 2, 100, 100, 100, 100, '', 1, '2026'),
(57, 10243311, 4, 100, 100, 100, 100, '', 1, '2026'),
(58, 10243311, 8, 100, 100, 100, 100, '', 1, '2026'),
(59, 10243311, 6, 100, 100, 100, 100, '', 1, '2026'),
(60, 10243311, 11, 100, 100, 100, 100, '', 1, '2026');

-- --------------------------------------------------------

--
-- Table structure for table `raditya_siswa`
--

CREATE TABLE `raditya_siswa` (
  `NIS_Raditya` int(10) NOT NULL,
  `Nama_Raditya` varchar(50) NOT NULL,
  `Jenis_Kelamin_Raditya` enum('Laki-Laki','Perempuan') NOT NULL,
  `Tempat_Lahir_Raditya` varchar(50) NOT NULL,
  `Tanggal_Lahir_Raditya` date NOT NULL,
  `Alamat_Raditya` text NOT NULL,
  `ID_Kelas` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `raditya_siswa`
--

INSERT INTO `raditya_siswa` (`NIS_Raditya`, `Nama_Raditya`, `Jenis_Kelamin_Raditya`, `Tempat_Lahir_Raditya`, `Tanggal_Lahir_Raditya`, `Alamat_Raditya`, `ID_Kelas`) VALUES
(10243309, 'Harry Granger', 'Laki-Laki', 'London ', '2008-12-07', 'West London', 1),
(10243310, 'Eren Yeager', 'Laki-Laki', 'Shiganshina District', '2008-07-02', 'Shiganshina City', 4),
(10243311, 'Mikasa Ackerman', 'Laki-Laki', 'Shiganshina District', '2008-02-15', 'Shiganshina City', 4),
(10243312, 'Armin Arlert', 'Laki-Laki', 'Shiganshina District', '2008-05-26', 'Shiganshina City', 3),
(10243313, 'Jean Kirstein', 'Laki-Laki', 'Orvud District', '2009-01-25', 'Orvud City', 2),
(10243314, 'Hermione Granger', 'Perempuan', 'Francè', '2008-11-12', 'Paris', 2);

-- --------------------------------------------------------

--
-- Table structure for table `raditya_user`
--

CREATE TABLE `raditya_user` (
  `ID_Raditya` int(10) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Role` enum('Admin','Guru','Walikelas') NOT NULL,
  `ID_Guru_Raditya` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `raditya_user`
--

INSERT INTO `raditya_user` (`ID_Raditya`, `Username`, `Password`, `Role`, `ID_Guru_Raditya`) VALUES
(1, 'Raditya', 'Raditya123', 'Admin', NULL),
(2, 'Harry', 'Harry123', 'Walikelas', NULL),
(3, 'Mikasa', 'Mikasa123', 'Guru', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `raditya_absensi`
--
ALTER TABLE `raditya_absensi`
  ADD PRIMARY KEY (`ID_Absen_Raditya`),
  ADD KEY `fk_absen_siswa` (`NIS_Raditya`);

--
-- Indexes for table `raditya_guru`
--
ALTER TABLE `raditya_guru`
  ADD PRIMARY KEY (`ID_Guru_Raditya`),
  ADD KEY `ID_Mapel` (`ID_Mapel`);

--
-- Indexes for table `raditya_kelas`
--
ALTER TABLE `raditya_kelas`
  ADD PRIMARY KEY (`ID_Kelas_Raditya`),
  ADD KEY `ID_Guru_Raditya` (`ID_Guru_Raditya`);

--
-- Indexes for table `raditya_mapel`
--
ALTER TABLE `raditya_mapel`
  ADD PRIMARY KEY (`ID_Mapel_Raditya`);

--
-- Indexes for table `raditya_nilai`
--
ALTER TABLE `raditya_nilai`
  ADD PRIMARY KEY (`ID_Nilai_Raditya`),
  ADD UNIQUE KEY `uniq_nilai` (`NIS_Raditya`,`ID_Mapel_Raditya`,`Semester_Raditya`,`Tahun_Ajaran_Raditya`),
  ADD KEY `NIS_Raditya` (`NIS_Raditya`),
  ADD KEY `ID_Mapel_Raditya` (`ID_Mapel_Raditya`);

--
-- Indexes for table `raditya_siswa`
--
ALTER TABLE `raditya_siswa`
  ADD PRIMARY KEY (`NIS_Raditya`),
  ADD KEY `ID_Kelas` (`ID_Kelas`);

--
-- Indexes for table `raditya_user`
--
ALTER TABLE `raditya_user`
  ADD PRIMARY KEY (`ID_Raditya`),
  ADD KEY `fk_user_guru` (`ID_Guru_Raditya`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `raditya_absensi`
--
ALTER TABLE `raditya_absensi`
  ADD CONSTRAINT `fk_absen_siswa` FOREIGN KEY (`NIS_Raditya`) REFERENCES `raditya_siswa` (`NIS_Raditya`) ON DELETE CASCADE;

--
-- Constraints for table `raditya_guru`
--
ALTER TABLE `raditya_guru`
  ADD CONSTRAINT `fk_guru_mapel` FOREIGN KEY (`ID_Mapel`) REFERENCES `raditya_mapel` (`ID_Mapel_Raditya`) ON UPDATE CASCADE;

--
-- Constraints for table `raditya_kelas`
--
ALTER TABLE `raditya_kelas`
  ADD CONSTRAINT `fk_kelas_guru` FOREIGN KEY (`ID_Guru_Raditya`) REFERENCES `raditya_guru` (`ID_Guru_Raditya`) ON UPDATE CASCADE;

--
-- Constraints for table `raditya_nilai`
--
ALTER TABLE `raditya_nilai`
  ADD CONSTRAINT `fk_nilai_mapel` FOREIGN KEY (`ID_Mapel_Raditya`) REFERENCES `raditya_mapel` (`ID_Mapel_Raditya`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_nilai_siswa` FOREIGN KEY (`NIS_Raditya`) REFERENCES `raditya_siswa` (`NIS_Raditya`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `raditya_siswa`
--
ALTER TABLE `raditya_siswa`
  ADD CONSTRAINT `fk_siswa_kelas` FOREIGN KEY (`ID_Kelas`) REFERENCES `raditya_kelas` (`ID_Kelas_Raditya`) ON UPDATE CASCADE;

--
-- Constraints for table `raditya_user`
--
ALTER TABLE `raditya_user`
  ADD CONSTRAINT `fk_user_guru` FOREIGN KEY (`ID_Guru_Raditya`) REFERENCES `raditya_guru` (`ID_Guru_Raditya`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
