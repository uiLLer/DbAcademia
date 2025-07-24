import tkinter as tk
from tkinter import ttk
from controllers.aluno_controller import AlunoController

class MainView:
    def __init__(self, master):
        self.master = master

        self.label = tk.Label(master, text="Academia Força Total", font=("Arial", 18))
        self.label.pack(pady=10)

        self.entities = ["Aluno", "Plano"]

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
#        elif entity == "Plano":
#            PlanoController(self.master).open_view()
        else:
            print("Entidade não implementada ainda.")
