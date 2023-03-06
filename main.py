def encontrandoNumeroEmFibonacci(x):
    fibonacci = 0
    cont = 0
    seqFibonacci = [0, 1]
    while fibonacci < x:
        fibonacci = seqFibonacci[cont] + seqFibonacci[cont+1]
        seqFibonacci.append(fibonacci)
        cont+=1
    if x in seqFibonacci:
        print(f"O número {x} está na Sequência de Fibonacci! Ele é o {seqFibonacci.index(x) + 1}º número da sequência.")
    else:
        print(f"O número {x} não está na Sequência de Fibonacci!")


if __name__ == '__main__':
    numero = int(input("Digite o número que você deseja encontrar na Sequência de Fibonacci: "))
    encontrandoNumeroEmFibonacci(numero)

