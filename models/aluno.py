# models/aluno.py
from conn import Conn  # Supondo que Conn está em conn.py

class Aluno:
    def __init__(self, nome_completo, cpf, data_nascimento, telefone=None, email=None, id=None):
        self.id = id
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email

    def inserir(self):
        db = Conn()
        conn = db.conectar()
        if not conn:
            return None

        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO academia.aluno (nome_completo, cpf, data_nascimento, telefone, email)
                VALUES (%s, %s, %s, %s, %s) RETURNING id
            """, (self.nome_completo, self.cpf, self.data_nascimento, self.telefone, self.email))
            self.id = cur.fetchone()[0]
            conn.commit()
            print(f"[INFO] Aluno inserido com ID: {self.id}")
        except Exception as e:
            print(f"[ERRO] Falha ao inserir aluno: {e}")
            conn.rollback()
        finally:
            cur.close()
            db.desconectar()
        return self.id

    def atualizar(self):
        if not self.id:
            print("[ERRO] ID do aluno não definido para atualização.")
            return

        db = Conn()
        conn = db.conectar()
        cur = conn.cursor()
        try:
            cur.execute("""
                UPDATE academia.aluno
                SET nome_completo = %s, cpf = %s, data_nascimento = %s, telefone = %s, email = %s
                WHERE id = %s
            """, (self.nome_completo, self.cpf, self.data_nascimento, self.telefone, self.email, self.id))
            conn.commit()
            print("[INFO] Aluno atualizado com sucesso.")
        except Exception as e:
            print(f"[ERRO] Falha ao atualizar aluno: {e}")
            conn.rollback()
        finally:
            cur.close()
            db.desconectar()

    def deletar(self):
        if not self.id:
            print("[ERRO] ID do aluno não definido para exclusão.")
            return

        db = Conn()
        conn = db.conectar()
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM academia.aluno WHERE id = %s", (self.id,))
            conn.commit()
            print(f"[INFO] Aluno ID {self.id} deletado.")
        except Exception as e:
            print(f"[ERRO] Falha ao deletar aluno: {e}")
            conn.rollback()
        finally:
            cur.close()
            db.desconectar()

    @staticmethod
    def consultar(id):
        db = Conn()
        conn = db.conectar()
        cur = conn.cursor()
        aluno = None
        try:
            cur.execute("SELECT id, nome_completo, cpf, data_nascimento, telefone, email FROM academia.aluno WHERE id = %s", (id,))
            row = cur.fetchone()
            if row:
                aluno = Aluno(*row[1:], id=row[0])
        except Exception as e:
            print(f"[ERRO] Falha ao consultar aluno: {e}")
        finally:
            cur.close()
            db.desconectar()
        return aluno

    @staticmethod
    def listar_todos():
        db = Conn()
        conn = db.conectar()
        cur = conn.cursor()
        alunos = []
        try:
            cur.execute("SELECT id, nome_completo, cpf, data_nascimento, telefone, email FROM academia.aluno")
            rows = cur.fetchall()
            for row in rows:
                alunos.append(Aluno(*row[1:], id=row[0]))
        except Exception as e:
            print(f"[ERRO] Falha ao listar alunos: {e}")
        finally:
            cur.close()
            db.desconectar()
        return alunos
