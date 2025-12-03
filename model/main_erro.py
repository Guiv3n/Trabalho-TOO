# main_erro.py

import sys
import os

# Correção do caminho de busca (necessário para encontrar os pacotes)
sys.path.append(os.path.dirname(__file__))

from enums import EnumGenero, EnumPlano, EnumStatus
from factory import FabricaConteudo

def testar_erros_criticos():
    """Demonstra o tratamento de excecoes no sistema."""
    print("================ INICIANDO TESTES CRITICOS DE ERRO ================")
    print("\nObjetivo: Provocar falhas nas classes e exibir a excecao.")
    print("-" * 50)

    # ------------------ TESTE 1: ERRO NO FACTORY (Parametros Ausentes) ------------------
    print("1. PROVOCANDO ERRO: PARAMETROS OBRIGATORIOS FALTANDO")
    try:
        # Faltam 'ano', 'duracao_min', 'genero', 'diretor', 'nota_imdb'
        FabricaConteudo.criar_conteudo(
            "FILME", 
            titulo="Filme Incompleto"
        )
    except ValueError as e:
        print(f" Tratamento de Erro (Factory): {e}")
        print("   Factory bloqueou a criacao por dados insuficientes.")
    
    print("-" * 50)

    # ------------------ TESTE 2: ERRO NO SETTER (Valor Invalido para Tipo) ------------------
    print("2. PROVOCANDO ERRO: VALOR DE TIPO INCORRETO (float para int)")
    try:
        # A Fabrica tenta converter nota_imdb='um' para float (falha esperada)
        FabricaConteudo.criar_conteudo(
            "FILME", 
            titulo="Erro de Tipo", ano=2020, duracao_min=100, 
            genero=EnumGenero.ACAO, diretor="X", nota_imdb="um" # Entrada invalida
        )
    except ValueError as e:
        print(f" Tratamento de Erro (Factory/Setter): {e}")
        print("   Factory bloqueou a criacao por erro de conversao de tipo.")

    print("-" * 50)

    # ------------------ TESTE 3: ERRO NO SETTER (Logica de Negocio Invalida) ------------------
    print("3. PROVOCANDO ERRO: LOGICA DE NEGOCIO (Duracao Negativa)")
    try:
        # A Fabrica passa duracao_min='-50', que falha no setter de Conteudo
        FabricaConteudo.criar_conteudo(
            "SERIE", 
            titulo="Duracao Negativa", ano=2020, duracao_min=-50, 
            genero=EnumGenero.DRAMA, num_temporadas=1, status=EnumStatus.EM_PRODUCAO
        )
    except ValueError as e:
        print(f" Alerta (Conteudo Setter): {e}")
        print("   A classe Conteudo.setter emitiu um aviso e usou o valor padrao (1).")
        # NOTE: Neste caso, o setter apenas emite o aviso e usa o valor padrao, 
        # mas a excecao nao 'sobe' ate aqui a menos que o setter a levante.

    print("================ TESTES CRITICOS CONCLUIDOS ======================")

if __name__ == "__main__":
    testar_erros_criticos()