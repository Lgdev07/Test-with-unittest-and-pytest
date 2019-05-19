from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def vini():
    return Usuario('Vini', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtratir_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0

def test_deve_permitir_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_for_igual_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_saldo_da_carteira(vini, leilao):
    with pytest.raises(LanceInvalido):
        vini.propoe_lance(leilao, 200.0)

        assert vini.carteira == 100.0