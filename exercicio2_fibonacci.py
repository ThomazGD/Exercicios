# Exercício 2

def pertence_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return num == 0 or b == num

def main():
    # Você pode trocar o valor de 'numero' para testar outros casos
    numero = 21
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()