"""""
PEP8- Python Emnhancement Proposal

São propostas de melhorias para a linguagem python

Zem of python
import this

A ideia da pep8 é que possamos escrever códigos de forma pythonica

1-Camel Case em nome de classes (Maiúsculo):

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

2-Utilize nomes em minúsculo, separados por underline para funções ou variaveis:

def soma():
    pass

def soma_valores():
    pass

numero = 4
numero_impar = 3

3-Utilize 4 espaços para identação(**IMPORTANTE**):

if 'a' in 'banana':
    print('tem')

4-linhas em branco: separar classe e funções em 2 espaços (enter)
-Métodos dentro de uma classe devem ser separados por apenas uma linha em branco;

5-Imports devem ser feitos sempre em linhas separadas:

import sys, os --erraso

import sys--correto
import os

-caso sejam vários imports:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

6-Espaços em expressões:
ERRADO!ADO!
funcao( algo[ 1 ], { outro: 2 }--)ERRADO!!

7-Termine sempre uma instrução com uma nova linha em branco
"""
