import tkinter as tk
from tkinter import ttk, messagebox

class FichaTreinoExercicioView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Gerenciar Detalhes da Ficha de Treino")
        self.geometry("800x400")

        self.tree = ttk.Treeview(self, columns=("Ficha Treino ID", "Exercício ID", "Séries", "Repetições", "Ordem"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)

        frame_btn = tk.Frame(self)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Atualizar Lista", command=self.atualizar_lista).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Inserir Novo", command=self.abrir_form_inserir).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Atualizar Selecionado", command=self.abrir_form_atualizar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Deletar Selecionado", command=self.deletar_selecionado).pack(side=tk.LEFT, padx=5)

        self.atualizar_lista()

    def atualizar_lista(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        detalhes = self.controller.listar_detalhes()
        for detalhe in detalhes:
            self.tree.insert("", tk.END, values=detalhe)

    def abrir_form_inserir(self):
        FormFichaTreinoExercicio(self, self.controller)

    def abrir_form_atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um detalhe para atualizar")
            return
        values = self.tree.item(selecionado[0])["values"]
        ficha_treino_id, exercicio_id = values[0], values[1]
        detalhe = self.controller.buscar_detalhe(ficha_treino_id, exercicio_id)
        if detalhe:
            FormFichaTreinoExercicio(self, self.controller, detalhe)
        else:
            messagebox.showerror("Erro", "Falha ao carregar dados do detalhe")

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um detalhe para deletar")
            return
        values = self.tree.item(selecionado[0])["values"]
        ficha_treino_id, exercicio_id = values[0], values[1]
        self.controller.deletar_detalhe(ficha_treino_id, exercicio_id)
        self.atualizar_lista()


class FormFichaTreinoExercicio(tk.Toplevel):
    def __init__(self, master, controller, detalhe=None):
        super().__init__(master)
        self.controller = controller
        self.detalhe = detalhe
        self.title("Inserir Novo Detalhe" if detalhe is None else "Atualizar Detalhe")
        self.geometry("400x300")

        labels = ["Ficha Treino ID", "Exercício ID", "Séries", "Repetições", "Ordem"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self, text=text).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[text] = entry

        if detalhe:
            self.entries["Ficha Treino ID"].insert(0, detalhe[0])
            self.entries["Ficha Treino ID"].config(state="disabled")  # PK - não alterar
            self.entries["Exercício ID"].insert(0, detalhe[1])
            self.entries["Exercício ID"].config(state="disabled")  # PK - não alterar
            self.entries["Séries"].insert(0, detalhe[2])
            self.entries["Repetições"].insert(0, detalhe[3])
            self.entries["Ordem"].insert(0, detalhe[4])

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def salvar(self):
        ficha_treino_id = self.entries["Ficha Treino ID"].get()
        exercicio_id = self.entries["Exercício ID"].get()
        series = self.entries["Séries"].get()
        repeticoes = self.entries["Repetições"].get()
        ordem = self.entries["Ordem"].get()

        if not ficha_treino_id or not exercicio_id or not series or not repeticoes or not ordem:
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios")
            return

        try:
            ficha_treino_id = int(ficha_treino_id)
            exercicio_id = int(exercicio_id)
            series = int(series)
            repeticoes = int(repeticoes)
            ordem = int(ordem)
        except ValueError:
            messagebox.showwarning("Aviso", "Os campos numéricos devem conter valores válidos")
            return

        try:
            if self.detalhe:
                self.controller.atualizar_detalhe(ficha_treino_id, exercicio_id, series, repeticoes, ordem)
            else:
                self.controller.inserir_detalhe(ficha_treino_id, exercicio_id, series, repeticoes, ordem)
            self.master.atualizar_lista()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar detalhe: {e}")
