#!/usr/bin/env/python3
#-*- coding: utf-8 -*-

import sqlite3

class Novo_tutorial:
	def __init__(self):
		self.conexao = sqlite3.connect("banco", timeout=1)
		self.conn = self.conexao.cursor()

	def criar_tabela_produtos(self):
		self.criar_tabela = """CREATE TABLE IF NOT EXISTS produtos (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nome TEXT,
				valor NUMERIC,
				descricao TEXT
		);"""
		self.conn.execute(self.criar_tabela)

	def add_dados(self, nome, valor, descricao):
		self.add_dados_tabela = """INSERT INTO produtos 
			VALUES (NULL, '{}', '{}', '{}');""".format(nome, valor, descricao)
		self.conn.execute(self.add_dados_tabela)
		self.conexao.commit()
		print("DADOS ADICIONADOS COM SUCESSO!")

	def consultar_table(self):
		self.consulta = "SELECT id FROM produtos"
		self.realizada = self.conn.execute(self.consulta)
		print(self.realizada.fetchall())

	def update_dados(self, nome, id):
		self.fazer_update = "UPDATE `produtos` SET `nome`='{}' WHERE rowid={};".format(nome, id)
		self.conn.execute(self.fazer_update)
		self.conexao.commit()
		print("DADOS ALTERADOS COM SUCESSO!")

Novo_tutorial().update_dados('Arroz', '1')