import tkinter as tk
from tkinter import ttk
from controllers.aluno_controller import AlunoController
from controllers.instrutor_controller import InstrutorController
from controllers.matricula_controller import MatriculaController
from controllers.plano_controller import PlanoController
from controllers.acesso_controller import AcessoController
from controllers.ficha_treino_controller import FichaTreinoController
from controllers.ficha_treino_exercicio_controller import FichaTreinoExercicioController
from controllers.exercicio_controller import ExercicioController
from controllers.exercicio_equipamento_controller import ExercicioEquipamentoController
from controllers.equipamento_controller import EquipamentoController
from controllers.matriculas_ativas_controller import AlunoMatriculaAtivaController

class MainView:
    def __init__(self, master):
        self.master = master

        self.label = tk.Label(master, text="Academia Força Total", font=("Arial", 18))
        self.label.pack(pady=10)

        self.entities = [
            "Aluno", "Instrutor", "Plano", "Matrícula", "Acesso",
            "Ficha de Treino", "Exercício", "Equipamento",
            "Ficha-Exercício", "Exercício-Equipamento", "Matrículas-Ativas"
        ]

        self.listbox = tk.Listbox(master)
        for e in self.entities:
            self.listbox.insert(tk.END, e)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.btn_manage = tk.Button(master, text="Gerenciar", command=self.open_entity)
        self.btn_manage.pack(pady=10)

    def open_entity(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        entity = self.listbox.get(selected)

        if entity == "Aluno":
            AlunoController(self.master).open_view()
        elif entity == "Instrutor":
            InstrutorController(self.master).open_view()
        elif entity == "Plano":
            PlanoController(self.master).open_view()
        elif entity == "Matrícula":
            MatriculaController(self.master).open_view()
        elif entity == "Acesso":
            AcessoController(self.master).open_view()
        elif entity == "Ficha de Treino":
            FichaTreinoController(self.master).open_view()
        elif entity == "Exercício":
            ExercicioController(self.master).open_view()
        elif entity == "Equipamento":
            EquipamentoController(self.master).open_view()
        elif entity == "Ficha-Exercício":
            FichaTreinoExercicioController(self.master).open_view()
        elif entity == "Exercício-Equipamento":
            ExercicioEquipamentoController(self.master).open_view()
        elif entity == "Matrículas-Ativas":
            AlunoMatriculaAtivaController(self.master).open_view()
        else:
            print("Entidade não implementada.")
