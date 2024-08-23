import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from trabalho_1.entidade.suprimento import Suprimento
from trabalho_1.limite.tela_suprimento import TelaSuprimento
from trabalho_1.DAOs.suprimento_dao import SuprimentoDAO
import random
from trabalho_1.excecoes.lista_vazia_exception import ListaVaziaException
from trabalho_1.excecoes.item_inexistente_exception import ItemInexistenteException
from trabalho_1.excecoes.dados_invalidos_exception import DadosInvalidosException

class ControladorSuprimento():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__suprimento_DAO = SuprimentoDAO()
        self.__tela_suprimento = TelaSuprimento()

    def pega_suprimento_por_codigo(self, codigo: int):
        try:
            for suprimento in self.__suprimento_DAO.get_all():
                if(suprimento.codigo == int(codigo)):
                    return suprimento
            raise ItemInexistenteException
        except ItemInexistenteException as e:
            self.__tela_suprimento.mostra_msg(f'Erro: {str(e)}')
        
    def incluir_suprimento(self):
        dados_suprimento = self.__tela_suprimento.pega_dados_suprimento()
        try:
            if dados_suprimento is not False:
                novo_suprimento = Suprimento(dados_suprimento["nome"],
                                            dados_suprimento["preco"])
                novo_suprimento.codigo = random.randint(1, 1000)
                if isinstance(novo_suprimento, Suprimento):
                    self.__suprimento_DAO.add(novo_suprimento)
                    self.__tela_suprimento.mostra_msg('Suprimento criado')
                else:
                    raise DadosInvalidosException
        except DadosInvalidosException as e:
            self.__tela_suprimento.mostra_msg(f'Erro: {str(e)}')
    
    def listar_suprimentos(self):
        dados_suprimento = []
        for sup in self.__suprimento_DAO.get_all():
            dados_suprimento.append({'nome': sup.nome, 'preco': sup.preco, 'codigo': sup.codigo})
        try:
            if len(dados_suprimento) > 0:
                self.__tela_suprimento.mostra_suprimento(dados_suprimento)
                return True
            raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_suprimento.mostra_msg(f'Erro: {str(e)}')
            return False

    def altera_suprimento(self):
        try:
            if self.listar_suprimentos():
                cod_sup = self.__tela_suprimento.seleciona_suprimento()
                sup = self.pega_suprimento_por_codigo(cod_sup)

                if sup is not None:
                    novos_dados_sup = self.__tela_suprimento.pega_dados_suprimento()
                    sup.nome = novos_dados_sup['nome']
                    sup.preco = float(novos_dados_sup['preco'])
                    self.__suprimento_DAO.update(sup)
                    self.listar_suprimentos()
                else:
                    raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_suprimento.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_suprimento.mostra_msg(f'Erro: {str(e)}')

    def excluir_suprimento(self):
        try:
            if self.listar_suprimentos():
                cod_sup = self.__tela_suprimento.seleciona_suprimento()
                sup = self.pega_suprimento_por_codigo(cod_sup)

                if sup is not None:
                    self.__suprimento_DAO.remove(sup.codigo)
                    self.listar_suprimentos()
                else:
                    raise ItemInexistenteException
            else:
                raise ListaVaziaException
        except ItemInexistenteException as e:
            self.__tela_suprimento.mostra_msg(f'Erro: {str(e)}')
        except ListaVaziaException as e:
            self.__tela_suprimento.mostra_msg(f'Erro: {str(e)}')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_suprimento,
                        2: self.altera_suprimento,
                        3: self.listar_suprimentos,
                        4: self.excluir_suprimento,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_suprimento.tela_opcoes()]()
