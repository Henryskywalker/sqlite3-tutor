#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sqlite3

class Classe_consulta:
	def __init__(self):
		self.conexao = sqlite3.connect("banco", timeout=1)
		self.conn = self.conexao.cursor()

	def consultar(self):
		self.listar = self.conn.execute("SELECT * FROM usuarios")
		print(self.listar.fetchall())

Classe_consulta().consultar()