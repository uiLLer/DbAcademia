from models.instrutor import Instrutor
from views.instrutor_view import InstrutorView

class InstrutorController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        InstrutorView(self.master, self)

    def listar_instrutores(self):
        return Instrutor.consultar_todos()

    def inserir_instrutor(self, nome_completo, cpf, telefone, email):
        Instrutor.inserir(nome_completo, cpf, telefone, email)

    def atualizar_instrutor(self, id, nome_completo, cpf, telefone, email):
        Instrutor.atualizar(id, nome_completo, cpf, telefone, email)

    def deletar_instrutor(self, id):
        Instrutor.deletar(id)

    def consultar_instrutor_por_cpf(self, cpf):
        return Instrutor.consultar_por_cpf(cpf)

    def buscar_instrutor_por_id(self, id):
        return Instrutor.consultar_por_id(id)
