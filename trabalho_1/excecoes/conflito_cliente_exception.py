class ConflitoClienteException(Exception):
    def __init__(self):
        super().__init__('Já existe um cliente com esse CPF no sistema.')