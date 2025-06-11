# Exercício 3
import json

def main():
    with open('faturamento.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
    valores = [dia['valor'] for dia in dados if dia['valor'] > 0]
    if not valores:
        print("Não há dias com faturamento para análise.")
        return
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_media = sum(1 for v in valores if v > media)
    print(f"Menor faturamento: R${menor:.2f}")
    print(f"Maior faturamento: R${maior:.2f}")
    print(f"Dias acima da média: {dias_acima_media}")

if __name__ == "__main__":
    main()