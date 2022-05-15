INSERT INTO tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_lista) VALUES (
'1037797', 'Clean - 2 Litros - Laranja', 'PET', '2 Litros', 'Laranja', 16.1)

INSERT INTO tbproduto (codigo_produto, nome_produto, embalagem, tamanho, sabor, preco_lista) VALUES
('544931', 'Frescor do Verão - 350 ml - Limão', 'PET', '350 ml','Limão',3.20);

UPDATE tbproduto SET embalagem = 'Lata', preco_lista = 2.46 WHERE codigo_produto = '544931';

DELETE FROM tbproduto
WHERE codigo_produto = '1078680';

ALTER TABLE tbproduto ADD PRIMARY KEY (codigo_produto);