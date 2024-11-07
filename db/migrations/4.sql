CREATE OR REPLACE TABLE sieges (
    numero int NOT NULL,
    section VARCHAR(255) NOT NULL,
    prixBase FLOAT
);

INSERT INTO sieges VALUES (1,'A',10);
INSERT INTO sieges VALUES (2,'B',10.1);
INSERT INTO sieges VALUES (3,'C', 13);