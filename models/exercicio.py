from db.conn import Conn

class Exercicio:
    @classmethod
    def inserir(cls, nome, grupo_muscular, descricao):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO academia.exercicio (nome, grupo_muscular, descricao)
                VALUES (%s, %s, %s)
            """, (nome, grupo_muscular, descricao))
            conn.commit()
            print("[INFO] Exercício inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir exercício: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def atualizar(cls, id, nome, grupo_muscular, descricao):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                UPDATE academia.exercicio
                SET nome = %s, grupo_muscular = %s, descricao = %s
                WHERE id = %s
            """, (nome, grupo_muscular, descricao, id))
            conn.commit()
            print("[INFO] Exercício atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar exercício: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def deletar(cls, id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM academia.exercicio WHERE id = %s", (id,))
            conn.commit()
            print("[INFO] Exercício deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar exercício: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def consultar(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM academia.exercicio")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao consultar exercícios: {e}")
            return []
        finally:
            cur.close()
            conn.close()

    @classmethod
    def listar_todos(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT id, nome, grupo_muscular FROM academia.exercicio ORDER BY nome")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao listar exercícios: {e}")
            return []
        finally:
            cur.close()
            conn.close()
