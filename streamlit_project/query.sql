CREATE TABLE IF NOT EXISTS USER (
    empID VARCHAR(50) NOT NULL, 
    emp_name varchar(250) NOT NULL, 
    emp_password INT(11) NOT NULL, 
    PRIMARY KEY (empID)
);

CREATE TABLE IF NOT EXISTS DOCUMENTS (
    docID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    doc MEDIUMBLOB NOT NULL,
    doc_type VARCHAR(20) NOT NULL,
    volume VARCHAR(10),
    title_of_doc VARCHAR(255) NOT NULL,
    authors VARCHAR(255) NOT NULL,
    publisher VARCHAR(255),
    date_of_publication VARCHAR(20),
    keyword VARCHAR(255)
);