# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem
#  que desejar, que calcule e retorne: 
# • O menor valor de faturamento ocorrido em um dia do mês; 
# • O maior valor de faturamento ocorrido em um dia do mês; 
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 

#IMPORTANTE: 
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; 


import json

def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def analisar_faturamento(dados):
    # Filtrar apenas os valores que são maiores que 0
    valores = [item["valor"] for item in dados if item["valor"] > 0]
    
    # Verificar se há valores para evitar divisão por zero
    if not valores:
        return None, None, None, 0
    
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    return menor_faturamento, maior_faturamento, media_mensal, dias_acima_media

caminho_arquivo = '03.json'

dados = carregar_dados(caminho_arquivo)
menor_faturamento, maior_faturamento, media_mensal, dias_acima_media = analisar_faturamento(dados)

print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Valor da Média Mensal: {media_mensal:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
