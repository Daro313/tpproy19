-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: grupo8
-- ------------------------------------------------------
-- Server version	5.7.23-2

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
  KEY `ix_configurations_email` (`email`),
  KEY `ix_configurations_title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configurations`
--

LOCK TABLES `configurations` WRITE;
/*!40000 ALTER TABLE `configurations` DISABLE KEYS */;
INSERT INTO `configurations` VALUES (1,1,'escuela orquesta beriso','escuela orquesta','escuela@orquesta.mail.com',20);
/*!40000 ALTER TABLE `configurations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `attend` tinyint(1) DEFAULT NULL,
  `workshop_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `workshop_id` (`workshop_id`),
  CONSTRAINT `lesson_ibfk_1` FOREIGN KEY (`workshop_id`) REFERENCES `workshop` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lesson`
--

LOCK TABLES `lesson` WRITE;
/*!40000 ALTER TABLE `lesson` DISABLE KEYS */;
/*!40000 ALTER TABLE `lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `permisos` varchar(60000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'docente','students_index,students_update,students_show,teachers_index,teachers_show,administration_index,administration_show'),(2,'administrador','students_index,students_new,students_destroy,students_update,students_show,user_index,user_new,user_destroy,user_update,user_show,teachers_index,teachers_new,teachers_destroy,teachers_update,teachers_show,configurations_index,configurations_new,configurations_destroy,configurations_update,configurations_show,administration_index,administration_new,administration_destroy,administration_update,administration_show'),(3,'preceptor','students_index,students_update,students_show');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `school_year`
--

DROP TABLE IF EXISTS `school_year`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `school_year` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `semesters` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `school_year`
--

LOCK TABLES `school_year` WRITE;
/*!40000 ALTER TABLE `school_year` DISABLE KEYS */;
INSERT INTO `school_year` VALUES (1,'2019-12-01','2019-12-26','1'),(2,'2019-12-31','2019-12-28','1'),(3,'2019-12-31','2019-12-28','1');
/*!40000 ALTER TABLE `school_year` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,NULL,'Juan',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_roles`
--

DROP TABLE IF EXISTS `user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_roles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `user_roles_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
INSERT INTO `user_roles` VALUES (1,1,2);
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('2019-12-11',NULL,1,0,'admin','admin@admin.com',NULL,NULL,1,'pbkdf2:sha256:150000$q2RauE6j$fb9f88cdf9781688b70c208ddfe7b787dacb52a85c8843e8615029a24d9f4fb8');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workshop`
--

DROP TABLE IF EXISTS `workshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workshop` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) DEFAULT NULL,
  `short_name` varchar(60) DEFAULT NULL,
  `semester_id` int(11) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `cant_lessons` int(11) DEFAULT NULL,
  `nucleo` varchar(120) DEFAULT NULL,
  `address` varchar(214) DEFAULT NULL,
  `days` varchar(520) DEFAULT NULL,
  `horario` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `semester_id` (`semester_id`),
  KEY `teacher_id` (`teacher_id`),
  CONSTRAINT `workshop_ibfk_1` FOREIGN KEY (`semester_id`) REFERENCES `school_year` (`id`),
  CONSTRAINT `workshop_ibfk_2` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workshop`
--

LOCK TABLES `workshop` WRITE;
/*!40000 ALTER TABLE `workshop` DISABLE KEYS */;
INSERT INTO `workshop` VALUES (1,'tito taller','tt',1,1,0,'1','Calle 41 1492, Apt 3b','Calle 41 1492, Apt 3b','05:01'),(2,'tito taller','tt',1,1,0,'1','Calle 41 1492, Apt 3b','Calle 41 1492, Apt 3b','05:01'),(3,'Guitarra','gt',1,1,0,'1','41 1492','41 1492','01:00'),(4,'Guitarra','gt',1,1,0,'1','41 1492','41 1492','01:00'),(5,'Guitarra','gt',1,1,0,'1','41','41','01:00'),(6,'Guitarra','gt',1,1,0,'1','41','41','01:00'),(7,'saxo','sx',1,1,0,'1','41 1492','41 1492','01:00');
/*!40000 ALTER TABLE `workshop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workshop_students`
--

DROP TABLE IF EXISTS `workshop_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workshop_students` (
  `workshop_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `attent_date` date DEFAULT NULL,
  PRIMARY KEY (`workshop_id`,`student_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `workshop_students_ibfk_1` FOREIGN KEY (`workshop_id`) REFERENCES `workshop` (`id`),
  CONSTRAINT `workshop_students_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workshop_students`
--

LOCK TABLES `workshop_students` WRITE;
/*!40000 ALTER TABLE `workshop_students` DISABLE KEYS */;
/*!40000 ALTER TABLE `workshop_students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-11 23:35:25
