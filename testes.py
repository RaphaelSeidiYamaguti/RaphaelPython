import unittest

from atividades import comer, dormir, engracada

class AtividadesTestes(unittest.TestCase):
    
    def test_come(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )
    def test_comer_gostosa(self):
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormindo_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas.'
        )
    
    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Dormi muito! Estou atrasado para o trabalho'
        )
    
    def test_engracada(self):
        #self.assertEqual(engracada('Sergio Malandro'), False)
        self.assertFalse(engracada('Sergio Malandro'))
        self.assertTrue(engracada('Jim Carrey'), 'Jim carrey deveria ser engraçado')
if __name__ == '__main__':
    unittest.main()