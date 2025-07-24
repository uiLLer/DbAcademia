from db.conn import Conn

class FichaTreino:
    @classmethod
    def inserir(cls, aluno_id, instrutor_id, data_criacao):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO academia.ficha_treino (aluno_id, instrutor_id, data_criacao)
                VALUES (%s, %s, %s)
            """, (aluno_id, instrutor_id, data_criacao))
            conn.commit()
            print("[INFO] Ficha de treino inserida com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir ficha de treino: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def atualizar(cls, id, aluno_id, instrutor_id, data_criacao):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                UPDATE academia.ficha_treino
                SET aluno_id = %s, instrutor_id = %s, data_criacao = %s
                WHERE id = %s
            """, (aluno_id, instrutor_id, data_criacao, id))
            conn.commit()
            print("[INFO] Ficha de treino atualizada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar ficha de treino: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def deletar(cls, id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM academia.ficha_treino WHERE id = %s", (id,))
            conn.commit()
            print("[INFO] Ficha de treino deletada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar ficha de treino: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def consultar(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM academia.ficha_treino")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao consultar fichas de treino: {e}")
            return []
        finally:
            cur.close()
            conn.close()

    @classmethod
    def listar_todos(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                SELECT id, aluno_id, instrutor_id, data_criacao 
                FROM academia.ficha_treino 
                ORDER BY data_criacao DESC
            """)
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao listar fichas de treino: {e}")
            return []
        finally:
            cur.close()
            conn.close()
