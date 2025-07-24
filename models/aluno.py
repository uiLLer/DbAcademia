from db.conn import Conn

class Aluno:
    def __init__(self, id=None, nome_completo=None, cpf=None, data_nascimento=None, telefone=None, email=None):
        self.id = id
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email

    @staticmethod
    def inserir(nome_completo, cpf, data_nascimento, telefone, email):
        conn = Conn().conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO academia.Aluno (nome_completo, cpf, data_nascimento, telefone, email)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome_completo, cpf, data_nascimento, telefone, email))
        conn.commit()
        conn.close()

    @staticmethod
    def atualizar(id, nome_completo, cpf, data_nascimento, telefone, email):
        conn = Conn().conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE academia.Aluno SET nome_completo=%s, cpf=%s, data_nascimento=%s, telefone=%s, email=%s
            WHERE id=%s
        """, (nome_completo, cpf, data_nascimento, telefone, email, id))
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(id):
        conn = Conn().conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM academia.Aluno WHERE id=%s", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def listar_todos():
        conn = Conn().conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM academia.Aluno")
        alunos = cursor.fetchall()
        conn.close()
        return alunos

    @staticmethod
    def consultar_por_cpf(cpf):
        conn = Conn().conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM academia.Aluno WHERE cpf = %s", (cpf,))
        aluno = cursor.fetchone()
        conn.close()
        return aluno

