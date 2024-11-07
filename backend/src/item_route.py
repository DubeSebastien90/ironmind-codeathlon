import mariadb
from fastapi import APIRouter

from src.item import Item
from src.item import User

router = APIRouter()
sql_connection = mariadb.connect(host='db', port=3306, user="username", password="password", database="database")


@router.get("/")
def index():
    return {"message": "Wassup go back N!"}


@router.get("/items")
def get_item():
    with sql_connection.cursor() as cursor:
        query = "SELECT name, description, price FROM items"
        cursor.execute(query)
        results = cursor.fetchall()
        return [Item(name=result[0], description=result[1], price=result[2]) for result in results]


@router.post("/item")
def add_item(item: Item):
    with sql_connection.cursor() as cursor:
        sql = "INSERT INTO items (name, description, price) VALUES (%s, %s, %s)"
        cursor.execute(sql, (item.name, item.description, item.price))
        sql_connection.commit()

@router.get("/users")
def get_user():
    with sql_connection.cursor() as cursor:
        query = "SELECT prenom, nomDeFamille, sexe, programme, date, courriel, motDePasse FROM users"
        cursor.execute(query)
        results = cursor.fetchall()
        return [User(prenom=result[0], nomDeFamille=result[1], sexe=result[2], programme=result[3], date=result[4], courriel=result[5], motDePasse=result[6]) for result in results]

@router.post("/user")
def add_user(user: User):
    with sql_connection.cursor() as cursor:
        sql = "INSERT INTO users (prenom, nomDeFamille, sexe, programme, date, courriel, motDePasse) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (user.prenom, user.nomDeFamille, user.sexe, user.programme, user.date, user.courriel, user.motDePasse))
        sql_connection.commit()


