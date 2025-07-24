from db.conn import Conn

class FichaTreinoExercicio:
    @classmethod
    def inserir(cls, ficha_treino_id, exercicio_id, series, repeticoes, ordem):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO academia.ficha_treino_exercicio (ficha_treino_id, exercicio_id, series, repeticoes, ordem)
                VALUES (%s, %s, %s, %s, %s)
            """, (ficha_treino_id, exercicio_id, series, repeticoes, ordem))
            conn.commit()
            print("[INFO] Detalhe da ficha de treino inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir detalhe da ficha de treino: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def atualizar(cls, ficha_treino_id, exercicio_id, series, repeticoes, ordem):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                UPDATE academia.ficha_treino_exercicio
                SET series = %s, repeticoes = %s, ordem = %s
                WHERE ficha_treino_id = %s AND exercicio_id = %s
            """, (series, repeticoes, ordem, ficha_treino_id, exercicio_id))
            conn.commit()
            print("[INFO] Detalhe da ficha de treino atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar detalhe da ficha de treino: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def deletar(cls, ficha_treino_id, exercicio_id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM academia.ficha_treino_exercicio
                WHERE ficha_treino_id = %s AND exercicio_id = %s
            """, (ficha_treino_id, exercicio_id))
            conn.commit()
            print("[INFO] Detalhe da ficha de treino deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar detalhe da ficha de treino: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def consultar(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM academia.ficha_treino_exercicio")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao consultar detalhes da ficha de treino: {e}")
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
                SELECT ficha_treino_id, exercicio_id, series, repeticoes, ordem 
                FROM academia.ficha_treino_exercicio 
                ORDER BY ficha_treino_id, ordem
            """)
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao listar detalhes da ficha de treino: {e}")
            return []
        finally:
            cur.close()
            conn.close()
