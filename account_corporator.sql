-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 19, 2023 at 01:14 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pothole`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_corporator`
--

-- CREATE TABLE `account_corporator` (
--   `ward_no` int(11) NOT NULL,
--   `name` varchar(50) NOT NULL
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account_corporator`
--

INSERT INTO `account_corporator` (`ward_no`, `name`) VALUES
(1, 'Ramesh'),
(2, 'Mahesh'),
(3, 'Rakesh'),
(4, 'Suresh'),
(5, 'Nagesh'),
(6, 'Rajesh'),
(7, 'Gowrish'),
(8, 'Ranganath'),
(9, 'Krishna'),
(10, 'Prakash');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_corporator`
--
-- ALTER TABLE `account_corporator`
--   ADD PRIMARY KEY (`ward_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
