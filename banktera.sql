-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2021 at 11:25 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `banktera`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `Account_ID` varchar(50) NOT NULL,
  `Customer_ID` varchar(50) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Balance` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`Account_ID`, `Customer_ID`, `Type`, `Balance`) VALUES
('ACCA1127', 'CS101567', 'Checking', 100000),
('ACCA1183', 'CS101199', 'Checking', -8100000),
('ACLA1365', 'CS101199', 'Loan', 73205),
('ACLA1401', 'CS101199', 'Loan', 0),
('ACSA1200', 'CS101199', 'Saving', 732050);

-- --------------------------------------------------------

--
-- Table structure for table `account_transactions`
--

CREATE TABLE `account_transactions` (
  `Account_ID` varchar(50) NOT NULL,
  `Date_Time` datetime NOT NULL,
  `Transaction_Type` varchar(50) NOT NULL,
  `Amount` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `account_transactions`
--

INSERT INTO `account_transactions` (`Account_ID`, `Date_Time`, `Transaction_Type`, `Amount`) VALUES
('ACCA1183', '2021-05-23 15:45:42', 'Deposit', 1000000),
('ACCA1183', '2021-05-23 15:45:52', 'Withdraw', 100000),
('ACCA1183', '2021-05-23 15:46:14', 'Withdraw', 9000000),
('ACSA1200', '2021-05-23 16:01:57', 'Deposit', 1000000),
('ACSA1200', '2021-05-23 16:02:36', 'Withdraw', 500000),
('ACCA1127', '2021-05-23 17:12:45', 'Deposit', 100000),
('ACLA1401', '2021-05-23 18:15:57', 'Deposit', 100000),
('ACLA1365', '2021-05-23 18:26:32', 'Interest', 0),
('ACLA1401', '2021-05-23 18:26:32', 'Interest', 0),
('ACLA1365', '2021-05-23 18:30:32', 'Interest', 5000),
('ACLA1401', '2021-05-23 18:30:32', 'Interest', 10000),
('ACSA1200', '2021-05-23 18:44:11', 'Interest', 50000),
('ACLA1401', '2021-05-23 19:07:19', 'Loan Pay Off', 110000),
('ACLA1401', '2021-05-23 19:07:41', 'Make Loan', 1000000),
('ACLA1401', '2021-05-23 19:09:41', 'Make Loan', 10000),
('ACLA1401', '2021-05-23 19:09:46', 'Loan Pay Off', 10000),
('ACLA1401', '2021-05-23 19:13:19', 'Make Loan', 1100000),
('ACLA1401', '2021-05-23 19:13:23', 'Loan Pay Off', 200000),
('ACLA1401', '2021-05-23 19:14:22', 'Loan Pay Off', 1900000),
('ACLA1365', '2021-05-25 16:13:56', 'Interest', 5500),
('ACLA1401', '2021-05-25 16:13:56', 'Interest', 0),
('ACSA1200', '2021-05-25 16:13:56', 'Interest', 55000),
('ACLA1365', '2021-05-25 16:14:04', 'Interest', 6050),
('ACLA1401', '2021-05-25 16:14:04', 'Interest', 0),
('ACSA1200', '2021-05-25 16:14:04', 'Interest', 60500),
('ACLA1365', '2021-05-25 16:21:02', 'Interest', 6655),
('ACLA1401', '2021-05-25 16:21:02', 'Interest', 0),
('ACSA1200', '2021-05-25 16:21:02', 'Interest', 66550);

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Admin_ID` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Admin_ID`, `Password`) VALUES
('ADMIN01', '0');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `Customer_ID` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Phone` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`Customer_ID`, `Name`, `Address`, `Phone`, `Email`) VALUES
('CS101199', 'Bambang', 'Jakarta', '0812', 'Gmail'),
('CS101567', 'Budi', 'Depok', '0819', 'Gmail');

-- --------------------------------------------------------

--
-- Table structure for table `interest_refresh`
--

CREATE TABLE `interest_refresh` (
  `Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `interest_refresh`
--

INSERT INTO `interest_refresh` (`Date`) VALUES
('2021-05-25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`Account_ID`),
  ADD KEY `Customer ID` (`Customer_ID`);

--
-- Indexes for table `account_transactions`
--
ALTER TABLE `account_transactions`
  ADD KEY `Account ID` (`Account_ID`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Admin_ID`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`Customer_ID`);

--
-- Indexes for table `interest_refresh`
--
ALTER TABLE `interest_refresh`
  ADD PRIMARY KEY (`Date`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `Customer ID` FOREIGN KEY (`Customer_ID`) REFERENCES `customers` (`Customer_ID`) ON UPDATE CASCADE;

--
-- Constraints for table `account_transactions`
--
ALTER TABLE `account_transactions`
  ADD CONSTRAINT `Account ID` FOREIGN KEY (`Account_ID`) REFERENCES `accounts` (`Account_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
