def calcular_desconto(preco: float, percentual_desconto: float) -> tuple[float, float]:
    """Calcula o valor do desconto e o preço final do veículo."""
    valor_desconto = preco * (percentual_desconto / 100)
    preco_final = preco - valor_desconto
    return valor_desconto, preco_final


def formatar_moeda(valor: float) -> str:
    """Formata um valor numérico para o padrão de moeda brasileiro (R$)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def obter_desconto_por_forma_pagamento(opcao: str) -> float:
    """Retorna a taxa de desconto com base na escolha de pagamento."""
    match opcao:
        case "1":
            return 12.0  # 12% à vista (PIX / Transferência)
        case "2":
            return 5.0   # 5% Financiamento
        case "3":
            return 3.0   # 3% Cartão de Crédito
        case _:
            return 0.0


def main():
    try:
        print("=== SISTEMA DE CONCESSIONÁRIA - CÁLCULO DE DESCONTOS ===")

        modelo = input("Modelo do carro: ").strip()

        while True:
            try:
                preco_original = float(input("Preço de tabela (R$): ").replace(",", "."))
                if preco_original <= 0:
                    print("O preço deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite apenas números.")

        print("\nOpções de Pagamento:")
        print("1. À vista (PIX / Transferência) - 12% de desconto")
        print("2. Financiamento com entrada     - 5% de desconto")
        print("3. Cartão de Crédito             - 3% de desconto")
        print("4. Cupom / Desconto manual")

        opcao = input("Selecione a forma de pagamento (1-4): ").strip()

        if opcao == "4":
            while True:
                try:
                    percentual = float(input("Digite a % de desconto desejada: ").replace(",", "."))
                    if 0 <= percentual <= 100:
                        break
                    print("O desconto deve estar entre 0% e 100%.")
                except ValueError:
                    print("Porcentagem inválida.")
        else:
            percentual = obter_desconto_por_forma_pagamento(opcao)

        valor_desconto, preco_final = calcular_desconto(preco_original, percentual)

        print("\n" + "=" * 45)
        print(f"RESUMO DA NEGOCIAÇÃO: {modelo.upper()}")
        print("=" * 45)
        print(f"Preço original:    {formatar_moeda(preco_original)}")
        print(f"Desconto ({percentual:.1f}%):  - {formatar_moeda(valor_desconto)}")
        print("-" * 45)
        print(f"Preço final:       {formatar_moeda(preco_final)}")
        print("=" * 45)

    except (KeyboardInterrupt, EOFError):
        print("\n\nExecução encerrada pelo usuário.")


if __name__ == "__main__":
    main()