class ItemInexistenteException(Exception):
    def __init__(self):
        super().__init__('O código/CPF inserido não corresponde á nenhum item da base de dados. Tente novamente')