import PySimpleGUI as sg
from trabalho_1.excecoes.dados_invalidos_exception import DadosInvalidosException

class TelaSuprimento:
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
            [sg.Text('-------- SUPRIMENTOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Suprimento', "RD1", key='1')],
            [sg.Radio('Alterar Suprimento', "RD1", key='2')],
            [sg.Radio('Listar todos os suprimento', "RD1", key='3')],
            [sg.Radio('Excluir Suprimento', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)

    def pega_dados_suprimento(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('---------- DADOS SUPRIMENTO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='preco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        preco = values['preco']

        self.close()
        try:
            if ((nome != '') and (preco != '')):
                return {"nome": nome, "preco": preco}
            raise DadosInvalidosException
        except DadosInvalidosException as e:
            self.mostra_msg(f'Erro: {str(e)}')
            return False


    def mostra_suprimento(self, dados_suprimento):
        string_todos_suprimentos = ''
        for dado in dados_suprimento:
            string_todos_suprimentos = string_todos_suprimentos + 'NOME DO SUPRIMENTO: ' + dado['nome'] + '\n'
            string_todos_suprimentos = string_todos_suprimentos + 'PREÇO DO SUPRIMENTO: ' + str(dado['preco']) + '\n'
            string_todos_suprimentos = string_todos_suprimentos + 'CÓDIGO DO SUPRIMENTO: ' + str(dado['codigo']) + '\n\n'

        sg.Popup('---------- LISTA DE SUPRIMENTOS ----------', string_todos_suprimentos)

    
    def seleciona_suprimento(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONAR SUPRIMENTO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código do suprimento que deseja selecionar:', font=("Helvica", 15))],
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
