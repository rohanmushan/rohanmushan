#SQL - Structured Query Language
#SQL is language used for query or get data out of database 

CREATE DATABASE Challenge;
use Challenge;
DROP database Challenge;

CREATE TABLE Day1(
	FName VARCHAR(15) NOT NULL,
    LName VARCHAR(15) NOT NULL,
    Age INT NOT NULL,
    Branch VARCHAR(20) NOT NULL,
    Mobile_no BIGINT PRIMARY KEY,
    EMail VARCHAR(35) NOT NULL,
    City VARCHAR(15)
);

INSERT INTO DAY1 VALUES ("Rohan", "Mushan", 20, "AI&DS", 123456789, "rohan@gmail.com", "Solapur");
INSERT INTO DAY1 VALUES ("Mahendra", "Topul", 20, "ENTC", 321654987, "mahi@gmail.com", "Silicon Valley");
INSERT INTO DAY1 VALUES ("Tanmay", "Naik", 20, "IT", 123479789, "tanny@gmail.com", "Pune");
INSERT INTO DAY1 VALUES ("Abhay", "Potabatti", 20, "CSE", 1234556789, "abhi@gmail.com", "Mumbai");
INSERT INTO DAY1 VALUES ("Akash", "Gajul", 20, "CSE", 123786789, "akash@gmail.com", "Solapur");
INSERT INTO DAY1 VALUES ("Girish", "Kanki", 20, "CSE", 141456789, "girish@gmail.com", "Hyderabad");


SELECT * FROM DAY1;
SELECT COUNT(Branch) from DAY1 where Branch = "CSE";
SELECT distinct(Branch) from DAY1 where City = "Solapur";
SELECT * FROM DAY1 LIMIT 3;