#5) Escreva um programa que inverta os caracteres de um string. 

# IMPORTANTE: 
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 
# b) Evite usar funções prontas, como, por exemplo, reverse; 

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
