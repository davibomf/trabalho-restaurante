from trabalho_1.DAOs.dao import DAO
from trabalho_1.entidade.venda import Venda

class VendaDAO(DAO):
    def __init__(self):
        super().__init__('venda.pkl')

    def add(self, venda: Venda):
        if (venda is not None) and (isinstance(venda, Venda)) and (isinstance(venda.codigo, int)):
            super().add(venda.codigo, venda)

    def update(self, venda: Venda):
        if (venda is not None) and (isinstance(venda, Venda)) and (isinstance(venda.codigo, int)):
            super().update(venda.codigo, venda)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)