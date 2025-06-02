from .Veiculo import Veiculo


class Proprietario(Veiculo):
    def __init__(self, nome, cpf, placa_veiculo=None):
        self.nome = nome
        self.cpf = cpf
        self.placa_veiculo = placa_veiculo # Placa do veículo que possui
        super().__init__(self, modelo=None)
       

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_placa_veiculo(self):
        return self.placa_veiculo


    def __str__(self):
        if f"({self.placa_veiculo})":
            return (f"Nome: {self.nome}, CPF: {self.cpf}, Modelo: {self.__modelo} Placa: {self.placa_veiculo}")
        else: "Nenhum"