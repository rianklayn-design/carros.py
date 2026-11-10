# 1. Lista com marcas, modelos e preços dos carros
lista_carros = [
    {"marca": "Toyota", "modelo": "Corolla", "preco": 148000.00},
    {"marca": "Chevrolet", "modelo": "Onix", "preco": 89000.00},
    {"marca": "Volkswagen", "modelo": "Polo", "preco": 95000.00},
    {"marca": "Fiat", "modelo": "Pulse", "preco": 102000.00},
    {"marca": "Ford", "modelo": "Ranger", "preco": 239000.00},
    {"marca": "Honda", "modelo": "Civic", "preco": 265000.00}
]

# 2. Criar e escrever os dados no arquivo 'carros.txt'
with open("carros.txt", "w", encoding="utf-8") as arquivo:
    # Escreve o cabeçalho separado por ponto e vírgula
    arquivo.write("Marca;Modelo;Preço\n")
    
    # Escreve os dados de cada carro
    for carro in lista_carros:
        arquivo.write(f"{carro['marca']};{carro['modelo']};{carro['preco']:.2f}\n")

print("Arquivo 'carros.txt' gerado com sucesso!\n")

# 3. Ler e exibir os dados salvos no arquivo
print("=== DADOS LIDOS DO ARQUIVO CARROS.TXT ===")

with open("carros.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    
    # Pega o cabeçalho
    cabecalho = linhas[0].strip().split(";")
    print(f"{cabecalho[0]:<15} | {cabecalho[1]:<15} | {cabecalho[2]}")
    print("-" * 50)
    
    # Processa e exibe cada carro registrado
    soma_precos = 0
    total_carros = 0
    
    for linha in linhas[1:]:
        marca, modelo, preco_str = linha.strip().split(";")
        preco = float(preco_str)
        soma_precos += preco
        total_carros += 1
        
        # Formatação do preço em moeda brasileira (R$)
        preco_formatado = f"R$ {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print(f"{marca:<15} | {modelo:<15} | {preco_formatado}")

    # Cálculo da média dos preços
    if total_carros > 0:
        media = soma_precos / total_carros
        media_fmt = f"R$ {media:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        print("-" * 50)
        print(f"Média de preço dos carros: {media_fmt}")
