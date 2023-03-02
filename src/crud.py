from sqlalchemy.orm import Session

from src import models, schemas


def create_provider(db: Session, provider: schemas.ProviderCreate):
    """
    Добавление нового пользователя
    """
    db_provider = models.Provider(email=provider.email,name=provider.name, phone = provider.phone, site=provider.site)
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
    return db_provider


def get_provider(db: Session, Provider_id: int):
    """
    Получить пользователя по его id
    """
    return db.query(models.Provider).filter(models.Provider.id == Provider_id).first()


def get_provider_by_name(db: Session, name: str):
    """
    Получить пользователя по его email
    """
    return db.query(models.Provider).filter(models.Provider.name == name).first()


def get_providers(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список пользователей из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Provider).offset(skip).limit(limit).all()

def create_model(db: Session, model: schemas.ModelCreate):
    """
    Добавление нового пользователя
    """
    db_model = models.Model(name=model.name, obifka=model.obifka, color=model.color, power=model.power, doors=model.doors, transmission=model.transmission)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


def get_model(db: Session, Model_id: int):
    """
    Получить пользователя по его id
    """
    return db.query(models.Model).filter(models.Model.id == Model_id).first()


def get_model_by_name(db: Session, name: str):
    """
    Получить пользователя по его email
    """
    return db.query(models.Model).filter(models.Model.name == name).first()



def get_models(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список пользователей из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Model).offset(skip).limit(limit).all()


def create_client(db: Session, client: schemas.ClientCreate):
    """
    Добавление нового пользователя
    """
    db_client = models.Client(name=client.name, number=client.number,date=client.date,phone=client.phone,address=client.address, NameModel=client.NameModel)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client



def get_client(db: Session, Client_id: int):
    """
    Получить пользователя по его id
    """
    return db.query(models.Client).filter(models.Client.id == Client_id).first()


def get_client_by_name(db: Session, name: str):
    """
    Получить пользователя по его email
    """
    return db.query(models.Client).filter(models.Client.name == name).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список пользователей из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Client).offset(skip).limit(limit).all()



def create_valuable_model(db: Session, valuables: schemas.ValuableCreate, model_id: int):
    """
    Добавление нового Item пользователю
    """
    db_valuable = models.Valuable(**valuables.dict(), modelID=model_id)
    db.add(db_valuable)
    db.commit()
    db.refresh(db_valuable)
    return db_valuable

def get_valuables(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список пользователей из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Valuable).offset(skip).limit(limit).all()

