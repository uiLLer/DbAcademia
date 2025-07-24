from db.conn import Conn

class Acesso:
    def __init__(self):
        self.conn = Conn().conectar()

    def inserir(self, aluno_id, data_hora):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO academia.acesso (aluno_id, data_hora)
                VALUES (%s, %s)
            """, (aluno_id, data_hora))
            self.conn.commit()
            print("[INFO] Acesso inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir acesso: {e}")

    def atualizar(self, id, aluno_id, data_hora):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                UPDATE academia.acesso
                SET aluno_id = %s, data_hora = %s
                WHERE id = %s
            """, (aluno_id, data_hora, id))
            self.conn.commit()
            print("[INFO] Acesso atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar acesso: {e}")

    def deletar(self, id):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM academia.acesso WHERE id = %s", (id,))
            self.conn.commit()
            print("[INFO] Acesso deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar acesso: {e}")

    def consultar(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM academia.acesso")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar acessos: {e}")
            return []
        
    def listar_todos(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT id, aluno_id, data_hora FROM academia.acesso ORDER BY data_hora DESC")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao listar acessos: {e}")
            return []