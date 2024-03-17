-- Supprimer les tables si elles existent déjà
DROP TABLE IF EXISTS type_account;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS user;

-- Création de la table 'type_account'
CREATE TABLE type_account (
    ID INTEGER PRIMARY KEY,
    label TEXT NOT NULL
);

-- Création de la table 'user'
CREATE TABLE user (
    ID INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    passwordUser TEXT NOT NULL,
    nickname TEXT NOT NULL,
    type_user INT,
    FOREIGN KEY (type_user) REFERENCES type_account(ID)
);

-- Création de la table 'events'
CREATE TABLE events (
    ID INTEGER PRIMARY KEY,
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
(1, 'alice', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'Alice', 1), -- password: 123
(2, 'bob', 'b3a8e0e1f9ab1bfe3a36f231f676f78bb30a519d2b21e6c530c0eee8ebb4a5d0', 'Bob', 2), -- password: 456
(3, 'charlie', '35a9e381b1a27567549b5f8a6f783c167ebf809f1c4d6a9e367240484d8ce281', 'Maman', 1), --password: 789
(4, 'admin', '713bfda78870bf9d1b261f565286f85e97ee614efe5f0faf7c34e7ca4f65baca', 'Theo', 3); --password: adminpass

-- Insertion des données dans la table 'events'
INSERT INTO events (ID, name, description, dateevents, createdBy) VALUES
(1, 'Party at Alice s Place', 'Birthday party for Alice', '2024-04-15', 1),
(2, 'Conference', 'Tech conference on AI', '2024-05-17', 2),
(3, 'Project Meeting', 'Team meeting for project X', '2024-06-20', 3),
(4, 'Admin Meeting', 'Meeting for administrators', '2024-07-22', 4);