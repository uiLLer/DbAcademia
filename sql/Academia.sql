-- Criar schema
CREATE SCHEMA academia;

-- Alunos
CREATE TABLE academia.aluno (
    id SERIAL PRIMARY KEY,
    nome_completo VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Planos
CREATE TABLE academia.plano (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    duracao_meses INTEGER NOT NULL CHECK (duracao_meses > 0),
    valor NUMERIC(10, 2) NOT NULL CHECK (valor >= 0)
);

-- Matrículas
CREATE TABLE academia.matricula (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL REFERENCES academia.aluno(id),
    plano_id INTEGER NOT NULL REFERENCES academia.plano(id),
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    CHECK (data_fim > data_inicio)
);

-- Acessos
CREATE TABLE academia.acesso (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL REFERENCES academia.aluno(id),
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Instrutores
CREATE TABLE academia.instrutor (
    id SERIAL PRIMARY KEY,
    nome_completo VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Equipamentos
CREATE TABLE academia.equipamento (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

-- Exercícios
CREATE TABLE academia.exercicio (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    grupo_muscular VARCHAR(50),
    descricao TEXT
);

-- Associação entre Exercícios e Equipamentos (muitos-para-muitos)
CREATE TABLE academia.exercicio_equipamento (
    exercicio_id INTEGER NOT NULL REFERENCES academia.exercicio(id) ON DELETE CASCADE,
    equipamento_id INTEGER NOT NULL REFERENCES academia.equipamento(id) ON DELETE CASCADE,
    PRIMARY KEY (exercicio_id, equipamento_id)
);

-- Fichas de Treino
CREATE TABLE academia.ficha_treino (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL REFERENCES academia.aluno(id),
    instrutor_id INTEGER NOT NULL REFERENCES academia.instrutor(id),
    data_criacao DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Detalhes da Ficha de Treino: exercícios e configurações
CREATE TABLE academia.ficha_treino_exercicio (
    ficha_treino_id INTEGER NOT NULL REFERENCES academia.ficha_treino(id) ON DELETE CASCADE,
    exercicio_id INTEGER NOT NULL REFERENCES academia.exercicio(id),
    series INTEGER NOT NULL CHECK (series > 0),
    repeticoes INTEGER NOT NULL CHECK (repeticoes > 0),
    ordem INTEGER NOT NULL CHECK (ordem > 0),
    PRIMARY KEY (ficha_treino_id, exercicio_id)
);
