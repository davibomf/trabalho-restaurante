class ConflitoFuncionarioException(Exception):
    def __init__(self):
        super().__init__('Já existe um funcionário com esse CPF no sistema.')