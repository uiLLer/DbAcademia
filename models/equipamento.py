from db.conn import Conn

class Equipamento:
    def __init__(self):
        self.conn = Conn().conectar()

    def inserir(self, nome, descricao):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO academia.equipamento (nome, descricao)
                VALUES (%s, %s)
            """, (nome, descricao))
            self.conn.commit()
            print("[INFO] Equipamento inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir equipamento: {e}")

    def atualizar(self, id, nome, descricao):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                UPDATE academia.equipamento
                SET nome = %s, descricao = %s
                WHERE id = %s
            """, (nome, descricao, id))
            self.conn.commit()
            print("[INFO] Equipamento atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar equipamento: {e}")

    def deletar(self, id):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM academia.equipamento WHERE id = %s", (id,))
            self.conn.commit()
            print("[INFO] Equipamento deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar equipamento: {e}")

    def consultar(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM academia.equipamento")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar equipamentos: {e}")
            return []

    def listar_todos(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT id, nome FROM academia.equipamento ORDER BY nome")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao listar equipamentos: {e}")
            return []