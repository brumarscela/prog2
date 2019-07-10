class Receita(BaseModel):
    nom_receita = peewee.CharField()

class Ingredientes(BaseModel):
    nom_ingrediente = peewee.CharField()
    quantidade = peewee.IntegerField()
    unidade = peewee.IntegerField()

class IngredientesDeReceitas(BaseModel):
    receita = Receita(ingredientes)

if __name__==__"main"__:
    quantidade = quantidade.create(quantidade="5")
    unidade = unidade.create(unidade="Kg")

    receita1 = Receita.create(nom_ingrediente="laranja", quantidade=2, unidade=2)
    print(receita1)