
from django.test import TestCase

from rxmz.models import Recibos

class TestModelRecibos(TestCase):
    def setUp(self)->None:
        self.recibo = Recibos(
            titulo = 'Titulo teste',
            descricao = 'Descrição teste',
            data = '2021-09-28'
        )
    
    def test_str_recibo_deve_retornar_dados_do_recibo(self):
        esperado = 'Titulo teste'
        resultado = str(self.recibo)
        self.assertEqual(esperado, resultado)