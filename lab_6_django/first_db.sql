-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: first_db
-- ------------------------------------------------------
-- Server version	5.7.20-0ubuntu0.16.04.1

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'Война и мир','Лев Толстой'),(16,'Как закалялась сталь','Николай Островский');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `db_app_author`
--

DROP TABLE IF EXISTS `db_app_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `db_app_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(1023) CHARACTER SET utf8 NOT NULL,
  `description` longtext CHARACTER SET utf8 NOT NULL,
  `birth_date` date DEFAULT NULL,
  `death_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `db_app_author`
--

LOCK TABLES `db_app_author` WRITE;
/*!40000 ALTER TABLE `db_app_author` DISABLE KEYS */;
INSERT INTO `db_app_author` VALUES (1,'Николай Островский','Советский писатель, автор романа «Как закалялась сталь».','1904-09-29','1936-12-22'),(2,'Лев Толстой','Один из наиболее известных русских писателей и мыслителей, один из величайших писателей мира. Участник обороны Севастополя. Просветитель, публицист, религиозный мыслитель, его авторитетное мнение послужило причиной возникновения нового религиозно-нравственного течения — толстовства. Член-корреспондент Императорской Академии наук (1873), почётный академик по разряду изящной словесности (1900).','1828-09-09','1910-11-20');
/*!40000 ALTER TABLE `db_app_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `db_app_book`
--

DROP TABLE IF EXISTS `db_app_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `db_app_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(1023) CHARACTER SET utf8 NOT NULL,
  `description` longtext CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `db_app_book`
--

LOCK TABLES `db_app_book` WRITE;
/*!40000 ALTER TABLE `db_app_book` DISABLE KEYS */;
INSERT INTO `db_app_book` VALUES (1,'Как закалялась сталь','Автобиографический роман советского писателя Николая Алексеевича Островского, написанный в 1932 году. Книга написана в стилистике социалистического реализма.'),(2,'Война и мир','Роман-эпопея Льва Николаевича Толстого, описывающий русское общество в эпоху войн против Наполеона в 1805—1812 годах.');
/*!40000 ALTER TABLE `db_app_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `db_app_book_author`
--

DROP TABLE IF EXISTS `db_app_book_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `db_app_book_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `db_app_book_author_book_id_author_id_05384c7e_uniq` (`book_id`,`author_id`),
  KEY `db_app_book_author_author_id_c1105049_fk_db_app_author_id` (`author_id`),
  CONSTRAINT `db_app_book_author_author_id_c1105049_fk_db_app_author_id` FOREIGN KEY (`author_id`) REFERENCES `db_app_author` (`id`),
  CONSTRAINT `db_app_book_author_book_id_477ee103_fk_db_app_book_id` FOREIGN KEY (`book_id`) REFERENCES `db_app_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `db_app_book_author`
--

LOCK TABLES `db_app_book_author` WRITE;
/*!40000 ALTER TABLE `db_app_book_author` DISABLE KEYS */;
INSERT INTO `db_app_book_author` VALUES (1,1,1),(2,2,2);
/*!40000 ALTER TABLE `db_app_book_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `db_app_book_genre`
--

DROP TABLE IF EXISTS `db_app_book_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `db_app_book_genre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `db_app_book_genre_book_id_genre_id_4bbe2ca6_uniq` (`book_id`,`genre_id`),
  KEY `db_app_book_genre_genre_id_24bcf384_fk_db_app_genre_id` (`genre_id`),
  CONSTRAINT `db_app_book_genre_book_id_c64e503d_fk_db_app_book_id` FOREIGN KEY (`book_id`) REFERENCES `db_app_book` (`id`),
  CONSTRAINT `db_app_book_genre_genre_id_24bcf384_fk_db_app_genre_id` FOREIGN KEY (`genre_id`) REFERENCES `db_app_genre` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `db_app_book_genre`
--

LOCK TABLES `db_app_book_genre` WRITE;
/*!40000 ALTER TABLE `db_app_book_genre` DISABLE KEYS */;
INSERT INTO `db_app_book_genre` VALUES (1,1,1),(2,2,2);
/*!40000 ALTER TABLE `db_app_book_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `db_app_genre`
--

DROP TABLE IF EXISTS `db_app_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `db_app_genre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(1023) CHARACTER SET utf8 NOT NULL,
  `description` longtext CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `db_app_genre`
--

LOCK TABLES `db_app_genre` WRITE;
/*!40000 ALTER TABLE `db_app_genre` DISABLE KEYS */;
INSERT INTO `db_app_genre` VALUES (1,'Роман','Литературный жанр, чаще прозаический, зародившийся в средние века у романских народов как рассказ на народном языке и ныне превратившийся в самый распространенный вид эпической литературы, изображающий жизнь человека с её волнующими страстями (на первом плане любовь), борьбой, социальными противоречиями и стремлениями к идеалу. Будучи развернутым повествованием о жизни и развитии личности главного героя (героев) в кризисный, нестандартный период его жизни, отличается от повести объёмом, сложностью содержания и более широким захватом описываемых явлений.'),(2,'Роман-эпопея','Не нашел определения');
/*!40000 ALTER TABLE `db_app_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'db_app','0001_initial','2017-12-24 16:17:36.013580');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-24 20:37:21
