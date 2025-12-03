# factory.py

# -*- coding: utf-8 -*-
from conteudo import Filme, Serie, Animacao 
from enums import EnumGenero, EnumStatus 

class FabricaConteudo:
    @staticmethod
    def criar_conteudo(tipo: str, **kwargs):
        """
        Metodo de fabrica que cria e retorna o objeto Conteudo correto,
        incluindo validacoes e tratamento de erro.
        """
        tipo = tipo.upper()

        # --- 1. Recupera e Valida Parametros Comuns e Obrigatorios ---
        titulo = kwargs.get('titulo')
        ano = kwargs.get('ano')
        duracao_min = kwargs.get('duracao_min')
        genero = kwargs.get('genero')
        eh_original = kwargs.get('eh_original', False)

        # 1.1. Verifica a existencia dos parametros basicos
        if not all([titulo, ano, duracao_min, genero]):
            raise ValueError("Parametros basicos obrigatorios (titulo, ano, duracao_min, genero) ausentes.")
        
        # 1.2. Verifica o tipo do Genero (deve ser um Enum)
        if not isinstance(genero, EnumGenero):
             raise TypeError(f"O parametro 'genero' deve ser um EnumGenero, recebido: {type(genero)}")

        # --- 2. Logica de Criacao por Tipo (Factory Method) ---
        
        if tipo == "FILME":
            diretor = kwargs.get('diretor')
            nota_imdb = kwargs.get('nota_imdb')
            
            # Validacao especifica de Filme
            if not all([diretor, nota_imdb]):
                raise ValueError("Parametros especificos para FILME (diretor, nota_imdb) ausentes.")
                
            try:
                # Cria a instancia, garantindo conversao de tipos criticos
                return Filme(
                    titulo=titulo,
                    ano=int(ano),
                    duracao_min=int(duracao_min),
                    genero=genero,
                    diretor=diretor,
                    nota_imdb=float(nota_imdb),
                    eh_original=eh_original
                )
            except ValueError as e:
                # Captura erros de conversao (ex: nota_imdb='invalido')
                raise ValueError(f"Erro de conversao de tipo ao criar FILME: {e}")

        elif tipo == "SERIE":
            num_temporadas = kwargs.get('num_temporadas')
            status = kwargs.get('status')
            
            # Validacao especifica de Serie
            if not all([num_temporadas, status]):
                raise ValueError("Parametros especificos para SERIE (num_temporadas, status) ausentes.")
            
            # Verifica se o status e o Enum correto
            if not isinstance(status, EnumStatus):
                 raise TypeError(f"O parametro 'status' deve ser um EnumStatus, recebido: {type(status)}")

            try:
                return Serie(
                    titulo=titulo,
                    ano=int(ano),
                    duracao_min=int(duracao_min),
                    genero=genero,
                    num_temporadas=int(num_temporadas),
                    status=status,
                    eh_original=eh_original
                )
            except ValueError as e:
                 raise ValueError(f"Erro de conversao de tipo ao criar SERIE: {e}")

        elif tipo == "ANIMACAO":
            estudio = kwargs.get('estudio')
            tecnica = kwargs.get('tecnica')
            
            # Validacao especifica de Animacao
            if not all([estudio, tecnica]):
                raise ValueError("Parametros especificos para ANIMACAO (estudio, tecnica) ausentes.")

            try:
                return Animacao(
                    titulo=titulo,
                    ano=int(ano),
                    duracao_min=int(duracao_min),
                    genero=genero,
                    estudio=estudio,
                    tecnica=tecnica,
                    eh_original=eh_original
                )
            except ValueError as e:
                 raise ValueError(f"Erro de conversao de tipo ao criar ANIMACAO: {e}")
                 
        else:
            # Caso o tipo nao seja reconhecido (mantido)
            raise ValueError(f"Tipo de conteudo '{tipo}' invalido para a Fabrica.")