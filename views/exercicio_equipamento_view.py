import tkinter as tk
from tkinter import ttk, messagebox

class ExercicioEquipamentoView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Associação Exercício - Equipamento")
        self.geometry("600x350")

        self.tree = ttk.Treeview(self, columns=("Exercício ID", "Equipamento ID"), show="headings")
        self.tree.heading("Exercício ID", text="Exercício ID")
        self.tree.heading("Equipamento ID", text="Equipamento ID")
        self.tree.pack(fill=tk.BOTH, expand=True)

        frame_btn = tk.Frame(self)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Atualizar Lista", command=self.atualizar_lista).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Adicionar Associação", command=self.abrir_form_inserir).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Deletar Selecionado", command=self.deletar_selecionado).pack(side=tk.LEFT, padx=5)

        self.atualizar_lista()

    def atualizar_lista(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        associacoes = self.controller.listar_associacoes()
        for a in associacoes:
            self.tree.insert("", tk.END, values=a)

    def abrir_form_inserir(self):
        FormAssociacao(self, self.controller)

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma associação para deletar")
            return
        values = self.tree.item(selecionado[0])["values"]
        exercicio_id, equipamento_id = values
        self.controller.deletar_associacao(exercicio_id, equipamento_id)
        self.atualizar_lista()


class FormAssociacao(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Adicionar Associação Exercício-Equipamento")
        self.geometry("350x150")

        tk.Label(self, text="Exercício ID").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_exercicio = tk.Entry(self)
        self.entry_exercicio.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Equipamento ID").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_equipamento = tk.Entry(self)
        self.entry_equipamento.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=2, column=0, columnspan=2, pady=10)

    def salvar(self):
        try:
            exercicio_id = int(self.entry_exercicio.get())
            equipamento_id = int(self.entry_equipamento.get())
        except ValueError:
            messagebox.showwarning("Aviso", "IDs devem ser números inteiros")
            return

        self.controller.inserir_associacao(exercicio_id, equipamento_id)
        self.master.atualizar_lista()
        self.destroy()
