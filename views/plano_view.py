import tkinter as tk
from tkinter import ttk, messagebox

class PlanoView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Gerenciar Planos")
        self.geometry("1200x600")

        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Duração (meses)", "Valor"), show="headings")
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
        planos = self.controller.listar_planos()
        for plano in planos:
            self.tree.insert("", tk.END, values=(plano.id, plano.nome, plano.duracao_meses, plano.valor))

    def abrir_form_inserir(self):
        FormPlano(self, self.controller)

    def abrir_form_atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um plano para atualizar")
            return
        plano_id = self.tree.item(selecionado[0])["values"][0]
        plano = self.controller.buscar_plano_por_id(plano_id)
        if plano:
            FormPlano(self, self.controller, plano)
        else:
            messagebox.showerror("Erro", "Falha ao carregar dados do plano")

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um plano para deletar")
            return
        plano_id = self.tree.item(selecionado[0])["values"][0]
        self.controller.deletar_plano(plano_id)
        self.atualizar_lista()


class FormPlano(tk.Toplevel):
    def __init__(self, master, controller, plano=None):
        super().__init__(master)
        self.controller = controller
        self.plano = plano
        self.title("Inserir Novo Plano" if plano is None else "Atualizar Plano")
        self.geometry("350x250")

        labels = ["Nome", "Duração (meses)", "Valor"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self, text=text).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[text] = entry

        if plano:
            self.entries["Nome"].insert(0, plano.nome)
            self.entries["Duração (meses)"].insert(0, str(plano.duracao_meses))
            self.entries["Valor"].insert(0, str(plano.valor))

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def salvar(self):
        nome = self.entries["Nome"].get()
        duracao = self.entries["Duração (meses)"].get()
        valor = self.entries["Valor"].get()

        if not nome or not duracao or not valor:
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios")
            return

        try:
            duracao = int(duracao)
            valor = float(valor)
        except ValueError:
            messagebox.showwarning("Aviso", "Duração deve ser um número inteiro e Valor um número decimal")
            return

        try:
            if self.plano:
                self.controller.atualizar_plano(self.plano.id, nome, duracao, valor)
            else:
                self.controller.inserir_plano(nome, duracao, valor)
            self.master.atualizar_lista()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar plano: {e}")
