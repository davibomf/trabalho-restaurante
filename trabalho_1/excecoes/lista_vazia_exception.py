class ListaVaziaException(Exception):
    def __init__(self):
        super().__init__('Lista vazia')