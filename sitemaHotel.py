import pickle
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
        
        self.guest_data = {}
        self.load_guest_info()
        self.quartos = [Quarto(i) for i in range(1, 10)]
        
    def validar_data(self, data):
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def check_in(self, nome, data_entrada, data_saida):
        if not nome.replace(" ", "").isalpha():
            print("Erro: O nome deve conter apenas letras.")
            return 

        if not self.validar_data(data_entrada) or not self.validar_data(data_saida):
            print("Erro: Data inválida. Use o formato dd/mm/yyyy.")
            return
        return True

    def get_guest_info(self):
        
        name = input("Nome do Cliente: ")
        date_in = input("Data de Entrada: ")
        date_out = input("Data de Saída: ")
        if self.check_in(name, date_in, date_out):
            self.guest_data["nome"] = name
            self.guest_data["data_entrada"] = date_in
            self.guest_data["data_saida"] = date_out
            print(self.guest_data["nome"])
            hospede = Hospede(self.guest_data["nome"],self.guest_data["data_entrada"], self.guest_data["data_saida"])
            for quarto in self.quartos:
                if quarto.disponivel:
                    quarto.disponivel = False
                    self.guest_data[self.guest_data['nome']] = (hospede, quarto)
                    print("Informações do hóspede registradas com sucesso!")
                    print(f"{self.guest_data['nome']} hospedado no quarto {quarto.numero} de {self.guest_data['data_entrada']} até {self.guest_data['data_saida']}.")                 
                    return
            print("Sem quartos disponíveis.")
            
        else:
            print("Registro cancelado devido a erros nos dados.")

    def show_guest_info(self):
        
        if not self.guest_data:
            print("\nNenhuma informação de hóspede encontrada.")
        else:
            print("\nInformações do Hóspede:")
            print(f"Nome: {self.guest_data.get('Nome')}")
            print(f"Telefone: {self.guest_data.get('Telefone')}")
            print(f"Endereço: {self.guest_data.get('Endereço')}")

    def save_guest_info(self):
        
        with open('guest_data.pkl', 'wb') as file:
            pickle.dump(self.guest_data, file)
        print("\nInformações do hóspede salvas com sucesso!")

    def load_guest_info(self):
        
        try:
            with open('guest_data.pkl', 'rb') as file:
                self.guest_data = pickle.load(file)
            print("\nInformações do hóspede carregadas com sucesso!")
        except FileNotFoundError:
            print("\nNenhum dado de hóspede encontrado. Nenhum arquivo salvo.")

    def run(self):
        
        while True:
            print("\nSistema de Check-in do Hotel")
            print("1. Registrar novo hóspede")
            print("2. Exibir informações do hóspede")
            print("3. Salvar informações")
            print("4. Carregar informações salvas")
            print("5. Sair")
            
            option = input("\nEscolha uma opção: ")

            if option == '1':
                self.get_guest_info()
            elif option == '2':
                self.show_guest_info()
            elif option == '3':
                self.save_guest_info()
            elif option == '4':
                self.load_guest_info()
            elif option == '5':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    hotel = HOTEL_MANAGEMENT_checkin()
    hotel.run()
