from db.conn import Conn

class Acesso:
    @classmethod
    def inserir(cls, aluno_id, data_hora):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO academia.acesso (aluno_id, data_hora)
                VALUES (%s, %s)
            """, (aluno_id, data_hora))
            conn.commit()
            print("[INFO] Acesso inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir acesso: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def atualizar(cls, id, aluno_id, data_hora):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                UPDATE academia.acesso
                SET aluno_id = %s, data_hora = %s
                WHERE id = %s
            """, (aluno_id, data_hora, id))
            conn.commit()
            print("[INFO] Acesso atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar acesso: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def deletar(cls, id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM academia.acesso WHERE id = %s", (id,))
            conn.commit()
            print("[INFO] Acesso deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar acesso: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def consultar(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM academia.acesso")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao consultar acessos: {e}")
            return []
        finally:
            cur.close()
            conn.close()

    @classmethod
    def listar_todos(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT id, aluno_id, data_hora FROM academia.acesso ORDER BY data_hora DESC")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao listar acessos: {e}")
            return []
        finally:
            cur.close()
            conn.close()
