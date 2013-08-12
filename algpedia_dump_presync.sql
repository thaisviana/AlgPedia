-- MySQL dump 10.14  Distrib 5.5.31-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: AlgPedia
-- ------------------------------------------------------
-- Server version	5.5.31-MariaDB-log

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
-- Table structure for table `algorithm_algorithm`
--

DROP TABLE IF EXISTS `algorithm_algorithm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_algorithm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `description` longtext NOT NULL,
  `classification_id` int(11) DEFAULT NULL,
  `uri` varchar(200) NOT NULL,
  `visible` tinyint(1) NOT NULL,
  `reputation` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `algorithm_algorithm_d3dde821` (`classification_id`),
  CONSTRAINT `classification_id_refs_id_61331f30` FOREIGN KEY (`classification_id`) REFERENCES `algorithm_classification` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_algorithm`
--

LOCK TABLES `algorithm_algorithm` WRITE;
/*!40000 ALTER TABLE `algorithm_algorithm` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_algorithm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_classification`
--

DROP TABLE IF EXISTS `algorithm_classification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_classification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(35) NOT NULL,
  `uri` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_classification`
--

LOCK TABLES `algorithm_classification` WRITE;
/*!40000 ALTER TABLE `algorithm_classification` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_classification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_classificationproeficiencyscale`
--

DROP TABLE IF EXISTS `algorithm_classificationproeficiencyscale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_classificationproeficiencyscale` (
  `proeficiencyscale_ptr_id` int(11) NOT NULL,
  `classification_id` int(11) NOT NULL,
  PRIMARY KEY (`proeficiencyscale_ptr_id`),
  KEY `algorithm_classificationproeficiencyscale_d3dde821` (`classification_id`),
  CONSTRAINT `proeficiencyscale_ptr_id_refs_id_726ec173` FOREIGN KEY (`proeficiencyscale_ptr_id`) REFERENCES `algorithm_proeficiencyscale` (`id`),
  CONSTRAINT `classification_id_refs_id_c9b52535` FOREIGN KEY (`classification_id`) REFERENCES `algorithm_classification` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_classificationproeficiencyscale`
--

LOCK TABLES `algorithm_classificationproeficiencyscale` WRITE;
/*!40000 ALTER TABLE `algorithm_classificationproeficiencyscale` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_classificationproeficiencyscale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_implementation`
--

DROP TABLE IF EXISTS `algorithm_implementation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_implementation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `algorithm_id` int(11) NOT NULL,
  `code` longtext NOT NULL,
  `programming_language_id` int(11) NOT NULL,
  `visible` tinyint(1) NOT NULL,
  `reputation` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `algorithm_implementation_5b72ffe3` (`algorithm_id`),
  KEY `algorithm_implementation_4a49299f` (`programming_language_id`),
  CONSTRAINT `algorithm_id_refs_id_18222f3a` FOREIGN KEY (`algorithm_id`) REFERENCES `algorithm_algorithm` (`id`),
  CONSTRAINT `programming_language_id_refs_id_5363fe85` FOREIGN KEY (`programming_language_id`) REFERENCES `algorithm_programminglanguage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_implementation`
--

LOCK TABLES `algorithm_implementation` WRITE;
/*!40000 ALTER TABLE `algorithm_implementation` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_implementation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_implementationquestion`
--

DROP TABLE IF EXISTS `algorithm_implementationquestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_implementationquestion` (
  `question_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`question_ptr_id`),
  CONSTRAINT `question_ptr_id_refs_id_4a6e9acc` FOREIGN KEY (`question_ptr_id`) REFERENCES `algorithm_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_implementationquestion`
--

LOCK TABLES `algorithm_implementationquestion` WRITE;
/*!40000 ALTER TABLE `algorithm_implementationquestion` DISABLE KEYS */;
INSERT INTO `algorithm_implementationquestion` VALUES (2),(3),(4);
/*!40000 ALTER TABLE `algorithm_implementationquestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_implementationquestionanswer`
--

DROP TABLE IF EXISTS `algorithm_implementationquestionanswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_implementationquestionanswer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `implementation_id` int(11) NOT NULL,
  `implementation_question_id` int(11) NOT NULL,
  `question_answer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `algorithm_implementationquestionanswer_6340c63c` (`user_id`),
  KEY `algorithm_implementationquestionanswer_b3719bb6` (`implementation_id`),
  KEY `algorithm_implementationquestionanswer_b4d1904d` (`implementation_question_id`),
  KEY `algorithm_implementationquestionanswer_6ed5681d` (`question_answer_id`),
  CONSTRAINT `implementation_question_id_refs_question_ptr_id_7a2dd5f5` FOREIGN KEY (`implementation_question_id`) REFERENCES `algorithm_implementationquestion` (`question_ptr_id`),
  CONSTRAINT `implementation_id_refs_id_a8cbae5a` FOREIGN KEY (`implementation_id`) REFERENCES `algorithm_implementation` (`id`),
  CONSTRAINT `question_answer_id_refs_id_487687c3` FOREIGN KEY (`question_answer_id`) REFERENCES `algorithm_questionanswer` (`id`),
  CONSTRAINT `user_id_refs_id_376352f9` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_implementationquestionanswer`
--

LOCK TABLES `algorithm_implementationquestionanswer` WRITE;
/*!40000 ALTER TABLE `algorithm_implementationquestionanswer` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_implementationquestionanswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_interest`
--

DROP TABLE IF EXISTS `algorithm_interest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_interest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classification_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `algorithm_interest_d3dde821` (`classification_id`),
  KEY `algorithm_interest_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_551022bb` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `classification_id_refs_id_fe0553e8` FOREIGN KEY (`classification_id`) REFERENCES `algorithm_classification` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_interest`
--

LOCK TABLES `algorithm_interest` WRITE;
/*!40000 ALTER TABLE `algorithm_interest` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_interest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_proeficiencyscale`
--

DROP TABLE IF EXISTS `algorithm_proeficiencyscale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_proeficiencyscale` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `value` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `algorithm_proeficiencyscale_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_00718f22` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_proeficiencyscale`
--

LOCK TABLES `algorithm_proeficiencyscale` WRITE;
/*!40000 ALTER TABLE `algorithm_proeficiencyscale` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_proeficiencyscale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_programminglanguage`
--

DROP TABLE IF EXISTS `algorithm_programminglanguage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_programminglanguage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_programminglanguage`
--

LOCK TABLES `algorithm_programminglanguage` WRITE;
/*!40000 ALTER TABLE `algorithm_programminglanguage` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_programminglanguage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_programminglanguageproeficiencyscale`
--

DROP TABLE IF EXISTS `algorithm_programminglanguageproeficiencyscale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_programminglanguageproeficiencyscale` (
  `proeficiencyscale_ptr_id` int(11) NOT NULL,
  `programming_language_id` int(11) NOT NULL,
  PRIMARY KEY (`proeficiencyscale_ptr_id`),
  KEY `algorithm_programminglanguageproeficiencyscale_4a49299f` (`programming_language_id`),
  CONSTRAINT `programming_language_id_refs_id_11fd400d` FOREIGN KEY (`programming_language_id`) REFERENCES `algorithm_programminglanguage` (`id`),
  CONSTRAINT `proeficiencyscale_ptr_id_refs_id_f868141a` FOREIGN KEY (`proeficiencyscale_ptr_id`) REFERENCES `algorithm_proeficiencyscale` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_programminglanguageproeficiencyscale`
--

LOCK TABLES `algorithm_programminglanguageproeficiencyscale` WRITE;
/*!40000 ALTER TABLE `algorithm_programminglanguageproeficiencyscale` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_programminglanguageproeficiencyscale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_question`
--

DROP TABLE IF EXISTS `algorithm_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `priority` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_question`
--

LOCK TABLES `algorithm_question` WRITE;
/*!40000 ALTER TABLE `algorithm_question` DISABLE KEYS */;
INSERT INTO `algorithm_question` VALUES (1,'What is your profile',2),(2,'This code compiles',3),(3,'How much readable is this code',4),(4,'How is this code\'s performance scalability',5);
/*!40000 ALTER TABLE `algorithm_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_questionanswer`
--

DROP TABLE IF EXISTS `algorithm_questionanswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_questionanswer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `value` int(11) NOT NULL,
  `text` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `algorithm_questionanswer_25110688` (`question_id`),
  CONSTRAINT `question_id_refs_id_17115741` FOREIGN KEY (`question_id`) REFERENCES `algorithm_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_questionanswer`
--

LOCK TABLES `algorithm_questionanswer` WRITE;
/*!40000 ALTER TABLE `algorithm_questionanswer` DISABLE KEYS */;
INSERT INTO `algorithm_questionanswer` VALUES (1,1,10,'Professor, UFRJ, IT'),(2,1,8,'Professional, UFRJ, IT'),(3,1,6,'Student, UFRJ, IT'),(4,1,4,'Professor, non-UFRJ, IT'),(5,1,2,'Professional, non-UFRJ, IT'),(6,1,1,'Student, non-UFRJ, IT'),(7,1,0,'non-IT'),(8,2,0,'No'),(9,2,1,'Yes'),(10,3,1,'1'),(11,3,2,'2'),(12,3,3,'3'),(13,3,4,'4'),(14,3,5,'5'),(15,4,1,'1'),(16,4,2,'2'),(17,4,3,'3'),(18,4,4,'4'),(19,4,5,'5');
/*!40000 ALTER TABLE `algorithm_questionanswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_userquestion`
--

DROP TABLE IF EXISTS `algorithm_userquestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_userquestion` (
  `question_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`question_ptr_id`),
  CONSTRAINT `question_ptr_id_refs_id_66daba40` FOREIGN KEY (`question_ptr_id`) REFERENCES `algorithm_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_userquestion`
--

LOCK TABLES `algorithm_userquestion` WRITE;
/*!40000 ALTER TABLE `algorithm_userquestion` DISABLE KEYS */;
INSERT INTO `algorithm_userquestion` VALUES (1);
/*!40000 ALTER TABLE `algorithm_userquestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algorithm_userquestionanswer`
--

DROP TABLE IF EXISTS `algorithm_userquestionanswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `algorithm_userquestionanswer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `user_question_id` int(11) NOT NULL,
  `question_answer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `algorithm_userquestionanswer_6340c63c` (`user_id`),
  KEY `algorithm_userquestionanswer_b9a81bdf` (`user_question_id`),
  KEY `algorithm_userquestionanswer_6ed5681d` (`question_answer_id`),
  CONSTRAINT `question_answer_id_refs_id_a5315bd3` FOREIGN KEY (`question_answer_id`) REFERENCES `algorithm_questionanswer` (`id`),
  CONSTRAINT `user_id_refs_id_f84ffcfb` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `user_question_id_refs_question_ptr_id_e84c7f23` FOREIGN KEY (`user_question_id`) REFERENCES `algorithm_userquestion` (`question_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algorithm_userquestionanswer`
--

LOCK TABLES `algorithm_userquestionanswer` WRITE;
/*!40000 ALTER TABLE `algorithm_userquestionanswer` DISABLE KEYS */;
/*!40000 ALTER TABLE `algorithm_userquestionanswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add log entry',4,'add_logentry'),(11,'Can change log entry',4,'change_logentry'),(12,'Can delete log entry',4,'delete_logentry'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add programming language',8,'add_programminglanguage'),(23,'Can change programming language',8,'change_programminglanguage'),(24,'Can delete programming language',8,'delete_programminglanguage'),(25,'Can add classification',9,'add_classification'),(26,'Can change classification',9,'change_classification'),(27,'Can delete classification',9,'delete_classification'),(28,'Can add algorithm',10,'add_algorithm'),(29,'Can change algorithm',10,'change_algorithm'),(30,'Can delete algorithm',10,'delete_algorithm'),(31,'Can add implementation',11,'add_implementation'),(32,'Can change implementation',11,'change_implementation'),(33,'Can delete implementation',11,'delete_implementation'),(34,'Can add interest',12,'add_interest'),(35,'Can change interest',12,'change_interest'),(36,'Can delete interest',12,'delete_interest'),(37,'Can add proeficiency scale',13,'add_proeficiencyscale'),(38,'Can change proeficiency scale',13,'change_proeficiencyscale'),(39,'Can delete proeficiency scale',13,'delete_proeficiencyscale'),(40,'Can add programming language proeficiency scale',14,'add_programminglanguageproeficiencyscale'),(41,'Can change programming language proeficiency scale',14,'change_programminglanguageproeficiencyscale'),(42,'Can delete programming language proeficiency scale',14,'delete_programminglanguageproeficiencyscale'),(43,'Can add classification proeficiency scale',15,'add_classificationproeficiencyscale'),(44,'Can change classification proeficiency scale',15,'change_classificationproeficiencyscale'),(45,'Can delete classification proeficiency scale',15,'delete_classificationproeficiencyscale'),(46,'Can add question',16,'add_question'),(47,'Can change question',16,'change_question'),(48,'Can delete question',16,'delete_question'),(49,'Can add question answer',17,'add_questionanswer'),(50,'Can change question answer',17,'change_questionanswer'),(51,'Can delete question answer',17,'delete_questionanswer'),(52,'Can add user question',18,'add_userquestion'),(53,'Can change user question',18,'change_userquestion'),(54,'Can delete user question',18,'delete_userquestion'),(55,'Can add user question answer',19,'add_userquestionanswer'),(56,'Can change user question answer',19,'change_userquestionanswer'),(57,'Can delete user question answer',19,'delete_userquestionanswer'),(58,'Can add implementation question',20,'add_implementationquestion'),(59,'Can change implementation question',20,'change_implementationquestion'),(60,'Can delete implementation question',20,'delete_implementationquestion'),(61,'Can add implementation question answer',21,'add_implementationquestionanswer'),(62,'Can change implementation question answer',21,'change_implementationquestionanswer'),(63,'Can delete implementation question answer',21,'delete_implementationquestionanswer');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$3bJEFa3n5UGd$3ulEPa8jqAGMh5tzyjqgjFUzO2EQURjG8YjByqqwIKU=','2013-07-11 02:43:54',1,'alfa','','','andreluiz90@ig.com.br',1,1,'2013-07-11 02:43:54');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'log entry','admin','logentry'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'programming language','algorithm','programminglanguage'),(9,'classification','algorithm','classification'),(10,'algorithm','algorithm','algorithm'),(11,'implementation','algorithm','implementation'),(12,'interest','algorithm','interest'),(13,'proeficiency scale','algorithm','proeficiencyscale'),(14,'programming language proeficiency scale','algorithm','programminglanguageproeficiencyscale'),(15,'classification proeficiency scale','algorithm','classificationproeficiencyscale'),(16,'question','algorithm','question'),(17,'question answer','algorithm','questionanswer'),(18,'user question','algorithm','userquestion'),(19,'user question answer','algorithm','userquestionanswer'),(20,'implementation question','algorithm','implementationquestion'),(21,'implementation question answer','algorithm','implementationquestionanswer');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-07-10 23:49:11
