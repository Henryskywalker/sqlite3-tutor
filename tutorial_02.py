#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sqlite3

class SegundoTutorial:
	def __init__(self):
		self.conexao = sqlite3.connect("banco", timeout=1)
		#self.cursor

	def adiocionar_dados(self, nome, sobrenome, endereco):
		self.conexao.execute("INSERT INTO usuarios VALUES (NULL, '{nome}', '{sobrenome}','{endereco}')".format(nome=nome, sobrenome=sobrenome, endereco=endereco))
		self.conexao.commit()

	def consultar_tabela(self):
		self.verifica = self.conexao.execute("SELECT nome FROM usuarios")
		for i in self.verifica:
			print(i)

	def alteracao_nome(self, nome, id):
		self.conexao.execute("UPDATE `usuarios` SET `nome`='{nome}' WHERE `id`='{id}'".format(nome=nome, id=id))
		self.conexao.commit()

SegundoTutorial().alteracao_nome("Carlos", "1")
#SegundoTutorial().adiocionar_dados('Fernando','Porto','25')