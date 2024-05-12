-- TB_CLIENTS
CREATE TABLE TB_CLIENTS (
    CD_ID INT PRIMARY KEY IDENTITY(1,1),
    DC_FULLNAME VARCHAR(100),
    DT_BIRTHDATE DATE,
    DC_DOCUMENT VARCHAR(14) UNIQUE,
    DC_MAIL VARCHAR(50) UNIQUE,
    DC_PHONE VARCHAR(12)
);

-- TB_DESTINY
CREATE TABLE TB_DESTINY (
    CD_ID INT IDENTITY(1,1) PRIMARY KEY,
    DC_COUNTRY VARCHAR(50),
    DC_CITY VARCHAR(50)
);

-- TB_PACKAGE
CREATE TABLE TB_PACKAGE (
    CD_ID INT IDENTITY(1,1) PRIMARY KEY, 
    ID_DESTINY INT NOT NULL, 
    VL_VALUE DECIMAL(10, 2) NOT NULL, 
    DC_DESCRIPTION TEXT, 
    NR_AMOUNT INT,
    DT_START_DATE DATE,
    DT_END_DATE DATE,
    FOREIGN KEY (ID_DESTINY) REFERENCES TB_DESTINY(CD_ID)
);

-- TB_SALES
CREATE TABLE TB_SALES ( 
    DC_ID INT IDENTITY(1,1) PRIMARY KEY,
    DC_FULLNAME VARCHAR(255), 
    DT_BIRTHDATE DATE, 
    DC_SEX CHAR(1), 
    DC_DOCUMENT VARCHAR(20), 
    DC_EMAIL VARCHAR(255), 
    DC_PHONE VARCHAR(20), 
    NR_NUMCHILDS INT, 
    DC_CIVILSTATE VARCHAR(50), 
    VL_MONTHLYEARNINGS DECIMAL(10, 2),
    DT_SALETIME DATETIME,
    ID_PACKAGE INT NOT NULL,
    FOREIGN KEY (ID_PACKAGE) REFERENCES TB_PACKAGE(CD_ID)
);

 --Inserir destinos
INSERT INTO tb_destiny (DC_COUNTRY, DC_CITY) VALUES ('Brasil', 'Rio de Janeiro'), 
('Estados Unidos', 'Nova Iorque'), ('França', 'Paris'), ('Reino Unido', 'Londres'), 
('Itália','Roma'),('Espanha', 'Barcelona'), ('Austrália', 'Sydney'), ('Alemanha', 'Berlim'), 
('Canadá', 'Toronto'), ('Japão', 'Tóquio'), ('Portugal', 'Lisboa'), ('Inglaterra', 'Londres'), 
('Canadá', 'Vancouver'), ('Egito', 'Cairo'), ('Austrália', 'Melbourne'), ('Espanha', 'Madri'), 
('Estados Unidos', 'Los Angeles'), ('França', 'Nice'), ('Japão', 'Osaka'), ('Índia', 'Delhi'), 
('Alemanha', 'Hamburgo'), ('Brasil', 'São Paulo'),('México', 'Cidade do México'), 
('Índia', 'Mumbai'), ('África do Sul', 'Cidade do Cabo'), ('Argentina', 'Buenos Aires'),
('Suécia', 'Estocolmo'), ('China', 'Pequim');


 --Inserir pacotes
INSERT INTO tb_package (id_DESTINY, VL_VALUE, DC_DESCRIPTION, NR_AMOUNT, DT_START_DATE, DT_END_DATE) 
VALUES (1, 500.00, 'Pacote de férias para praia', 20, '2023-11-01', '2023-11-15'), 
(2, 800.00, 'Pacote de aventura nas montanhas', 15, '2023-10-20', '2023-10-30'), 
(3, 350.00, 'Pacote cultural na cidade', 30, '2023-12-05', '2023-12-20'), 
(4, 700.00, 'Pacote de esportes aquáticos', 25, '2023-11-15', '2023-11-30'), 
(5, 900.00, 'Pacote de lua de mel', 10, '2023-10-25', '2023-11-05'), 
(6, 600.00, 'Pacote de relaxamento na floresta', 18, '2023-11-10', '2023-11-28'), 
(7, 450.00, 'Pacote gastronômico na cidade', 12, '2023-12-15', '2023-12-30'), 
(8, 550.00, 'Pacote de ecoturismo', 22, '2023-10-15', '2023-10-25'), 
(9, 750.00, 'Pacote de esqui nas montanhas', 16, '2023-12-01', '2023-12-15'), 
(10, 400.00, 'Pacote de turismo histórico', 28, '2023-11-05', '2023-11-20');


 --Inserindo valores de vendas
