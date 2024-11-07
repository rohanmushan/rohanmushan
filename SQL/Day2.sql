CREATE DATABASE Challenge;
use Challenge;
DROP database Challenge;

CREATE TABLE DAY2(
	Name VARCHAR(15) NOT NULL,
    Age INT NOT NULL,
    Branch VARCHAR(20) NOT NULL,
    Mobile_no BIGINT PRIMARY KEY,
    EMail VARCHAR(35) NOT NULL,
    City VARCHAR(15)
);

INSERT INTO DAY2 VALUES ("Rohan Mushan", 20, "AI&DS", 123456789, "rohan@gmail.com", "Solapur"),
						("Mahendra Topul", 20, "ENTC", 321654987, "mahi@gmail.com", "Silicon Valley"),
						("Tanmay Naik", 20, "IT", 123479789, "tanny@gmail.com", "Pune"),
						("Abhay Potabatti", 20, "CSE", 1234556789, "abhi@gmail.com", "Mumbai"),
						("Akash Gajul", 20, "CSE", 123786789, "akash@gmail.com", "Solapur"),
						("Girish Kanki", 20, "CSE", 141456789, "girish@gmail.com", "Hyderabad");


SELECT * FROM DAY2;
SELECT Branch,FName,LName FROM DAY2 WHERE Branch="CSE";
SELECT SUM(Mobile_no) FROM DAY2;
SELECT AVG(Mobile_no) FROM DAY2;
SELECT AVG(Mobile_no) as Average FROM DAY2;
SELECT STD(Mobile_no) as Standard_Deviation FROM DAY2;
UPDATE DAY2 SET Name = "Mushan Rohan" WHERE Name = "Rohan Mushan";
DELETE FROM DAY2 WHERE Name = "Mushan Rohan";