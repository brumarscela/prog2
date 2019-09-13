from peewee import *

arq = './pessoas-front-end.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    email = CharField()
    
if __name__ == "__main__":
    db.connect()
    db.create_tables([Pessoa])
    joao = Pessoa.create(nome="Joao da Silva", 
        endereco="Casa 9", telefone="3541-1230", email = "joao.s@gmail.com")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone, joao.email)