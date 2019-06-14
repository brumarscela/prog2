"""40 - comando que obtém todas as instâncias de uma classe

alunos = Alunos.select()"""

"""41 - Ao realizar o teste da classe Livro (cujos atributos são: titulo, ano, autores e editora, todos do tipo texto), utilizou-se o seguinte comando para exibir as informações de uma instância:
print(livro). Entretanto, foram exibidas informações que não eram os valores dos atributos
do objeto (por exemplo, endereço de memória da variável, comando SQL de mapeamento,
etc). O que pode ser feito para que o comando mencionado apresente o efeito desejado (listar
os valores dos atributos do objeto)

def __str__ (self):
    return self.titulo, self.ano, self.autores, self.editora"""


"""42 - Considere o código descrito a seguir, que modela a relação entre alunos e disciplinas.
Complete as lacunas informando o número da linha na qual a ação comentada é executada.

(a) linha 5: é estabelecido que
o banco de dados utilizado é o
SqliteDatabase.

(b) linhas 8 e 14: define-se
que as classes-filhas da classe
BaseModel serão conectadas ao
banco de dados.

(c) linha 19: define-se que existem
um relacionamento N para
N entre as classes Disciplina e
Aluno.

(d) linha 23: solicita-se a criação
da tabela que armazena a informação
de quais alunos cursam
quais disciplinas.

(e) linha 26: define-se que um
aluno chamado João da Silva
cursa a disciplina de Inglês.

(f) linha 26: obtém-se uma lista
contendo todos os alunos existentes
na base de dados.

(g) linha 33: são exibidos os nomes
das disciplinas cursadas por
João da Silva."""


"""43 - Considere uma loja de informática que comercializa computadores, impressoras e periféricos
(mouse, teclado, etc). A loja realiza vendas e precisa registrar, para cada venda, as seguintes
informações: data e hora, produtos vendidos e cliente comprador. Sobre o cliente, são
registrados nome e email. Sobre os produtos, são registradas informações mínimas: descrição
e preço. Apresente o código de modelagem das classes que possam armazenar as informações
de venda da loja de informática mencionada.

class Produto(BaseModel):
    descricao = CharField ()
    preco = FloatField ()

class Cliente (BaseModel):
    nome = CharField()
    email = CharField ()

class Venda(BaseModel):
    data_hora = DateTimeField()
    produtos = ManyToManyField(Produto)
    cliente = ForeignKeyField(Cliente)

db.create_tables([Produto, Cliente, Venda, Venda.produtos.get_through_model()])

prod1 = Produto.create(descricao = "Mouse", preco = 50.00)
prod2 = Produto.create(descricao = "Impressora", preco = 1800.0)
cli = Cliente.create(nome = "Bruna Marcela" , email = "bru@gmail.com")
venda = Venda.create(data_hora = datetime.datetime (2019, 5, 06, 8, 40), cliente = cli )
venda.produtos.add(prod1)

vendas = Venda.select()

for x in vendas:
print("Data/hora: "+str (x.data_hora))

for prod in x.produtos:
print (prod.descricao +", R$ "+str(prod.preco))


print("Comprador: "+x.cliente.nome+", email="+x.cliente.email)

"""