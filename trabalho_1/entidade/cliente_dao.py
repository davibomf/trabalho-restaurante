from trabalho_1.DAOs.dao import DAO
from trabalho_1.entidade.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('cliente.pkl')

    def add(self, cliente:Cliente):
        if (cliente is not None) and (isinstance(cliente, Cliente)) and (isinstance(cliente.codigo, int)):
            super().add(cliente.codigo, cliente)

    def update(self, cliente: Cliente):
        if (cliente is not None) and (isinstance(cliente, Cliente)) and (isinstance(cliente.codigo, int)):
            super().update(cliente.codigo, cliente)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)