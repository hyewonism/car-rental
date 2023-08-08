/* check database */
show databases;

/* define database */
CREATE DATABASE carrental;

/* use database */
USE carrental;

/* define table */
CREATE TABLE user (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(50) NOT NULL UNIQUE,
    password varchar(200) NOT NULL,
    role varchar(10) NOT NULL,

    PRIMARY KEY(id)
);

CREATE TABLE customer (
    customer_number int NOT NULL AUTO_INCREMENT,
    user_id int NOT NULL,
    name varchar(100) NOT NULL,
    address char(100) NOT NULL,
    email char(100) NOT NULL,
    phone_number char(20) NOT NULL,

    PRIMARY KEY (customer_number),
    FOREIGN KEY (user_id)
    REFERENCES user(id) ON UPDATE CASCADE
);

CREATE TABLE staff (
    staff_number int NOT NULL AUTO_INCREMENT,
    user_id int NOT NULL,
    name varchar(100) NOT NULL,
    address char(100) NOT NULL,
    email char(100) NOT NULL,
    phone_number char(20) NOT NULL,

    PRIMARY KEY (staff_number),
    FOREIGN KEY (user_id)
    REFERENCES user(id) ON UPDATE CASCADE
);

CREATE TABLE car_rental (
     id int NOT NULL AUTO_INCREMENT,
     model varchar(50) NOT NULL,
     description varchar(1000) NOT NULL,
     registration_number varchar(50) NOT NULL,
     year int NOT NULL,
     seating_capacity int NOT NULL,
     rental_per_day int NOT NULL,
     image varchar(100) NOT NULL,
     PRIMARY KEY (id)
);

/* Drop table */
DROP TABLE car_rental;

/* show table */
SHOW tables;