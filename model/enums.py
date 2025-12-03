# enums.py

from enum import Enum
# somente o pacote dos enums
class EnumGenero(Enum):
    ACAO = "Acao"
    DRAMA = "Drama"
    TERROR = "Terror"
    FICCAO_CIENTIFICA = "Ficcao Cientifica"
    ROMANCE = "Romance"

class EnumPlano(Enum):
    BASICO = "Basico"
    PREMIUM = "Premium"

class EnumStatus(Enum):
    EM_PRODUCAO = "Em Producao"
    FINALIZADA = "Finalizada"
    CANCELADA = "Cancelada"