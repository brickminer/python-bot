-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: brickminer
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

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
-- Current Database: `brickminer`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `localbot` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `localbot`;

--
-- Table structure for table `sets`
--

DROP TABLE IF EXISTS `sets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sets` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `number` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `type` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `theme_group` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `theme` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `subtheme` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tags` varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `pieces` int(11) DEFAULT NULL,
  `minifigs` int(11) DEFAULT NULL,
  `uk_price` double(5,2) DEFAULT NULL,
  `us_price` double(5,2) DEFAULT NULL,
  `eu_price` double(5,2) DEFAULT NULL,
  `packaging` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dimensions` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `weight` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `barcodes` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `item_number` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sets_number_unique` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=13690 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sets`
--

LOCK TABLES `sets` WRITE;
/*!40000 ALTER TABLE `sets` DISABLE KEYS */;
INSERT INTO `sets` VALUES
    (13661,'854031-1','Statue of Liberty Magnet',NULL,'Miscellaneous','501','Magnets/Locations','Female USA Statue Magnet New York ',2020,11,NULL,3.99,0.00,4.99,NULL,NULL,NULL,'UPC: 673419324137',NULL,'https://cdn.rebrickable.com/media/sets/854031-1/55066.jpg','https://rebrickable.com/sets/854031-1/statue-of-liberty-magnet/','2020-04-28 00:34:17','2020-04-28 00:34:17'),
    (13662,'854032-1','New York Key Chain',NULL,'Miscellaneous','503','Key Chains/Miscellaneous','',2020,0,NULL,0.00,0.00,0.00,NULL,NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/854032-1/55070.jpg','https://rebrickable.com/sets/854032-1/new-york-key-chain/','2020-04-28 00:34:18','2020-04-28 00:34:18'),
    (13663,'891958-1','Jay',NULL,'Action/Adventure','435','Magazine Gift','Jay Walker ',2019,9,1,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/891958-1/16344.jpg','https://rebrickable.com/sets/891958-1/jay/','2020-04-28 00:35:39','2020-04-28 00:35:39'),
    (13664,'892059-1','Kai',NULL,'Action/Adventure','435',NULL,'Kai ',2020,6,1,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/892059-1/55282.jpg','https://rebrickable.com/sets/892059-1/kai/','2020-04-28 00:35:40','2020-04-28 00:35:40'),
    (13665,'892060-1','Lloyd',NULL,'Action/Adventure','435','Magazine Gift','Lloyd Garmadon ',2020,6,1,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/892060-1/55697.jpg','https://rebrickable.com/sets/892060-1/lloyd/','2020-04-28 00:35:40','2020-04-28 00:35:40'),
    (13666,'892061-1','Ice Emperor',NULL,'Action/Adventure','435','Magazine Gift','Ice Emperor ',2020,10,1,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/892061-1/55801.jpg','https://rebrickable.com/sets/892061-1/ice-emperor/','2020-04-28 00:35:40','2020-04-28 00:35:40'),
    (13667,'892062-1','Cole with Cyber-sledge and Katana',NULL,'Action/Adventure','435','Magazine Gift','Cole ',2020,21,1,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/892062-1/56516.jpg','https://rebrickable.com/sets/892062-1/cole-with-cyber-sledge-and-katana/','2020-04-28 00:35:40','2020-04-28 00:35:40'),
    (13668,'9008-1','Baby Set',NULL,'Educational','516','Duplo','',1986,13,NULL,0.00,0.00,0.00,NULL,NULL,NULL,NULL,NULL,NULL,'https://rebrickable.com/sets/9008-1/baby-set/','2020-04-28 00:35:51','2020-04-28 00:35:51'),
    (13669,'912055-1','Snowspeeder',NULL,'Licensed','158','Magazine Gift','Microscale Snowspeeder ',2020,28,NULL,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/912055-1/16576.jpg','https://rebrickable.com/sets/912055-1/snowspeeder/','2020-04-28 00:36:08','2020-04-28 00:36:08'),
    (13670,'912056-1','TIE Striker',NULL,'Licensed','158','Magazine Gift','Microscale ',2020,28,NULL,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/912056-1/54276.jpg','https://rebrickable.com/sets/912056-1/tie-striker/','2020-04-28 00:36:08','2020-04-28 00:36:08'),
    (13671,'912057-1','R2-D2 & MSE-6',NULL,'Licensed','158','Magazine Gift','Mouse Droid R2-D2 ',2020,13,2,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/912057-1/56483.jpg','https://rebrickable.com/sets/912057-1/r2-d2-mse-6/','2020-04-28 00:36:09','2020-04-28 00:36:09'),
    (13672,'912058-1','Darth Maul\'s Sith Infiltrator',NULL,'Licensed','158','Magazine Gift','Microscale ',2020,34,NULL,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/912058-1/55848.jpg','https://rebrickable.com/sets/912058-1/darth-mauls-sith-infiltrator/','2020-04-28 00:36:09','2020-04-28 00:36:09'),
    (13673,'912059-1','Elite Praetorian Guard',NULL,'Licensed','158','Magazine Gift','Elite Praetorian Guard ',2020,7,1,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/912059-1/58536.jpg','https://rebrickable.com/sets/912059-1/elite-praetorian-guard/','2020-04-28 00:36:09','2020-04-28 00:36:09'),
    (13674,'9409-1','Islander Key Chain',NULL,'Miscellaneous','503','Furniture','',1994,0,NULL,262.99,0.00,0.00,NULL,NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/9409-1/14456.jpg','https://rebrickable.com/sets/9409-1/islander-key-chain/','2020-04-28 00:36:30','2020-04-28 00:36:30'),
    (13675,'952001-1','Policeman & Motorbike',NULL,'Modern day','61','Magazine Gift','Motorcycle Police ',2020,15,1,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/952001-1/19167.jpg','https://rebrickable.com/sets/952001-1/policeman-motorbike/','2020-04-28 00:36:41','2020-04-28 00:36:41'),
    (13676,'952002-1','Bobby Brenner with Extinguishing Drone',NULL,'Modern day','58','Magazine Gift','Fire Drone ',2020,17,1,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/952002-1/54931.jpg','https://rebrickable.com/sets/952002-1/bobby-brenner-with-extinguishing-drone/','2020-04-28 00:36:41','2020-04-28 00:36:41'),
    (13677,'952003-1','Eddy Erker with Bulldozer',NULL,'Modern day','56','Magazine Gift','',2020,27,1,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/952003-1/55678.jpg','https://rebrickable.com/sets/952003-1/eddy-erker-with-bulldozer/','2020-04-28 00:36:41','2020-04-28 00:36:41'),
    (13678,'952016-1','Policeman and robber',NULL,'Modern day','61','Magazine Gift','',2020,10,2,0.00,0.00,0.00,'Foil pack',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/952016-1/56492.jpg','https://rebrickable.com/sets/952016-1/policeman-and-robber/','2020-04-28 00:36:42','2020-04-28 00:36:42'),
    (13679,'GMRACER6-1','General Mills Racer Car #6',NULL,'Miscellaneous','112','General Mills','',2009,4,NULL,0.00,0.00,0.00,NULL,NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/gmracer6-1/1550.jpg','https://rebrickable.com/sets/GMRACER6-1/general-mills-racer-car-6/','2020-04-28 00:37:53','2020-04-28 00:37:53'),
    (13680,'LHGO-1','LEGO House Grand Opening',NULL,'Miscellaneous','599','LEGO House','Microscale Lego House ',2017,26,NULL,0.00,0.00,0.00,'Zip-lock bag',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/lhgo-1/58.jpg','https://rebrickable.com/sets/LHGO-1/lego-house-grand-opening/','2020-04-28 00:38:10','2020-04-28 00:38:10'),
    (13681,'NEWSSTAND-1','Newsstand',NULL,'Miscellaneous','155',NULL,'Shop Street Vendor In Store Build ',2020,155,NULL,0.00,0.00,0.00,'None (loose parts)',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/newsstand-1/2643.jpg','https://rebrickable.com/sets/NEWSSTAND-1/newsstand/','2020-04-28 00:38:21','2020-04-28 00:38:21'),
    (13682,'PENGUIN-1','Penguin',NULL,'Miscellaneous','621','LEGO brand stores','Polybag Penguin Brick Built Animals ',2020,24,NULL,0.00,0.00,0.00,'Polybag',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/penguin-1/52199.jpg','https://rebrickable.com/sets/PENGUIN-1/penguin/','2020-04-28 00:38:23','2020-04-28 00:38:23'),
    (13683,'SDCC2018-1','Sheriff Deadpool',NULL,'Licensed','493','Promotional','Deadpool  SDCC Super Hero Wild West X Men ',2018,0,1,0.00,0.00,0.00,'Plastic box',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/sdcc2018-1/6565.jpg','https://rebrickable.com/sets/SDCC2018-1/sheriff-deadpool/','2020-04-28 00:38:25','2020-04-28 00:38:25'),
    (13684,'SDCC2018-2','Black Lightning',NULL,'Licensed','482','Promotional','Black Lightning  SDCC The Cw Dc Shows ',2018,0,1,0.00,0.00,0.00,'Plastic box',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/sdcc2018-2/17502.jpg','https://rebrickable.com/sets/SDCC2018-2/black-lightning/','2020-04-28 00:38:25','2020-04-28 00:38:25'),
    (13685,'SDCC2018-3','Apocalypseburg Unikitty',NULL,'Licensed','670','Promotional','Rage Kitty  Cat SDCC Apocalypseburg Brick Built Animals Master Builders The Lego Movie ',2018,18,1,0.00,0.00,0.00,'Plastic box',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/sdcc2018-3/515.jpg','https://rebrickable.com/sets/SDCC2018-3/apocalypseburg-unikitty/','2020-04-28 00:38:26','2020-04-28 00:38:26'),
    (13686,'SUPERMAN-1','Superman',NULL,'Miscellaneous','408','LEGO brand stores','In Store Build Brick Built Figure Dc Comics Super Heroes ',2013,40,NULL,0.00,0.00,0.00,'None (loose parts)',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/superman-1/55656.jpg','https://rebrickable.com/sets/SUPERMAN-1/superman/','2020-04-28 00:38:27','2020-04-28 00:38:27'),
    (13687,'TRUSHIELD-3','Captain America\'s Shield',NULL,'Licensed','487','Promotional','In Store Build Toys R Us ',2014,261,NULL,0.00,0.00,0.00,'None (loose parts)',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/trushield-3/16620.jpg','https://rebrickable.com/sets/TRUSHIELD-3/captain-americas-shield/','2020-04-28 00:38:32','2020-04-28 00:38:32'),
    (13688,'TRUWEASLEYCAR-1','Weasley Family Car',NULL,'Licensed','246',NULL,'',2018,36,NULL,0.00,0.00,0.00,'None (loose parts)',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/truweasleycar-1/9869.jpg','https://rebrickable.com/sets/TRUWEASLEYCAR-1/weasley-family-car/','2020-04-28 00:38:32','2020-04-28 00:38:32'),
    (13689,'XWING-2','X-Wing Trench Run',NULL,'Licensed','158',NULL,'',2019,52,NULL,0.00,0.00,0.00,'None (loose parts)',NULL,NULL,NULL,NULL,'https://cdn.rebrickable.com/media/sets/xwing-2/14758.jpg','https://rebrickable.com/sets/XWING-2/x-wing-trench-run/','2020-04-28 00:38:36','2020-04-28 00:38:36');
/*!40000 ALTER TABLE `sets` ENABLE KEYS */;
UNLOCK TABLES;
