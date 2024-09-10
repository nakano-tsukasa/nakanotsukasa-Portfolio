-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: user_db
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book_groups`
--

DROP TABLE IF EXISTS `book_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book_groups` (
  `g_id` int(11) NOT NULL AUTO_INCREMENT,
  `g_name` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`g_id`),
  KEY `fk_user_id` (`user_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_profiles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_groups`
--

LOCK TABLES `book_groups` WRITE;
/*!40000 ALTER TABLE `book_groups` DISABLE KEYS */;
INSERT INTO `book_groups` VALUES (1,'others',1),(3,'others',2);
/*!40000 ALTER TABLE `book_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `book_name` varchar(255) NOT NULL,
  `g_id` int(11) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `published_date` text DEFAULT NULL,
  `b_created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `b_updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`book_id`),
  KEY `user_id` (`user_id`),
  KEY `fk_book_group` (`g_id`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_profiles` (`id`),
  CONSTRAINT `fk_book_group` FOREIGN KEY (`g_id`) REFERENCES `book_groups` (`g_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,1,'new book',1,'emily','1990-09-29','2024-09-06 10:53:44','2024-09-10 10:45:32'),(3,2,'new book',3,'nakano','19900929','2024-09-10 13:34:10','2024-09-10 13:34:10'),(4,2,'dreams',3,'ｔｔｔ',NULL,'2024-09-10 13:35:27','2024-09-10 13:35:27'),(5,2,'おおお',3,'ｗｗｗ',NULL,'2024-09-10 13:35:43','2024-09-10 13:35:43');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `derived_summaries`
--

DROP TABLE IF EXISTS `derived_summaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `derived_summaries` (
  `d_summary_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `d_summary_text` text NOT NULL,
  `d_created_at` timestamp NULL DEFAULT current_timestamp(),
  `d_updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`d_summary_id`),
  KEY `user_id` (`user_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `derived_summaries_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_profiles` (`id`),
  CONSTRAINT `derived_summaries_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `derived_summaries`
--

LOCK TABLES `derived_summaries` WRITE;
/*!40000 ALTER TABLE `derived_summaries` DISABLE KEYS */;
INSERT INTO `derived_summaries` VALUES (1,1,1,'自由が人々にとって重荷となり、抑圧や同調圧力の形で現れると論じられています。','2024-09-06 10:55:17','2024-09-06 10:55:17'),(2,1,1,'自由は自己実現に向けた自主性と責任を求める社会において、抑圧や同調圧力の重荷となる可能性がある。','2024-09-06 10:55:31','2024-09-06 10:55:31'),(3,1,1,'自由は自己実現に向けた責任と抑圧という二面性を持つ。','2024-09-06 10:55:47','2024-09-06 10:55:47');
/*!40000 ALTER TABLE `derived_summaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `summaries`
--

DROP TABLE IF EXISTS `summaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `summaries` (
  `summary_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `summary_text` text NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`summary_id`),
  KEY `user_id` (`user_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `summaries_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_profiles` (`id`),
  CONSTRAINT `summaries_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `summaries`
--

LOCK TABLES `summaries` WRITE;
/*!40000 ALTER TABLE `summaries` DISABLE KEYS */;
INSERT INTO `summaries` VALUES (1,1,1,'自由が人々にとって重荷となり、抑圧や同調圧力の形で現れると論じられています。','2024-09-06 10:55:17','2024-09-06 10:55:17'),(2,1,1,'フロムは、自由が真の自己実現につながるためには、自主性と責任を持った社会が必要だと提唱します。','2024-09-06 10:55:30','2024-09-06 10:55:30'),(3,1,1,'彼の著作は、自由の本質とその社会的な影響を深く考察するものです。','2024-09-06 10:55:45','2024-09-06 10:55:45');
/*!40000 ALTER TABLE `summaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profiles`
--

DROP TABLE IF EXISTS `user_profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_profiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `is_verified` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profiles`
--

LOCK TABLES `user_profiles` WRITE;
/*!40000 ALTER TABLE `user_profiles` DISABLE KEYS */;
INSERT INTO `user_profiles` VALUES (1,'nakano','tsukka929@gmail.com','pbkdf2:sha256:600000$bU33JHoIj4xD1PRC$c9c6416cef8c344d0a32d6517a593a1b9695647f08959274e363b4f23e24241e',1),(2,'nakano tsukasa','nakanotsukasa929@gmail.com','pbkdf2:sha256:600000$hNM16OHOP0yR8w3H$0dd9b23f29453db46b7f6795d4c3239f61353051247b01d0efc84a85da7e0cb4',1);
/*!40000 ALTER TABLE `user_profiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-10 23:28:59
