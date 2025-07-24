import tkinter as tk
from tkinter import ttk, messagebox,simpledialog

class AlunoView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Gerenciar Alunos")
        self.geometry("1200x600")

        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "CPF", "Nascimento", "Telefone", "Email"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)

        frame_btn = tk.Frame(self)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Atualizar Lista", command=self.atualizar_lista).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Inserir Novo", command=self.abrir_form_inserir).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Deletar Selecionado", command=self.deletar_selecionado).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Consultar por CPF", command=self.consultar_por_cpf).pack(side=tk.LEFT, padx=5)

        self.atualizar_lista()

    def atualizar_lista(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        alunos = self.controller.listar_alunos()
        for a in alunos:
            self.tree.insert("", tk.END, values=a)

    def abrir_form_inserir(self):
        FormAluno(self, self.controller)

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um aluno para deletar")
            return
        aluno_id = self.tree.item(selecionado[0])["values"][0]
        self.controller.deletar_aluno(aluno_id)
        self.atualizar_lista()
    def consultar_por_cpf(self):
        cpf = tk.simpledialog.askstring("Consultar CPF", "Digite o CPF do aluno:")
        if not cpf:
            return
        aluno = self.controller.consultar_aluno(cpf)
        if aluno:
            messagebox.showinfo("Aluno Encontrado", f"""
            ID: {aluno[0]}
            Nome: {aluno[1]}
            CPF: {aluno[2]}
            Nascimento: {aluno[3]}
            Telefone: {aluno[4]}
            Email: {aluno[5]}
            """)
        else:
            messagebox.showwarning("Não encontrado", "Aluno com esse CPF não foi encontrado.")


class FormAluno(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Inserir Novo Aluno")
        self.geometry("400x300")

        labels = ["Nome Completo", "CPF", "Data Nascimento (YYYY-MM-DD)", "Telefone", "Email"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self, text=text).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[text] = entry

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def salvar(self):
        try:
            nome = self.entries["Nome Completo"].get()
            cpf = self.entries["CPF"].get()
            nascimento = self.entries["Data Nascimento (YYYY-MM-DD)"].get()
            telefone = self.entries["Telefone"].get()
            email = self.entries["Email"].get()
            self.controller.inserir_aluno(nome, cpf, nascimento, telefone, email)
            self.master.atualizar_lista()
            self.destroy()
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Falha ao salvar aluno: {e}")
