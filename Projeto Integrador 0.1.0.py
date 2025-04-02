def cadastro_data():
    while True:
        try:
            data = input("Digite a data de hoje (DD/MM/YYYY): ")

            data = data.replace("/", "")

            if not data.isdigit():
                print("A data deve conter somente números. Tente novamente.")
                continue

            if data > 8 or data < 8 :
                print("A data deve ter somente 8 dígitos numéricos, tente novamente.")
                continue

            dia, mes, ano = int(data[:2]), int(data[2:4]), int(data[4:])

            if dia < 1 or dia > 31:
                print("Digite um dia válido, entre 01 e 31.")
                continue

            if mes < 1 or mes > 12:
                print("Digite um mês válido, o mês deve estar entre 01 e 12.")
                continue

            if mes == 2 and dia > 28:
                print("O mês de fevereiro tem somente até o dia 28.")
                print("Digite outro dia, entre 01 e 28.")
                continue

            break

        except ValueError:
            print("Ocorreu um erro inesperado. Tente novamente.")  

    return f"{dia:02d}/{mes:02d}/{ano}"

data = cadastro_data()
print(f"Data cadastrada: {data}")


while True:
    try:
        consumo_agua = float(input("Digite quanto você consumiu de água hoje (em litros): "))
        if consumo_agua < 0:
            print("O consumo de água não pode ser negativo. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

print(f"Consumo de água registrado: {consumo_agua} litros")

while True:
    try:
        consumo_kWh = float(input("Quantos kWh você consumiu de energia elétrica hoje: "))
        if consumo_kWh < 0:
            print("O consumo de energia não pode ser negativo. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

print(f"Consumo de energia elétrica registrado: {consumo_kWh} kWh")

while True:
    try:
        consumo_residuos = float(input("Quantos kg de resíduos não recicláveis você gerou hoje: "))
        if consumo_residuos < 0:
            print("A quantidade de resíduos não pode ser negativa. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

print(f"Consumo de resíduos não recicláveis registrado: {consumo_residuos} kg")

while True:
    try:
        consumo_reciclado = float(input("Qual a porcentagem de resíduos reciclados no total (em %): "))
        if not 0 <= consumo_reciclado <= 100:
            print("A porcentagem deve estar entre 0 e 100. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

print(f"Consumo de resíduos reciclados registrado: {consumo_reciclado}%")

