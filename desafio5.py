def inverter_string(s):
    invertida = ""
    
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    
    return invertida

# Entrada de dados - pode ser definida diretamente ou informada pelo usuário
entrada = input("Digite a string que deseja inverter: ")

# Invertendo a string
resultado = inverter_string(entrada)

# Exibindo o resultado
print("String invertida:", resultado)
