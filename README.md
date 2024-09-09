## Conteúdo

1. [Soma de Números Inteiros](#soma-de-números-inteiros)
2. [Verificar Número na Sequência de Fibonacci](#verificar-número-na-sequência-de-fibonacci)
3. [Análise de Faturamento Diário](#análise-de-faturamento-diário)
4. [Percentual de Representação dos Estados](#percentual-de-representação-dos-estados)
5. [Inverter Caracteres de uma String](#inverter-caracteres-de-uma-string)

## 1. Soma de Números Inteiros

O seguinte código calcula a soma dos números inteiros de 1 até um valor definido:

```python
INDICE = 13
SOMA = 0
K = 0
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print(SOMA)
```

**Resultado:** O valor da variável `SOMA` será **91**.

## 2. Verificar Número na Sequência de Fibonacci

Este programa verifica se um número informado pertence à sequência de Fibonacci.

```python
def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Exemplo de uso
numero = int(input("Digite um número: "))
if is_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
```

## 3. Análise de Faturamento Diário

O programa a seguir analisa um vetor de faturamento diário e calcula o menor valor, o maior valor e o número de dias com faturamento acima da média.

```python
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


```

```json
{
    {
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	}
}

```

## 4. Percentual de Representação dos Estados

O programa calcula o percentual de representação de cada estado em relação ao faturamento total.

```python
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
```

## 5. Inverter Caracteres de uma String

Este código inverte os caracteres de uma string fornecida.

```python
def inverter_string(s):
    lista = list(s)
    esquerda = 0
    direita = len(lista) - 1
    while esquerda < direita:
        lista[esquerda], lista[direita] = lista[direita], lista[esquerda]
        esquerda += 1
        direita -= 1
    return ''.join(lista)

entrada = input("Digite uma string: ")
print(f"String invertida: {inverter_string(entrada)}")
```

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Copie o código desejado para um arquivo `.py`.
3. Execute o arquivo usando o comando `python nome_do_arquivo.py` no terminal ou prompt de comando.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

