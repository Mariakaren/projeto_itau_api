class Pessoa:
    def __init__(self, nome_completo, data_nascimento, endereco, cpf, estado_civil):
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cpf = cpf
        self.estado_civil = estado_civil

    def __str__(self):
        return f"Nome: {self.nome_completo}\nData de Nascimento: {self.data_nascimento}\nEndereço: {self.endereco}\nCPF: {self.cpf}\nEstado Civil: {self.estado_civil}"
    
nome_completo = input("Digite seu nome completo:")
data_nascimento = input("Digite data_nascimento:")
endereco = input("Digite endereco:")
cpf = input("Digite cpf:")
estado_civil = input("Digite estado_civil:")

p1 = Pessoa(nome_completo, data_nascimento, endereco, cpf, estado_civil)

