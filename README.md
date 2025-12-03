# Projeto Final: Sistema de Gerenciamento de Streaming (TOO)

## Introdução

Este projeto consiste em um sistema de gerenciamento de conteúdo e usuários, implementado em Python, que visa a demonstração acadêmica dos **quatro pilares da Programação Orientada a Objetos (POO)** e de dois **Design Patterns** fundamentais: **Factory** e **Strategy**.

O sistema simula a arquitetura de uma plataforma de *streaming*, gerenciando a criação de diferentes tipos de conteúdo (`Filme`, `Série`, `Animação`) e controlando a qualidade de reprodução com base no plano de assinatura do usuário.

---

## Modelagem e Estrutura

O design do sistema é baseado em uma **hierarquia de classes** para o conteúdo e uma **separação de responsabilidades** para os comportamentos de criação e execução.

### Estrutura de Arquivos (Nível Único)
Todos os módulos (`.py`) residem no mesmo diretório para simplificar a resolução de dependências e importações.

* `main.py`: Script principal de testes e demonstração.
* `conteudo.py`: Contém a hierarquia de classes `Conteudo`, `Filme`, `Série`, e `Animação`.
* `usuario.py`: Contém a classe `Usuario`.
* `factory.py`: Implementa o **Factory Pattern**.
* `strategy.py`: Implementa o **Strategy Pattern**.
* `enums.py`: Contém as enumerações (`Enums`) utilizadas no sistema.

### Diagrama UML de Classes
O diagrama representa a relação de Herança entre o Conteúdo e a relação de Associação/Strategy com o Usuário e a Fábrica.


---

## Aplicação dos Pilares da POO

### 1. Abstração e Herança

A base do sistema é estabelecida pela reutilização e especialização de código:

* **Abstração**: A classe **`Conteudo`** é definida como uma **Classe Abstrata (ABC)**, impedindo sua instanciação direta. Ela estabelece um **contrato** de métodos obrigatórios, como `exibir_detalhes()`, que devem ser implementados pelas classes filhas.
* **Herança**: As classes **`Filme`**, **`Série`**, e **`Animação`** herdam de `Conteudo`, adquirindo seus atributos e métodos, promovendo a reutilização de código e a criação de hierarquias.

### 2. Polimorfismo

O princípio do Polimorfismo é demonstrado na adaptabilidade dos métodos:

* O método **`exibir_detalhes()`** é definido como abstrato na classe `Conteudo`.
* Cada subclasse concreta **sobrescreve (Override)** esse método, fornecendo uma implementação única que exibe dados específicos (e.g., `diretor` para Filme vs. `num_temporadas` para Série), refletindo o comportamento de "muitas formas".

### 3. Encapsulamento

O Encapsulamento é utilizado para proteger a integridade dos dados e controlar o acesso aos atributos:

* **Proteção de Dados**: Atributos internos são designados como protegidos ou privados (`__titulo`, `_duracao_min`).
* **Validação por Setters**: A manipulação de atributos críticos (`ano_lancamento`, `duracao_min`) é realizada através de métodos **`@property`** e **`@setter`**. O *setter* incorpora a lógica **`try...except`** para validar o valor de entrada (e.g., garantir que o ano não seja futuro e que a duração seja positiva), protegendo o estado do objeto.

---

## Implementação dos Design Patterns

### 1. Factory Pattern (Padrão de Criação Obrigatório)

O Factory Pattern é implementado para desacoplar a lógica de criação de objetos da lógica principal do sistema.

* **Classe**: **`FabricaConteudo`** (`factory.py`).
* **Função**: O método estático `criar_conteudo()` centraliza a lógica de instanciação. Ele recebe um identificador de `tipo` (e.g., `"FILME"`) e retorna a subclasse correta, eliminando a necessidade de lógica condicional explícita (`if/else`) no código de chamada.
* **Robustez**: A Fábrica serve como o ponto primário de **validação de dados**, verificando se os parâmetros obrigatórios foram fornecidos e se a conversão de tipos é segura antes de criar o objeto.

### 2. Strategy Pattern (Padrão Comportamental Adicional)

O Strategy Pattern permite que o algoritmo a ser utilizado seja selecionado em tempo de execução, promovendo flexibilidade.

* **Classes**: **`IEstrategiaReproducao`** (interface) e **`ReproducaoSD`**, **`ReproducaoHD`**, **`Reproducao4K`** (Estratégias Concretas).
* **Função**: Permite que o **algoritmo** de determinação de qualidade de reprodução (`aplicar_qualidade()`) seja trocado **dinamicamente** no objeto `Usuario`.
* **Execução**: O `Usuario` armazena a estratégia atual e delega a execução do método de qualidade à instância configurada, garantindo que o comportamento seja apropriado ao plano de assinatura.

---

## Instruções de Execução

O script principal (`main.py`) é configurado para realizar um conjunto de testes que validam a correta aplicação de todos os pilares e padrões.

1.  **Requisitos**: Certifique-se de que todos os arquivos (`.py`) estejam no mesmo diretório e que o código não contenha caracteres acentuados ou emojis, para compatibilidade com a codificação do terminal.
2.  **Execução**: Abra o terminal no diretório do projeto e execute o script de testes:

python main.py
