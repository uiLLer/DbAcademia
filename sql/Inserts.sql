

INSERT INTO academia.aluno (id,nome_completo, cpf, data_nascimento, telefone, email)
VALUES 
  (2,'João da Silva', '123.456.789-00', '1990-05-20', '11999999999', 'joao.silva@email.com'),
  (3,'Maria Oliveira', '987.654.321-00', '1985-11-15', '11888888888', 'maria.oliveira@email.com');

INSERT INTO academia.plano (id, nome, duracao_meses, valor)
VALUES 
  (1,'Mensal', 1, 100.00),
  (2,'Trimestral', 3, 270.00),
  (3,'Anual', 12, 960.00);



INSERT INTO academia.equipamento (id, nome, descricao)
VALUES 
  (1, 'Leg Press', 'Equipamento para treino de pernas'),
  (2, 'Supino Reto', 'Equipamento para treino de peito');

INSERT INTO academia.exercicio (id, nome, grupo_muscular, descricao)
VALUES 
  (1, 'Agachamento', 'Pernas', 'Agachamento livre com barra'),
  (2, 'Supino', 'Peito', 'Supino com barra no banco reto');

INSERT INTO academia.exercicio_equipamento (exercicio_id, equipamento_id)
VALUES 
  (1, 1),
  (2, 2);

INSERT INTO academia.instrutor (nome_completo, cpf, telefone, email)
VALUES 
  ('Carlos Personal', '111.222.333-44', '11777777777', 'carlos.personal@email.com');

INSERT INTO academia.ficha_treino (id, aluno_id, instrutor_id)
VALUES 
  (1, 1, 1);

INSERT INTO academia.ficha_treino_exercicio (ficha_treino_id, exercicio_id, series, repeticoes, ordem)
VALUES 
  (1, 1, 4, 12, 1),
  (1, 2, 3, 10, 2);


  
-- Matrícula ativa
INSERT INTO academia.matricula (aluno_id, plano_id, data_inicio, data_fim)
VALUES 
  (1, 2, CURRENT_DATE - INTERVAL '15 days', CURRENT_DATE + INTERVAL '2 months');

-- Matrícula inativa
INSERT INTO academia.matricula (aluno_id, plano_id, data_inicio, data_fim)
VALUES 
  (2, 1, '2024-01-01', '2024-01-31');