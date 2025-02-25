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
        print(f"Quartos Ocupados: {quartos_ocupados}")
        print(f"Quartos Disponíveis: {quartos_livres}")
        print("Quartos Livres:", ', '.join(map(str, quartos_disponiveis)))

    def save_guest_info(self):
        atualizar_dtbase('guest_data.txt', self.guest_data)
        print("\nInformações do hóspede salvas com sucesso!")

    def load_guest_info(self):
        self.guest_data = ler_dtbase('guest_data.txt')
        print("\nInformações dos hóspedes carregadas com sucesso!")

    def update_room_status(self):
        for hospede in self.guest_data:
            if hospede['status']:
                for quarto in self.quartos:
                    if quarto.numero == hospede['quarto']:
                        quarto.disponivel = False

    def run(self):
        while True:
            print("\nSistema de Check-in do Hotel")
            print("1. Registrar novo hóspede")
            print("2. Exibir Dashboard")
            print("3. Realizar Check-out")
            print("4. Salvar informações")
            print("5. Sair")
            
            option = input("\nEscolha uma opção: ")

            if option == '1':
                self.get_guest_info()
            elif option == '2':
                self.show_dashboard()
            elif option == '3':
                self.checkout_guest()
            elif option == '4':
                self.save_guest_info()
            elif option == '5':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida, tente novamente.")


def atualizar_dtbase(file, hospedes):
    with open(file, 'w') as dt:
        for hospede in hospedes:
            linha = f"{hospede['nome']},{hospede['quarto']},{hospede['entrada']},{hospede['saida']},{hospede['status']}\n"
            dt.write(linha)


def ler_dtbase(file):
    hospedes = []
    if os.path.exists(file):
        with open(file, 'r') as dt:
            for linha in dt:
                nome, quarto, entrada, saida, status = linha.strip().split(',')
                hospedes.append({
                    'nome': nome,
                    'quarto': int(quarto),
                    'entrada': entrada,
                    'saida': saida,
                    'status': status == 'True'
                })
    return hospedes


if __name__ == '__main__':
    hotel = HOTEL_MANAGEMENT_checkin()
    hotel.run()
