"""
Unit Test

Introdução ao módulo UnitTest

Unittest -> Testes Unitários

Oque são testes unitários?

Teste unitário é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

#OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que hgerdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

Método                      Checa que
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               x é verdadeiro
assertFalse(x)              x é falso
assertIs(a, b)              a é b
assertIsNot(a, b)           a não é b
assertIsNone(x)             x é None
assertIsNotNone(x)          x não é None
assertIn(a, b)              a está em b
assertNotIn(a, b)           a não está em b
assertIsInstance(a, b)      a é instancia de b
asserNotIsInstance(a, b)    a não é instância de b

Por convenção, todos os testes em um test case, devem ter seu nome
iniviado com test_ exemplo: test_comer

# Para exercutar os testes com unittest

python nome_do_modulo.py

#Para exercutar os testes com unittest no modo verbose

python nome_do_modulo -v

#Docstrings
"""

#Prática - Utilizando a abordagem TDD
