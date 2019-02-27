schema = """

DROP TABLE IF EXISTS offices CASCADE;

CREATE TABLE offices(
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS parties CASCADE;

CREATE TABLE parties(
    id SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    hqaddress VARCHAR(100) NOT NULL,
    logoUrl VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users(
   id SERIAL NOT NULL PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    othername VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    phonenumber VARCHAR(100) UNIQUE NOT NULL,
    passporturl VARCHAR(100) NOT NULL,
    isadmin BOOLEAN DEFAULT FALSE
);

DROP TABLE IF EXISTS candidates CASCADE;

CREATE TABLE candidates(
    id SERIAL NOT NULL PRIMARY KEY,
    office INT REFERENCES offices(id),
    party INT  REFERENCES parties(id),
    candidate INT UNIQUE REFERENCES users(id)
);

DROP TABLE IF EXISTS votes CASCADE;

CREATE TABLE votes(
    id SERIAL NOT NULL PRIMARY KEY,
    createdon TIMESTAMP DEFAULT now(),
    createdby INT REFERENCES users(id),
    office INT REFERENCES offices(id),
    candidate INT UNIQUE REFERENCES users(id)
);

DROP TABLE IF EXISTS petition CASCADE;

CREATE TABLE petition(
    id SERIAL NOT NULL PRIMARY KEY,
    createdon TIMESTAMP DEFAULT now(),
    createdby INT REFERENCES users(id),
    office INT REFERENCES offices(id),
    body TEXT NOT NULL
);
"""
