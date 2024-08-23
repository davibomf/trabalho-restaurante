class DadosInvalidosException(Exception):
    def __init__(self):
        super().__init__('Os dados inseridos são inválidos. Tente novamente.')