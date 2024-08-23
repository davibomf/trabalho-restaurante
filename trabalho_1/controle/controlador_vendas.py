import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from collections import defaultdict, Counter
from trabalho_1.entidade.venda import Venda
from trabalho_1.limite.tela_venda import TelaVenda
from trabalho_1.DAOs.venda_dao import VendaDAO
from trabalho_1.excecoes.lista_vazia_exception import ListaVaziaException
from trabalho_1.excecoes.item_inexistente_exception import ItemInexistenteException
from trabalho_1.excecoes.dados_invalidos_exception import DadosInvalidosException
import random

class ControladorVendas:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__venda_DAO = VendaDAO()
        self.__tela_venda = TelaVenda()

    def pega_venda_p_codigo(self, codigo):
        try:
            for venda in self.__venda_DAO.get_all():
                if venda.codigo == int(codigo):
                    return venda
            raise ItemInexistenteException
        except ItemInexistenteException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')

    def incluir_venda(self):
        try:
            self.__controlador_sistema.controlador_cliente.lista_clientes()
            self.__controlador_sistema.controlador_funcionario.lista_funcionarios()
            self.__controlador_sistema.controlador_refeicao.lista_refeicao()
            self.__controlador_sistema.controlador_bebida.lista_bebida()
            dados_venda = self.__tela_venda.pega_dados_venda()
            if dados_venda is not False:
                cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_p_cod(dados_venda['cliente'])
                funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_p_cod(dados_venda['funcionario'])
                refeicao = self.__controlador_sistema.controlador_refeicao.pega_refeicao_por_codigo(dados_venda['refeicao'])
                bebida = self.__controlador_sistema.controlador_bebida.pega_bebida_por_codigo(dados_venda['bebida'])
                if (cliente is not None and funcionario is not None and (refeicao is not None or bebida is not None)):
                    venda = Venda(cliente, funcionario, refeicao, bebida)
                    venda.codigo = random.randint(1, 1000)
                    self.__controlador_sistema.controlador_funcionario.incrementa_vendas(funcionario)
                    self.__venda_DAO.add(venda)
                    self.__tela_venda.mostra_msg('Venda criada')
                else:
                    raise DadosInvalidosException
        except DadosInvalidosException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')


    def lista_vendas(self):
        dados_venda = []
        for venda in self.__venda_DAO.get_all():
            dados_venda.append({'codigo': venda.codigo,
                                'cliente': venda.cliente.nome,
                                'funcionario': venda.funcionario.nome,
                                'refeicoes': venda.refeicoes,
                                'bebidas': venda.bebidas})
        try:
            if len(dados_venda) > 0:
                self.__tela_venda.mostra_venda(dados_venda)
                return True
            raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
            return False

    def altera_venda(self):
        try:
            if self.lista_vendas():
                cod_venda = self.__tela_venda.seleciona_venda()
                if cod_venda is not False:
                    venda = self.pega_venda_p_codigo(int(cod_venda))

                    if venda is not None:
                        novos_dados_venda = self.__tela_venda.pega_dados_venda()
                        venda.cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_p_cod(novos_dados_venda['cliente'])
                        venda.funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_p_cod(novos_dados_venda['funcionario'])
                        venda.clear_ref_beb()
                        venda.refeicoes = self.__controlador_sistema.controlador_refeicao.pega_refeicao_por_codigo(novos_dados_venda['refeicao'])
                        venda.bebidas = self.__controlador_sistema.controlador_bebida.pega_bebida_por_codigo(novos_dados_venda['bebida'])
                        self.__venda_DAO.update(venda)
                        self.__tela_venda.mostra_msg('Venda alterada')
                        self.lista_vendas()
                    else:
                        raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')

    def excluir_venda(self):
        try:
            if self.lista_vendas():
                cod_venda = self.__tela_venda.seleciona_venda()
                if cod_venda is not False:
                    venda = self.pega_venda_p_codigo(int(cod_venda))

                    if venda is not None:
                        self.__controlador_sistema.controlador_funcionario.decrementa_vendas(venda.funcionario)
                        self.__venda_DAO.remove(venda.codigo)
                        self.__tela_venda.mostra_msg('Venda removida')
                        self.lista_vendas()
                    else:
                        raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')

    def vendas_p_cliente(self):
        try:
            if self.__controlador_sistema.controlador_cliente.lista_clientes():
                cod_cli = self.__tela_venda.seleciona_cliente()
                if cod_cli is not False:
                    cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_p_cod(int(cod_cli))
                    if cliente is not None:
                        vendas_cli = []
                        for venda in self.__venda_DAO.get_all():
                            if venda.cliente.codigo == cliente.codigo:
                                vendas_cli.append({'codigo': venda.codigo,
                                                                'cliente': venda.cliente.nome,
                                                                'funcionario': venda.funcionario.nome,
                                                                'refeicoes': venda.refeicoes,
                                                                'bebidas': venda.bebidas})
                        if len(vendas_cli) > 0:
                            self.__tela_venda.mostra_venda(vendas_cli)
                        else:
                            raise ListaVaziaException
                    else:
                        raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')

    def vendas_p_funcionario(self):
        try:
            if self.__controlador_sistema.controlador_funcionario.lista_funcionarios():
                cod_func = self.__tela_venda.seleciona_funcionario()
                if cod_func is not False:
                    funcionario = self.__controlador_sistema.controlador_funcionario.pega_funcionario_p_cod(cod_func)
                    if funcionario is not None:
                        vendas_func = []
                        for venda in self.__venda_DAO.get_all():
                            if venda.funcionario.codigo == funcionario.codigo:
                                vendas_func.append({'codigo': venda.codigo,
                                                                'cliente': venda.cliente.nome,
                                                                'funcionario': venda.funcionario.nome,
                                                                'refeicoes': venda.refeicoes,
                                                                'bebidas': venda.bebidas})
                        if len(vendas_func) > 0:
                            self.__tela_venda.mostra_venda(vendas_func)
                        else:
                            raise ListaVaziaException
                    else:
                        raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')

    def vendas_abertas(self):
        try:
            vendas_abertas = []
            for venda in self.__venda_DAO.get_all():
                if venda.aberta is True:
                    vendas_abertas.append({'codigo': venda.codigo,
                                                    'cliente': venda.cliente.nome,
                                                    'funcionario': venda.funcionario.nome,
                                                    'refeicoes': venda.refeicoes,
                                                    'bebidas': venda.bebidas})
            if len(vendas_abertas) > 0:
                self.__tela_venda.mostra_venda(vendas_abertas)
                return True
            else:
                raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
            return False

    def vendas_encerradas(self):
        try:
            vendas_encerradas = []
            for venda in self.__venda_DAO.get_all():
                if venda.aberta is False:
                    vendas_encerradas.append({'codigo': venda.codigo,
                                                'cliente': venda.cliente.nome,
                                                'funcionario': venda.funcionario.nome,
                                                'refeicoes': venda.refeicoes,
                                                'bebidas': venda.bebidas})
            if len(vendas_encerradas) > 0:
                self.__tela_venda.mostra_venda(vendas_encerradas)
                return True
            else:
                raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
            return False

    def encerrar_venda(self):
        try:
            if self.vendas_abertas():
                cod_venda = self.__tela_venda.seleciona_venda()
                if cod_venda is not False:
                    venda = self.pega_venda_p_codigo(int(cod_venda))
                    if venda is not None:
                        for vend in self.__venda_DAO.get_all():
                            if vend.codigo == venda.codigo:
                                vend.aberta = False
                                self.__venda_DAO.update(vend)
                                self.__tela_venda.mostra_msg('Venda encerrada')
                    else:
                        raise ItemInexistenteException
            else:
                return None
        except ItemInexistenteException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
    
    def adicionar_bebida(self):
        try:
            if self.vendas_abertas():
                self.__controlador_sistema.controlador_bebida.lista_bebida()
                cod_venda = self.__tela_venda.seleciona_venda()
                if cod_venda is not False:
                    venda = self.pega_venda_p_codigo(int(cod_venda))
                    if venda is not None:
                        cod_bebida = self.__tela_venda.seleciona_bebida()
                        if cod_bebida is not False:
                            bebida = self.__controlador_sistema.controlador_bebida.pega_bebida_por_codigo(int(cod_bebida))
                            if bebida is not None:
                                dados_venda = []
                                venda.bebidas = bebida
                                self.__venda_DAO.update(venda)
                                dados_venda.append({'codigo': venda.codigo,
                                                        'cliente': venda.cliente.nome,
                                                        'funcionario': venda.funcionario.nome,
                                                        'refeicoes': venda.refeicoes,
                                                        'bebidas': venda.bebidas})
                                self.__tela_venda.mostra_venda(dados_venda)
                            else:
                                raise ItemInexistenteException
                    else:
                        raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
        
    def adicionar_refeicao(self):
        try:
            if self.vendas_abertas():
                self.__controlador_sistema.controlador_refeicao.lista_refeicao()
                cod_venda = self.__tela_venda.seleciona_venda()
                if cod_venda is not False:
                    venda = self.pega_venda_p_codigo(int(cod_venda))
                    if venda is not None:
                        cod_refeicao = self.__tela_venda.seleciona_refeicao()
                        if cod_refeicao is not False:
                            refeicao = self.__controlador_sistema.controlador_refeicao.pega_refeicao_por_codigo(int(cod_refeicao))
                            if refeicao is not None:
                                dados_venda = []
                                venda.refeicoes = refeicao
                                self.__venda_DAO.update(venda)
                                dados_venda.append({'codigo': venda.codigo,
                                                        'cliente': venda.cliente.nome,
                                                        'funcionario': venda.funcionario.nome,
                                                        'refeicoes': venda.refeicoes,
                                                        'bebidas': venda.bebidas})
                                self.__tela_venda.mostra_venda(dados_venda)
                            else:
                                raise ItemInexistenteException
                    else:
                        raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_venda.mostra_msg(f'Erro: {str(e)}')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_venda,
                        2: self.altera_venda,
                        3: self.lista_vendas,
                        4: self.excluir_venda,
                        5: self.vendas_p_funcionario,
                        6: self.vendas_p_cliente,
                        7: self.vendas_abertas,
                        8: self.vendas_encerradas,
                        9: self.encerrar_venda,
                        10: self.adicionar_bebida,
                        11: self. adicionar_refeicao,
                        0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_venda.tela_opcoes()]()
