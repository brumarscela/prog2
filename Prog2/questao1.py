import os
from peewee import *

arq = 'compra.db'

db = SqliteDatabase(arq)

class BaseModel(Base):
    class Meta:
        database = db

class Peca(BaseModel):
    nome_peca = CharField()
    funcionalidade = CharField()


class Vendedor(BaseModel):
    nome = CharField()
    endereco = CharField()


class VendaDaPeca(BaseModel):
    tempo_entrega = FloatField()
    preco = FloatField()
    peca = ForeignKeyField(Peca)
    vendedor = ForeignKeyField(Vendedor)


if os.path.exists(arq):
    os.remove(arq)


db.connect()
db.create_tables([Peca, Vendedor, VendaDaPeca.get_through_model()])


p1 = Peca.create(nome_peca = "Placa Arduino", funcionalidade = "Controlar o robô")
v1 = Vendedor.create(nome = "Blu Peças", endereco = "Blumenau")
vd = VendaDaPeca.create(tempo_entrega = 0, preco = 130, peca = Peca, vendedor = Vendedor)


print(p1.nome_peca, p1.funcionalidade, v1.nome, v1.endereco, vd.tempo_entrega, vd.preco, vd.peca, vd.vendedor)