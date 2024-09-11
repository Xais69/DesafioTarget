import json

def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        dados = json.load(f)
    return dados

def calcular_faturamento(faturamento):
    faturamento_filtrado = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    
    if not faturamento_filtrado:
        print("Não há dados de faturamento válido.")
        return
    
    menor_valor = min(faturamento_filtrado)
    maior_valor = max(faturamento_filtrado)
    
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
    
    dias_acima_da_media = sum(1 for dia in faturamento_filtrado if dia > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_da_media

caminho_arquivo = 'dados.json'

faturamento = carregar_dados_json(caminho_arquivo)
menor, maior, dias_acima_media = calcular_faturamento(faturamento)

print(f"Menor valor de faturamento: {menor:.2f}")
print(f"Maior valor de faturamento: {maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
