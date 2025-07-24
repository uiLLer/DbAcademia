from models.ficha_treino import FichaTreino
from views.ficha_treino_view import FichaTreinoView

class FichaTreinoController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        FichaTreinoView(self.master, self)

    def listar_fichas(self):
        return FichaTreino.listar_todos()

    def inserir_ficha(self, aluno_id, instrutor_id, data_criacao):
        FichaTreino.inserir(aluno_id, instrutor_id, data_criacao)

    def atualizar_ficha(self, id, aluno_id, instrutor_id, data_criacao):
        FichaTreino.atualizar(id, aluno_id, instrutor_id, data_criacao)

    def deletar_ficha(self, id):
        FichaTreino.deletar(id)

    def buscar_ficha_por_id(self, id):
        fichas = FichaTreino.consultar()
        for ficha in fichas:
            if ficha[0] == id:
                return ficha
        return None
