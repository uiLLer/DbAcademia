from db.conn import Conn

class FichaTreino:
    def __init__(self):
        self.conn = Conn().conectar()

    def inserir(self, aluno_id, instrutor_id, data_criacao):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO academia.ficha_treino (aluno_id, instrutor_id, data_criacao)
                VALUES (%s, %s, %s)
            """, (aluno_id, instrutor_id, data_criacao))
            self.conn.commit()
            print("[INFO] Ficha de treino inserida com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir ficha de treino: {e}")

    def atualizar(self, id, aluno_id, instrutor_id, data_criacao):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                UPDATE academia.ficha_treino
                SET aluno_id = %s, instrutor_id = %s, data_criacao = %s
                WHERE id = %s
            """, (aluno_id, instrutor_id, data_criacao, id))
            self.conn.commit()
            print("[INFO] Ficha de treino atualizada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar ficha de treino: {e}")

    def deletar(self, id):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM academia.ficha_treino WHERE id = %s", (id,))
            self.conn.commit()
            print("[INFO] Ficha de treino deletada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar ficha de treino: {e}")

    def consultar(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM academia.ficha_treino")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar fichas de treino: {e}")
            return []

    def listar_todos(self):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                SELECT id, aluno_id, instrutor_id, data_criacao 
                FROM academia.ficha_treino 
                ORDER BY data_criacao DESC
            """)
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao listar fichas de treino: {e}")
            return []