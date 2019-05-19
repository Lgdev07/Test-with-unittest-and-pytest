from src.leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self.valor_e_valido(valor):
            raise LanceInvalido('Não pode propor um lance com valor acima do saldo da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def valor_e_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0
        self.menor_lance = 0

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance: Lance):
        if self._lance_e_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        else:
            raise LanceInvalido('A sequencia de lances deve ser realizada por ususarios diferentes')

    def _lance_crescente(self, lance):
        if self.__lances[-1].valor < lance.valor:
            return True
        else:
            raise LanceInvalido('O lance deve ser crescente')

    def _lance_e_valido(self, lance):
        return not self._tem_lances() or self._usuarios_diferentes(lance) and self._lance_crescente(lance)



