from models.matricula import Matricula
from views.matricula_view import MatriculaView

class MatriculaController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        MatriculaView(self.master, self)

    def listar_matriculas(self):
        return Matricula.listar_todos()

    def inserir_matricula(self, aluno_id, plano_id, data_inicio, data_fim):
        Matricula.inserir(aluno_id, plano_id, data_inicio, data_fim)

    def atualizar_matricula(self, id, aluno_id, plano_id, data_inicio, data_fim):
        Matricula.atualizar(id, aluno_id, plano_id, data_inicio, data_fim)

    def deletar_matricula(self, id):
        Matricula.deletar(id)

    def buscar_matricula_por_id(self, id):
        return Matricula.consultar_por_id(id)
