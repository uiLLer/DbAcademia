from models.exercicio_equipamento import ExercicioEquipamento
from views.exercicio_equipamento_view import ExercicioEquipamentoView

class ExercicioEquipamentoController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        ExercicioEquipamentoView(self.master, self)

    def listar_associacoes(self):
        return ExercicioEquipamento.listar_todos()

    def inserir_associacao(self, exercicio_id, equipamento_id):
        ExercicioEquipamento.inserir(exercicio_id, equipamento_id)

    def deletar_associacao(self, exercicio_id, equipamento_id):
        ExercicioEquipamento.deletar(exercicio_id, equipamento_id)
