import psycopg2

class Conn:
    def __init__(self, dbname='postgres', user='postgres', password='123', host='localhost', port='5432'):
        self.conn = None
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print(f"[INFO] Conectado ao banco '{self.dbname}'")
            return self.conn
        except psycopg2.Error as e:
            print(f"[ERRO] Falha na conexão com o PostgreSQL: {e}")
            return None

    def desconectar(self):
        if self.conn:
            self.conn.close()
            print(f"[INFO] Desconectado do banco '{self.dbname}'")
            self.conn = None
