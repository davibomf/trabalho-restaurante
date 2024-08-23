from trabalho_1.DAOs.dao import DAO

class GeradorCodigo:
    def __init__(self):
        self.__cod_venda = 0
        self.__cod_cliente = 0
        self.__cod_refeicao = 0
        self.__cod_bebida = 0
        self.__cod_suprimento = 0

    @property
    def cod_venda(self):
        return self.__cod_venda

    @property
    def cod_cliente(self):
        return self.__cod_cliente

    @property
    def cod_refeicao(self):
        return self.__cod_refeicao

    @property
    def cod_bebida(self):
        return self.__cod_bebida
    
    @property
    def cod_suprimento(self):
        return self.__cod_suprimento

    def gera_cod_venda(self):
        cod_atual = self.cod_venda
        novo = cod_atual + 1
        self.__cod_venda = novo
        return self.cod_venda

    def gera_cod_cliente(self):
        cod_atual = self.cod_cliente
        novo = cod_atual + 1
        self.__cod_cliente = novo
        return self.cod_cliente

    def gera_cod_refeicao(self):
        cod_atual = self.cod_refeicao
        novo = cod_atual + 1
        self.__cod_refeicao = novo
        return self.cod_refeicao

    def gera_cod_bebida(self):
        cod_atual = self.cod_bebida
        novo = cod_atual + 1
        self.__cod_bebida = novo
        return self.cod_bebida

    def gera_cod_suprimento(self):
        cod_atual = self.cod_suprimento
        novo = cod_atual + 1
        self.__cod_suprimento = novo
        return self.cod_suprimento
