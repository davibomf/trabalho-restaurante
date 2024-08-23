import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.cliente import Cliente
from trabalho_1.limite.tela_cliente import TelaCliente
from trabalho_1.DAOs.cliente_dao import ClienteDAO
import random
from trabalho_1.excecoes.lista_vazia_exception import ListaVaziaException
from trabalho_1.excecoes.item_inexistente_exception import ItemInexistenteException
from trabalho_1.excecoes.dados_invalidos_exception import DadosInvalidosException


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__cliente_DAO = ClienteDAO()
        self.__tela_cliente = TelaCliente()
        self.__controlador_sistema = controlador_sistema

    def pega_cliente_p_cod(self, cod: int):
        try:
            for cliente in self.__cliente_DAO.get_all():
                if cliente.codigo == int(cod):
                    return cliente
            raise ItemInexistenteException
        except ItemInexistenteException as e:
            self.__tela_cliente.mostra_msg(f'Erro: {str(e)}')

    def add_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        try:
            if dados_cliente is not False:
                new_cli = Cliente(dados_cliente['nome'],
                                        dados_cliente['cpf'])
                new_cli.codigo = random.randint(1, 1000)
                if isinstance(new_cli, Cliente):
                    self.__cliente_DAO.add(new_cli)
                    self.__tela_cliente.mostra_msg('Cliente criado')
                else:
                    raise DadosInvalidosException
        except DadosInvalidosException as e:
            self.__tela_cliente.mostra_msg(f'Erro: {str(e)}')

    def lista_clientes(self):
        dados_cliente = []
        for cli in self.__cliente_DAO.get_all():
            dados_cliente.append({'nome': cli.nome, 'cpf': cli.cpf, 'codigo': cli.codigo})
        try:
            if len(dados_cliente) > 0:
                self.__tela_cliente.mostra_cliente(dados_cliente)
                return True
            raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_cliente.mostra_msg(f'Erro: {str(e)}')
            return False

    def altera_cliente(self):
        try:
            if self.lista_clientes():
                cod_cli = self.__tela_cliente.seleciona_cliente()
                if cod_cli is not False:
                    cli = self.pega_cliente_p_cod(cod_cli)

                    if cli is not None:
                        novos_dados_cli = self.__tela_cliente.pega_dados_cliente()
                        cli.nome = novos_dados_cli['nome']
                        cli.cpf = novos_dados_cli['cpf']
                        self.__cliente_DAO.update(cli)
                        self.lista_clientes()
                    else:
                        raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_cliente.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_cliente.mostra_msg(f'Erro: {str(e)}')

    def del_cliente(self):
        try:
            if self.lista_clientes():
                cod_cli = self.__tela_cliente.seleciona_cliente()
                if cod_cli is not False:
                    cli = self.pega_cliente_p_cod(int(cod_cli))

                    if cli is not None:
                        self.__cliente_DAO.remove(cli.codigo)
                        self.lista_clientes()
                    else:
                        raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_cliente.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_cliente.mostra_msg(f'Erro: {str(e)}')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_cliente,
                        2: self.altera_cliente,
                        3: self.lista_clientes,
                        4: self.del_cliente,
                        0: self.retornar}
    
        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
