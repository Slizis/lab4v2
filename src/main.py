from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db(): # pragma: no cover
    """
    Задаем зависимость к БД. При каждом запросе будет создаваться новое
    подключение.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/provider/", response_model=schemas.Provider)
def create_Provider(provider: schemas.ProviderCreate, db: Session = Depends(get_db)):
    """
    Создание пользователя, если такой email уже есть в БД, то выдается ошибка
    """
    db_provider = crud.get_provider_by_name(db, name=provider.name)
    if db_provider:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_provider(db=db, provider=provider)


@app.get("/provider/", response_model=list[schemas.Provider])
def read_Providers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка пользователей
    """
    Providers = crud.get_providers(db, skip=skip, limit=limit)
    return Providers


@app.get("/provider/{Provider_id}", response_model=schemas.Provider)
def read_Provider(Provider_id: int, db: Session = Depends(get_db)):
    """
    Получение пользователя по id, если такого id нет, то выдается ошибка
    """
    db_provider = crud.get_provider(db, Provider_id=Provider_id)
    if db_provider is None:
        raise HTTPException(status_code=404, detail="Provider not found")
    return db_provider


@app.post("/model/", response_model=schemas.Model)
def create_Model(model: schemas.ModelCreate, db: Session = Depends(get_db)):
    """
    Создание пользователя, если такой email уже есть в БД, то выдается ошибка
    """
    db_model = crud.get_model_by_name(db, name=model.name)
    if db_model:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_model(db=db, model=model)


@app.get("/model/", response_model=list[schemas.Model])
def read_Models(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка пользователей
    """
    Models = crud.get_models(db, skip=skip, limit=limit)
    return Models


@app.get("/model/{Model_id}", response_model=schemas.Model)
def read_Model(Model_id: int, db: Session = Depends(get_db)):
    """
    Получение пользователя по id, если такого id нет, то выдается ошибка
    """
    db_model = crud.get_model(db, Model_id=Model_id)
    if db_model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return db_model

@app.post("/client/", response_model=schemas.Client)
def create_Client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    """
    Создание пользователя, если такой email уже есть в БД, то выдается ошибка
    """
    db_client = crud.get_client_by_name(db, name=client.name)
    if db_client:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_client(db=db, client=client)


@app.get("/client/", response_model=list[schemas.Client])
def read_Clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка пользователей
    """
    Clients = crud.get_clients(db, skip=skip, limit=limit)
    return Clients


@app.get("/client/{Client_id}", response_model=schemas.Client)
def read_Client(Client_id: int, db: Session = Depends(get_db)):
    """
    Получение пользователя по id, если такого id нет, то выдается ошибка
    """
    db_client = crud.get_client(db,Client_id=Client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@app.post("/model/{model_id}/valuable/", response_model=schemas.Valuable)
def create_models_for_valuable(
    model_id: int, valuable: schemas.ValuableCreate, db: Session = Depends(get_db)
):
    """
    Добавление пользователю нового предмета
    """
    return crud.create_valuable_model(db=db, valuables=valuable, model_id=model_id)

@app.get("/valuable/", response_model=list[schemas.Valuable])
def read_valuable(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка предметов
    """
    valuables = crud.get_valuables(db, skip=skip, limit=limit)
    return valuables

