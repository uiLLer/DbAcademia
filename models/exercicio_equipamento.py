from db.conn import Conn

class ExercicioEquipamento:
    @classmethod
    def inserir(cls, exercicio_id, equipamento_id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO academia.exercicio_equipamento (exercicio_id, equipamento_id)
                VALUES (%s, %s)
            """, (exercicio_id, equipamento_id))
            conn.commit()
            print("[INFO] Associação exercício-equipamento inserida com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir associação exercício-equipamento: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def deletar(cls, exercicio_id, equipamento_id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM academia.exercicio_equipamento
                WHERE exercicio_id = %s AND equipamento_id = %s
            """, (exercicio_id, equipamento_id))
            conn.commit()
            print("[INFO] Associação exercício-equipamento deletada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar associação exercício-equipamento: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def consultar(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM academia.exercicio_equipamento")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao consultar associações exercício-equipamento: {e}")
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
                SELECT exercicio_id, equipamento_id 
                FROM academia.exercicio_equipamento 
                ORDER BY exercicio_id, equipamento_id
            """)
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao listar associações exercício-equipamento: {e}")
            return []
        finally:
            cur.close()
            conn.close()
