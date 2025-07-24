from models.exercicio import Exercicio
from views.exercicio_view import ExercicioView

class ExercicioController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        ExercicioView(self.master, self)

    def listar_exercicios(self):
        return Exercicio.listar_todos()

    def inserir_exercicio(self, nome, grupo_muscular, descricao):
        Exercicio.inserir(nome, grupo_muscular, descricao)

    def atualizar_exercicio(self, id, nome, grupo_muscular, descricao):
        Exercicio.atualizar(id, nome, grupo_muscular, descricao)

    def deletar_exercicio(self, id):
        Exercicio.deletar(id)

    def buscar_exercicio(self, id):
        exercicios = Exercicio.consultar()
        for e in exercicios:
            if e[0] == id:
                return e
        return None
