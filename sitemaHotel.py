import os
from datetime import datetime

class Hospede:
    def __init__(self, nome, data_entrada, data_saida):
        self.nome = nome
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        
class Quarto:
    def __init__(self, numero):
        self.numero = numero
        self.disponivel = True

class HOTEL_MANAGEMENT_checkin:
    def __init__(self):
        self.guest_data = []
        self.quartos = [Quarto(i) for i in range(1, 10)]
        self.load_guest_info()
        self.update_room_status()

    def validar_data(self, data):
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return True
        except ValueError:
            return False
        
    def validarPeriodo(self, data_entrada, data_saida):
        data_entrada = datetime.strptime(data_entrada, "%d/%m/%Y")
        data_saida = datetime.strptime(data_saida, "%d/%m/%Y")
        return data_saida >= data_entrada
           
    def check_in(self, nome, data_entrada, data_saida):
        if not nome.replace(" ", "").isalpha():
            print("Erro: O nome deve conter apenas letras.")
            return False

        if not self.validar_data(data_entrada) or not self.validar_data(data_saida):
            print("Erro: Data inválida. Use o formato dd/mm/yyyy.")
            return False
        
        if not self.validarPeriodo(data_entrada, data_saida):
            print("Erro: A data de saída não pode ser anterior à data de entrada.")
            return False
        
        return True

    def get_guest_info(self):
        name = input("Nome do Cliente: ")
        date_in = input("Data de Entrada: ")
        date_out = input("Data de Saída: ")
        if self.check_in(name, date_in, date_out):
            hospede = Hospede(name, date_in, date_out)
            for quarto in self.quartos:
                if quarto.disponivel:
                    quarto.disponivel = False
                    self.guest_data.append({
                        'nome': hospede.nome,
                        'quarto': quarto.numero,
                        'entrada': hospede.data_entrada,
                        'saida': hospede.data_saida,
                        'status': True
                    })
                    print(f"{hospede.nome} hospedado no quarto {quarto.numero} de {hospede.data_entrada} até {hospede.data_saida}.")
                    return
            print("Sem quartos disponíveis.")
        else:
            print("Registro cancelado devido a erros nos dados.")

    def checkout_guest(self):
        nome = input("Digite o nome do hóspede para check-out: ")
        for hospede in self.guest_data:
            if hospede['nome'].lower() == nome.lower() and hospede['status']:
                hospede['status'] = False
                for quarto in self.quartos:
                    if quarto.numero == hospede['quarto']:
                        quarto.disponivel = True
                        break
                print(f"Check-out realizado com sucesso para {nome}.")
                return
        print("Hóspede não encontrado ou já fez check-out.")

    def show_dashboard(self):
        print("\nDashboard do Hotel:")
        print("===================================")
        quartos_ocupados = 0
        quartos_disponiveis = []
        for quarto in self.quartos:
            if not quarto.disponivel:
                quartos_ocupados += 1
                print(f"Quarto {quarto.numero} ocupado")
                for guest in self.guest_data:
                    if guest['quarto'] == quarto.numero and guest['status']:
                        print(f"  Hóspede: {guest['nome']}, Entrada: {guest['entrada']}, Saída: {guest['saida']}")
            else:
                quartos_disponiveis.append(quarto.numero)
        quartos_livres = len(self.quartos) - quartos_ocupados
        print("\nResumo:")
        print(f"Total de Quartos: {len(self.quartos)}")
