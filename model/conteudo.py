# conteudo.py

from abc import ABC, abstractmethod
import datetime 
from enums import EnumGenero, EnumStatus

# A Superclasse Abstrata (Abstracao)
class Conteudo(ABC):
    def __init__(self, titulo: str, ano: int, duracao_min: int, genero: EnumGenero, eh_original: bool = False):
        # Encapsulamento
        self.titulo = titulo
        self.ano_lancamento = ano      
        self.duracao_min = duracao_min 
        self.genero = genero
        self.eh_original = eh_original

    
    # Atributo: Titulo
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, novo_titulo: str):
        self.__titulo = novo_titulo.strip().title()

    # Atributo: Ano de Lancamento
    @property
    def ano_lancamento(self):
        return self.__ano_lancamento
    
    @ano_lancamento.setter
    def ano_lancamento(self, ano):
        ano_atual = datetime.date.today().year 
        
        try:
            ano_int = int(ano)
            
            if ano_int > ano_atual:
                raise ValueError("O ano de lancamento nao pode ser futuro.")
            if ano_int < 1890:
                raise ValueError("Ano de lancamento muito antigo (minimo 1890).")
                
            self.__ano_lancamento = ano_int
            
        except (ValueError, TypeError) as e:
            # Captura erros de conversao de tipo e erros logicos
            print(f"\n ERRO DE VALIDACAO de Ano: {e}. Valor '{ano}' ignorado.")
            self.__ano_lancamento = None 

    # Atributo: Duracao Minima
    @property
    def duracao_min(self):
        return self._duracao_min 
    
    @duracao_min.setter
    def duracao_min(self, minutos):
        try:
            minutos_int = int(minutos)
            
            if minutos_int <= 0:
                raise ValueError("A duracao deve ser um numero positivo.")
                
            self._duracao_min = minutos_int
            
        except (ValueError, TypeError) as e:
            print(f"\n ERRO DE VALIDACAO de Duracao: {e}. Valor '{minutos}' ignorado.")
            self._duracao_min = 1 # Valor padrao

    # Metodo comum herdado pelas subclasses
    def reproduzir(self, usuario):
        status_original = "ORIGINAL" if self.eh_original else "LICENCIADO"
        print(f"[{status_original}] Iniciando '{self.titulo}'...") 

    # Metodo Abstrato (Obrigatorio para as subclasses)
    @abstractmethod
    def exibir_detalhes(self) -> str:
        pass

# ---------------- SUBCLASSES CONCRETAS ----------------

class Filme(Conteudo):
    def __init__(self, titulo, ano, duracao_min, genero, diretor: str, nota_imdb: float, eh_original=False):
        super().__init__(titulo, ano, duracao_min, genero, eh_original) # Chama o construtor do pai
        self.diretor = diretor
        self.nota_imdb = nota_imdb

    # Polimorfismo: Implementacao especifica para Filme
    def exibir_detalhes(self) -> str:
        detalhes = f"Filme: {self.titulo} ({self.ano_lancamento})\n"
        detalhes += f" 	Genero: {self.genero.value} | Duracao: {self.duracao_min} min\n"
        detalhes += f" 	Diretor: {self.diretor} | IMDb: {self.nota_imdb}\n"
        return detalhes

class Serie(Conteudo):
    def __init__(self, titulo, ano, duracao_min, genero, num_temporadas: int, status: EnumStatus, eh_original=False):
        super().__init__(titulo, ano, duracao_min, genero, eh_original)
        self.num_temporadas = num_temporadas
        self.status_producao = status

    # Polimorfismo: Implementacao especifica para Serie
    def exibir_detalhes(self) -> str:
        detalhes = f"Serie: {self.titulo} ({self.ano_lancamento})\n"
        detalhes += f" 	Genero: {self.genero.value} | {self.num_temporadas} Temporadas\n"
        detalhes += f" 	Status: {self.status_producao.value}\n"
        return detalhes

class Animacao(Conteudo):
    def __init__(self, titulo, ano, duracao_min, genero, estudio: str, tecnica: str, eh_original=False):
        super().__init__(titulo, ano, duracao_min, genero, eh_original)
        self.estudio_animacao = estudio
        self.tecnica_animacao = tecnica

    # Polimorfismo: Implementacao especifica para Animacao
    def exibir_detalhes(self) -> str:
        detalhes = f"Animacao: {self.titulo} ({self.ano_lancamento})\n"
        detalhes += f" 	Genero: {self.genero.value} | Duracao: {self.duracao_min} min\n"
        detalhes += f" 	Estudio: {self.estudio_animacao} | Tecnica: {self.tecnica_animacao}\n"
        return detalhes