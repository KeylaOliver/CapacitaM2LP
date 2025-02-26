from datetime import datetime

def ler_dtbase(file):
    hospedes = []
    with open(file, 'r') as dt:
        for linha in dt:
            nome, quarto, entrada,saida, status = linha.strip().split(',')
            hospedes.append({
                'nome': nome,
                'quarto': int(quarto),
                'entrada': entrada,
                'saida': saida,
                'status': bool(status)
            })
    return hospedes

def save_hostorico(hospede):
    with open('historico.txt', 'a') as ht:
        linha_historico = f'{hospede["nome"]}\n'
        ht.write(linha_historico)
        return

def atualizar_dtbase(file, hospedes):
    with open(file, 'w') as dt:
        for hospede in hospedes:
            linha = f"{hospede['nome']},{hospede['quarto']},{hospede['entrada']},{hospede['status']}\n"
            dt.write(linha)
        return

def valorEstadia(dataEntrada):
    diaria = 50  
    entrada = datetime.strptime(dataEntrada, "%Y-%m-%d")
    saida = datetime.now()  
    
    diferenca = (saida - entrada).days
    valorApagar = diferenca * diaria
    
    return max(0, valorApagar)
