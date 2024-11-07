from datetime import datetime
from enum import Enum
from pydantic import BaseModel

Sexe = Enum('Male', 'Female')

class Item(BaseModel):
    name: str
    description: str
    price: float

class User(BaseModel):
    prenom: str
    nomDeFamille: str
    sexe: str
    programme: str
    date: str
    courriel: str
    motDePasse: str

    class SexeItem(BaseModel):
        sexe: Sexe

    class ProgrammeItem(BaseModel):
        listeProgrammes: list[str]

    class Billets(BaseModel):
        listeBillets: list[Item]

