class Livro(BaseModel):
    titulo = peewee.CharField()
    ano = peewee.CharField()
    nom_autores = peewee.CharField()

class FormaDeAquisicao(BaseModel):
    forma_aquisicao = peewee.CharField()

if __name__ == __"main"__:
    presente = forma_aquisicao.create(forma_aquisicao="Presente")
    livro1 = Livro.create(titulo="Harry Potter", ano="2001", nom_autores="JK Rowling", forma_aquisicao=presente)
    print(livro1)