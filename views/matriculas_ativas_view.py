import tkinter as tk
from tkinter import ttk, messagebox

class AlunoMatriculaAtivaView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Alunos com Matrículas Ativas")
        self.geometry("900x400")

        colunas = ("ID", "Nome", "CPF", "Início Matrícula", "Fim Matrícula", "Plano", "Instrutor")

        self.tree = ttk.Treeview(self, columns=colunas, show="headings")
        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.W, width=120)

        self.tree.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=5)

        btn_atualizar = tk.Button(btn_frame, text="Atualizar", command=self.atualizar_lista)
        btn_atualizar.pack()

        self.atualizar_lista()

    def atualizar_lista(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        dados = self.controller.listar_alunos_matriculas_ativas()
        for item in dados:
            self.tree.insert("", tk.END, values=item)
