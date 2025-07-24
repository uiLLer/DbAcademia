from db.conn import Conn
from views.matriculas_ativas_view import AlunoMatriculaAtivaView

class AlunoMatriculaAtivaController:
    def __init__(self, master):
        self.master = master

    def open_view(self):
        AlunoMatriculaAtivaView(self.master, self)

    def listar_alunos_matriculas_ativas(self):
        try:
            conn = Conn().conectar()
            cur = conn.cursor()
            cur.execute("SELECT * FROM academia.vw_alunos_matriculas_ativas")
            resultados = cur.fetchall()
            return resultados
        except Exception as e:
            print(f"[ERRO] Falha ao listar alunos com matrículas ativas: {e}")
            return []
        finally:
            cur.close()
            conn.close()
