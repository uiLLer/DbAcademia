from db.conn import Conn

class Plano:
    def __init__(self, nome=None, duracao_meses=None, valor=None, id=None):
        self.id = id
        self.nome = nome
        self.duracao_meses = duracao_meses
        self.valor = valor

    @classmethod
    def inserir(cls, nome, duracao_meses, valor):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO academia.plano (nome, duracao_meses, valor)
                VALUES (%s, %s, %s) RETURNING id
            """, (nome, duracao_meses, valor))
            id_inserido = cur.fetchone()[0]
            conn.commit()
            return id_inserido
        except Exception as e:
            print(f"[ERRO] Falha ao inserir plano: {e}")
            return None
        finally:
            cur.close()
            conn.close()

    @classmethod
    def atualizar(cls, id, nome, duracao_meses, valor):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("""
                UPDATE academia.plano
                SET nome = %s, duracao_meses = %s, valor = %s
                WHERE id = %s
            """, (nome, duracao_meses, valor, id))
            conn.commit()
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar plano: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def deletar(cls, id):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("DELETE FROM academia.plano WHERE id = %s", (id,))
            conn.commit()
        except Exception as e:
            print(f"[ERRO] Falha ao deletar plano: {e}")
        finally:
            cur.close()
            conn.close()

    @classmethod
    def consultar(cls, id):
        plano = None
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT id, nome, duracao_meses, valor FROM academia.plano WHERE id = %s", (id,))
            row = cur.fetchone()
            if row:
                plano = Plano(*row[1:], id=row[0])
        except Exception as e:
            print(f"[ERRO] Falha ao consultar plano: {e}")
        finally:
            cur.close()
            conn.close()
        return plano

    @classmethod
    def listar_todos(cls):
        planos = []
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT id, nome, duracao_meses, valor FROM academia.plano ORDER BY nome")
            rows = cur.fetchall()
            for row in rows:
                planos.append(Plano(*row[1:], id=row[0]))
        except Exception as e:
            print(f"[ERRO] Falha ao listar planos: {e}")
        finally:
            cur.close()
            conn.close()
        return planos
