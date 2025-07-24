from db.conn import Conn

class ExercicioEquipamento:
    def __init__(self):
        self.conn = Conn().conectar()

    def inserir(self, exercicio_id, equipamento_id):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO academia.exercicio_equipamento (exercicio_id, equipamento_id)
                VALUES (%s, %s)
            """, (exercicio_id, equipamento_id))
            self.conn.commit()
            print("[INFO] Associação exercício-equipamento inserida com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir associação exercício-equipamento: {e}")

    def deletar(self, exercicio_id, equipamento_id):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                DELETE FROM academia.exercicio_equipamento
                WHERE exercicio_id = %s AND equipamento_id = %s
            """, (exercicio_id, equipamento_id))
            self.conn.commit()
            print("[INFO] Associação exercício-equipamento deletada com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar associação exercício-equipamento: {e}")

    def consultar(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM academia.exercicio_equipamento")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar associações exercício-equipamento: {e}")
            return []

    def listar_todos(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT exercicio_id, equipamento_id FROM academia.exercicio_equipamento ORDER BY exercicio_id, equipamento_id")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao listar associações exercício-equipamento: {e}")
            return []