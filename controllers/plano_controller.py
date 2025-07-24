from models.plano import Plano
from views.plano_view import PlanoView

class PlanoController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        PlanoView(self.master, self)

    def listar_planos(self):
        return Plano.listar_todos()

    def inserir_plano(self, nome, duracao_meses, valor):
        return Plano.inserir(nome, duracao_meses, valor)

    def atualizar_plano(self, id, nome, duracao_meses, valor):
        Plano.atualizar(id, nome, duracao_meses, valor)

    def deletar_plano(self, id):
        Plano.deletar(id)

    def buscar_plano_por_id(self, id):
        return Plano.consultar(id)
