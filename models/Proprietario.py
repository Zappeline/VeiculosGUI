class Proprietario:
    def __init__(self, nome, cpf, placa_veiculo=None, veiculo_associado=None):
        self.nome = nome
        self.cpf = cpf
        self.placa_veiculo = placa_veiculo # Placa do veículo que possui
        self.veiculo_associado = veiculo_associado # Referência ao objeto Veiculo

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_placa_veiculo(self):
        return self.placa_veiculo

    def set_veiculo_associado(self, veiculo):
        self.veiculo_associado = veiculo

    def __str__(self):
        veiculo_info = f"Veículo: {self.veiculo_associado.get_modelo()} ({self.placa_veiculo})" if self.veiculo_associado else "Nenhum"
        return f"Nome: {self.nome}, CPF: {self.cpf}, {veiculo_info}"