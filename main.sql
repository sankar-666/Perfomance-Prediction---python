/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - main
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`main` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `main`;

/*Table structure for table `assignments` */

DROP TABLE IF EXISTS `assignments`;

CREATE TABLE `assignments` (
  `assignment_id` int(11) NOT NULL AUTO_INCREMENT,
  `faculty_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `title` varchar(30) DEFAULT NULL,
  `decription` varchar(50) DEFAULT NULL,
  `maximum_mark` varchar(50) DEFAULT NULL,
  `assignment_date` varchar(30) DEFAULT NULL,
  `fial_date_submission` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`assignment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `assignments` */

insert  into `assignments`(`assignment_id`,`faculty_id`,`course_id`,`title`,`decription`,`maximum_mark`,`assignment_date`,`fial_date_submission`) values (4,2,5,'bigdata','assignment for bigdata and datascience','60','2022-09-19','2022-09-29');

/*Table structure for table `courses` */

DROP TABLE IF EXISTS `courses`;

CREATE TABLE `courses` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_title` varchar(35) DEFAULT NULL,
  `course_description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `courses` */

insert  into `courses`(`course_id`,`course_title`,`course_description`) values (6,'Mba','Master of buisness applications'),(5,'MCA','master of computer applications'),(7,'BCA','Bachelor of computer Application\r\n');

/*Table structure for table `doubts` */

DROP TABLE IF EXISTS `doubts`;

CREATE TABLE `doubts` (
  `doubt_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `note_id` int(11) DEFAULT NULL,
  `doubt_description` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `doubt_date` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`doubt_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `doubts` */

insert  into `doubts`(`doubt_id`,`student_id`,`note_id`,`doubt_description`,`reply`,`doubt_date`) values (1,5,1,'need clarification','ok','2022-09-15'),(2,5,1,'eee','pending','2022-09-26'),(3,1,1,'i want clarification..','pending','2022-10-12');

/*Table structure for table `exercise` */

DROP TABLE IF EXISTS `exercise`;

CREATE TABLE `exercise` (
  `exercise_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) DEFAULT NULL,
  `exercise_question` varchar(50) DEFAULT NULL,
  `correct_option_id` int(50) DEFAULT NULL,
  `assignment_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`exercise_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `exercise` */

insert  into `exercise`(`exercise_id`,`subject_id`,`exercise_question`,`correct_option_id`,`assignment_date`) values (1,2,'Which of the following statements should be used t',3,'2020-03-20'),(2,2,'What are the types of linkages?',6,'2020-03-20'),(3,2,'Which of the following special symbol allowed in a',12,'2020-03-20'),(4,3,'What is a bit array?',14,'2020-03-24'),(5,3,' Which of the following bitwise operations will yo',18,'2020-03-24'),(6,2,'Wrapping data and its related functionality into a',22,'2020-03-20'),(7,2,'i like u',26,'2022-10-12'),(8,3,'hello',31,'2022-10-12'),(9,10,'do or die',32,'2022-10-12'),(10,11,'difference Between = , == and === in JS? ',35,'2022-10-12'),(11,11,'is 5 or 4 greater?',37,'2022-10-12'),(12,10,'how ar u',40,'2022-10-12');

/*Table structure for table `exerciseknowledges` */

DROP TABLE IF EXISTS `exerciseknowledges`;

CREATE TABLE `exerciseknowledges` (
  `exercise_knowledge_id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) DEFAULT NULL,
  `knowledge_area_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`exercise_knowledge_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `exerciseknowledges` */

insert  into `exerciseknowledges`(`exercise_knowledge_id`,`exercise_id`,`knowledge_area_id`) values (12,12,3),(11,11,1),(10,10,3),(9,9,1),(8,8,1);

/*Table structure for table `exerciseoptions` */

DROP TABLE IF EXISTS `exerciseoptions`;

CREATE TABLE `exerciseoptions` (
  `option_id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` int(11) DEFAULT NULL,
  `option_description` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`option_id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

/*Data for the table `exerciseoptions` */

insert  into `exerciseoptions`(`option_id`,`exercise_id`,`option_description`,`status`) values (1,1,'rem = 3.14 % 2.1;','No'),(2,1,'rem = modf(3.14, 2.1);','No'),(3,1,'rem = fmod(3.14, 2.1);','Yes'),(4,1,'Remainder cannot be obtain in floating point divis','No'),(5,2,'Internal and External','No'),(6,2,'External, Internal and None','Yes'),(7,2,'External and None','No'),(8,2,'Internal','No'),(9,3,'* (asterisk)','No'),(10,3,'| (pipeline)','No'),(11,3,'- (hyphen)','No'),(12,3,'_ (underscore)','Yes'),(13,4,'Data structure for representing arrays of records','No'),(14,4,'Data structure that compactly stores bits','Yes'),(15,4,'An array in which most of the elements have the sa','No'),(16,4,'Array in which elements are not present in continu','No'),(17,5,'OR','No'),(18,5,'AND','Yes'),(19,5,'XOR','No'),(20,5,'NAND','No'),(21,6,'Abstraction','No'),(22,6,'Encapsulation','Yes'),(23,6,'Polymorphism','No'),(24,6,'Modularity','No'),(25,7,'good','No'),(26,7,'bad','Yes'),(27,7,'perfect','No'),(28,8,'good','No'),(29,8,'bad','No'),(30,8,'good','No'),(31,8,'perfect','Yes'),(32,9,'do','Yes'),(33,9,'die','No'),(34,10,'All are same','No'),(35,10,'differece in working.','Yes'),(36,10,'assignment and  conditonal ','No'),(37,11,'yes','Yes'),(38,11,'no','No'),(39,12,'o','No'),(40,12,'s','Yes');

/*Table structure for table `faculty` */

DROP TABLE IF EXISTS `faculty`;

CREATE TABLE `faculty` (
  `faculty_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `qualification` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`faculty_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `faculty` */

insert  into `faculty`(`faculty_id`,`login_id`,`subject_id`,`first_name`,`last_name`,`phone`,`email`,`qualification`) values (2,7,2,'manuu','ka','7766443528','anu@gmail.com','mca');

/*Table structure for table `knowledgeareas` */

DROP TABLE IF EXISTS `knowledgeareas`;

CREATE TABLE `knowledgeareas` (
  `knowledge_area_id` int(11) NOT NULL AUTO_INCREMENT,
  `knowledge_area_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`knowledge_area_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `knowledgeareas` */

insert  into `knowledgeareas`(`knowledge_area_id`,`knowledge_area_name`,`description`) values (1,'Cyber ','i like it'),(2,'Protocols','Some logic'),(3,'program','competetive coding\r\n');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(25) DEFAULT NULL,
  `password` varchar(25) DEFAULT NULL,
  `user_type` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values (1,'admin','admin','admin'),(2,'anu','anu123','user'),(7,'manu','manu123','faculty'),(12,'abc','abc123','students');

/*Table structure for table `notes` */

DROP TABLE IF EXISTS `notes`;

CREATE TABLE `notes` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `faculty_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `title` varchar(30) DEFAULT NULL,
  `description` varchar(35) DEFAULT NULL,
  `note_date` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`note_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notes` */

insert  into `notes`(`note_id`,`faculty_id`,`course_id`,`title`,`description`,`note_date`) values (1,2,5,'data sciences','data science and bigdata','2022-08-24');

/*Table structure for table `perfomance` */

DROP TABLE IF EXISTS `perfomance`;

CREATE TABLE `perfomance` (
  `perfomance_id` int(11) NOT NULL AUTO_INCREMENT,
  `knowledge_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `perfomance` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`perfomance_id`)
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;

/*Data for the table `perfomance` */

insert  into `perfomance`(`perfomance_id`,`knowledge_id`,`student_id`,`perfomance`) values (64,1,1,'0'),(63,3,1,'1'),(62,1,1,'1'),(61,1,1,'0'),(60,1,1,'0'),(59,1,1,'1'),(58,1,1,'0');

/*Table structure for table `quiz_master` */

DROP TABLE IF EXISTS `quiz_master`;

CREATE TABLE `quiz_master` (
  `quiz_id` int(11) NOT NULL AUTO_INCREMENT,
  `faculty_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `title` varchar(35) DEFAULT NULL,
  `quiz_date` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`quiz_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `quiz_master` */

/*Table structure for table `quiz_options` */

DROP TABLE IF EXISTS `quiz_options`;

CREATE TABLE `quiz_options` (
  `option_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `option_description` varchar(50) DEFAULT NULL,
  `correct_answer` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`option_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `quiz_options` */

/*Table structure for table `quiz_questions` */

DROP TABLE IF EXISTS `quiz_questions`;

CREATE TABLE `quiz_questions` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `quiz_id` int(11) DEFAULT NULL,
  `question` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `quiz_questions` */

/*Table structure for table `student_answer` */

DROP TABLE IF EXISTS `student_answer`;

CREATE TABLE `student_answer` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `option_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`answer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `student_answer` */

/*Table structure for table `students` */

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `gender` varchar(25) DEFAULT NULL,
  `dob` varchar(30) DEFAULT NULL,
  `house_name` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `pincode` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `students` */

insert  into `students`(`student_id`,`login_id`,`first_name`,`last_name`,`course_id`,`phone`,`email`,`gender`,`dob`,`house_name`,`place`,`pincode`) values (1,12,'abc','df',6,'346578721','abc@gmail.com','FEMALE','2022-08-29','qwfe','dgbf','45621');

/*Table structure for table `studentssubmissions` */

DROP TABLE IF EXISTS `studentssubmissions`;

CREATE TABLE `studentssubmissions` (
  `submission_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `exercise_id` int(11) DEFAULT NULL,
  `answered_option_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`submission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `studentssubmissions` */

insert  into `studentssubmissions`(`submission_id`,`student_id`,`exercise_id`,`answered_option_id`) values (12,1,9,32),(11,1,7,26),(10,1,2,5),(9,1,6,23),(8,1,3,10),(7,1,1,1),(13,1,10,35),(14,1,11,37);

/*Table structure for table `subjects` */

DROP TABLE IF EXISTS `subjects`;

CREATE TABLE `subjects` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `subject_name` varchar(30) DEFAULT NULL,
  `subject_description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `subjects` */

insert  into `subjects`(`subject_id`,`course_id`,`subject_name`,`subject_description`) values (2,5,'erp','enterprise'),(3,5,'eee','sadf'),(10,6,'astology','good for u'),(11,7,'OOAD','algoritham based\r\n');

/*Table structure for table `submissions` */

DROP TABLE IF EXISTS `submissions`;

CREATE TABLE `submissions` (
  `submission_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `assignment_id` int(11) DEFAULT NULL,
  `file_path` varchar(500) DEFAULT NULL,
  `faculty_note` varchar(50) DEFAULT NULL,
  `mark_awarded` varchar(30) DEFAULT NULL,
  `submission_date` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`submission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `submissions` */

insert  into `submissions`(`submission_id`,`student_id`,`assignment_id`,`file_path`,`faculty_note`,`mark_awarded`,`submission_date`) values (1,5,4,'static/cb55bda9-b981-411d-82f9-7c8ec5b7c571tour image.jpg','good','50','2022-09-16'),(2,1,4,'static/04fcf2d0-6661-4d6e-9edc-4b2f44cfc6e7edicted.png','pending','pending','2022-10-12');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
