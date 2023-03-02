"""empty message

Revision ID: first_data
Revises: 86e8f8e976dc
Create Date: 2022-12-09 20:09:08.004541

"""
from alembic import op
from sqlalchemy import orm
from datetime import datetime
from src.models import Provider, Model, Client, Valuable, Provider_Model, Model_Client


# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = '86e8f8e976dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    provider1 = Provider(name='ivan',email='petrov@mail.ru', phone=88005553535, site = '')
    provider2 = Provider(name='ivan1',email='petrov1@mail.ru', phone=88005553536, site = '')

    session.add_all([provider1, provider2])
    session.flush()

    kiorio = Model(name='kiorio', obifka='paper', color ='pink', power='115 kVt', doors = 2, transmission = 'hand')
    kikbutovski = Model(name='kik', obifka='paper', color ='white', power='1000 kVt', doors = 0, transmission = 'hand')

    session.add_all([kiorio,kikbutovski])
    session.flush()

    Petya = Client(name='Petya', number = 2211133331, date =datetime(1,2,4) ,phone='88005553535', address='2211', NameModel = 'kikbutovski')
    Petya1 = Client(name='Petya1', number = 2211133331, date =datetime(1,2,4) ,phone='88005553536', address='2212', NameModel = 'kiorio')

    session.add_all([Petya, Petya1])
    session.commit()

    Bizness = Valuable(release=datetime(2,4,2), valuables = '5000$', preparation = '400$' ,costs = '30$',modelID = kikbutovski.id)
    Ocherednoi = Valuable(release=datetime(1,1,2), valuables = '2000$', preparation = '100$' ,costs = '5$',modelID = kiorio.id)

    session.add_all([Bizness, Ocherednoi])
    session.commit()

    voina = Provider_Model(modelID = kikbutovski.id, providerID = provider1.id)
    voina1 = Provider_Model(modelID = kiorio.id, providerID = provider1.id)
    mir = Provider_Model(modelID = kikbutovski.id, providerID = provider1.id)
    mir1 = Provider_Model(modelID = kikbutovski.id, providerID = provider2.id)

    session.add_all([voina,voina1,mir,mir1])
    session.commit()

    slem = Model_Client(modelID = kikbutovski.id, clientID = Petya.id)
    slem1 = Model_Client(modelID = kiorio.id, clientID = Petya.id)
    silense = Model_Client(modelID = kikbutovski.id, clientID = Petya1.id)
    silense1 = Model_Client(modelID = kikbutovski.id, clientID = Petya.id)


    session.add_all([slem,slem1,silense,silense1])
    session.commit()



def downgrade() -> None:
    pass