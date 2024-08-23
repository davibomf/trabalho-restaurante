from trabalho_1.DAOs.dao import DAO
from trabalho_1.entidade.bebida import Bebida

class BebidaDAO(DAO):
    def __init__(self):
        super().__init__('bebida.pkl')

    def add(self, bebida: Bebida):
        if (bebida is not None) and (isinstance(bebida, Bebida)) and (isinstance(bebida.codigo, int)):
            super().add(bebida.codigo, bebida)

    def update(self, bebida: Bebida):
        if (bebida is not None) and (isinstance(bebida, Bebida)) and (isinstance(bebida.codigo, int)):
            super().update(bebida.codigo, bebida)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)