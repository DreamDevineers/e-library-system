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

CREATE TABLE loans (
    loan_id CHAR(36) PRIMARY KEY,
    member_id CHAR(36) NOT NULL,
    book_id CHAR(36) NOT NULL,
    loan_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    status VARCHAR(20) NOT NULL,

    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);