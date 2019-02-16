schema = """

DROP TABLE IF EXISTS offices;

CREATE TABLE offices(
    id  INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS parties;

CREATE TABLE parties(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    hqaddress VARCHAR(100) NOT NULL,
    logoUrl VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS users;

CREATE TABLE users(
    id INT PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    othername VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phonenumber VARCHAR(100) NOT NULL,
    passportUrl VARCHAR(100) NOT NULL,
    isadmin BOOLEAN DEFAULT FALSE
);

DROP TABLE IF EXISTS candidates;

CREATE TABLE candidates(
    id INT PRIMARY KEY,
    office INT REFERENCES offices(id),
    party INT  REFERENCES parties(id),
    candidate INT UNIQUE REFERENCES users(id)
);

DROP TABLE IF EXISTS votes;

CREATE TABLE votes(
    id INT PRIMARY KEY,
    createdon TIMESTAMP DEFAULT now(),
    createdby INT REFERENCES users(id),
    office INT REFERENCES offices(id),
    candidate INT UNIQUE REFERENCES users(id)
);

DROP TABLE IF EXISTS petition;

CREATE TABLE petition(
    id INT PRIMARY KEY,
    createdon TIMESTAMP DEFAULT now(),
    createdby INT REFERENCES users(id),
    office INT REFERENCES offices(id),
    body TEXT NOT NULL
);
"""
