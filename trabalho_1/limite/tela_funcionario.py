import PySimpleGUI as sg
from trabalho_1.excecoes.dados_invalidos_exception import DadosInvalidosException


class TelaFuncionario:
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
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- FUNCIONÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Funcionário', "RD1", key='1')],
            [sg.Radio('Alterar Funcionário', "RD1", key='2')],
            [sg.Radio('Listar Funcionários', "RD1", key='3')],
            [sg.Radio('Excluir Funcionário', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)

    def pega_dados_funcionario(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- DADOS FUNCIONÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Função:', size=(15, 1)), sg.InputText('', key='funcao')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
            [sg.Text('Rua:', size=(15, 1)), sg.InputText('', key='rua')],
            [sg.Text('Bairro:', size=(15, 1)), sg.InputText('', key='bairro')],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']
        funcao = values['funcao']
        salario = values['salario']
        rua = values['rua']
        bairro = values['bairro']
        cidade = values['cidade']

        self.close()
        try:
            if ((nome != '') and
                (cpf != '') and
                (salario != '') and
                (funcao != '') and
                (rua != '') and
                (bairro != '') and
                (cidade != '')):
                return {'nome': nome,
                        'cpf': cpf,
                        'salario': salario,
                        'funcao': funcao,
                        'rua': rua,
                        'bairro': bairro,
                        'cidade': cidade}
            raise DadosInvalidosException
        except DadosInvalidosException as e:
            self.mostra_msg(f'Erro: {str(e)}')
            return False

    def pega_dados_funcionario_att(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- DADOS FUNCIONÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Função:', size=(15, 1)), sg.InputText('', key='funcao')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
            [sg.Text('Rua:', size=(15, 1)), sg.InputText('', key='rua')],
            [sg.Text('Bairro:', size=(15, 1)), sg.InputText('', key='bairro')],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema RestBAR 1.0').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        funcao = values['funcao']
        salario = values['salario']
        rua = values['rua']
        bairro = values['bairro']
        cidade = values['cidade']

        self.close()
        try:
            if ((nome != '') and
                (salario != '') and
                (funcao != '') and
                (rua != '') and
                (bairro != '') and
                (cidade != '')):
                return {'nome': nome,
                        'salario': salario,
                        'funcao': funcao,
                        'rua': rua,
                        'bairro': bairro,
                        'cidade': cidade}
            raise DadosInvalidosException
        except DadosInvalidosException as e:
            self.mostra_msg(f'Erro: {str(e)}')
            return False

    def mostra_funcionario(self, dados_funcionario):
        string_todos_funcionarios = ''
        for dado in dados_funcionario:
            string_todos_funcionarios = string_todos_funcionarios + 'NOME DO FUNCIONÁRIO: ' + str(dado['nome']) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + 'CPF DO FUNCIONÁRIO: ' + str(dado['cpf']) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + 'CÓDIGO DO FUNCIONÁRIO: ' + str(dado['codigo']) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + 'SALÁRIO DO FUNCIONÁRIO: ' + str(dado['salario']) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + 'FUNÇÃO DO FUNCIONÁRIO: ' + str(dado['funcao']) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + 'ENDEREÇO DO FUNCIONÁRIO: ' + str(dado['endereco']) + '\n'
            string_todos_funcionarios = string_todos_funcionarios + 'VENDAS DO FUNCIONÁRIO: ' + str(dado['num_vendas']) + '\n\n'

        sg.Popup('-------- LISTA DE FUNCIONÁRIOS ----------', string_todos_funcionarios)


    def seleciona_funcionario(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- SELECIONAR FUNCIONÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código do funcionário que deseja selecionar:', font=("Helvica", 15))],
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