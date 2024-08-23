from trabalho_1.DAOs.dao import DAO
from trabalho_1.entidade.refeicao import Refeicao

class RefeicaoDAO(DAO):
    def __init__(self):
        super().__init__('refeicao.pkl')

    def add(self, refeicao: Refeicao):
        if (refeicao is not None) and (isinstance(refeicao, Refeicao)) and (isinstance(refeicao.codigo, int)):
            super().add(refeicao.codigo, refeicao)

    def update(self, refeicao: Refeicao):
        if (refeicao is not None) and (isinstance(refeicao, Refeicao)) and (isinstance(refeicao.codigo, int)):
            super().update(refeicao.codigo, refeicao)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)