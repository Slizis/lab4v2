from pydantic import BaseModel
from datetime import date

class Provider_ModelBase(BaseModel):
    
    pass
    

class Provider_ModelCreate(Provider_ModelBase):
    
   pass


class Provider_Model(Provider_ModelBase):
   
    id: int
    modelID: int
    providerID:int
    
    class Config:
        orm_mode = True

class Model_ClientBase(BaseModel):
    
    pass
    

class Model_ClientCreate(Model_ClientBase):
    
   pass


class Model_Client(Model_ClientBase):
   
    id: int
    modelID: int
    clientID:int
    
    class Config:
        orm_mode = True

class ProviderBase(BaseModel):

    name: str
    phone: int
    email: str
    site: str


class ProviderCreate(ProviderBase):
   
    pass


class Provider(ProviderBase):
   
    id: int
    provider_model: list[Provider_Model]

    class Config:
        
        orm_mode = True


class ValuableBase(BaseModel):
    
    release: date
    valuables: str
    preparation: str
    costs: str
    

class ValuableCreate(ValuableBase):
    
   pass


class Valuable(ValuableBase):
   
    id: int
    modelID: int
    
    class Config:
        orm_mode = True


class ModelBase(BaseModel):
    
    name: str
    obifka: str
    color: str
    power: str
    doors: int
    transmission: str
    

class ModelCreate(ModelBase):
    
   pass


class Model(ModelBase):
   
    id: int
    provider_model: list[Provider_Model]
    valuable : list[Valuable]
    model_client: list[Model_Client]

    class Config:
        orm_mode = True

class ClientBase(BaseModel):
    
    name: str
    number: int
    date: date
    phone: str
    address: str
    NameModel: str
    

class ClientCreate(ClientBase):
    
   pass


class Client(ClientBase):
   
    id: int
    model_client: list[Model_Client]
    
    class Config:
        orm_mode = True


