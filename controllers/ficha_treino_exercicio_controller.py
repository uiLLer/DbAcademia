from models.ficha_treino_exercicio import FichaTreinoExercicio
from views.ficha_treino_exercicio_view import FichaTreinoExercicioView

class FichaTreinoExercicioController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        FichaTreinoExercicioView(self.master, self)

    def listar_detalhes(self):
        return FichaTreinoExercicio.listar_todos()

    def inserir_detalhe(self, ficha_treino_id, exercicio_id, series, repeticoes, ordem):
        FichaTreinoExercicio.inserir(ficha_treino_id, exercicio_id, series, repeticoes, ordem)

    def atualizar_detalhe(self, ficha_treino_id, exercicio_id, series, repeticoes, ordem):
        FichaTreinoExercicio.atualizar(ficha_treino_id, exercicio_id, series, repeticoes, ordem)

    def deletar_detalhe(self, ficha_treino_id, exercicio_id):
        FichaTreinoExercicio.deletar(ficha_treino_id, exercicio_id)

    def buscar_detalhe(self, ficha_treino_id, exercicio_id):
        detalhes = FichaTreinoExercicio.consultar()
        for detalhe in detalhes:
            if detalhe[0] == ficha_treino_id and detalhe[1] == exercicio_id:
                return detalhe
        return None
