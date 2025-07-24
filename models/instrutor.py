from db.conn import Conn

class Instrutor:
    def __init__(self):
        self.conn = Conn().conectar()

    def inserir(self, nome_completo, cpf, telefone, email):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO academia.instrutor (nome_completo, cpf, telefone, email)
                VALUES (%s, %s, %s, %s)
            """, (nome_completo, cpf, telefone, email))
            self.conn.commit()
            print("[INFO] Instrutor inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir instrutor: {e}")

    def atualizar(self, id, nome_completo, cpf, telefone, email):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                UPDATE academia.instrutor
                SET nome_completo = %s, cpf = %s, telefone = %s, email = %s
                WHERE id = %s
            """, (nome_completo, cpf, telefone, email, id))
            self.conn.commit()
            print("[INFO] Instrutor atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar instrutor: {e}")

    def deletar(self, id):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM academia.instrutor WHERE id = %s", (id,))
            self.conn.commit()
            print("[INFO] Instrutor deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar instrutor: {e}")

    def consultar(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM academia.instrutor")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar instrutores: {e}")
            return []

    def listar_todos(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT id, nome_completo FROM academia.instrutor ORDER BY nome_completo")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao listar instrutores: {e}")
            return []