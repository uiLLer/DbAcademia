import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class InstrutorView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Gerenciar Instrutores")
        self.geometry("1200x600")

        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "CPF", "Telefone", "Email"), show="headings")
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
        instrutores = self.controller.listar_instrutores()
        for i in instrutores:
            self.tree.insert("", tk.END, values=i)

    def abrir_form_inserir(self):
        FormInstrutor(self, self.controller)

    def abrir_form_atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um instrutor para atualizar")
            return
        instrutor_id = self.tree.item(selecionado[0])["values"][0]
        dados = self.controller.buscar_instrutor_por_id(instrutor_id)
        if dados:
            FormInstrutor(self, self.controller, dados)
        else:
            messagebox.showerror("Erro", "Falha ao carregar dados do instrutor")

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um instrutor para deletar")
            return
        instrutor_id = self.tree.item(selecionado[0])["values"][0]
        self.controller.deletar_instrutor(instrutor_id)
        self.atualizar_lista()


class FormInstrutor(tk.Toplevel):
    def __init__(self, master, controller, dados=None):
        super().__init__(master)
        self.controller = controller
        self.dados = dados
        self.title("Inserir Novo Instrutor" if dados is None else "Atualizar Instrutor")
        self.geometry("400x300")

        labels = ["Nome Completo", "CPF", "Telefone", "Email"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self, text=text).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[text] = entry

        if dados:
            self.entries["Nome Completo"].insert(0, dados[1])
            self.entries["CPF"].insert(0, dados[2])
            self.entries["Telefone"].insert(0, dados[3])
            self.entries["Email"].insert(0, dados[4])

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def salvar(self):
        nome = self.entries["Nome Completo"].get()
        cpf = self.entries["CPF"].get()
        telefone = self.entries["Telefone"].get()
        email = self.entries["Email"].get()

        try:
            if self.dados:
                id_instrutor = self.dados[0]
                self.controller.atualizar_instrutor(id_instrutor, nome, cpf, telefone, email)
            else:
                self.controller.inserir_instrutor(nome, cpf, telefone, email)
            self.master.atualizar_lista()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar instrutor: {e}")
