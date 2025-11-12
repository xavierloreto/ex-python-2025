cokeprice = 50
amount_due = price
accepted_coins = (25, 10, 5)

while amount_due > 0:
    # Solicita que o usuário insira uma moeda
    input_value = input("Insert coin: ")
    coin = int(input_value)

    # Verifica se a moeda inserida é válida
    if coin in accepted_coins:
        amount_due -= coin
    else:
        print("Invalid coin")

    # Se ainda houver valor a pagar, mostra quanto falta
    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

# Quando o valor devido for 0 ou menor, o programa termina
if amount_due <= 0:
    change = abs(amount_due)  # Calcula o troco
    print(f"Change Owed: {change}")


