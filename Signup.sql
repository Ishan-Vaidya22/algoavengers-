CREATE DATABASE signup_db;
use signup_db;
CREATE SCHEMA signup_schema;
CREATE TABLE signup_schema.users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DELIMITER //
CREATE FUNCTION signup_schema.hash_password(password TEXT) RETURNS VARBINARY(255) DETERMINISTIC
BEGIN
  DECLARE salt BINARY(16);
  DECLARE hashed_password VARBINARY(255);
  
  SET salt = UNHEX(REPLACE(UUID(), '-', ''));
  SET hashed_password = CONCAT('$2a$', LPAD(CONV(FLOOR(RAND() * 11), 10, 10), 2, '0'), '$', HEX(salt), SUBSTR(SHA2(CONCAT(password, HEX(salt)), 256), 1, 60));
  
  RETURN hashed_password;
END//
DELIMITER ;


INSERT INTO signup_schema.users (username, email, password_hash)
VALUES ('xyzpqrr', 'anishkapanna1511@gmail.com', signup_schema.hash_password('ddhhfnc123'));

SELECT * FROM signup_schema.users;





