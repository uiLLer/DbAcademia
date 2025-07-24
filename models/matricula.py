from db.conn import Conn

class Matricula:
    def __init__(self):
        self.conn = Conn().conectar()

    def inserir(self, aluno_id, plano_id, data_inicio, data_fim):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO academia.matricula (aluno_id, plano_id, data_inicio, data_fim)
                VALUES (%s, %s, %s, %s)
            """, (aluno_id, plano_id, data_inicio, data_fim))
            self.conn.commit()
            print("[INFO] Matrícula inserida com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir matrícula: {e}")

    def atualizar(self, id, aluno_id, plano_id, data_inicio, data_fim):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                UPDATE academia.matricula
                SET aluno_id = %s, plano_id = %s, data_inicio = %s, data_fim = %s
                WHERE id = %s
            """, (aluno_id, plano_id, data_inicio, data_fim, id))
            self.conn.commit()
            print("[INFO] Matrícula atualizada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar matrícula: {e}")

    def deletar(self, id):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM academia.matricula WHERE id = %s", (id,))
            self.conn.commit()
            print("[INFO] Matrícula deletada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar matrícula: {e}")

    def consultar(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM academia.matricula")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar matrículas: {e}")
            return []

    def listar_todos(self):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                SELECT id, aluno_id, plano_id, data_inicio, data_fim 
                FROM academia.matricula 
                ORDER BY data_inicio DESC
            """)
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao listar matrículas: {e}")
            return []