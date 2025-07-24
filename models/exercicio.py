from db.conn import Conn

class Exercicio:
    def __init__(self):
        self.conn = Conn().conectar()

    def inserir(self, nome, grupo_muscular, descricao):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                INSERT INTO academia.exercicio (nome, grupo_muscular, descricao)
                VALUES (%s, %s, %s)
            """, (nome, grupo_muscular, descricao))
            self.conn.commit()
            print("[INFO] Exercício inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir exercício: {e}")

    def atualizar(self, id, nome, grupo_muscular, descricao):
        try:
            cur = self.conn.cursor()
            cur.execute("""
                UPDATE academia.exercicio
                SET nome = %s, grupo_muscular = %s, descricao = %s
                WHERE id = %s
            """, (nome, grupo_muscular, descricao, id))
            self.conn.commit()
            print("[INFO] Exercício atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar exercício: {e}")

    def deletar(self, id):
        try:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM academia.exercicio WHERE id = %s", (id,))
            self.conn.commit()
            print("[INFO] Exercício deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar exercício: {e}")

    def consultar(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM academia.exercicio")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar exercícios: {e}")
            return []

    def listar_todos(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT id, nome, grupo_muscular FROM academia.exercicio ORDER BY nome")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao listar exercícios: {e}")
            return []