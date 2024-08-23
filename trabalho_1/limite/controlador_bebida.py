import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.limite.tela_bebida import TelaBebida
from trabalho_1.entidade.bebida import Bebida
from trabalho_1.DAOs.bebida_dao import BebidaDAO
from trabalho_1.DAOs.suprimento_dao import SuprimentoDAO
import random
from trabalho_1.excecoes.lista_vazia_exception import ListaVaziaException
from trabalho_1.excecoes.item_inexistente_exception import ItemInexistenteException
from trabalho_1.excecoes.dados_invalidos_exception import DadosInvalidosException

class ControladorBebida():

    def __init__(self, controlador_sistema):
        self.__suprimento_DAO = SuprimentoDAO()
        self.__bebida_DAO = BebidaDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_bebida = TelaBebida()

    def pega_bebida_por_codigo(self, codigo: int):
        try:
            for bebida in self.__bebida_DAO.get_all():
                if(bebida.codigo == int(codigo)):
                    return bebida
            raise ItemInexistenteException
        except ItemInexistenteException as e:
            self.__tela_bebida.mostra_msg(f'Erro: {str(e)}')

    def incluir_bebida(self):
        dados_bebida = self.__tela_bebida.pega_dados_bebida()  

        try:
            if dados_bebida is not False:
                ing1 = self.__suprimento_DAO.get(int(dados_bebida['ingrediente1']))
                ing2 = self.__suprimento_DAO.get(int(dados_bebida['ingrediente2']))
                if ing1 is not None and ing2 is not None:
                    if (isinstance(dados_bebida["nome"], str) and
                        isinstance(float(dados_bebida["grau_alcoolico"]), float)):
                        if (isinstance(self.verifica_booleano(dados_bebida["veget"]), bool) and
                            isinstance(self.verifica_booleano(dados_bebida["vegan"]), bool) and
                            isinstance(self.verifica_booleano(dados_bebida["gluten"]), bool) and
                            isinstance(self.verifica_booleano(dados_bebida["lactose"]), bool)):

                            nova_bebida = Bebida(dados_bebida["nome"],
                                                dados_bebida["veget"], dados_bebida["vegan"],
                                                dados_bebida["gluten"], dados_bebida["lactose"],
                                                ing1, ing2,
                                                dados_bebida["grau_alcoolico"])
                            nova_bebida.codigo = random.randint(1, 1000)
                            if isinstance(nova_bebida, Bebida):
                                self.__bebida_DAO.add(nova_bebida)
                                self.__tela_bebida.mostra_msg('Bebida criada')
                            else:
                                raise DadosInvalidosException
                        else:
                            raise DadosInvalidosException
                    else:
                        raise DadosInvalidosException
                else:
                    raise DadosInvalidosException
            else:
                raise ItemInexistenteException
        except ItemInexistenteException as e:
            self.__tela_bebida.mostra_msg(f'Erro: {str(e)}')
        except DadosInvalidosException as e:
            self.__tela_bebida.mostra_msg(f'Erro: {str(e)}')

    def alterar_bebida(self):
        try:
            if self.lista_bebida():
                codigo_bebida = self.__tela_bebida.seleciona_bebida()
                bebida = self.pega_bebida_por_codigo(codigo_bebida)

            
                if(bebida is not None):
                    novos_dados_bebida = self.__tela_bebida.pega_dados_bebida()

                    ing1 = self.__suprimento_DAO.get(int(novos_dados_bebida['ingrediente1']))
                    ing2 = self.__suprimento_DAO.get(int(novos_dados_bebida['ingrediente2']))

                    if ing1 is not None and ing2 is not None:
                        if (isinstance(novos_dados_bebida["nome"], str) and
                        isinstance(float(novos_dados_bebida["grau_alcoolico"]), float)):   
                            if (isinstance(self.verifica_booleano(novos_dados_bebida["veget"]), bool) and
                            isinstance(self.verifica_booleano(novos_dados_bebida["vegan"]), bool) and
                            isinstance(self.verifica_booleano(novos_dados_bebida["gluten"]), bool) and
                            isinstance(self.verifica_booleano(novos_dados_bebida["lactose"]), bool)):
                                
                                bebida.nome = novos_dados_bebida["nome"]
                                bebida.veget = novos_dados_bebida["veget"]
                                bebida.vegan = novos_dados_bebida["vegan"]
                                bebida.gluten = novos_dados_bebida["gluten"]
                                bebida.lactose = novos_dados_bebida["lactose"]
                                bebida.grau_alcoolico = novos_dados_bebida["grau_alcoolico"]

                                bebida.altera_primeiro_ing(ing1)
                                bebida.altera_segundo_ing(ing2)
                                self.__bebida_DAO.update(bebida)
                                self.lista_bebida()
                            else:
                                raise DadosInvalidosException
                        else:
                            raise DadosInvalidosException  
                    else:
                        raise DadosInvalidosException     
                else:
                    raise ItemInexistenteException
        except ItemInexistenteException as e:
            self.__tela_bebida.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_bebida.mostra_msg(f'Erro: {str(e)}')
        except DadosInvalidosException as e:
            self.__tela_bebida.mostra_msg(f'Erro: {str(e)}')

    def lista_bebida(self):
        dados_bebida = []
        for sup in self.__bebida_DAO.get_all():
            dados_bebida.append({'nome': sup.nome, 'veget': sup.veget, 'vegan': sup.vegan,
                                   'gluten': sup.gluten, 'lactose': sup.lactose,
                                   'codigo': sup.codigo, 'preco': sup.preco, 'grau_alcoolico': sup.grau_alcoolico
                                   #'ingrediente1': sup.ingrediente1.nome, 'ingrediente2': sup.ingrediente2.nome
                                   })
        try:
            if len(dados_bebida) > 0:
                self.__tela_bebida.mostra_bebida(dados_bebida)
                return True
            raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_bebida.mostra_msg(f'Erro: {str(e)}')
            return False

    def excluir_bebida(self):
        try:
            if self.lista_bebida():
                codigo_bebida = self.__tela_bebida.seleciona_bebida()
                bebida = self.pega_bebida_por_codigo(codigo_bebida)

                if(bebida is not None):
                    self.__bebida_DAO.remove(bebida.codigo)
                    self.lista_bebida()
                else:
                    raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_bebida.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_bebida.mostra_msg(f'Erro: {str(e)}')

    def verifica_booleano(self, dado_em_string):
        if dado_em_string.lower() == 'true':
            return True
        elif dado_em_string.lower() == 'false':
            return False
        else:
            return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_bebida, 2: self.alterar_bebida, 3: self.lista_bebida,
                        4: self.excluir_bebida, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_bebida.tela_opcoes()]()

    