import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Bem vindo ao sistema RestBAR 1.0!', font = ('Helvetica', 25))],
            [sg.Text('Escolha sua opção:', font = ('Helvetica', 15))],
            [sg.Radio('Clientes', 'RD1', key='1')],
            [sg.Radio('Funcionários', 'RD1', key='2')],
            [sg.Radio('Refeições', 'RD1', key='3')],
            [sg.Radio('Bebidas', 'RD1', key='4')],
            [sg.Radio('Suprimentos', 'RD1', key='5')],
            [sg.Radio('Vendas', 'RD1', key='6')],
            [sg.Radio('Finalizar sistema', 'RD1', key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)