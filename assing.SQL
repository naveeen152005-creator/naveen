create database newDB1;

CREATE TABLE Student11 (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    Course VARCHAR(50),
    Fees DECIMAL(10,2),
    City VARCHAR(50)
);

INSERT INTO Student11 VALUES
(1,'Akhil',20,'Male','Data Analytics',25000,'Calicut'),
(2,'Anu',21,'Female','Python',22000,'Kochi'),
(3,'Rahul',22,'Male','SQL',20000,'Trivandrum'),
(4,'Meera',20,'Female','Data Science',30000,'Kannur'),
(5,'Neha',23,'Female','Python',24000,'Calicut'),
(6,'Arun',21,'Male','SQL',21000,'Kochi'),
(7,'Sneha',22,'Female','Data Analytics',26000,'Malappuram'),
(8,'Vishnu',24,'Male','Power BI',28000,'Thrissur'),
(9,'Fathima',20,'Female','Excel',18000,'Kasaragod'),
(10,'Jithin',23,'Male','Power BI',29000,'Palakkad');

CREATE TABLE Employees11 (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(50),
    Department VARCHAR(30),
    Salary DECIMAL(10,2),
    Age INT,
    City VARCHAR(50),
    Experience INT
);

INSERT INTO Employees11 VALUES
(1,'Akhil','IT',45000,28,'Kochi',3),
(2,'Anu','HR',30000,25,'Calicut',2),
(3,'Rahul','Finance',40000,32,'Trivandrum',6),
(4,'Meera','IT',55000,30,'Kochi',5),
(5,'Neha','Sales',24000,24,'Kannur',1),
(6,'Arun','HR',27000,29,'Calicut',4),
(7,'Sneha','Finance',35000,27,'Kochi',3),
(8,'Vishnu','IT',38000,35,'Trivandrum',8),
(9,'Fathima','Marketing',22000,23,'Malappuram',2),
(10,'Jithin','Sales',32000,31,'Palakkad',7);

SELECT EmployeeName, Salary + 5000 AS BonusSalary FROM Employees11;

SELECT EmployeeName, Salary - 2000 AS DeductSalary FROM Employees11;

SELECT EmployeeName, Salary * 12 AS AnnualSalary FROM Employees11;

SELECT EmployeeName, (Salary * 1.10) / 12 AS MonthlySalary FROM Employees11;

SELECT EmployeeName, Salary * 1.15 AS IncreasedSalary FROM Employees11;

SELECT * FROM Employees11 WHERE Salary > 30000;

SELECT * FROM Employees11 WHERE Salary < 25000;

SELECT * FROM Employees WHERE Salary = 40000;

SELECT * FROM Employees11 WHERE Age >= 30;

SELECT * FROM Employees11 WHERE Age <= 25;

SELECT * FROM Employees11 WHERE Experience <> 2;



SELECT * FROM Employees11
WHERE Salary > 30000 AND Experience > 2;

SELECT * FROM Employees11
WHERE Department = 'IT' AND Salary > 35000;

SELECT * FROM Employees11
WHERE City = 'Kochi' OR City = 'Trivandrum';

SELECT * FROM Employees11
WHERE Age > 25 AND Salary < 40000;

SELECT * FROM Employees11
WHERE Department = 'HR' OR Experience > 5;

SELECT * FROM Employees11
WHERE Salary > 25000 AND City <> 'Kochi';



SELECT * FROM Employees11
WHERE Salary BETWEEN 25000 AND 50000;

SELECT * FROM Employees11
WHERE Age BETWEEN 25 AND 35;

SELECT * FROM Employees11
WHERE Experience BETWEEN 2 AND 5;

SELECT * FROM Employees11
WHERE Department IN ('IT','HR','Finance');

SELECT * FROM Employees11
WHERE City IN ('Kochi','Calicut','Trivandrum');

SELECT * FROM Employees11
WHERE Department NOT IN ('HR','Finance');