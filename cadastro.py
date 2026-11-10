import json

ARQUIVO_DADOS = "carros_cadastrados.json"


def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salvar_dados(carros):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(carros, arquivo, ensure_ascii=False, indent=4)


def cadastrar_carro(carros):
    print("\n--- NOVO CADASTRO ---")
    marca = input("Marca do carro (ex: Toyota): ").strip()
    modelo = input("Modelo do carro (ex: Corolla): ").strip()

    while True:
        try:
            preco_input = input("Preço do carro (R$): ").replace(",", ".")
            preco = float(preco_input)
            if preco < 0:
                print("O preço não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um valor numérico.")

    carro = {"marca": marca, "modelo": modelo, "preco": preco}
    carros.append(carro)
    salvar_dados(carros)
    print(f"\n✓ Carro '{marca} {modelo}' cadastrado e salvo com sucesso!\n")


def listar_carros(carros):
    if not carros:
        print("\nNenhum carro cadastrado no momento.\n")
        return

    print("\n" + "=" * 50)
    print(f"{'MARCA':<15} | {'MODELO':<15} | {'PREÇO'}")
    print("=" * 50)

    for carro in carros:
        preco_fmt = f"R$ {carro['preco']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"{carro['marca']:<15} | {carro['modelo']:<15} | {preco_fmt}")

    print("=" * 50 + "\n")


def main():
    carros = carregar_dados()

    while True:
        print("=== CADASTRO DE MARCAS E CARROS ===")
        print("1. Cadastrar novo carro")
        print("2. Listar todos os carros")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_carro(carros)
        elif opcao == "2":
            listar_carros(carros)
        elif opcao == "0":
            print("\nSaindo do sistema... Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()