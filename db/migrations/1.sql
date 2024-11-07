CREATE TABLE users (
    prenom VARCHAR(255) NOT NULL,
    nom VARCHAR(255) NOT NULL,
    sexe VARCHAR(10) NOT NULL CHECK (sexe IN('Homme', 'Femme')),
    programme VARCHAR(10) NOT NULL CHECK (programme IN('IFT', 'GLO', 'IIG')),
    dateNaissance DATE NOT NULL,
    courriel VARCHAR(255) NOT NULL PRIMARY KEY,
    mdp VARCHAR(255) NOT NULL
);

INSERT INTO users VALUES ( 'sebastien', 'PROUT', 'Homme', 'IFT', '2000-02-01', 'aaa@ulaval.ca', 'pipipipi');

--Bon les gars en vrai j’ai pas dead. Je ne suis pas sur de comprendre pourquoi mais il semble avoir un probleme dans la syntaxe de ma table que je crée.

--Donc pour le prochain il va falloir que tu comprenne comment créer la table de la bonne facon. 

-- Il va falloir également se pencher sur les autres tables a faire pour les autres types de données

-- En vrai bonne chance frérot

--FAISONS LE SEXEs
