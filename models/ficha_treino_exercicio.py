from db.conn import Conn

class FichaTreinoExercicio:
    def __init__(self):
        self.conn = Conn().conectar()

    def inserir(self, ficha_treino_id, exercicio_id, series, repeticoes, ordem):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO academia.ficha_treino_exercicio (ficha_treino_id, exercicio_id, series, repeticoes, ordem)
                VALUES (%s, %s, %s, %s, %s)
            """, (ficha_treino_id, exercicio_id, series, repeticoes, ordem))
            self.conn.commit()
            print("[INFO] Detalhe da ficha de treino inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir detalhe da ficha de treino: {e}")

    def atualizar(self, ficha_treino_id, exercicio_id, series, repeticoes, ordem):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                UPDATE academia.ficha_treino_exercicio
                SET series = %s, repeticoes = %s, ordem = %s
                WHERE ficha_treino_id = %s AND exercicio_id = %s
            """, (series, repeticoes, ordem, ficha_treino_id, exercicio_id))
            self.conn.commit()
            print("[INFO] Detalhe da ficha de treino atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar detalhe da ficha de treino: {e}")

    def deletar(self, ficha_treino_id, exercicio_id):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                DELETE FROM academia.ficha_treino_exercicio
                WHERE ficha_treino_id = %s AND exercicio_id = %s
            """, (ficha_treino_id, exercicio_id))
            self.conn.commit()
            print("[INFO] Detalhe da ficha de treino deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar detalhe da ficha de treino: {e}")

    def consultar(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM academia.ficha_treino_exercicio")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar detalhes da ficha de treino: {e}")
            return []

    def listar_todos(self):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                SELECT ficha_treino_id, exercicio_id, series, repeticoes, ordem 
                FROM academia.ficha_treino_exercicio 
                ORDER BY ficha_treino_id, ordem
            """)
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao listar detalhes da ficha de treino: {e}")
            return []