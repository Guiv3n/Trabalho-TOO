# main.py

# -*- coding: utf-8 -*- 
# Codificacao mantida, mas caracteres especiais serao substituidos na saida.

import sys
import os

# ====================================================================
# CORRECAO DO CAMINHO DE BUSCA (Solucao para ModuleNotFoundError)
# Isso adiciona o diretorio atual ao sys.path.
# ====================================================================
sys.path.append(os.path.dirname(__file__))


# CORRECAO: Importacoes diretas (sem 'model.' e sem 'patterns.')
from enums import EnumGenero, EnumPlano, EnumStatus
from usuario import Usuario
from factory import FabricaConteudo
from strategy import EstrategiaReproducao, ReproducaoSD, Reproducao4K, ReproducaoHD

print("================ INICIANDO TESTES DO SISTEMA DE STREAMING ================")
print("\n## 1. CRIACAO DE USUARIOS (SETUP DO STRATEGY INICIAL)")

# Usuario PREMIUM: Estrategia inicial e 4K
usuario_premium = Usuario("Mariana", "mariana@email.com", EnumPlano.PREMIUM)
# Usuario BASICO: Estrategia inicial e SD
usuario_basico = Usuario("Joao", "joao@email.com", EnumPlano.BASICO)
print("-" * 50)

# ==============================================================================
# TESTE 2: FACTORY PATTERN COM DADOS VALIDOS E INVALIDOS
# ==============================================================================
print("\n## 2. TESTE DE CRIACAO (FACTORY PATTERN)")

# 2.1. Criacao de Conteudo VALIDO (Factory em Acao)
print("--- 2.1. CRIACAO DE CONTEUDO VALIDO ---")
try:
    filme1 = FabricaConteudo.criar_conteudo(
        "FILME", 
        titulo="O Herdeiro da Terra", ano=2024, duracao_min=180, 
        genero=EnumGenero.FICCAO_CIENTIFICA, diretor="Guilherme", 
        nota_imdb=9.1, eh_original=True
    )
    serie1 = FabricaConteudo.criar_conteudo(
        "SERIE", 
        titulo="O Labirinto do Tempo", ano=2020, duracao_min=50, 
        genero=EnumGenero.DRAMA, num_temporadas=4, 
        status=EnumStatus.FINALIZADA, eh_original=False
    )
    animacao1 = FabricaConteudo.criar_conteudo(
        "ANIMACAO", 
        titulo="Os Bichos da Floresta", ano=2023, duracao_min=90, 
        genero=EnumGenero.ACAO, estudio="Toon Studios", 
        tecnica="2D", eh_original=True
    )
    print("Sucesso na criacao dos 3 conteudos validos.")
except Exception as e:
    print(f"ERRO CRITICO NA CRIACAO VALIDA: {e}")

# 2.2. Criacao de Conteudo INVALIDO (Verificacao das Validacoes)
print("\n--- 2.2. TESTE DE VALIDACOES DE ERRO (Factory e Setters) ---")

# A. Teste de Falha na Fabrica (Tipo invalido)
# CORRECAO DA LOGICA DO TESTE: Passar dados obrigatorios para que a Fabrica possa levantar o erro de TIPO invalido
try:
    FabricaConteudo.criar_conteudo(
        "DOCUMENTARIO", 
        titulo="...", ano=2020, duracao_min=60, genero=EnumGenero.DRAMA # Dados obrigatorios adicionados
    )
except ValueError as e:
    # A saida agora deve ser o erro mais especifico: "Tipo de conteudo 'DOCUMENTARIO' invalido para a Fabrica."
    print(f" Factory Erro Esperado (Tipo): {e}")

# B. Teste de Falha no Setter (Ano Invalido no construtor)
print("\nTeste de Validacao de Ano (try...except no Conteudo.setter):")
filme_invalido = FabricaConteudo.criar_conteudo(
    "FILME", 
    titulo="Viagem ao Futuro", ano=2030, duracao_min=120, # 2030 e invalido
    genero=EnumGenero.FICCAO_CIENTIFICA, diretor="B. Souza", 
    nota_imdb=7.0
)
# Verifica se o setter definiu o ano como None (Valor de seguranca)
print(f"Ano do filme invalido apos criacao: {filme_invalido.ano_lancamento}")
print("-" * 50)

# ==============================================================================
# TESTE 3: HERANCA E POLIMORFISMO (exibir_detalhes)
# ==============================================================================
print("\n## 3. TESTE DE POLIMORFISMO E HERANCA")
# O mesmo metodo, diferentes saidas (Heranca de Conteudo, Polimorfismo nas Subclasses)
print(filme1.exibir_detalhes())
print(serie1.exibir_detalhes())
print(animacao1.exibir_detalhes())
print("-" * 50)


# ==============================================================================
# TESTE 4: STRATEGY PATTERN (Reproducao de Conteudo)
# ==============================================================================
print("\n## 4. TESTE DE STRATEGY PATTERN E AGREGACAO")

# Adicionar a lista para poder assistir
usuario_premium.adicionar_na_lista(filme1)
usuario_premium.adicionar_na_lista(serie1)
usuario_basico.adicionar_na_lista(filme1) # Joao adiciona o mesmo filme

# 4.1. Teste de Estrategia Inicial (4K vs SD)
print("--- 4.1. ESTRATEGIA INICIAL ---")
usuario_premium.assistir(filme1) # Deve usar 4K (Estrategia inicial)
usuario_basico.assistir(filme1) # Deve usar SD (Estrategia inicial)

# 4.2. Teste de Mudanca de Estrategia em Tempo de Execucao
print("\n--- 4.2. MUDANCA DE ESTRATEGIA (FLEXIBILIDADE) ---")
# Muda o plano basico para usar HD (demonstrando a flexibilidade do Strategy)
usuario_basico.configurar_estrategia(ReproducaoHD())
usuario_basico.assistir(filme1) # Agora deve usar HD

# 4.3. Teste de Logica Especifica da Estrategia (duracao longa no SD)
usuario_basico.configurar_estrategia(ReproducaoSD())
usuario_basico.assistir(filme1) # O filme1 tem 180 min, deve acionar o aviso SD.
print("-" * 50)

print("\n================ FIM DOS TESTES ================ ")