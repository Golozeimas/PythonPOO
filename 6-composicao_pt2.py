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
        # AQUI ACONTECE A COMPOSIÇÃO:
        # O Carro cria e gerencia as instâncias de Motor e Pneus
        self.motor = Motor(tipo_motor)
        self.pneus = Pneus(marca_pneu)

    def dirigir(self):
        # O Carro delega as tarefas para os objetos componentes
        ignicao = self.motor.ligar()
        movimento = self.pneus.rodar()
        return f"Dirigindo {self.modelo}:\n - {ignicao}\n - {movimento}"

# Uso
meu_carro = Carro("Ferrari", "V8", "Pirelli")
print(meu_carro.dirigir())