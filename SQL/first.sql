CREATE TABLE loan(
   dept_name VARCHAR(20),
   loan_number INT,
   amount INT,
   PRIMARY KEY(loan_number),
   FOREIGN KEY (dept_name) REFERENCES department
);