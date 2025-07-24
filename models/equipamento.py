from db.conn import Conn

class Equipamento:
    @classmethod
    def inserir(cls, nome, descricao):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO academia.equipamento (nome, descricao)
                VALUES (%s, %s)
            """, (nome, descricao))
            conn.commit()
            print("[INFO] Equipamento inserido com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir equipamento: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def atualizar(cls, id, nome, descricao):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                UPDATE academia.equipamento
                SET nome = %s, descricao = %s
                WHERE id = %s
            """, (nome, descricao, id))
            conn.commit()
            print("[INFO] Equipamento atualizado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar equipamento: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def deletar(cls, id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM academia.equipamento WHERE id = %s", (id,))
            conn.commit()
            print("[INFO] Equipamento deletado com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar equipamento: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def consultar(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM academia.equipamento")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao consultar equipamentos: {e}")
            return []
        finally:
            cur.close()
            conn.close()

    @classmethod
    def listar_todos(cls):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT id, nome FROM academia.equipamento ORDER BY nome")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao listar equipamentos: {e}")
            return []
        finally:
            cur.close()
            conn.close()
