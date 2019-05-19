from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui', 500)
        self.yuri = Usuario('Yuri', 500)
        self.luan = Usuario('Luan', 500)
        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.lance_do_luan = Lance(self.luan, 180.0)
        self.leilao = Leilao('Celular')


    def test_deve_retornar_o_maior_e_menor_numero_quando_adicionados_em_ordem_crescente(self):

        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_luan)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 180.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_não_deve_permitir_que_sejam_adicionados_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_luan)
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(self.lance_do_yuri)


    def test_deve_retornar_o_mesmo_valor_para_quando_for_lancado_apenas_um_lance(self):

        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    # se o leilao não tiver lances, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lances_recebida = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebida)

    # se o ultimo usuario for diferente, deve permitir propor o lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        bruna = Usuario('Bruna', 500.0)
        lance__da_bruna = Lance(bruna, 200.0)

        self.leilao.propoe(self.lance_do_luan)
        self.leilao.propoe(lance__da_bruna)

        quantidade_de_lances_recebida = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebida)

    # se o ultimo usuario for o mesmo ele não deve permitir propor o lance
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_luan200 = Lance(self.luan, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_luan)
            self.leilao.propoe(lance_do_luan200)


