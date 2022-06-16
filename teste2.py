# Por criterios da escrita ("informado um número, ele calcule a sequência de Fibonacci")
# do problema, este problema foi resolvido com um algoritmo que refaz a sequência
# a cada chamada da função, porém é possivel chegar em uma solução que 
# alcance o tempo de Omega(log n)

def verifica_numero_na_sequencia(numero_sequencia, numero_entrada):
    return (numero_sequencia == numero_entrada)

def teste(numero):
    antecessor = 0
    atual = 1
    
    # Verifica se o número informado é um dos números iniciais da Sequencia de Fibonacci
    if numero == 1 or numero == 1:
        return "Pertence a sequência"
    
    # Calcula a Sequência e para cada passo verifica se o número informado faz parte da sequência 
    # Tal procediomento está na ordem de O(n), onde n é o número de elementos processado
    while atual < numero:
        proximo = antecessor + atual
        antecessor = atual
        atual = proximo
        if verifica_numero_na_sequencia(atual, numero):
            return "Pertence a sequência"
    return "Não pertence a sequência"

def main():
    print(teste(144)) # Pertence
    print(teste(18)) # Não pertence
    print(teste(1597)) # Pertence
    print(teste(1964)) # Não pertence

if __name__ == "__main__":
    main()