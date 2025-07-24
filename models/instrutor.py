from db.conn import Conn

class Instrutor:
    @classmethod
    def inserir(cls, nome_completo, cpf, telefone, email):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO academia.instrutor (nome_completo, cpf, telefone, email)
                VALUES (%s, %s, %s, %s)
            """, (nome_completo, cpf, telefone, email))
            conn.commit()
            print("[INFO] Instrutor inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir instrutor: {e}")

    @classmethod
    def atualizar(cls, id, nome_completo, cpf, telefone, email):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                UPDATE academia.instrutor
                SET nome_completo = %s, cpf = %s, telefone = %s, email = %s
                WHERE id = %s
            """, (nome_completo, cpf, telefone, email, id))
            conn.commit()
            print("[INFO] Instrutor atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar instrutor: {e}")

    @classmethod
    def deletar(cls, id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM academia.instrutor WHERE id = %s", (id,))
            conn.commit()
            print("[INFO] Instrutor deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar instrutor: {e}")

    @classmethod
    def consultar_todos(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT id, nome_completo, cpf, telefone, email FROM academia.instrutor ORDER BY nome_completo")
            return cur.fetchall()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar instrutores: {e}")
            return []

    @classmethod
    def consultar_por_cpf(cls, cpf):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT id, nome_completo, cpf, telefone, email FROM academia.instrutor WHERE cpf = %s", (cpf,))
            return cur.fetchone()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar por CPF: {e}")
            return None

    @classmethod
    def consultar_por_id(cls, id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM academia.instrutor WHERE id = %s", (id,))
            return cur.fetchone()
        except Exception as e:
            print(f"[ERRO] Falha ao consultar instrutor por id: {e}")
            return None
