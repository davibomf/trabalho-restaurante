import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.limite.tela_refeicao import TelaRefeicao
from trabalho_1.entidade.refeicao import Refeicao
from trabalho_1.DAOs.refeicao_dao import RefeicaoDAO
from trabalho_1.DAOs.suprimento_dao import SuprimentoDAO
import random
from trabalho_1.excecoes.lista_vazia_exception import ListaVaziaException
from trabalho_1.excecoes.item_inexistente_exception import ItemInexistenteException
from trabalho_1.excecoes.dados_invalidos_exception import DadosInvalidosException

class ControladorRefeicao():

    def __init__(self, controlador_sistema):
        self.__suprimento_DAO = SuprimentoDAO()
        self.__refeicao_DAO = RefeicaoDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_refeicao = TelaRefeicao()

    def pega_refeicao_por_codigo(self, codigo: int):
        try:
            for refeicao in self.__refeicao_DAO.get_all():
                if(refeicao.codigo == int(codigo)):
                    return refeicao
            raise ItemInexistenteException
        except ItemInexistenteException as e:
            self.__tela_refeicao.mostra_msg(f'Erro: {str(e)}')

    def incluir_refeicao(self):
        dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()
        
        try:
            if dados_refeicao is not False:
                ing1 = self.__suprimento_DAO.get(int(dados_refeicao['ingrediente1']))
                ing2 = self.__suprimento_DAO.get(int(dados_refeicao['ingrediente2']))
                if ing1 is not None and ing2 is not None:
                    if (isinstance(dados_refeicao["nome"], str)):
                        if (isinstance(self.verifica_booleano(dados_refeicao["veget"]), bool) and
                            isinstance(self.verifica_booleano(dados_refeicao["vegan"]), bool) and
                            isinstance(self.verifica_booleano(dados_refeicao["gluten"]), bool) and
                            isinstance(self.verifica_booleano(dados_refeicao["lactose"]), bool)):
                                
                                nova_refeicao = Refeicao(dados_refeicao["nome"],
                                                    dados_refeicao["veget"], dados_refeicao["vegan"], 
                                                    dados_refeicao["gluten"], dados_refeicao["lactose"],
                                                    ing1, ing2)
                                nova_refeicao.codigo = random.randint(1, 1000)
                                if isinstance(nova_refeicao, Refeicao):
                                    self.__refeicao_DAO.add(nova_refeicao)
                                    self.__tela_refeicao.mostra_msg('Refeição criada')
                                else:
                                    raise DadosInvalidosException
                        else:
                            raise DadosInvalidosException
                    else:
                        raise DadosInvalidosException
            else:
                raise ItemInexistenteException
        except DadosInvalidosException as e:
            self.__tela_refeicao.mostra_msg(f'Erro: {str(e)}')
        except ItemInexistenteException as e:
            self.__tela_refeicao.mostra_msg(f'Erro: {str(e)}')

    def alterar_refeicao(self):
        try:
            if self.lista_refeicao():
                codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
                refeicao = self.pega_refeicao_por_codigo(codigo_refeicao)

                if(refeicao is not None):
                    novos_dados_refeicao = self.__tela_refeicao.pega_dados_refeicao()

                    ing1 = self.__suprimento_DAO.get(int(novos_dados_refeicao['ingrediente1']))
                    ing2 = self.__suprimento_DAO.get(int(novos_dados_refeicao['ingrediente2']))

                    if ing1 is not None and ing2 is not None:
                        if (isinstance(novos_dados_refeicao["nome"], str)):
                            if (isinstance(self.verifica_booleano(novos_dados_refeicao["veget"]), bool) and
                            isinstance(self.verifica_booleano(novos_dados_refeicao["vegan"]), bool) and
                            isinstance(self.verifica_booleano(novos_dados_refeicao["gluten"]), bool) and
                            isinstance(self.verifica_booleano(novos_dados_refeicao["lactose"]), bool)):

                                refeicao.nome = novos_dados_refeicao["nome"]
                                refeicao.veget = novos_dados_refeicao["veget"]
                                refeicao.vegan = novos_dados_refeicao["vegan"]
                                refeicao.gluten = novos_dados_refeicao["gluten"]
                                refeicao.lactose = novos_dados_refeicao["lactose"]

                                refeicao.altera_primeiro_ing(ing1)
                                refeicao.altera_segundo_ing(ing2)
                                self.__refeicao_DAO.update(refeicao)
                                self.lista_refeicao()
                            else:
                                raise DadosInvalidosException
                        else:
                            raise DadosInvalidosException  
                    else:
                        raise DadosInvalidosException     
                else:
                    raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_refeicao.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_refeicao.mostra_msg(f'Erro: {str(e)}')
        except DadosInvalidosException as e:
            self.__tela_refeicao.mostra_msg(f'Erro: {str(e)}')

    def lista_refeicao(self):
        dados_refeicao = []
        for sup in self.__refeicao_DAO.get_all():
            dados_refeicao.append({'nome': sup.nome, 'veget': sup.veget, 'vegan': sup.vegan,
                                   'gluten': sup.gluten, 'lactose': sup.lactose,
                                   'codigo': sup.codigo, 'preco': sup.preco
                                   #'ingrediente1': sup.ingrediente1.nome, 'ingrediente2': sup.ingrediente2.nome
                                   })
        try:
            if len(dados_refeicao) > 0:
                self.__tela_refeicao.mostra_refeicao(dados_refeicao)
                return True
            raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_refeicao.mostra_msg(f'Erro: {str(e)}')
            return False

    def excluir_refeicao(self):
        try:
            if self.lista_refeicao():
                codigo_refeicao = self.__tela_refeicao.seleciona_refeicao()
                refeicao = self.pega_refeicao_por_codigo(codigo_refeicao)

                if(refeicao is not None):
                    self.__refeicao_DAO.remove(refeicao.codigo)
                    self.lista_refeicao()
                else:
                        raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_refeicao.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_refeicao.mostra_msg(f'Erro: {str(e)}')

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
        lista_opcoes = {1: self.incluir_refeicao, 2: self.alterar_refeicao, 3: self.lista_refeicao,
                        4: self.excluir_refeicao, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_refeicao.tela_opcoes()]()