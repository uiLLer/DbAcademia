from db.conn import Conn

class Plano:
    def __init__(self, nome, duracao_meses, valor, id=None):
        self.id = id
        self.nome = nome
        self.duracao_meses = duracao_meses
        self.valor = valor

    def inserir(self):
        db = Conn()
        conn = db.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO academia.plano (nome, duracao_meses, valor)
                VALUES (%s, %s, %s) RETURNING id
            """, (self.nome, self.duracao_meses, self.valor))
            self.id = cur.fetchone()[0]
            conn.commit()
        except Exception as e:
            print(f"[ERRO] Falha ao inserir plano: {e}")
            conn.rollback()
        finally:
            cur.close()
            db.desconectar()
        return self.id

    def atualizar(self):
        if not self.id:
            return
        db = Conn()
        conn = db.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""
                UPDATE academia.plano
                SET nome = %s, duracao_meses = %s, valor = %s
                WHERE id = %s
            """, (self.nome, self.duracao_meses, self.valor, self.id))
            conn.commit()
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar plano: {e}")
            conn.rollback()
        finally:
            cur.close()
            db.desconectar()

    def deletar(self):
        if not self.id:
            return
        db = Conn()
        conn = db.conectar()
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM academia.plano WHERE id = %s", (self.id,))
            conn.commit()
        except Exception as e:
            print(f"[ERRO] Falha ao deletar plano: {e}")
            conn.rollback()
        finally:
            cur.close()
            db.desconectar()

    @staticmethod
    def consultar(id):
        db = Conn()
        conn = db.conectar()
        cur = conn.cursor()
        plano = None
        try:
            cur.execute("SELECT id, nome, duracao_meses, valor FROM academia.plano WHERE id = %s", (id,))
            row = cur.fetchone()
            if row:
                plano = Plano(*row[1:], id=row[0])
        except Exception as e:
            print(f"[ERRO] Falha ao consultar plano: {e}")
        finally:
            cur.close()
            db.desconectar()
        return plano

    @staticmethod
    def listar_todos():
        db = Conn()
        conn = db.conectar()
        cur = conn.cursor()
        planos = []
        try:
            cur.execute("SELECT id, nome, duracao_meses, valor FROM academia.plano")
            for row in cur.fetchall():
                planos.append(Plano(*row[1:], id=row[0]))
        except Exception as e:
            print(f"[ERRO] Falha ao listar planos: {e}")
        finally:
            cur.close()
            db.desconectar()
        return planos