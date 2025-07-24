from models.acesso import Acesso
from views.acesso_view import AcessoView

class AcessoController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        AcessoView(self.master, self)

    def listar_acessos(self):
        return Acesso.listar_todos()

    def inserir_acesso(self, aluno_id, data_hora):
        Acesso.inserir(aluno_id, data_hora)

    def atualizar_acesso(self, id, aluno_id, data_hora):
        Acesso.atualizar(id, aluno_id, data_hora)

    def deletar_acesso(self, id):
        Acesso.deletar(id)

    def buscar_acesso_por_id(self, id):
        return Acesso.consultar_por_id(id)
