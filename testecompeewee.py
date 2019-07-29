import os
from peewee import *

arq = 'receita.db'

db = SqliteDatabase(arq)

class BaseModel(Base):
    class Meta:
        database = db

class Receita(BaseModel):
    categoria = ForeignKeyField(Categoria)
    ingrediente = ManyToManyField(IngredienteReceita)
    passo = ForeignKeyField(Passo)

class Categoria(BaseModel):
    doce = CharField()
    salgado = CharField()
    sucos = CharField()
    adicionar_categoria = ForeignKeyField(AdicionarReceita)

class CadastrarReceita(BaseModel):
    nome = CharField()
    ingrediente = CharField(IngredienteReceita)
    categoria = CharField()

class Ingrediente(BaseModel):
    ingrediente = CharField()
    quantidade = FloatField()

class IngredienteReceita(BaseModel):
    receita = ForeignKeyField(Receita)
    ingrediente =ForeignKeyField(AdicionarReceita)
    quantidade = FloatField()

class Passo(BaseModel):
    passo1 = FloatField()

if os.path.exists(arq):
    os.remove(arq)

db.connect()

db.create_tables([Receita, Categoria, IngredienteReceita.ingrediente.get_through_model(), Passo, CadastrarReceita])