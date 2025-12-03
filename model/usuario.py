# usuario.py

# -*- coding: utf-8 -*-
from conteudo import Conteudo
from enums import EnumPlano
from strategy import EstrategiaReproducao, ReproducaoSD, Reproducao4K, ReproducaoHD 

class Usuario:
    def __init__(self, nome: str, email: str, plano: EnumPlano):
        # As atribuicoes passam diretamente (string/Enum nao precisam de setter complexo)
        self.__nome = nome
        self.__email = email
        self.__plano = plano
        self.__lista_assistir = []  # Agregacao: Lista de Conteudo
        self._estrategia_reproducao = None # Objeto que armazena a estrategia atual

        # Define a estrategia inicial baseada no plano
        self.__configurar_estrategia_inicial()

    # Getters para acesso controlado (Encapsulamento)
    @property
    def nome(self):
        return self.__nome
    
    @property
    def plano(self):
        return self.__plano

    def __configurar_estrategia_inicial(self):
        """Define a estrategia inicial (padrao) com base no plano."""
        # Se for PREMIUM, ja inicia com 4K, senao, inicia com SD
        if self.__plano == EnumPlano.PREMIUM:
             self.configurar_estrategia(Reproducao4K()) 
        else:
             self.configurar_estrategia(ReproducaoSD())

    def configurar_estrategia(self, estrategia: EstrategiaReproducao):
        """
        Define qual classe de Estrategia de Reproducao sera usada.
        (Parte da implementacao do Strategy Pattern)
        """
        # Adicao de Validacao (validacao de tipo e boa pratica)
        if not isinstance(estrategia, EstrategiaReproducao):
            raise TypeError("A estrategia deve ser uma instancia de EstrategiaReproducao.")
            
        self._estrategia_reproducao = estrategia
        print(f"[{self.nome}] Estrategia de reproducao configurada para: {type(estrategia).__name__}")

    def adicionar_na_lista(self, item: Conteudo):
        """Adiciona um item Conteudo a lista do usuario."""
        if isinstance(item, Conteudo):
            self.__lista_assistir.append(item)
            print(f"'{item.titulo}' adicionado a lista de {self.nome}.") 
        else:
            print("Erro: O item deve ser um objeto Conteudo.")

    def listar_biblioteca(self):
        """Exibe todos os titulos na lista do usuario."""
        print(f"\n--- Lista de Assistir de {self.nome} ({len(self.__lista_assistir)} titulos) ---")
        for i, item in enumerate(self.__lista_assistir):
            print(f"     {i+1}. {item.titulo} ({item.genero.value})")

    def assistir(self, conteudo: Conteudo):
        """
        Tenta reproduzir o conteudo usando a estrategia configurada.
        (Execucao do Strategy Pattern)
        """
        if conteudo in self.__lista_assistir:
            print(f"\n[{self.nome} - {self.plano.value}] Preparando para assistir '{conteudo.titulo}'")
            
            # Chama o metodo da ESTRATEGIA configurada
            self._estrategia_reproducao.aplicar_qualidade(conteudo)
            
            conteudo.reproduzir(self)
        else:
            print(f"'{conteudo.titulo}' nao esta na lista de {self.nome}. Adicione primeiro.")