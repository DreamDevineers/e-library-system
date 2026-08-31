CREATE DATABASE IF NOT EXISTS e_library_system;
USE e_library_system;

CREATE TABLE members (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    joined_at DATETIME NOT NULL,
    active BOOLEAN DEFAULT FALSE
);

