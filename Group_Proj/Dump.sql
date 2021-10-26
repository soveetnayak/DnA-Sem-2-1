/*
~Books
~Magazine
~Members
~Staff
Issued
~Storage 
Details
~Author
~Publishers
~Multi_Authors
Multi_lingual
~Genre
~Multi_Genres
~Contact_number_Members
~Contact_number_Staff
Book_issued
*/

CREATE DATABASE /*!32312 IF NOT EXISTS*/ Library /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION=N */;

USE Library;



DROP TABLE IF EXISTS Books;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE Books (
  Book_id INT NOT NULL AUTO_INCREMENT,
  Book_Name VARCHAR(255) NOT NULL CHECK (length(Book_Name) > 0),
  Edition INT CHECK (Edition > 0),   
  ISBN_value BIGINT NOT NULL CHECK (ISBN_value > 0),
  Price INT NOT NULL CHECK (Price > 0),
  Publisher_id INT NOT NULL CHECK (Publisher_id > 0),
  Status VARCHAR(255) NOT NULL  /*CHECK (Status IN (Available, Borrowed))*/, PRIMARY KEY (Book_id))
  ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS Members;
CREATE TABLE Members (
  Member_id INT NOT NULL AUTO_INCREMENT, 
  Government_id INT NOT NULL CHECK (Government_id > 0),
  First_Name VARCHAR(255) NOT NULL ,  
  Last_Name VARCHAR(255) NOT NULL , 
  Date_of_birth  DATE ,
  Age INT NOT NULL CHECK(Age > 0),
  House_no VARCHAR(255), 
  Locality VARCHAR(255) ,
  City VARCHAR(255), 
  Pin_Code INT NOT NULL CONSTRAINT C_Pin_Code CHECK (Pin_Code > 0),
  Date_of_joining DATE , 
  Membership_expiration DATE ,  
  PRIMARY KEY(Member_id)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci; 


DROP TABLE IF EXISTS Staff;
CREATE TABLE Staff (
  Staff_id INT NOT NULL AUTO_INCREMENT CONSTRAINT Member_id CHECK (Member_id > 0), 
  Government_id INT NOT NULL CONSTRAINT Government_id CHECK (Government_id > 0),
  First_Name VARCHAR(255) NOT NULL ,  
  Last_Name VARCHAR(255) NOT NULL , 
  Date_of_birth  DATE CONSTRAINT Date_of_birth CHECK (Date_of_birth > 1900-01-01),
  Age INT CHECK(Age > 0),
  House_no VARCHAR(255), 
  Locality VARCHAR(255) ,
  City VARCHAR(255), 
  Pin_Code INT NOT NULL CONSTRAINT Pin_Code CHECK (Pin_Code > 0),, 
  Designation VARCHAR(255),
  Duty VARCHAR(255),
  Type VARCHAR(255),  
  PRIMARY KEY(Member_id)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci; 


DROP TABLE IF EXISTS Magazine;
CREATE TABLE Magazine ( 
  Magazine_id INT NOT NULL, 
  Magazine_Name VARCHAR(255),
  Volume_no INT NOT NULL, 
  Issue_no INT NOT NULL, 
  Publisher_id INT NOT NULL, 
  PRIMARY KEY(Magazine_id));

DROP TABLE IF EXISTS Multi_Authors;
CREATE TABLE Multi_Authors ( 
    Author_id INT NOT NULL CHECK (Author_id > 0), 
    Book_id INT NOT NULL CHECK (Book_id > 0),  
    PRIMARY KEY (Author_id, Book_id))
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS Issued;
CREATE TABLE Issued(
  Book_id INT NOT NULL CHECK (Book_id > 0), 
  Member_id INT NOT NULL CHECK (Member_id > 0), 
  Date_of_issue  DATE CHECK (Date_of_issue > 1900-01-01), 
  Due_date  DATE CHECK (Due_date > 1900-01-01), 
  Fine INT CHECK (Fine > 0), 
  Submission_date DATE CHECK (Submission_date > 1900-01-01),
  PRIMARY KEY(Book_id, Member_id, Date_of_issue));

DROP TABLE IF EXISTS Storage;
CREATE TABLE Storage (
  Book_id INT NOT NULL CHECK (Book_id > 0), 
  Shelf_Number INT NOT NULL CHECK (Shelf_Number > 0), 
  Rack_Number INT NOT NULL,
  PRIMARY KEY (Book_id));

DROP TABLE IF EXISTS Details;
CREATE TABLE Details ( 
  Book_id INT NOT NULL, 
  Author_id INT NOT NULL, 
  Genre_id INT NOT NULL, 
  Publisher_id INT NOT NULL, 
  PRIMARY KEY(Book_id, Author_id , Genre_id));

  
DROP TABLE IF EXISTS Multi_lingual;
CREATE TABLE Multi_lingual ( 
    Author_id INT NOT NULL CHECK (Author_id > 0),
    Language  Varchar(255), 
    PRIMARY KEY (Author_id,Language))
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS Multi_Genres;
CREATE TABLE Multi_Genres ( 
    Genre_id  INT NOT NULL CHECK(Genre_id > 0),
    Book_id INT NOT NULL CHECK (Book_id > 0), 
    PRIMARY KEY (Genre_id,Book_id))
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS Genre;
CREATE TABLE Genre ( 
    Genre_id INT NOT NULL CHECK (Genre_id > 0),
    Genre_name  VARCHAR(255),
    PRIMARY KEY (Genre_id))
    ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DROP TABLE IF EXISTS Author;
CREATE TABLE Author (
  Author_id INT NOT NULL AUTO_INCREMENT CONSTRAINT Author_id CHECK (Member_id > 0), 
  First_Name VARCHAR(255) NOT NULL ,  
  Last_Name VARCHAR(255) NOT NULL , 
  PRIMARY KEY(Author_id));

DROP TABLE IF EXISTS Contact_number_Staff;
CREATE TABLE Contact_number_Staff(
  Staff_id INT NOT NULL,
  Mobile_No BIGINT NOT NULL,
    PRIMARY KEY(Staff_id, Mobile_No)
);

DROP TABLE IF EXISTS Contact_number_Members;
CREATE TABLE Contact_number_Members(
  Member_id INT NOT NULL ,
  Mobile_No BIGINT NOT NULL,
  PRIMARY KEY(Member_id, Mobile_No)
);

DROP TABLE IF EXISTS Publishers;
CREATE TABLE Publishers (
  Publisher_id INT NOT NULL AUTO_INCREMENT CONSTRAINT Publisher_id CHECK (Member_id > 0), 
  Publisher_Name VARCHAR(255) NOT NULL ,  
  PRIMARY KEY(Publisher_id));

DROP TABLE IF EXISTS Book_issued;
CREATE TABLE Book_issued (
  Book_id INT NOT NULL , 
  Member_id INT NOT NULL , 
  Date_of_issue DATE ,
  PRIMARY KEY(Date_of_issue));