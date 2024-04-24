-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`polarity` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE polarity

/*Table structure for table `userdetails` */

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `address` (
  `email` varchar(15) DEFAULT NULL,
  `address` varchar(7) DEFAULT NULL,
  `postcode` varchar(6) DEFAULT NULL,
  `mobile` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES ('ruban@gmail.com','dsffsdf','3423','cvcvxc'),('ruban@gmail.com','dsffsdf','3423','cvcvxc'),('ruban@gmail.com','dddd','ddd','434343'),('ruban@gmail.com','dddd','ddd','434343'),('steve@gmail.com','1234','9877','45678'),('ruban@gmail.com','dfsd','785873','784378483');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `categoryId` tinyint(4) DEFAULT NULL,
  `name` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'watch\r\n'),(2,'gajets'),(3,'TV'),(4,'Headphone'),(5,'Printers'),(6,'Accessories'),(7,'others');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kart`
--

DROP TABLE IF EXISTS `kart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kart` (
  `userId` tinyint(4) DEFAULT NULL,
  `productId` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kart`
--

LOCK TABLES `kart` WRITE;
/*!40000 ALTER TABLE `kart` DISABLE KEYS */;
INSERT INTO `kart` VALUES (5,10),(5,10),(6,10),(6,10),(6,10),(6,16),(2,25),(3,23),(4,26),(4,21);
/*!40000 ALTER TABLE `kart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `productId` tinyint(4) DEFAULT NULL,
  `name` varchar(15) DEFAULT NULL,
  `price` decimal(6,1) DEFAULT NULL,
  `description` varchar(64) DEFAULT NULL,
  `image` varchar(15) DEFAULT NULL,
  `stock` varchar(0) DEFAULT NULL,
  `categoryId` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (2,'SONY',1150.0,'EXTRA BASS','sonyear.png','',4),(3,'JBL',1550.0,'super company with ow cost','jblear.jpg','',4),(4,'Samsung',500.0,'perfect product for samsung users','samear.jpg','',4),(5,'HP printer',7500.0,'high branded printer with gud outut','hpprint.jpg','',5),(6,'Godrej printers',11150.0,'A long lasting quality of printouts','godrejprint.jpg','',5),(7,'HCL printers',12000.0,'A wide range of colors which are used to give gud output results','HCLprint.jpg','',5),(8,'EPSON Printers',15000.0,'3D printing with scanners','epsonprint.jpg','',5),(9,'Panasonic 32',25000.0,'An HD 32 Inch TV with gud sound quality','panosonictv.jpg','',3),(10,'Sony 3D',50000.0,'3D Dimensional TV with ','sonytv.jpg','',3),(11,'Onida 42 Inch',45000.0,'An 42 inch hd tv with high quality','onidatv.jpeg','',3),(12,'BLP 22 Inch',22000.0,'An basic model of TV','bpltv.jpg','',3),(13,'HCL Keyboards',650.0,'A keyboard with band of HCL','hclkey.jpg','',6),(14,'MAC Keyboard',2550.0,'A apple system with pple mac keyboard','mackey.jpg','',6),(15,'Keyboard Combo',4500.0,'A set of three items','combo.jpg','',6),(16,'OTG',70.0,'connects the mobile with pendrive','otg.jpg','',6),(17,'SONY LAPTOP',45000.0,'A sony laptop with 4gb ram and 1 tb ram','laptopsony.png','',7),(18,'SAMSUNG TAB',7050.0,'An tab with medium sized display with samsung brand','samtab.jpg','',7),(19,'WATCH',750.0,'watch with gud design and make','watch.png','',7),(20,'VR',3550.0,'enjoy the good experience of the virtual reality','vr.jpg\r\n','',7),(21,'DRONE',5000.0,'USED TO TAKE A 360degree soots ','123.png','',2),(22,'Smart watch',1250.0,'A red color  watch  ','e.png','',1),(23,'Smart watch',1250.0,'A green coloured watch','w.png','',1),(24,'Smart watch',1150.0,'An yellow color watcg','r.png','',1),(25,'Mi note Pro',7999.0,'A good medium sized image for mi lovers','mi.png','',2),(26,'Mi note 5 pro',16999.0,'a good pixel image of 16gb','sd.png','',2);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sqlite_sequence`
--

DROP TABLE IF EXISTS `sqlite_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sqlite_sequence` (
  `name` varchar(0) DEFAULT NULL,
  `seq` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sqlite_sequence`
--

LOCK TABLES `sqlite_sequence` WRITE;
/*!40000 ALTER TABLE `sqlite_sequence` DISABLE KEYS */;
/*!40000 ALTER TABLE `sqlite_sequence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `userId` tinyint(4) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `email` varchar(24) DEFAULT NULL,
  `firstName` varchar(13) DEFAULT NULL,
  `lastName` varchar(0) DEFAULT NULL,
  `address1` varchar(0) DEFAULT NULL,
  `address2` varchar(0) DEFAULT NULL,
  `zipcode` varchar(0) DEFAULT NULL,
  `city` varchar(0) DEFAULT NULL,
  `state` varchar(0) DEFAULT NULL,
  `country` varchar(0) DEFAULT NULL,
  `phone` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'','','','','','','','','','',''),(2,'21232f297a57a5a743894a0e4a801fc3','ruban@gmail.com','RUBAN BHARATH','','','','','','','',''),(3,'21232f297a57a5a743894a0e4a801fc3','rubanbharath25@gmail.com','ruban','','','','','','','',''),(4,'7815696ecbf1c96e6894b779456d330e','asd@gmail.com','asd','','','','','','','',''),(5,'83878c91171338902e0fe0fb97a8c47a','p@gmail.com','pratham','','','','','','','','');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-22 15:20:26
