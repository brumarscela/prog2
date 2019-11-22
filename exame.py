from peewee import *
import os

arq = '/home/bruna.santos/Downloads/pessoas-backend.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db


class Paciente(BaseModel):
    nome_paciente = CharField()
    data_exame = DateField()
    nome_medico = CharField()
    exames = ManyToManyField(Exame)


class Exame(BaseModel):
    nome_exame = CharField()
    preco = FloatField()
    prazo_resultado = IntegerField()


p1 = Paciente.create(nome_paciente = "João da Silva", data_exame = "09/08/2019", nome_medico = "John Hank", exames = [])
ex1 = Exame.create(nome_exame = "triglicerídeos", preco = 50, prazo_resultado = 2)


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)

    db.connect()
    db.create_tables([Paciente], [Exame]) 

    print(p1.nome_paciente, ",", p1.data_exame, ",", p1.nome_medico, ",", exames = Exame, "," ex1.nome_exame, "," ex1.preco, "," ex1.prazo_resultado".")