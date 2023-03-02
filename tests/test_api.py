from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению


def test_create_Provider():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/provider/",
        json={"name": "test",
              'phone': 123322,
              "email": "test@email.com",
              "site": "mamajama.com"
              }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "test"


def test_create_exist_Providers():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/provider/",
        json={"name": "test",
              'phone': 123322,
              "email": "test@email.com",
              "site": "mamajama.com"
              
              }
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Email already registered"


def test_get_Provider():
    """
    Тест на получение списка пользователей из БД
    """
    response = client.get("/provider/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "test"


def test_get_Provider_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/provider/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "test"

def test_Provider_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/provider/32")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Provider not found"

def test_create_Model():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/model/",
        json={"name": "bird",
              "obifka": "paper",
              "color": "red",
              "power": "siladuha",
              'doors': 3,
              "transmission": "cool"
              }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "bird"

def test_create_exist_Model():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/model/",
        json={"name": "bird",
              "obifka": "paper",
              "color": "red",
              "power": "siladuha",
              'doors': 3,
              "transmission": "cool"
              }
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Email already registered"    

def test_get_Model():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/model/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "bird"
    assert data[0]["color"] == "red"

def test_Model_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/model/32")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Model not found"


def test_get_Model_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/model/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "bird"

def test_create_Client():
    """
    Тест на создание нового пользователя
    """
    response = client.post(
        "/client/",
        json={"name": "jack",
              "number": "1",
              "date": "1",
              "phone": "232132131",
              'address': "2332",
              "NameModel": "1"
              }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "jack"

def test_create_exist_Client():
    """
    Проверка случая, когда мы пытаемся добавить существующего пользователя
    в БД, т.е. когда данный email уже присутствует в БД.
    """
    response = client.post(
        "/client/",
        json={"name": "jack",
              "number": "1",
              "date": "1",
              "phone": "232132131",
              'address': "2332",
              "NameModel": "1"
              }
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Email already registered"

def test_get_Client():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/client/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "jack"

def test_client_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/client/32")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Client not found"

def test_get_Client_by_id():
    """
    Тест на получение пользователя из БД по его id
    """
    response = client.get("/client/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "jack"

def test_add_valuable_to_models():
    """
    Тест на добавление Item пользователю
    """
    response = client.post(
        "/model/1/valuable/",
        json={"release": "1970-01-01",
              "valuables": "strdds",
              "preparation": "dsds",
              "costs": "3323232"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["release"] == "1970-01-01"
    assert data["valuables"] == "strdds"
    assert data["preparation"] == "dsds"
    assert data["costs"] == "3323232"
    assert data["modelID"] == 1


def test_get_valuables():
    """
    Тест на получение списка Item-ов из БД
    """
    response = client.get("/valuable/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["release"] == "1970-01-01"
    assert data[0]["valuables"] == "strdds"
    assert data[0]["preparation"] == "dsds"
    assert data[0]["costs"] == "3323232"
    assert data[0]["modelID"] == 1