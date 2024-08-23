import PySimpleGUI as sg
from trabalho_1.excecoes.dados_invalidos_exception import DadosInvalidosException

class TelaBebida():
  def __init__(self):
        self.__window = None
        self.init_opcoes()

  def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

  def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- BEBIDAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Bebida', "RD1", key='1')],
            [sg.Radio('Alterar Bebida', "RD1", key='2')],
            [sg.Radio('Listar todas as Bebidas', "RD1", key='3')],
            [sg.Radio('Excluir Bebida', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)

  def pega_dados_bebida(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('---------- DADOS BEBIDA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Veget:', size=(15, 1)), sg.InputText('', key='veget')],
            [sg.Text('Vegan:', size=(15, 1)), sg.InputText('', key='vegan')],
            [sg.Text('Gluten:', size=(15, 1)), sg.InputText('', key='gluten')],
            [sg.Text('Lactose:', size=(15, 1)), sg.InputText('', key='lactose')],
            [sg.Text('Ingrediente 1:', size=(15, 1)), sg.InputText('', key='ingrediente1')],
            [sg.Text('Ingrediente 2:', size=(15, 1)), sg.InputText('', key='ingrediente2')],
            [sg.Text('Grau alcoolico:', size=(15, 1)), sg.InputText('', key='grau_alcoolico')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        veget = values['veget']
        vegan = values['vegan']
        gluten = values['gluten']
        lactose = values['lactose']
        ingrediente1 = values['ingrediente1']
        ingrediente2 = values['ingrediente2']
        grau_alcoolico = values['grau_alcoolico']

        self.close()
        try:
            if ((nome != '') and (veget != '') and (vegan != '')
                and (gluten != '') and (lactose != '') and (ingrediente1 != '') and (ingrediente2 != '')):
                return {"nome": nome, "veget": veget, "vegan": vegan,
                "gluten": gluten, "lactose": lactose,
                "ingrediente1": ingrediente1, "ingrediente2": ingrediente2,
                "grau_alcoolico": grau_alcoolico}
            raise DadosInvalidosException
        except DadosInvalidosException as e:
            self.mostra_msg(f'Erro: {str(e)}')
            return False

  def mostra_bebida(self, dados_refeicao):
        string_todas_refeicoes = ''
        for dado in dados_refeicao:
            string_todas_refeicoes = string_todas_refeicoes + 'NOME DA BEBIDA: ' + dado['nome'] + '\n'
            string_todas_refeicoes = string_todas_refeicoes + 'VEGET: ' + str(dado['veget']) + '\n'
            string_todas_refeicoes = string_todas_refeicoes + 'VEGAN: ' + str(dado['vegan']) + '\n'
            string_todas_refeicoes = string_todas_refeicoes + 'GLUTEN: ' + str(dado['gluten']) + '\n'
            string_todas_refeicoes = string_todas_refeicoes + 'LACTOSE: ' + str(dado['lactose']) + '\n'
            string_todas_refeicoes = string_todas_refeicoes + 'PREÇO DO SUPRIMENTO: ' + str(dado['preco']) + '\n'
            string_todas_refeicoes = string_todas_refeicoes + 'GRAU ALCOOLICO: ' + str(dado['grau_alcoolico']) + '\n'
            string_todas_refeicoes = string_todas_refeicoes + 'CÓDIGO DA BEBIDA: ' + str(dado['codigo']) + '\n\n'

        sg.Popup('---------- LISTA DE BEBIDAS ----------', string_todas_refeicoes)

    
  def seleciona_bebida(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONAR SUPRIMENTO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da bebida que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        try:
            if (codigo != ''):
                return codigo
            raise DadosInvalidosException
        except DadosInvalidosException as e:
            self.mostra_msg(f'Erro: {str(e)}')
            return False

  def mostra_msg(self, msg):
        sg.popup("", msg)

  def close(self):
        self.__window.Close()

  def open(self):
        button, values = self.__window.Read()
        return button, values
