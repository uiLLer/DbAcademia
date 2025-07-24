from models.equipamento import Equipamento
from views.equipamento_view import EquipamentoView

class EquipamentoController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        EquipamentoView(self.master, self)

    def listar_equipamentos(self):
        return Equipamento.consultar()

    def inserir_equipamento(self, nome, descricao):
        Equipamento.inserir(nome, descricao)

    def atualizar_equipamento(self, id, nome, descricao):
        Equipamento.atualizar(id, nome, descricao)

    def deletar_equipamento(self, id):
        Equipamento.deletar(id)
