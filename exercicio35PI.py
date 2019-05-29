class ProjetoIntegrador():
    def __init__(self, Aluno, ProfessorOrientador, titulo, ano):
        self.titulo = titulo
        self.ano = ano
        self.Aluno = Aluno
        self.ProfessorOrientador = ProfessorOrientador

class Aluno():
    def __init__(self, nome_aluno, turma):
        self.nome_aluno = nome_aluno
        self.turma = turma

class ProfessorOrientador():
    def __init__(self, nome_professor, AreaAtuacao):
        self.nome_professor = nome_professor
        self.AreaAtuacao = AreaAtuacao

class AreaAtuacao():
    def __init__(self, nome, EventosPublicacao, Periodicos):
        self.nome = nome
        self.EventosPublicacao = EventosPublicacao
        self.Periodicos = Periodicos

class Eventos_Publicacao():
    def __init__(self, ano, local):
        self.ano = ano
        self.local = local

class Periodicos():
    def __init__(self, nome, issn):
        self.nome = nome
        self.issn = issn

class AnaisEvento():
    def __init__(self, Eventos_Publicacao):
        self.Eventos_Publicacao = Eventos_Publicacao
