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
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumno` (
  `idAlumno` int NOT NULL AUTO_INCREMENT,
  `Curp` varchar(45) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Paterno` varchar(45) NOT NULL,
  `Materno` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Municipio_id` int NOT NULL,
  `NivelCurso_id` int NOT NULL,
  `Tramite_id` int NOT NULL,
  PRIMARY KEY (`idAlumno`,`Curp`),
  KEY `Municipio_id_idx` (`Municipio_id`),
  KEY `NivelCurso_id_idx` (`NivelCurso_id`),
  KEY `Tramite_id_idx` (`Tramite_id`),
  CONSTRAINT `Municipio_id` FOREIGN KEY (`Municipio_id`) REFERENCES `municipio` (`idmunicipio`),
  CONSTRAINT `NivelCurso_id` FOREIGN KEY (`NivelCurso_id`) REFERENCES `nivelcurso` (`idnivelCurso`),
  CONSTRAINT `Tramite_id` FOREIGN KEY (`Tramite_id`) REFERENCES `tramite` (`idTramite`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno`
--

LOCK TABLES `alumno` WRITE;
/*!40000 ALTER TABLE `alumno` DISABLE KEYS */;
INSERT INTO `alumno` VALUES (1,'PEGJ850315HJCRRN07','jose','Ontiveros','Moran','78323443232',5,5,5),(2,'DEGJ850315HJCRRN07','jose','Perez','Rivera','4332432123',3,3,5),(3,'DFGJ850315HJCRRN07','Diego','Rivera','Lopez','43243243',6,6,4),(4,'FEGJ850315HJCRRN07','diego','Perez','Rosales','21345324332',2,4,3),(5,'PEGJ850315HJCRRN07','jose','ontiveros','moran','23543534',6,6,5),(6,'RFGJ850315HJCRRN07','Rafael','ontiveros','moran','32423532',2,3,5),(7,'PGGJ850315HJCRRN07','Adrian','ontiveros','moran','84358345453',3,3,2),(8,'PGGJ850315HJCRRN07','Andres','Poso','Gonzales','21453452',15,3,7),(9,'HGGJ850315HJCRRN07','adrian','talavera','lopez','34324234243',5,1,7),(10,'LEGJ850315HJCRRN07','Jose','sdaads','adsads','433424323',15,12,7),(11,'LEGJ850315HJCRRN07','Jose','leiva','gutierrez','43243234323',1,1,1),(12,'FEGJ850315HJCRRN07','niño','leiva','gutierrez','43243234323',1,1,1),(13,'CEGJ850315HJCRRN07','Gabreil','Perez','Rocha','4535354435543',22,3,2),(14,'HEGJ850315HJCRRN07','Hector','Martin','Flores','',36,1,5),(15,'HFGJ850315HJCRRN07','Fausto','Martin','Flores','435345543543',36,1,5),(16,'DFÑJ850315HJCRRN07','Daniuel','Martin','Flores','435345543543',36,1,5),(17,'KFÑJ850315HJCRRN07','Cardona','Martin','Flores','435345543543',34,1,5),(18,'GFÑJ850315HJCRRN07','Eduardo','Martin','Flores','435345543543',34,1,5),(19,'APGJ850315HJCRRN07','Andres','Corpus','Garcia','856455433',6,6,4),(20,'ERGR850315HJCRRN07','Garcia','Corpus','Garcia','213223',26,1,1),(21,'EFGR850315HJCRRN07','Fausto','Corpus','Garcia','213223',26,1,1),(22,'ZZGJ850315HJCRRN07','Jose','Ontiveros','Mo0ran','45453435453',1,1,1),(23,'PEGJ850315HJCRRN07','jose','adrian','ontiveros','moran',23,5,6),(24,'FDGR850315HJCRRN07','Fausto','Corpus','Garcia','213223',1,6,3),(25,'LLGR850315HJCRRN07','Rodrigo','Corpus','Garcia','213223',1,1,1),(26,'EKGR850315HJCRRN07','Juan','Perez','Gaona','84358345453',12,7,11),(27,'TRGR850315HJCRRN07','Intriago','Perez','Gaona','84358345453',1,7,1),(28,'DRGR850315HJCRRN07','Solo','Perez','Gaona','84358345453',1,2,8),(29,'saddsasda','aa','sad','sad','sda',19,7,13),(30,'sda','sad','dsa','dsa','sad',20,12,11),(31,'dasdsa','asc','sad','das','sad',12,8,1),(32,'sdaaddsasda','dsadsa','dsasad','dsasdasdsad','sdadsasad',12,1,1),(33,'IEGJ850315HJCRRN07','damian','del rio','sanches','1234567890',33,1,1),(34,'PETD800714HCLRNV02','jose','adrian','ontiveros','1234567890',18,1,1),(35,'LETD800714HCLRNV02','ads','ads','das','8445394717',17,1,1);
/*!40000 ALTER TABLE `alumno` ENABLE KEYS */;
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
