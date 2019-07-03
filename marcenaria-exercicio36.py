import os, datetime
from peewee import *

arq_dados_sql = 'mobilia.db'

db = SqliteDatabase(arq_dados_sql)

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    nome_cliente = CharField()
    email = CharField()
    telefone = CharField()

    def __str__(self):
        return self.nome_cliente, self.email, self.telefone

class Material(BaseModel):
    nome_material = CharField()
    estoque = CharField()

    def __str__(self):
        return self.nome_material, self.estoque

class Mobilia(BaseModel):
    mobilia = CharField()
    nome_materiais = ManyToManyField(Material)
    cor = CharField()

    def __str__(self):
        momobilia = self.mobilia, self.nome_materiais, self.cor

        for i in self.nome_materiais:
            momobilia += str(i)

        return momobilia

class Pedido(BaseModel):
    data = DateTimeField()
    nome_cliente = ForeignKeyField(Cliente)
    mobilias = ManyToManyField(Mobilia)

    def __str__(self):
        p_pedido = self.data, self.nome_cliente
        for i in self.mobilias:
            p_pedido += str(i)
        return p_pedido

if os.path.exists(arq_dados_sql):
    os.remove(arq_dados_sql)

db.connect()
db.create_tables([Cliente, Material, Mobilia, 
Mobilia.nome_materiais.get_through_model(), Pedido, Pedido.mobilias.get_through_model()])

joao = Cliente.create(nome="Joao da Silva", email="jsilva@gmail.com", telefone="47 9 9200 1020")
madeira = Material.create(nome="Tábua Eucalipto Aplainada 15x220cm Massol", estoque = 20) # 20 tábuas de madeira
parafuso = Material.create(nome="Parafuso Chipboard Philips p/ Madeira 3,5x40 dourado", estoque = 50)
estante = Mobilia.create(nome = "Estante de eucalipto 5 andares", cor = "natural")

estante.materiais.add(madeira)
estante.materiais.add(parafuso)
madeira.estoque = madeira.estoque - 5 
parafuso.estoque = parafuso.estoque - 20 
madeira.save()
parafuso.save()
pedido = Pedido.create(data = datetime.datetime(2019, 7, 1, 9, 0), cliente=joao)
Pedido.mobilias.add(estante)

print(pedido)