from models.aluno import Aluno
from views.aluno_view import AlunoView

class AlunoController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        AlunoView(self.master, self)

    def listar_alunos(self):
        return Aluno.listar_todos()

    def inserir_aluno(self, nome_completo, cpf, data_nascimento, telefone, email):
        Aluno.inserir(nome_completo, cpf, data_nascimento, telefone, email)

    def atualizar_aluno(self, id, nome_completo, cpf, data_nascimento, telefone, email):
        Aluno.atualizar(id, nome_completo, cpf, data_nascimento, telefone, email)

    def deletar_aluno(self, id):
        Aluno.deletar(id)

    def consultar_aluno(self, cpf):
        return Aluno.consultar_por_cpf(cpf)
