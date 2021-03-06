import peewee, os
db = peewee.SqliteDatabase('Clinica.db')
render_template("Consulta.html", consulta=Consulta.select())

novo_animal = Animal(request.form["nome_dono, nome_animal, tipo_animal, raca, idade"])
animal.add(novo_animal)

Consulta.create(animal=request.form["nome_animal"],
servico=request.form["servico"],
data=request.form["data"],
horario=request.form["horario"]

class Animal(peewee.Model):
    nome_dono = peewee.CharField()
    nome_animal = peewee.CharField()
    tipo_animal = peewee.CharField()
    raca = peewee.CharField()
    idade = peewee.CharField()

    class Meta():"""subclasse Meta estabelece o vınculo entre a classe e o banco de dados, pelo atributo database."""
        database = db

        def __str__(self): """O metodo str agrega de maneira textual as informacoes da classe"""
            return self.nome_dono+", nome do animal " self.nome_animal+", espécie " self.tipo_animal+", raça " self.raca+", idade " self.idade

class Consulta(peewee.Model):
    servico = peewee.CharField()
    data = peewee.CharField()
    horario = peewee.CharField()
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField()
    my_id = peewee.CharField()

    class Meta():
        database = conec_bd

    def __str__(self):
        return self.servico+", data", self.data ", horário", self.horario", animal ", str(self.animal)", confirma ", self.confirma ", id ", self.my_id

class Excluir(peewee.Model):
    Animal.delete_by_id(request.args.get("id"))

class Alterar(peewee.Model):
    fluflu = Animal.get_by_id(request.form["id"])
    fluflu.nome_animal = request.form["nome_animal"]
    fluflu.save()

class Consulta(peewee.Model):
    servico = peewee.CharField()
    data = peewee.CharField()
    horario = peewee.CharField()
    animal = peewee.ForeignKeyField(Animal)
    confirma = peewee.CharField()
    my_id = peewee.CharField()

#Teste#

if __name__ == __"main"__:
    arquivo = 'Consultas.conect_bd'

    if os.path.exists(arquivo):
        os.remove(arquivo)

    try:
        conec_bd.connect()
        conec_bd.create_tables(Animal, Consulta)

    except peewee.OperationalError as i:
        print("Erro ao criar tabelas: "+str(i))


    print("TESTE DO ANIMAL")

    a1 = Animal(nome_dono = "Bruna", tipo_animal="C", animal="Cachorro")
    print(a1)
    print("TESTE DA CONSULTA")

    c1 = Consulta(data="05/06/2001", servico="Consulta de rotina", horario="15h30", animal=a1, confirma="OK")
    print(c1)
    print("TESTE DA PERSISTÊNCIA")

    al.save()
    cl.save()

    c2 = Consulta(data="07/06/2004", servico="Vacina", horario="10h30", animal=a1, confirma="OK")
    c2.save()
    todos = Consulta.select()
    

for consulta in todos:
    print(consulta)