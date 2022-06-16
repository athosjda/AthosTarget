import json

def maior_valor_dos_dados(dados):
    valor = 0
    for ele in dados:
        if ele['valor'] > valor:
            valor = ele['valor']
    return valor

def menor_valor_dos_dados(dados, maior_valor):
    valor = maior_valor+1
    for ele in dados:
        if ele['valor'] < valor and ele['valor'] > 0.0:
            valor = ele['valor']
    return valor

def media_dos_valores_dos_dados(dados):
    soma = 0.0
    numero_de_elementos_validos = 0
    for ele in dados:
        if ele['valor'] > 0.0:
            soma = soma + ele['valor']
            numero_de_elementos_validos += 1
    return soma / numero_de_elementos_validos

def dias_superior_a_media(dados):
    media = media_dos_valores_dos_dados(dados)
    dias = [ele['dia'] for ele in dados if ele['valor'] > media]
    return dias

def main():
    dados = {}
    with open('dados.json') as dados_json:
        dados = json.load(dados_json)
    maior = maior_valor_dos_dados(dados)
    menor = menor_valor_dos_dados(dados, maior)
    dias = dias_superior_a_media(dados)
    print(menor)
    print(maior)
    print(len(dias))

if __name__ == "__main__":
    main()