import os
from peewee import *

arq = "jardineiro.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta():
        database = db

class Planta(BaseModel):
    nome_planta = CharField()
    nome_cientifico = CharField()
    tamanho_folha = CharField()
    periodo_poda = IntegerField()

class Jardineiro(BaseModel):
    nome_jardineiro = CharField()
    cpf_jardineiro = FloatField()
    
class Jardim(BaseModel):
    nome_jardineiro = ForeignKeyField(Jardineiro)
    nome_jardim = FloatField()

class Cultivo(BaseModel):
    jardim = ForeignKeyField(Jardim)
    nome_planta = ForeignKeyField(Planta)
    data_plantio = IntegerField()

if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Planta,Planta.nome_planta.get_through_model(),Jardineiro,Jardim,Jardim.plantas.get_through_model()])

    rosa_vermelha = Planta.create(nome_planta = "rosa vermelha", nome_cientifico = "Rosa gallica", tamanho_folha = "media", periodo_poda = "120")
    bruna = Jardinerio.create(nome_jardineiro = "Bruna", cpf_jardineiro = "110.888.777-05")
    jardim = Jardim.create(nome_jardim = "Jardim das Rosas", nome_jardineiro = bruna)
    cultivo = Cultivo.create(nome_planta = rosa_vermelha, data_plantio = "09/08/2019")

    print(rosa_vermelha)
    print(bruna)
    print(jardim)
    print(cultivo)