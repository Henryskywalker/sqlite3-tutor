#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sqlite3

class SegundoTutorial:
	def __init__(self):
		self.conexao = sqlite3.connect("banco")

	def adiocionar_dados(self, nome, sobrenome, endereco):
		self.conexao.execute("INSERT INTO usuarios VALUES (NULL, '{nome}', '{sobrenome}','{endereco}')".format(nome=nome, sobrenome=sobrenome, endereco=endereco))
		self.conexao.commit()

SegundoTutorial().adiocionar_dados('Henrique', 'Nascimento', 'Rua do Comercio')