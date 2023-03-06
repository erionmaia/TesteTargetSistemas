from encontrandoNumeroEmFibonacci import encontrandoNumeroEmFibonacci
from faturamentoDiario import faturamento
from faturamentoMensal import porcentagemFaturamento
from stringReverse import reversible

dadoJSON = "dados.json"

if __name__ == '__main__':
    numero = int(input("Digite o número que você deseja encontrar na Sequência de Fibonacci: "))
    encontrandoNumeroEmFibonacci(numero)
    print(30*"-*-*")
    faturamento(dadoJSON)
    print(30 * "-*-*")
    porcentagemFaturamento()
    print(30 * "-*-*")
    palavra = str(input("Digite o número que você deseja encontrar na Sequência de Fibonacci: "))
    reversible(palavra)


