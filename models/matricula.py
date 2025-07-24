from db.conn import Conn

class Matricula:
    @classmethod
    def inserir(cls, aluno_id, plano_id, data_inicio, data_fim):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO academia.matricula (aluno_id, plano_id, data_inicio, data_fim)
                VALUES (%s, %s, %s, %s)
            """, (aluno_id, plano_id, data_inicio, data_fim))
            conn.commit()
            conn.close()
            print("[INFO] Matrícula inserida com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir matrícula: {e}")

    @classmethod
    def atualizar(cls, id, aluno_id, plano_id, data_inicio, data_fim):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                UPDATE academia.matricula
                SET aluno_id = %s, plano_id = %s, data_inicio = %s, data_fim = %s
                WHERE id = %s
            """, (aluno_id, plano_id, data_inicio, data_fim, id))
            conn.commit()
            conn.close()
            print("[INFO] Matrícula atualizada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar matrícula: {e}")

    @classmethod
    def deletar(cls, id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM academia.matricula WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            print("[INFO] Matrícula deletada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar matrícula: {e}")

    @classmethod
    def listar_todos(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                SELECT id, aluno_id, plano_id, data_inicio, data_fim 
                FROM academia.matricula 
                ORDER BY data_inicio DESC
            """)
            resultados = cur.fetchall()
            conn.close()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao listar matrículas: {e}")
            return []

    @classmethod
    def consultar_por_id(cls, id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM academia.matricula WHERE id = %s", (id,))
            resultado = cur.fetchone()
            conn.close()
            return resultado
        except Exception as e:
            print(f"[ERRO] Falha ao consultar matrícula por id: {e}")
            return None
