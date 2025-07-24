import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.simpledialog import askstring

class AcessoView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Gerenciar Acessos")
        self.geometry("1200x600")

        self.tree = ttk.Treeview(self, columns=("ID", "Aluno ID", "Data/Hora"), show="headings")
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
        acessos = self.controller.listar_acessos()
        for acesso in acessos:
            self.tree.insert("", tk.END, values=acesso)

    def abrir_form_inserir(self):
        FormAcesso(self, self.controller)

    def abrir_form_atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um acesso para atualizar")
            return
        acesso_id = self.tree.item(selecionado[0])["values"][0]
        dados = self.controller.buscar_acesso_por_id(acesso_id)
        if dados:
            FormAcesso(self, self.controller, dados)
        else:
            messagebox.showerror("Erro", "Falha ao carregar dados do acesso")

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um acesso para deletar")
            return
        acesso_id = self.tree.item(selecionado[0])["values"][0]
        self.controller.deletar_acesso(acesso_id)
        self.atualizar_lista()


class FormAcesso(tk.Toplevel):
    def __init__(self, master, controller, dados=None):
        super().__init__(master)
        self.controller = controller
        self.dados = dados
        self.title("Inserir Novo Acesso" if dados is None else "Atualizar Acesso")
        self.geometry("400x200")

        tk.Label(self, text="Aluno ID").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_aluno = tk.Entry(self)
        self.entry_aluno.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self, text="Data/Hora (YYYY-MM-DD HH:MM:SS)").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_datahora = tk.Entry(self)
        self.entry_datahora.grid(row=1, column=1, padx=5, pady=5)

        if dados:
            self.entry_aluno.insert(0, dados[1])
            self.entry_datahora.insert(0, dados[2])

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=2, column=0, columnspan=2, pady=10)

    def salvar(self):
        aluno_id = self.entry_aluno.get()
        data_hora = self.entry_datahora.get()

        try:
            if self.dados:
                acesso_id = self.dados[0]
                self.controller.atualizar_acesso(acesso_id, aluno_id, data_hora)
            else:
                self.controller.inserir_acesso(aluno_id, data_hora)
            self.master.atualizar_lista()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar acesso: {e}")
