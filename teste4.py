def soma_dos_valores(dados):
    total = 0.0
    for ele in dados:
        total += ele['valor']
    return total

def porcentagem(total, valor):
    return (valor*100)/total

def main():
    dados = [{'estado': 'SP', 'valor': 67836.43},
    {'estado': 'RJ', 'valor': 36678.66},
    {'estado': 'MG', 'valor': 29229.88},
    {'estado': 'ES', 'valor': 27165.48},
    {'estado': 'Outros', 'valor': 19849.53}]

    valor_total = soma_dos_valores(dados)
    for ele in dados:
        print(f'{ele["estado"]}: {round(porcentagem(valor_total, ele["valor"]), 2)}%')

    

if __name__ == "__main__":
    main()