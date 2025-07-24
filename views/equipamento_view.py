import tkinter as tk
from tkinter import ttk, messagebox

class EquipamentoView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Equipamentos")
        self.geometry("600x400")

        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Descrição"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Descrição", text="Descrição")
        self.tree.pack(fill=tk.BOTH, expand=True)

        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Atualizar Lista", command=self.atualizar_lista).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Adicionar", command=self.abrir_form_adicionar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Atualizar Selecionado", command=self.abrir_form_atualizar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Deletar Selecionado", command=self.deletar_selecionado).pack(side=tk.LEFT, padx=5)

        self.atualizar_lista()

    def atualizar_lista(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        equipamentos = self.controller.listar_equipamentos()
        for eq in equipamentos:
            self.tree.insert("", tk.END, values=eq)

    def abrir_form_adicionar(self):
        FormEquipamento(self, self.controller, modo="adicionar")

    def abrir_form_atualizar(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um equipamento para atualizar")
            return
        valores = self.tree.item(selecionado[0])["values"]
        FormEquipamento(self, self.controller, modo="atualizar", equipamento=valores)

    def deletar_selecionado(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um equipamento para deletar")
            return
        id = self.tree.item(selecionado[0])["values"][0]
        self.controller.deletar_equipamento(id)
        self.atualizar_lista()


class FormEquipamento(tk.Toplevel):
    def __init__(self, master, controller, modo="adicionar", equipamento=None):
        super().__init__(master)
        self.controller = controller
        self.master = master
        self.modo = modo
        self.equipamento = equipamento

        self.title("Adicionar Equipamento" if modo == "adicionar" else "Atualizar Equipamento")
        self.geometry("400x200")

        tk.Label(self, text="Nome").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_nome = tk.Entry(self, width=40)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Descrição").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry_descricao = tk.Entry(self, width=40)
        self.entry_descricao.grid(row=1, column=1, padx=10, pady=10)

        if modo == "atualizar" and equipamento:
            self.entry_nome.insert(0, equipamento[1])
            self.entry_descricao.insert(0, equipamento[2])

        btn_text = "Salvar" if modo == "adicionar" else "Atualizar"
        tk.Button(self, text=btn_text, command=self.salvar).grid(row=2, column=0, columnspan=2, pady=20)

    def salvar(self):
        nome = self.entry_nome.get()
        descricao = self.entry_descricao.get()

        if not nome:
            messagebox.showwarning("Aviso", "O campo nome é obrigatório.")
            return

        if self.modo == "adicionar":
            self.controller.inserir_equipamento(nome, descricao)
        else:
            id = self.equipamento[0]
            self.controller.atualizar_equipamento(id, nome, descricao)

        self.master.atualizar_lista()
        self.destroy()
