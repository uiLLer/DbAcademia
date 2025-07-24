import tkinter as tk
from tkinter import ttk, messagebox

class ExercicioView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Gerenciar Exercícios")
        self.geometry("700x400")

        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Grupo Muscular"), show="headings")
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
        exercicios = self.controller.listar_exercicios()
        for e in exercicios:
            self.tree.insert("", tk.END, values=e)

    def abrir_form_inserir(self):
        FormExercicio(self, self.controller)

    def abrir_form_atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um exercício para atualizar")
            return
        values = self.tree.item(selecionado[0])["values"]
        id_exercicio = values[0]
        exercicio = self.controller.buscar_exercicio(id_exercicio)
        if exercicio:
            FormExercicio(self, self.controller, exercicio)
        else:
            messagebox.showerror("Erro", "Falha ao carregar dados do exercício")

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um exercício para deletar")
            return
        values = self.tree.item(selecionado[0])["values"]
        id_exercicio = values[0]
        self.controller.deletar_exercicio(id_exercicio)
        self.atualizar_lista()


class FormExercicio(tk.Toplevel):
    def __init__(self, master, controller, exercicio=None):
        super().__init__(master)
        self.controller = controller
        self.exercicio = exercicio
        self.title("Inserir Novo Exercício" if exercicio is None else "Atualizar Exercício")
        self.geometry("400x250")

        tk.Label(self, text="Nome").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_nome = tk.Entry(self)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Grupo Muscular").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_grupo = tk.Entry(self)
        self.entry_grupo.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self, text="Descrição").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_descricao = tk.Text(self, height=5, width=30)
        self.entry_descricao.grid(row=2, column=1, padx=5, pady=5)

        if exercicio:
            self.entry_nome.insert(0, exercicio[1])
            self.entry_grupo.insert(0, exercicio[2])
            self.entry_descricao.insert("1.0", exercicio[3])

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=3, column=0, columnspan=2, pady=10)

    def salvar(self):
        nome = self.entry_nome.get().strip()
        grupo = self.entry_grupo.get().strip()
        descricao = self.entry_descricao.get("1.0", tk.END).strip()

        if not nome or not grupo or not descricao:
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios")
            return

        try:
            if self.exercicio:
                self.controller.atualizar_exercicio(self.exercicio[0], nome, grupo, descricao)
            else:
                self.controller.inserir_exercicio(nome, grupo, descricao)
            self.master.atualizar_lista()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar exercício: {e}")
