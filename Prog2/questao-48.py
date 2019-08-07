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
    tamanho = CharField()

class Jardineiro(BaseModel):
    nome_jardineiro = CharField()
    cpf_jardineiro = FloatField()
    
class Jardim(BaseModel):
    nome_jardineiro = ForeignKeyField(Jardineiro)
    nome_planta = ForeignKeyField(Planta)
    numero_jardim = FloatField()

class PeriodoPoda(BaseModel):
    periodo_poda = IntegerField()
    data_plantio = IntegerField()


if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Planta,Planta.nome_planta.get_through_model(),Jardineiro,Jardim,Jardim.plantas.get_through_model()])

    rosa_vermelha = Planta.create(nome_planta = "rosa vermelha", nome_cientifico = "Rosa gallica", tamanho = "media")
    bruna = Jardinerio.create(nome_jardineiro = "Bruna", cpf_jardineiro = "110.888.777-05")
    doze = Jardim.create(numero_jardim = "12", nome_planta = "rosa vermelha", nome_jardineiro = "Bruna")
    poda = PeriodoPoda.create(periodo_poda = "20", data_plantio = "08/08/2019")

    print(rosa_vermelha)
    print(bruna)
    print(doze)
    print(poda)