from utils import *
hospedes = ler_dtbase('dataBase.txt') 
    
def check_out(nomeHospede):
    for hospede in hospedes:
        if hospede['nome'] == nomeHospede: 
            valor_a_pagar = valorEstadia(hospede['entrada'])
            save_hostorico(hospede)
            
            hospede['nome'] = 'nome do hospede'
            hospede['entrada'] = 'data chek-in'
            hospede['saida'] = 'data check-out'
            hospede['status'] = True
            atualizar_dtbase('dataBase.txt',hospedes)
            print(f'{nomeHospede} fez check-out \nA estadia ficou em R${valor_a_pagar}')
            return
            
    print('O Hospede {} não está cadastrado no hotel'.format(nomeHospede))
    return
