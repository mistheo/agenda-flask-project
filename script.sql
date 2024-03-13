-- Supprimer les tables si elles existent déjà
DROP TABLE IF EXISTS type_account;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS user;

-- Création de la table 'type_account'
CREATE TABLE type_account (
    ID INT PRIMARY KEY,
    label TEXT NOT NULL
);

-- Création de la table 'user'
CREATE TABLE user (
    ID INT PRIMARY KEY,
    username TEXT NOT NULL,
    passwordUser TEXT NOT NULL,
    nickname TEXT NOT NULL,
    type_user INT,
    FOREIGN KEY (type_user) REFERENCES type_account(ID)
);

-- Création de la table 'events'
CREATE TABLE events (
    ID INT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    dateevents DATE NOT NULL DEFAULT '0000-00-00',
    createdBy INT,
    FOREIGN KEY (createdBy) REFERENCES user(ID)
);

-- Insertion des données dans la table 'type_account'
INSERT INTO type_account (ID, label) VALUES
(1, 'classic'),
(2, 'master'),
(3, 'admin');

-- Insertion des données dans la table 'user'
INSERT INTO user (ID, username, passwordUser, nickname, type_user) VALUES
(1, 'alice', '123', 'Alice', 1),
(2, 'bob', '456', 'Bob', 2),
(3, 'charlie', '789', 'Charlie', 1),
(4, 'admin', 'adminpass', 'Admin', 3);

-- Insertion des données dans la table 'events'
INSERT INTO events (ID, name, description, dateevents, createdBy) VALUES
(1, 'Party at Alice s Place', 'Birthday party for Alice', '2024-04-15', 1),
(2, 'Conference', 'Tech conference on AI', '2024-05-17', 2),
(3, 'Project Meeting', 'Team meeting for project X', '2024-06-20', 3),
(4, 'Admin Meeting', 'Meeting for administrators', '2024-07-22', 4);