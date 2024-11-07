import bcrypt
from genderize import Genderize


# fonction pour hasher le mdp
def encrypterMdp(User):
    # Declaring our password
    mdp = User.motDePasse
    # Adding the salt to password - généré aléatoirement
    salt = bcrypt.gensalt()
    # Hashing the password
    hashed = bcrypt.hashpw(mdp, salt)
    return hashed


def verifierSex(User):
    SexeACheck = User.sexe
    NomACheck = User.nom
    SexeDonne = Genderize(User.gender)
