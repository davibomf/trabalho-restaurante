from trabalho_1.DAOs.dao import DAO
from trabalho_1.entidade.suprimento import Suprimento

class SuprimentoDAO(DAO):
    def __init__(self):
        super().__init__('suprimento.pkl')

    def add(self, suprimento: Suprimento):
        if (suprimento is not None) and (isinstance(suprimento, Suprimento)) and (isinstance(suprimento.codigo, int)):
            super().add(suprimento.codigo, suprimento)

    def update(self, suprimento: Suprimento):
        if (suprimento is not None) and (isinstance(suprimento, Suprimento)) and (isinstance(suprimento.codigo, int)):
            super().update(suprimento.codigo, suprimento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)