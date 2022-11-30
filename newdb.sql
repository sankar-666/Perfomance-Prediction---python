/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - onlineexam
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`onlineexam` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `onlineexam`;

/*Table structure for table `answers` */

DROP TABLE IF EXISTS `answers`;

CREATE TABLE `answers` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `qstn_id` int(11) DEFAULT NULL,
  `stud_id` int(11) DEFAULT NULL,
  `qstnansr_id` int(11) DEFAULT NULL,
  `mark_awd` int(11) DEFAULT NULL,
  PRIMARY KEY (`answer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `answers` */

insert  into `answers`(`answer_id`,`qstn_id`,`stud_id`,`qstnansr_id`,`mark_awd`) values (1,6,1,19,0),(2,2,1,6,0),(3,5,1,16,0),(4,1,1,1,0),(5,3,1,8,0),(6,4,1,11,0),(7,1,2,1,0),(8,5,2,17,0),(9,3,2,9,0),(10,4,2,10,0),(11,2,2,7,0),(12,6,2,18,0),(13,4,3,11,0),(14,5,3,15,0),(15,3,3,8,0),(16,4,4,10,0),(17,2,4,7,0);

/*Table structure for table `assignments` */

DROP TABLE IF EXISTS `assignments`;

CREATE TABLE `assignments` (
  `assignment_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `crse_id` int(11) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `maximum_mark` varchar(50) DEFAULT NULL,
  `assignment_date` varchar(50) DEFAULT NULL,
  `final_date_submission` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`assignment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `assignments` */

insert  into `assignments`(`assignment_id`,`teacher_id`,`crse_id`,`title`,`description`,`maximum_mark`,`assignment_date`,`final_date_submission`) values (2,1,2,'dasd','dsadsa','2324','2022-11-05','2022-10-09');

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `crse_id` int(11) NOT NULL AUTO_INCREMENT,
  `crse_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`crse_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`crse_id`,`crse_name`) values (1,'mtchh'),(2,'MBA'),(3,'software developer');

/*Table structure for table `doubts` */

DROP TABLE IF EXISTS `doubts`;

CREATE TABLE `doubts` (
  `doubt_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `note_id` int(11) DEFAULT NULL,
  `dout_description` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `doubt_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`doubt_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `doubts` */

insert  into `doubts`(`doubt_id`,`student_id`,`note_id`,`dout_description`,`reply`,`doubt_date`) values (1,2,2,'dsadsadsa','hello','dsadsa'),(2,2,2,'Care with Beauty is here ','pending','2022-10-11');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `Exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `Exam_Title` varchar(50) DEFAULT NULL,
  `Exam_Details` varchar(50) DEFAULT NULL,
  `Subject_id` int(11) DEFAULT NULL,
  `Teacher_id` int(11) DEFAULT NULL,
  `Exam_Date` varchar(50) DEFAULT NULL,
  `Exam_Status` varchar(50) DEFAULT NULL,
  `Time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

insert  into `exam`(`Exam_id`,`Exam_Title`,`Exam_Details`,`Subject_id`,`Teacher_id`,`Exam_Date`,`Exam_Status`,`Time`) values (1,'C Programming','Attend all question',1,1,'2020-01-10','In Work','30min');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Login_ID` int(11) NOT NULL AUTO_INCREMENT,
  `User_Name` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `User_Type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Login_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Login_ID`,`User_Name`,`Password`,`User_Type`) values (1,'admin','admin','admin'),(2,'anu','anu123','teacher'),(3,'neethu','neethu123','teacher'),(4,'gayathri','gayathri123','teacher'),(5,'anitta','anitta123','teacher'),(6,'amitha','amitha123','student'),(7,'remya','remya123','student'),(8,'juby','juby123','student'),(9,'changel','changel123','student');

/*Table structure for table `notes` */

DROP TABLE IF EXISTS `notes`;

CREATE TABLE `notes` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `crse_id` int(11) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `note_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`note_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notes` */

insert  into `notes`(`note_id`,`teacher_id`,`crse_id`,`title`,`description`,`note_date`) values (2,1,3,'dasdsa','dssadsa','2022-09-22');

/*Table structure for table `participation` */

DROP TABLE IF EXISTS `participation`;

CREATE TABLE `participation` (
  `part_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `Student_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`part_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `participation` */

/*Table structure for table `qstnanswer` */

DROP TABLE IF EXISTS `qstnanswer`;

CREATE TABLE `qstnanswer` (
  `qstnansr_id` int(11) NOT NULL AUTO_INCREMENT,
  `qstn_id` int(11) DEFAULT NULL,
  `option` varchar(500) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`qstnansr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `qstnanswer` */

insert  into `qstnanswer`(`qstnansr_id`,`qstn_id`,`option`,`status`) values (1,1,'Lowercase letter','Yes'),(2,1,'Uppercase letter','No'),(3,1,'Camelcase letter','No'),(4,1,'None of these','No'),(5,2,'int number;','No'),(6,2,'float rate;','No'),(7,2,'int $main;','Yes'),(8,3,'Dennis Ritchie','Yes'),(9,3,'Antony Thomas','No'),(10,4,'1966','No'),(11,4,'1972','Yes'),(12,4,'1971','No'),(13,4,'1980','No'),(14,4,'1973','No'),(15,5,'short long','No'),(16,5,'short int','Yes'),(17,5,'short float','No'),(18,6,'!','No'),(19,6,'&&','Yes'),(20,6,'&','No');

/*Table structure for table `questions` */

DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `qstn_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `teach_id` int(11) DEFAULT NULL,
  `sub_id` int(11) DEFAULT NULL,
  `question` varchar(500) DEFAULT NULL,
  `max_mark` int(11) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`qstn_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `questions` */

insert  into `questions`(`qstn_id`,`exam_id`,`teach_id`,`sub_id`,`question`,`max_mark`,`description`) values (1,1,1,1,'All keywords in C are in',1,'attend all questions'),(2,1,1,1,'Which of the following is not a valid C variable name',1,'attend all questions'),(3,1,1,1,'Who designed C programming languge',1,'attend all questions'),(4,1,1,1,'When does C language first appeared',1,'attend all questions'),(5,1,1,1,'The type name/reserved word short is',1,'attend all questions'),(6,1,1,1,'Which of the following is a logical AND operator',1,'attend all questions');

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `Student_id` int(11) DEFAULT NULL,
  `Total_Mark` int(11) DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`result_id`,`exam_id`,`Student_id`,`Total_Mark`) values (1,1,1,5),(2,1,2,2),(3,1,3,2),(4,1,4,0);

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `Student_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_ID` int(11) DEFAULT NULL,
  `First_Name` varchar(50) DEFAULT NULL,
  `Last_Name` varchar(50) DEFAULT NULL,
  `DOB` varchar(50) DEFAULT NULL,
  `Phone` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `House_Name` varchar(50) DEFAULT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Pincode` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`Student_id`,`Login_ID`,`First_Name`,`Last_Name`,`DOB`,`Phone`,`Email`,`House_Name`,`Place`,`Pincode`) values (1,6,'Amitha','AJ','1999-07-31','7418529633','amitha@gmail.com','Amitha villa','Thopumpaddy','682006'),(2,7,'Remya','Krishnan','1998-01-11','9874563210','remya@gmail.com','Remya Villa','Edapally','682005'),(3,8,'Juby','P','1999-08-13','7896541200','juby@gmail.com','Juby Villa','Chellanam','682001'),(4,9,'Changel','Bonnie','1999-10-13','9120210120','changel@gmail.com','Changel Villa','Edapally','682007');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `Subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `Subject_Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`Subject_id`,`Subject_Name`) values (1,'C'),(2,'C++'),(3,'Java'),(4,'Operating System'),(5,'BlockChain');

/*Table structure for table `submissions` */

DROP TABLE IF EXISTS `submissions`;

CREATE TABLE `submissions` (
  `submission_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `assignment_id` int(11) DEFAULT NULL,
  `file_path` varchar(1000) DEFAULT NULL,
  `teacher_note` varchar(50) DEFAULT NULL,
  `mark_awarded` varchar(50) DEFAULT NULL,
  `submission_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`submission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `submissions` */

insert  into `submissions`(`submission_id`,`student_id`,`assignment_id`,`file_path`,`teacher_note`,`mark_awarded`,`submission_date`) values (1,2,2,'sdsadsa','oddd','-000','infinity'),(2,2,2,'static/4e388173-176f-424f-b73a-57ecc562cb6enetflix.jpg','pending','pending','2022-10-11'),(3,2,2,'static/c57fbf5a-8168-4cce-a63b-7e412e257aa4edicted.png','pending','pending','2022-10-11');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `Teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_ID` int(11) DEFAULT NULL,
  `Subject_id` int(11) DEFAULT NULL,
  `First_Name` varchar(50) DEFAULT NULL,
  `Last_Name` varchar(50) DEFAULT NULL,
  `Qualification` varchar(50) DEFAULT NULL,
  `Phone` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Joined_Date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `teacher` */

insert  into `teacher`(`Teacher_id`,`Login_ID`,`Subject_id`,`First_Name`,`Last_Name`,`Qualification`,`Phone`,`Email`,`Joined_Date`) values (1,2,1,'Anu','Varghese','Msc.CA','7854210258','anu@gmail.com','2019-04-13'),(2,3,2,'Neethu','Thomas','Msc.CA,MBA','9754213548','neethu@gmail.com','2020-01-01'),(3,4,3,'Gayathri','Menon','Phd','7854210258','gayathri@gmail.com','2019-08-24'),(4,5,4,'Anitta','joy','Msc.CA,MBA','7845785421','anitta@gmail.com','2020-01-12');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
