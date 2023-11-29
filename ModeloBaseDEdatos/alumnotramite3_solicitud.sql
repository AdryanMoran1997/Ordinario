-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: alumnotramite3
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `solicitud`
--

DROP TABLE IF EXISTS `solicitud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solicitud` (
  `idSolicitud` int NOT NULL AUTO_INCREMENT,
  `Turno` int NOT NULL,
  `id_alumno` int NOT NULL,
  `id_estatus` int NOT NULL,
  `id_tramite` int NOT NULL,
  `id_municipio` int NOT NULL,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`idSolicitud`),
  KEY `id_alumno_idx` (`id_alumno`),
  KEY `id_estatus_idx` (`id_estatus`),
  KEY `id_tramite_idx` (`id_tramite`),
  KEY `id_municipio_idx` (`id_municipio`),
  CONSTRAINT `id_alumno` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`idAlumno`),
  CONSTRAINT `id_estatus` FOREIGN KEY (`id_estatus`) REFERENCES `estatus` (`idmestatus`),
  CONSTRAINT `id_municipio` FOREIGN KEY (`id_municipio`) REFERENCES `municipio` (`idmunicipio`),
  CONSTRAINT `id_tramite` FOREIGN KEY (`id_tramite`) REFERENCES `tramite` (`idTramite`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitud`
--

LOCK TABLES `solicitud` WRITE;
/*!40000 ALTER TABLE `solicitud` DISABLE KEYS */;
INSERT INTO `solicitud` VALUES (2,1,8,1,7,15,'2023-11-16'),(3,1,9,1,7,5,'2023-11-16'),(4,1,10,1,7,15,'2023-11-16'),(5,1,11,1,1,1,'2023-11-16'),(6,2,12,1,1,1,'2023-11-16'),(7,1,13,1,2,22,'2023-11-16'),(8,1,14,1,5,36,'2023-11-16'),(9,2,15,1,5,36,'2023-11-16'),(10,3,16,1,5,36,'2023-11-16'),(11,1,17,1,5,34,'2023-11-16'),(12,2,18,1,5,34,'2023-11-16'),(13,1,19,1,4,6,'2023-11-16'),(15,2,21,1,1,26,'2023-11-16'),(16,1,22,1,4,19,'2023-11-16'),(17,1,23,1,6,23,'2023-11-16'),(18,3,24,1,3,1,'2023-11-16'),(19,4,25,1,1,1,'2023-11-16'),(20,1,26,1,11,12,'2023-11-16'),(21,5,27,1,1,1,'2023-11-16'),(22,6,28,1,8,1,'2023-11-16'),(23,2,29,1,13,19,'2023-11-16'),(24,1,30,1,11,20,'2023-11-16'),(25,2,31,1,1,12,'2023-11-16'),(26,3,32,1,1,12,'2023-11-16'),(27,1,33,1,1,33,'2023-11-16'),(28,1,34,1,1,18,'2023-11-16'),(29,1,35,1,1,17,'2023-11-16');
/*!40000 ALTER TABLE `solicitud` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-29  6:49:58
