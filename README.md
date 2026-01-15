# Guia de Programação Orientada a Objetos em Python

## Introdução

Este guia apresenta os conceitos fundamentais de Programação Orientada a Objetos (POO) em Python, desde a criação de classes básicas até conceitos avançados como herança, composição e encapsulamento.

## 1. Classes Básicas

Uma classe é um modelo para criar objetos. Em Python, definimos classes usando a palavra-chave `class`.

```python
class Game:
    gameName = ""
    yearLaunch = 0
    note = 0.0
    multiplayer = False
```

## 2. Criando Objetos

Objetos são instâncias de uma classe. Criamos objetos chamando a classe como se fosse uma função.

```python
# Criando o primeiro objeto
game1 = Game()
game1.gameName = "Star wars jedi fallen order"
game1.yearLaunch = 2019
game1.note = 9.5
game1.multiplayer = False

# Criando o segundo objeto
game2 = Game()
game2.gameName = "Devil may cry 5"
game2.yearLaunch = 2019
game2.note = 9
game2.multiplayer = False
```

## 3. Métodos Especiais

### `__init__` - Construtor

O método `__init__` funciona como um construtor, inicializando os atributos do objeto quando ele é criado.

```python
def __init__(self, gameName="", yearLaunch=0, note=0.0, multiplayer=False):
    self.gameName = gameName
    self.yearLaunch = yearLaunch
    self.multiplayer = multiplayer
    self.note = note
```

### `__str__` - Representação em String

O método `__str__` define como o objeto será representado quando convertido para string.

```python
def __str__(self):
    return f"- nome do jogo: {self.gameName},\n- nota do jogo: {self.note}\n e ano de lançamento: {self.yearLaunch}"
```

### Variáveis de Classe vs Instância

```python
class Game:
    total_games = 0  # Variável de classe (compartilhada por todos os objetos)
    
    def __init__(self, gameName):
        self.gameName = gameName  # Variável de instância (única para cada objeto)
        Game.total_games += 1
```

## 4. Herança

Herança permite que uma classe (filha) herde atributos e métodos de outra classe (pai).

```python
class Game:
    def __init__(self, gameName, yearLaunch, note, multiplayer):
        self.gameName = gameName
        self.yearLaunch = yearLaunch
        self.note = note
        self.multiplayer = multiplayer

# Classe filha herda de Game
class SinglePlayGame(Game):
    def __init__(self, gameName="", yearLaunch=0, note=0.0, multiplayer=False, storyline=""):
        super().__init__(gameName, yearLaunch, note, multiplayer)
        self.storyline = storyline
```

### Sobrescrita de Métodos

A classe filha pode modificar o comportamento de métodos herdados.

```python
def substitui_os_dados(self):
    super().substitui_os_dados()  # Chama o método da classe pai
    self.storyline = input("Coloque o enredo do jogo:\n")
    print(f"\nenredo: {self.storyline}")
```

## 5. Composição

Composição é quando uma classe contém objetos de outras classes como atributos.

### Exemplo 1: Studio de Jogos

```python
class StudioGame:
    def __init__(self, nome_do_estudio):
        self.nome_do_estudio = nome_do_estudio
        self.jogos_lancados = []  # Lista de objetos Game
    
    def adiciona_jogo(self, game):
        self.jogos_lancados.append(game)
    
    def media_do_estudio(self):
        notas = sum(game.note for game in self.jogos_lancados)
        jogos = len(self.jogos_lancados)
        
        if jogos == 0:
            print("Não existe jogos da empresa")
        else:
            media = notas / jogos
            print(f"Essa é média do estudio: {media:.2f}")
```

### Exemplo 2: Carro com Motor e Pneus

```python
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def ligar(self):
        return f"Motor {self.tipo} fazendo VRUMMM!"

class Pneus:
    def __init__(self, marca):
        self.marca = marca
    
    def rodar(self):
        return f"Pneus {self.marca} girando na estrada."

class Carro:
    def __init__(self, modelo, tipo_motor, marca_pneu):
        self.modelo = modelo
        self.motor = Motor(tipo_motor)      # Composição
        self.pneus = Pneus(marca_pneu)       # Composição
```

## 6. Encapsulamento

Encapsulamento protege atributos de acesso direto, usando convenções de nomenclatura.

### Atributos Privados

