1) class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} tenho {self.idade} anos e trabalho como {self.profissao} ")

igor = Pessoa("Igor", 18, "Cientista da computação")
igor.saudacao()

2) class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def salario(self):
        print(f"O seu salario é de {self.saldo} dolares")
        
    def deposito(self, dinheiro):
        self.saldo += dinheiro
    
    def sacar_dinheiro(self, valor):
        if valor > self.saldo:
            print('voce nao pode sacar =)')
        else:
            self.saldo -= valor

igor = ContaBancaria('igor', 0)
igor.deposito(87)
igor.salario()

3) class Carro():
    def __init__(self, marca , modelo , ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def gerais(self):
        print(f"O carro da marca {self.marca}, de modelo {self.modelo} e ano {self.ano} esta andando a uma velocidade de {self.velocidade}")

    def rapido(self, acelerar):
        self.velocidade += acelerar

carro = Carro("Mercedes", "CL200", 2023, 187)
carro.rapido(37)
carro.gerais()

4) class FormaGeometrica:
    def calcular_a_área(self, raio):
        return 3.14*(raio**2)
    
class Circulo(FormaGeometrica):
    pass

class Retangulo(FormaGeometrica):
    def calcular_a_área(self, base, altura):
        return base*altura

class Quadrado(Retangulo):
    pass

circulo = Circulo()
area = circulo.calcular_a_área(12)
print(area)

retangulo = Retangulo()
area = retangulo.calcular_a_área(6,21)
print(area)

quadrado = Quadrado()
area = quadrado.calcular_a_área(6,6)
print(area)


5) class Animal():
    def __init__(self, patas, olhos, sons):
        self.patas = patas
        self.olhos = olhos
        self.sons = sons

class Cachorro(Animal):
    def qnt_patas(self , patas):
        print(f'O número de patas é: {self.patas}')

    def qnt_olhos(self,olhos):
        print(f'A quantidade de olhos é: {self.olhos}')

    def som_emitido(self,sons):
        print(f'O som emitido é: {self.sons}')

class Gato(Cachorro):
    pass

cachorro = Cachorro(4, 2, 'auau')
print("Cachorro:")
cachorro.qnt_patas(4)
cachorro.qnt_olhos(2)
cachorro.som_emitido('auau')

print()

gato = Gato(4,2,'miau')
print('Gato:')
gato.qnt_patas(4)
gato.qnt_olhos(2)
gato.som_emitido('miau')
