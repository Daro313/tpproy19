-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: grupo8
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

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

--
-- Current Database: `grupo8`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `grupo8` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `grupo8`;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configurations`
--

DROP TABLE IF EXISTS `configurations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configurations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `active` tinyint(1) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `title` varchar(60) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `offset_paginator` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_configurations_title` (`title`),
  KEY `ix_configurations_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configurations`
--

LOCK TABLES `configurations` WRITE;
/*!40000 ALTER TABLE `configurations` DISABLE KEYS */;
INSERT INTO `configurations` VALUES (1,1,'Orquesta escuela','Orquesta escuela','orquestaescuela@mail.com',3);
/*!40000 ALTER TABLE `configurations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `page`
--

DROP TABLE IF EXISTS `page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `page` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `page`
--

LOCK TABLES `page` WRITE;
/*!40000 ALTER TABLE `page` DISABLE KEYS */;
/*!40000 ALTER TABLE `page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES (3,'administrador'),(2,'docente'),(1,'preceptor');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `surname` varchar(60) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `birth_date` varchar(60) DEFAULT NULL,
  `borned` varchar(60) DEFAULT NULL,
  `locality` varchar(60) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `neighborhood` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `document_type` varchar(60) DEFAULT NULL,
  `document_number` varchar(60) DEFAULT NULL,
  `tutor` varchar(60) DEFAULT NULL,
  `phone` varchar(60) DEFAULT NULL,
  `school` varchar(60) DEFAULT NULL,
  `level` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (4,'afai','Prueba DOM','1985-05-21','safaaga      ','localidad','dm 1','2','female','LC','513131','madre','123456','2','5'),(6,'sarasa','Juancito','1980-11-11','asdasd ','Mar del Plata','dsadfsa 1223','2','male','CI','123','2','123456','2','5'),(7,'apotromas','otromas','2019-06-08','Alabahama ','General San Martín','1 123','2','male','Pasaporte','123456','2','1225555','2','9'),(8,'Dangelo','Daro','1985-06-08','dagiogo','Azul','sadfaffa','2','male','DNI','31550240','3','123456789','3','2');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tags` (
  `tag_id` int(11) NOT NULL,
  `page_id` int(11) NOT NULL,
  PRIMARY KEY (`tag_id`,`page_id`),
  KEY `page_id` (`page_id`),
  CONSTRAINT `tags_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`),
  CONSTRAINT `tags_ibfk_2` FOREIGN KEY (`page_id`) REFERENCES `page` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teachers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `surname` varchar(60) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `birth_date` varchar(60) DEFAULT NULL,
  `locality` varchar(60) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `document_type` varchar(60) DEFAULT NULL,
  `document_number` varchar(60) DEFAULT NULL,
  `phone` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (9,'DOCNETE','NUEVODOCE','1933-11-06','General Rodríguez','DSGAGADGA 541514','LC','4569789','6161526');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `created_at` date DEFAULT NULL,
  `updated_at` date DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_admin` tinyint(1) DEFAULT NULL,
  `username` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `name` varchar(60) DEFAULT NULL,
  `surname` varchar(60) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('2019-11-15','2019-11-20',1,0,'superadmin','admin@admin.com','ADMIN','ADMIN',1,'pbkdf2:sha256:150000$evXQSHEd$3943367f686e4fcd65772087be0baa77f8c93afcfb08218f068b8c9cf57fa346'),('2019-11-17','2019-11-20',20,0,'nomusu4edit','usu4edit@mail.com','usuario4edit','usuario4edit',1,'pbkdf2:sha256:150000$BhKL5rId$b6cfd8d9e3874d19d2586b4acf31257ce846ce145859182eace2a08d64e5851c'),('2019-11-17','2019-11-20',21,0,'nomusu5edit','usu5edit@mail.com','usuainac2','usuainac2',0,'pbkdf2:sha256:150000$lPYdPgEQ$dea0e82bf7f9621a0aa35c10c2930ed2ee69ddd1c99829397cabb190a686250d'),('2019-11-17',NULL,23,0,'nomusu7','usu7@mail.com','usuario7','ape7',1,'pbkdf2:sha256:150000$3K2mxPAo$e164111643bc25647f435346fce4869aa5d459f0d7d217e899f14af9f73b46be'),('2019-11-17',NULL,24,0,'nomusu8','usu8@mail.com','usuario8','ape8',1,'pbkdf2:sha256:150000$sg2mVCsv$0ebd8c718d5a619a794d8c073552a21d5a7f456319139da8ca926e8c6f96f594'),('2019-11-17',NULL,25,0,'nomusu9','usu9@mail.com','usuario9','ape9',1,'pbkdf2:sha256:150000$rhagk8IQ$f5a4b2663432e167cba3c17c1e8885632486b485bc3a19e50faf3f9dc9f1fa21'),('2019-11-17',NULL,26,0,'nomusu10','usu10@mail.com','usuario10','ape10',1,'pbkdf2:sha256:150000$Chdkibnv$40b9f07ad846cfc44e62b1afed72539347c1c67224856d0d9e8b3f1590f15e9d'),('2019-11-17',NULL,27,0,'nomusu11','usu11@mail.com','usuario11','ape11',1,'pbkdf2:sha256:150000$ZEfBd3j6$118ea2f96b25362b5453dc1465d639d8af852389fab09c158af9c7b0d680894a'),('2019-11-17',NULL,28,0,'nomusu12','usu12@mail.com','usuario12','ape12',1,'pbkdf2:sha256:150000$UWxohjCM$5b9d72568014de71f1e8130b9d77c3193bfe27be2aa3db34fe4b5b7e1bc92141'),('2019-11-18',NULL,29,0,'nomusu','email@email2.com','Usuario super','creado recien',1,'pbkdf2:sha256:150000$JjWLGnqW$e57482c9ec2746bfc0d7bc8bd54d1de2f21cc9eda9d549a98832ec7820a9e6aa'),('2019-11-18',NULL,30,0,'nomsusuma','asfegf@mail.com','otromas','sisi',1,'pbkdf2:sha256:150000$lHHny7nN$e2cc6f75ddeedced46466b86620403ed20c355f43dab05e8c65c327782c883b1'),('2019-11-20',NULL,32,0,'safafw3r3','asadaf33@mail.com','Juancito','ApDocente2',1,'pbkdf2:sha256:150000$GmEY2j30$ceca0d725b1405935a1798b0cec1d23cb9a997ac155db6cf3318cc0052a3bbec'),('2019-11-20',NULL,34,0,'nomususunuevo','adasmo@admin.com','usunuevo','apusunuevo',1,'pbkdf2:sha256:150000$dmDaRFfQ$d01c4d113330b551ae151030fc78dc092beadb8687f13d833b290f20038e99bc'),('2019-11-20',NULL,36,0,'dpmfgapfma','afmapW@mail.com','omfaofm','sfdomfoadm',1,'pbkdf2:sha256:150000$1MteiskK$2226d9a06b7bbe7fcfc6b107e1d8db90d0c6b52bda7e87a958662d4636b2a940'),('2019-11-20',NULL,38,0,'afaef','faef4@mail.com','safsf','afafaf',1,'pbkdf2:sha256:150000$slmIsalb$5c0406139092d7d4cae09b73b1aecc72f4449e4d23fafc075c02339ce12de477');
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

-- Dump completed on 2019-11-20 22:30:15
