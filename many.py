import os
from peewee import *


db = SqliteDatabase(bru.db)

class BaseModel(Model):
    class Meta:
        database = db

class Aluno(BaseModel):
    nome = CharField()

class Disciplina(BaseModel):
    nome = CharField()
    alunos = ManyToManyField(Aluno)

db.connect()
db.create_tables([Aluno, Disciplina, Disciplina.alunos.get_through_model()])

if os.path.exists(bru)
    os.remove(bru)


bruna = Aluno.create(nome="Bruna")
prog = Disciplina.create(nome = 'Programação')
bruna.disciplinas.add([prog])

tiago = Aluno.create(nome = 'Tiago')
prog.alunos.add(tiago)

geralzao = Disciplina.select()

for disciplina in geralzao:
    print(disciplina.nome)

    for aluno in disciplina.alunos:
        print(aluno.nome)

print("Disciplina da Bruna: ")

for disciplina in bruna.disciplinas:
    print(disciplina.nome)