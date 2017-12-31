#! /usr/bin/env python3
#-*- coding: utf-8 -*-

import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect("banco")
    
    def criar_tabela(self):
        self.conexao.execute("""CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            sobrenome TEXT,
            endereco TEXT
        );
        """)
        print("criado!")

Banco().criar_tabela()