INSERT INTO tb_sales (DC_FULLNAME, DT_BIRTHDATE, DC_SEX, DC_DOCUMENT, DC_EMAIL, DC_PHONE, NR_NUMCHILDS, DC_CIVILSTATE, VL_MONTHLYEARNINGS, DT_SALETIME, id_PACKAGE) VALUES
('João Silva', '1980-05-15', 'M', '123456789', 'joao@example.com', '+1 (555) 123-4567', 2, 'Casado', 5000.00, '2023-10-10 14:30:00', 2), 
('Maria Souza', '1992-08-20', 'F', '987654321', 'maria@example.com', '+1 (555) 987-6543', 1, 'Solteira', 4500.00, '2023-10-11 15:15:00', 4), 
('Pedro Santos', '1975-03-03', 'M', '345678901', 'pedro@example.com', '+1 (555) 345-6789', 3, 'Casado', 6000.00, '2023-10-12 16:45:00', 1), 
('Ana Pereira', '1988-11-25', 'F', '876543210', 'ana@example.com', '+1 (555) 876-5432', 2, 'Casada', 5500.00, '2023-10-13 14:00:00', 6), 
('Luiz Oliveira', '1995-06-30', 'M', '234567890', 'luiz@example.com', '+1 (555) 234-5678', 0, 'Solteiro', 4800.00, '2023-10-14 17:30:00', 7),
('Carlos Santos', '1984-07-12', 'M', '987123456', 'carlos@example.com', '+1 (555) 987-1234', 1, 'Solteiro', 4200.00, '2023-10-15 10:45:00', 8), 
('Fernanda Lima', '1990-01-30', 'F', '654987321', 'fernanda@example.com', '+1 (555) 654-9873', 2, 'Casada', 5200.00, '2023-10-16 12:30:00', 5), 
('Ricardo Gomes', '1972-05-05', 'M', '123456789', 'ricardo@example.com', '+1 (555) 123-4567', 3, 'Casado', 6000.00, '2023-10-17 15:15:00', 10), 
('Mariana Alves', '1988-09-18', 'F', '987654321', 'mariana@example.com', '+1 (555) 987-6543', 0, 'Solteira', 4800.00, '2023-10-18 14:30:00', 9), 
('Paulo Torres', '1996-04-03', 'M', '234567890', 'paulo@example.com', '+1 (555) 234-5678', 1, 'Casado', 5500.00, '2023-10-19 11:00:00', 2);

SELECT
    S.DC_ID AS SALEID,
    S.DC_FULLNAME AS CUSTOMERNAME,
    S.DT_BIRTHDATE AS CUSTOMERBIRTHDATE,
    S.DC_SEX AS CUSTOMERSEX,
    S.DC_DOCUMENT AS CUSTOMERDOCUMENT,
    S.DC_EMAIL AS CUSTOMEREMAIL,
    S.DC_PHONE AS CUSTOMERPHONE,
    S.NR_NUMCHILDS AS NUMCHILDREN,
    S.DC_CIVILSTATE AS CUSTOMERCIVILSTATE,
    S.VL_MONTHLYEARNINGS AS CUSTOMERMONTHLYEARNINGS,
    S.DT_SALETIME AS SALETIME,
    D.DC_COUNTRY AS DESTINATIONCOUNTRY,
    D.DC_CITY AS DESTINATIONCITY,
    P.DC_DESCRIPTION AS PACKAGEDESCRIPTION,
    P.VL_VALUE AS PACKAGEVALUE
FROM TB_SALES AS S
INNER JOIN TB_PACKAGE AS P ON S.ID_PACKAGE = P.CD_ID
INNER JOIN TB_DESTINY AS D ON P.ID_DESTINY = D.CD_ID;