/*
SQLyog Community Edition- MySQL GUI v7.15 
MySQL - 5.5.29 : Database - disease projection ml
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`disease projection ml` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `disease projection ml`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `Username` varchar(10) DEFAULT NULL,
  `Password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admin` */

insert  into `admin`(`Username`,`Password`) values ('admin','admin');

/*Table structure for table `billdetails` */

DROP TABLE IF EXISTS `billdetails`;

CREATE TABLE `billdetails` (
  `Pid` varchar(100) DEFAULT NULL,
  `Prescription` varchar(100) DEFAULT NULL,
  `Suggestion` varchar(100) DEFAULT NULL,
  `amount` int(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `billdetails` */

insert  into `billdetails`(`Pid`,`Prescription`,`Suggestion`,`amount`,`status`) values ('245','drug reaction /care full','have good food',100,'paid');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `Did` int(100) NOT NULL,
  `Dname` varchar(100) DEFAULT NULL,
  `Dphone` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Did`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `doctor` */

insert  into `doctor`(`Did`,`Dname`,`Dphone`,`Email`,`Address`,`Password`) values (148,'Moulali','gdenral medicine','10am - 2pm','300','123');

/*Table structure for table `dpres` */

DROP TABLE IF EXISTS `dpres`;

CREATE TABLE `dpres` (
  `did` varchar(100) DEFAULT NULL,
  `doctor` varchar(100) DEFAULT NULL,
  `pid` varchar(100) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `pres` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dpres` */

insert  into `dpres`(`did`,`doctor`,`pid`,`pname`,`pres`) values ('148','Moulali','147','chotu','dolo-6'),('148','Moulali','147','chotu','dolo-6'),('148','Moulali','147','chotu','dolo-6');

/*Table structure for table `medicene` */

DROP TABLE IF EXISTS `medicene`;

CREATE TABLE `medicene` (
  `tname` varchar(100) DEFAULT NULL,
  `price` int(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `medicene` */

insert  into `medicene`(`tname`,`price`,`image`,`status`) values ('dolo',80,'dolo.jpg','pending');

/*Table structure for table `op` */

DROP TABLE IF EXISTS `op`;

CREATE TABLE `op` (
  `c` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `op` */

/*Table structure for table `patient` */

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `Pid` int(100) NOT NULL,
  `Pname` varchar(100) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Pid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `patient` */

insert  into `patient`(`Pid`,`Pname`,`Email`,`Phone`,`Address`,`Password`) values (123,'wajiha','qwe@gmail.com','7258963258','begumpet','123'),(147,'chotu','chotu@gmail.com','+918639966858','15-8-424','123'),(245,'alekhya','alekhya.1000projects@gmail.com','7258963258','hyderabad','123');

/*Table structure for table `patientsymptoms` */

DROP TABLE IF EXISTS `patientsymptoms`;

CREATE TABLE `patientsymptoms` (
  `Pid` int(100) DEFAULT NULL,
  `symptom1` varchar(100) DEFAULT NULL,
  `symptom2` varchar(100) DEFAULT NULL,
  `symptom3` varchar(100) DEFAULT NULL,
  `symptom4` varchar(100) DEFAULT NULL,
  `symptom5` varchar(100) DEFAULT NULL,
  `dt` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `patientsymptoms` */

insert  into `patientsymptoms`(`Pid`,`symptom1`,`symptom2`,`symptom3`,`symptom4`,`symptom5`,`dt`) values (147,'phlegm','throat_irritation','redness_of_eyes','chest_pain','runny_nose','28/02/2022 20:08:19');

/*Table structure for table `purchase` */

DROP TABLE IF EXISTS `purchase`;

CREATE TABLE `purchase` (
  `mname` varchar(100) DEFAULT NULL,
  `price` int(100) DEFAULT NULL,
  `f` int(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `id` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `cn` varchar(100) DEFAULT NULL,
  `cvv` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `purchase` */

insert  into `purchase`(`mname`,`price`,`f`,`name`,`id`,`phone`,`cn`,`cvv`) values ('dolo',80,160,'chotu','147','8639966858','147852369','149');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `fee` varchar(100) DEFAULT NULL,
  `dt` varchar(100) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `pname` varchar(100) DEFAULT NULL,
  `cn` varchar(100) DEFAULT NULL,
  `cvv` varchar(100) DEFAULT NULL,
  `tt` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`id`,`name`,`fee`,`dt`,`pid`,`pname`,`cn`,`cvv`,`tt`,`status`) values (148,'Moulali','300','2022-02-28',147,'chotu','741258963','158','11:00','accepted');

/*Table structure for table `transcationdetails` */

DROP TABLE IF EXISTS `transcationdetails`;

CREATE TABLE `transcationdetails` (
  `Pid` int(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `Tno` varchar(100) DEFAULT NULL,
  `Cvv` varchar(100) DEFAULT NULL,
  `dt` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `transcationdetails` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
