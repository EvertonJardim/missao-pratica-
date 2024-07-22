entrada_idade = ''  # Inicializa a variável como string vazia

while str(entrada_idade) != '0':  # Verifica se a entrada é diferente de '0'
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')  # Pede entrada ao usuário
    
    if entrada_idade == '0':  # Verifica se o número digitado é 0
        print('Programa encerrado.')  # Imprime a mensagem de encerramento
        break  # Sai do loop
    
    print(f'Número digitado: {entrada_idade}')  # Imprime o número digitado