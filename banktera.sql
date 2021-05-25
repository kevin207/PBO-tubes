-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 25, 2021 at 01:10 PM
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
('ACCA1007', 'CS101199', 'Checking', -100000),
('ACLA1762', 'CS101199', 'Loan', 66000),
('ACSA1866', 'CS101199', 'Saving', 110000);

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
('ACCA1007', '2021-05-25 17:57:46', 'Deposit', 100000),
('ACCA1007', '2021-05-25 17:58:11', 'Withdraw', 200000),
('ACSA1866', '2021-05-25 17:59:05', 'Deposit', 1000000),
('ACSA1866', '2021-05-25 17:59:18', 'Withdraw', 500000),
('ACSA1866', '2021-05-25 17:59:30', 'Withdraw', 500000),
('ACLA1762', '2021-05-25 18:00:13', 'Make Loan', 100000),
('ACLA1762', '2021-05-25 18:00:20', 'Loan Pay Off', 50000),
('ACSA1866', '2021-05-25 18:00:39', 'Deposit', 100000),
('ACLA1762', '2021-05-25 18:01:05', 'Interest', 5000),
('ACSA1866', '2021-05-25 18:01:05', 'Interest', 10000),
('ACLA1762', '2021-05-25 18:01:05', 'Loan Penalty', 11000);

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
('CS101199', 'Ihza Fajrur RH', 'Jakarta', '081292834124', 'ihzafrh@gmail.com'),
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
