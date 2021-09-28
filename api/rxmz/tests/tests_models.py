
from django.test import TestCase
from rxmz.models import Recibos

class TestModelRecibos(TestCase):
    def setUp(self)->None:        
        self.recibo = Recibos.objects.create(
            titulo = 'Titulo teste',
            descricao = 'Descrição teste',
            data = '2021-09-28'
        )
    
    def test_buscar_recibo(self):
        resultado = Recibos.objects.get(pk=1)
        self.assertEqual(self.recibo, resultado)