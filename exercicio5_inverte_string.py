# Exercício 5

def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

def main():
    texto = "Exemplo de string!"
    print(f"Original: {texto}")
    print(f"Invertida: {inverter_string(texto)}")

if __name__ == "__main__":
    main()