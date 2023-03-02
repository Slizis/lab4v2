from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self): # pragma: no cover
        return f"<{type(self).__name__}(id={self.id})>"

class Provider(BaseModel):
    __tablename__ = "providers"

    name = Column(String)
    phone = Column(Integer)
    email = Column(String)
    site = Column(String)

    provider_model = relationship ("Provider_Model", back_populates = "provider")


class Model(BaseModel):
    __tablename__ = "models"

    name = Column(String)
    obifka = Column(String)
    color = Column(String)
    power = Column(String)
    doors = Column(Integer)
    transmission = Column(String)

    provider_model = relationship ("Provider_Model", back_populates = "model")
    valuable = relationship("Valuable", back_populates="model")
    model_client = relationship ("Model_Client", back_populates = "model")

class Client(BaseModel):
    __tablename__ = "clients"

    name = Column(String)
    number = Column(Integer)
    date = Column(DateTime)
    phone = Column(String)
    address = Column(String)
    NameModel = Column(String)
    
    model_client = relationship ("Model_Client", back_populates = "client")

class Valuable(BaseModel):
    __tablename__ = "valuables"

    release= Column(DateTime)
    valuables = Column(String)
    preparation = Column(String)
    costs = Column(String)
    modelID = Column(Integer, ForeignKey("models.id"))

    model = relationship("Model", back_populates="valuable")

class Provider_Model(BaseModel):
    __tablename__ = "provider_models"

    modelID = Column(Integer, ForeignKey("models.id"))
    providerID = Column(Integer, ForeignKey("providers.id"))

    model = relationship("Model", back_populates="provider_model")
    provider = relationship("Provider", back_populates="provider_model")

class Model_Client(BaseModel):
    __tablename__ = "model_clients"

    modelID = Column(Integer, ForeignKey("models.id"))
    clientID = Column(Integer, ForeignKey("clients.id"))

    model = relationship("Model", back_populates="model_client")
    client = relationship("Client", back_populates="model_client")