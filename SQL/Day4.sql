CREATE DATABASE Challenge;
USE Challenge;
DROP DATABASE Challenge;
DROP TABLE DAY4;

CREATE TABLE DAY4 (
	FName VARCHAR(15) NOT NULL,
    LName VARCHAR(15) NOT NULL, 
	Age INT NOT NULL,
    Gender CHAR(5) NOT NULL, 
	Mobile_no BIGINT PRIMARY KEY,
    EMail VARCHAR(35) NOT NULL,
    City VARCHAR(15), 
    Salary INT NOT NULL
);

INSERT INTO DAY4 VALUES ("Rohan", "Mushan", 21, "M", 1234567890, "rohan@gmail.com","Solapur", 33000),
						("Mahendra", "Topul", 21, "M", 4534564290, "mahi@gmail.com","Banglore", 45000),
                        ("Atipra", "Sonawane", 20, "F", 1234512590, "atipra@gmail.com","Solapur", 40000),
                        ("Tanmay", "Naik", 21, "M", 9134575890, "tanny@gmail.com","Lonavala", 41000),
                        ("Girish", "Kanki", 21, "M", 1123567890, "girish@gmail.com","Solapur", 40000),
                        ("Girija", "Billa", 20, "F", 8934567890, "girija@gmail.com","Hyderabad", 30000),
                        ("Abhay", "Potabatti", 21, "M", 9334567890, "abhi@gmail.com","Mumbai", 39000),
                        ("Akash", "Gajul", 21, "M", 8534567890, "akash@gmail.com","Solapur", 33000),
                        ("Akanksha", "Potabatti", 19, "F", 9934567890, "abhi@gmail.com","Mumbai", 30000);
                        
SELECT * FROM DAY4;
-- SELECT FName FROM DAY4 WHERE FName = "A%";
-- SELECT FName, City FROM DAY4 WHERE City ='Mumbai' or 'Solapur';
SELECT FName, Salary FROM DAY4 WHERE Salary BETWEEN 33000 AND 40000;

SELECT FName FROM DAY4 ORDER BY FName;
SELECT FName FROM DAY4 ORDER BY FName DESC; #ASC