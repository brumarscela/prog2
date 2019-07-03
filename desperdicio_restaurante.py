import os, datetime
from peewee import *


arq = 'desperdicio.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Produto(BaseModel):
    descricao = CharField()
    def __str__(self):
        return self.descricao
    
class Desperdicio(BaseModel):
    produto = ForeignKeyField(Produto)
    quantidade = IntegerField()
    def __str__(self):
        return "Desperdicio de "+str(self.quantidade)+"%"+" de "+str(self.produto)

class Registro(BaseModel):
    data = DateField()
    desperdicios = ManyToManyField(Desperdicio)
    pessoas = IntegerField()
    def __str__(self):
        s = "Em: "+str(self.data) + " h
        avia "+str(self.pessoas)+" pessoas: "
        for d in self.desperdicios:
            s += str(d)
        return s            

if os.path.exists(arq):
    os.remove(arq)

db.connect()
db.create_tables([Produto, Desperdicio, Registro, Registro.desperdicios.get_through_model()])

portG = Produto.create(descricao = "Batatão")
reg1 = Registro.create(data = datetime.date(2019, 7, 3), pessoas = 4)
reg1.desperdicios.add(Desperdicio.create(produto = portG, quantidade = 10))

print(reg1)
