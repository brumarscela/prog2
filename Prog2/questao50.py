import os, datetime
from peewee import *

arq = 'compra.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Peca(BaseModel):
    nom_peca = CharField()
    funcionalidade = CharField()

class Vendedor(BaseModel):
    lugar_venda = CharField()
    endereco = CharField()

class Orcamento(BaseModel):
    produto = ForeignKeyField(Peca)
    vendedor = ForeignKeyField(Vendedor)
    preco = FloatField()
    tempo_entrega = IntegerField()

peca1 = Peca.create(nom_peca = "motor de passo", funcionalidade = "deslocar robô na superfície")
v1 = Vendedor.create(lugar_venda = "AliExpress", endereco = "aliexpress.com")
orc = Orcamento.create(produto = Peca, vendedor = Vendedor, preco = 120, tempo_entrega = 7)


print(orc.peca1.nom_peca, orc.peca1.funcionalidade, orc.v1.lugar_venda, orc.v1.endereco, orc.preco, orc.tempo_entrega)