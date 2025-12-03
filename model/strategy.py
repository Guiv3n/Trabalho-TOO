# strategy.py

# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from conteudo import Conteudo # Para tipagem

# Interface/Classe Abstrata da Estrategia
class EstrategiaReproducao(ABC):
    """Define a interface para o algoritmo de reproducao."""
    @abstractmethod
    def aplicar_qualidade(self, conteudo: Conteudo):
        pass

# Estrategia Concreta 1: Qualidade Padrao
class ReproducaoSD(EstrategiaReproducao):
    def aplicar_qualidade(self, conteudo: Conteudo):
        print("   Qualidade: SD (Definicao Padrao) aplicada.")
        if conteudo._duracao_min > 150:
             print("   Aviso: Filmes longos em SD podem demorar a carregar.")

# Estrategia Concreta 2: Qualidade Alta
class Reproducao4K(EstrategiaReproducao):
    def aplicar_qualidade(self, conteudo: Conteudo):
        print("   Qualidade: 4K Ultra HD aplicada.")
        print("   Verificando compatibilidade com dispositivo e banda larga...")

# Estrategia Concreta 3 (Opcional para demonstrar flexibilidade)
class ReproducaoHD(EstrategiaReproducao):
    def aplicar_qualidade(self, conteudo: Conteudo):
        print("   Qualidade: HD (Alta Definicao) aplicada.")