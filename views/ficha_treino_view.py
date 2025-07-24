import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class FichaTreinoView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Gerenciar Fichas de Treino")
        self.geometry("700x400")

        self.tree = ttk.Treeview(self, columns=("ID", "Aluno ID", "Instrutor ID", "Data Criação"), show="headings")
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
        fichas = self.controller.listar_fichas()
        for ficha in fichas:
            self.tree.insert("", tk.END, values=ficha)

    def abrir_form_inserir(self):
        FormFichaTreino(self, self.controller)

    def abrir_form_atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma ficha para atualizar")
            return
        ficha_id = self.tree.item(selecionado[0])["values"][0]
        ficha = self.controller.buscar_ficha_por_id(ficha_id)
        if ficha:
            FormFichaTreino(self, self.controller, ficha)
        else:
            messagebox.showerror("Erro", "Falha ao carregar dados da ficha")

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma ficha para deletar")
            return
        ficha_id = self.tree.item(selecionado[0])["values"][0]
        self.controller.deletar_ficha(ficha_id)
        self.atualizar_lista()


class FormFichaTreino(tk.Toplevel):
    def __init__(self, master, controller, ficha=None):
        super().__init__(master)
        self.controller = controller
        self.ficha = ficha
        self.title("Inserir Nova Ficha" if ficha is None else "Atualizar Ficha")
        self.geometry("350x250")

        labels = ["Aluno ID", "Instrutor ID", "Data Criação (YYYY-MM-DD)"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self, text=text).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[text] = entry

        if ficha:
            self.entries["Aluno ID"].insert(0, ficha[1])
            self.entries["Instrutor ID"].insert(0, ficha[2])
            self.entries["Data Criação (YYYY-MM-DD)"].insert(0, ficha[3].strftime('%Y-%m-%d') if isinstance(ficha[3], (datetime,)) else ficha[3])

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def salvar(self):
        aluno_id = self.entries["Aluno ID"].get()
        instrutor_id = self.entries["Instrutor ID"].get()
        data_criacao = self.entries["Data Criação (YYYY-MM-DD)"].get()

        if not aluno_id or not instrutor_id or not data_criacao:
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios")
            return

        try:
            # Valida data (apenas básica)
            datetime.strptime(data_criacao, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Aviso", "Data inválida. Use o formato YYYY-MM-DD.")
            return

        try:
            if self.ficha:
                self.controller.atualizar_ficha(self.ficha[0], int(aluno_id), int(instrutor_id), data_criacao)
            else:
                self.controller.inserir_ficha(int(aluno_id), int(instrutor_id), data_criacao)
            self.master.atualizar_lista()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar ficha: {e}")
