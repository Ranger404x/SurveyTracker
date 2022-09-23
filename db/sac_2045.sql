-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 06, 2022 at 06:26 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sac_2045`
--

-- --------------------------------------------------------

--
-- Table structure for table `dat0-3`
--

CREATE TABLE `dat0-3` (
  `namedb` varchar(225) NOT NULL,
  `dobdb` varchar(225) NOT NULL,
  `fnamedb` varchar(225) NOT NULL,
  `mnamedb` varchar(225) NOT NULL,
  `condb` varchar(225) NOT NULL,
  `agedb` varchar(225) NOT NULL,
  `gendb` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='0-3 Age Child Group Data';

-- --------------------------------------------------------

--
-- Table structure for table `dat3-6a`
--

CREATE TABLE `dat3-6a` (
  `namedb` varchar(225) NOT NULL,
  `dobdb` varchar(225) NOT NULL,
  `fnamedb` varchar(225) NOT NULL,
  `mnamedb` varchar(225) NOT NULL,
  `condb` varchar(225) NOT NULL,
  `agedb` varchar(225) NOT NULL,
  `gendb` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='3-6 Age Child Group Data';
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