Usamos dois underscores (`__`) para tornar atributos privados.

```python
class Pessoa:
    def __init__(self, idade):
        self.__idade = idade  # Atributo privado
```

### Property (Getter)

Permite acessar atributos privados de forma controlada.

```python
@property
def idade(self):
    return self.__idade
```

### Setter

Permite modificar atributos privados com validação.

```python
@idade.setter
def idade(self, valor):
    if valor < 0:
        raise ValueError("Digite uma idade válida!")
    else:
        self.__idade = valor
```

### Uso

```python
pessoa1 = Pessoa(13)
print(pessoa1.idade)    # Usa o getter
pessoa1.idade = 20      # Usa o setter
```

## 7. Classes Abstratas

Classes abstratas definem métodos que devem ser implementados pelas classes filhas.

```python
from abc import ABC, abstractmethod

class Item_biblioteca(ABC):
    def __init__(self, titulo, autor, paginas, preco):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.preco = preco
    
    @abstractmethod
    def aplica_desconto(self):
        pass
```

### Implementando Classes Concretas

```python
class Livro(Item_biblioteca):
    def __init__(self, titulo, autor, paginas, isbn, preco):
        super().__init__(titulo, autor, paginas, preco)
        self.isbn = isbn
    
    def aplica_desconto(self):
        desconto = (self.preco * 10/100)
        valor_descontado = self.preco - desconto
        print(f"valor após desconto de 10%: {valor_descontado}")
        self.preco = valor_descontado

class Revista(Item_biblioteca):
    def __init__(self, titulo, autor, paginas, edicao, preco):
        super().__init__(titulo, autor, paginas, preco)
        self.edicao = edicao
    
    def aplica_desconto(self):
        desconto = (self.preco * 15/100)
        valor_descontado = self.preco - desconto
        print(f"valor após desconto de 15%: {valor_descontado}")
        self.preco = valor_descontado
```

## 8. Projeto Prático: Sistema de Biblioteca

### Estrutura do Projeto

```
OO_Projeto/
├── itens/
│   ├── item_biblioteca.py
│   ├── livros.py
│   └── revista.py
├── modelos/
│   ├── avaliacao.py
│   └── biblioteca.py
└── app.py
```

### Classe Biblioteca

```python
class Biblioteca:
    bibliotecas = []
    
    def __init__(self, nome_da_biblioteca, localizacao, ativa):
        Biblioteca.bibliotecas.append(self)
        self.nome_da_biblioteca = nome_da_biblioteca
        self.localizacao = localizacao
        self.__ativa = ativa
        self.lista_de_itens = []
    
    def adiciona_item(self, item):
        if isinstance(item, Item_biblioteca):
            self.lista_de_itens.append(item)
    
    @classmethod
    def listar_bibliotecas(cls):
        for bili in cls.bibliotecas:
            print(bili)
```

### Métodos Úteis

**`isinstance()`**: Verifica se um objeto é instância de uma classe.

```python
if isinstance(item, Item_biblioteca):
    self.lista_de_itens.append(item)
```

**`hasattr()`**: Verifica se um objeto possui determinado atributo.

```python
if hasattr(item, "isbn"):
    print(f"ISBN: {item.isbn}")
```

**`enumerate()`**: Itera sobre uma lista retornando índice e valor.

```python
for i, item in enumerate(self.lista_de_itens, start=1):
    print(f"Item {i}: {item.titulo}")
```

## Conceitos-Chave

### self
Referência ao objeto atual da classe.

### super()
Chama métodos da classe pai.

### @property
Cria getters para atributos.

### @classmethod
Métodos que recebem a classe (cls) ao invés da instância (self).

### ABC e @abstractmethod
Criam classes e métodos abstratos que devem ser implementados.

## Boas Práticas

1. Use nomes descritivos para classes e métodos
2. Encapsule dados sensíveis com atributos privados
3. Prefira composição à herança quando apropriado
4. Implemente `__str__` para representação legível dos objetos
5. Use classes abstratas para definir contratos entre classes
6. Documente suas classes e métodos
7. Valide dados nos setters

## Conclusão

A Programação Orientada a Objetos em Python oferece ferramentas poderosas para organizar e estruturar código de forma modular e reutilizável. Os conceitos de herança, composição, encapsulamento e abstração permitem criar sistemas complexos de maneira organizada e manutenível.
