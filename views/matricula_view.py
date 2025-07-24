import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog

class MatriculaView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Gerenciar Matrículas")
        self.geometry("800x400")

        self.tree = ttk.Treeview(self, columns=("ID", "Aluno ID", "Plano ID", "Data Início", "Data Fim"), show="headings")
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
        matriculas = self.controller.listar_matriculas()
        for m in matriculas:
            self.tree.insert("", tk.END, values=m)

    def abrir_form_inserir(self):
        FormMatricula(self, self.controller)

    def abrir_form_atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma matrícula para atualizar")
            return
        matricula_id = self.tree.item(selecionado[0])["values"][0]
        dados = self.controller.buscar_matricula_por_id(matricula_id)
        if dados:
            FormMatricula(self, self.controller, dados)
        else:
            messagebox.showerror("Erro", "Falha ao carregar dados da matrícula")

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma matrícula para deletar")
            return
        matricula_id = self.tree.item(selecionado[0])["values"][0]
        self.controller.deletar_matricula(matricula_id)
        self.atualizar_lista()

class FormMatricula(tk.Toplevel):
    def __init__(self, master, controller, dados=None):
        super().__init__(master)
        self.controller = controller
        self.dados = dados
        self.title("Inserir Nova Matrícula" if dados is None else "Atualizar Matrícula")
        self.geometry("400x300")

        labels = ["Aluno ID", "Plano ID", "Data Início (YYYY-MM-DD)", "Data Fim (YYYY-MM-DD)"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(self, text=text).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[text] = entry

        if dados:
            self.entries["Aluno ID"].insert(0, dados[1])
            self.entries["Plano ID"].insert(0, dados[2])
            self.entries["Data Início (YYYY-MM-DD)"].insert(0, dados[3])
            self.entries["Data Fim (YYYY-MM-DD)"].insert(0, dados[4])

        tk.Button(self, text="Salvar", command=self.salvar).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def salvar(self):
        try:
            aluno_id = int(self.entries["Aluno ID"].get())
            plano_id = int(self.entries["Plano ID"].get())
            data_inicio = self.entries["Data Início (YYYY-MM-DD)"].get()
            data_fim = self.entries["Data Fim (YYYY-MM-DD)"].get()

            if self.dados:
                id_matricula = self.dados[0]
                self.controller.atualizar_matricula(id_matricula, aluno_id, plano_id, data_inicio, data_fim)
            else:
                self.controller.inserir_matricula(aluno_id, plano_id, data_inicio, data_fim)

            self.master.atualizar_lista()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar matrícula: {e}")
