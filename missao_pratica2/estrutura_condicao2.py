# Criação da variável tempoExperiencia e atribuição do valor 5
tempoExperiencia = 3

# Verificação da condição se o tempo de experiência é menor que 2
if tempoExperiencia < 2:
    # Caso a condição seja verdadeira, imprime a mensagem
    print('Nível de conhecimento júnior.')
# Verificação da condição se o tempo de experiência é maior que 2 e menor que 5
elif 2 < tempoExperiencia < 5:
    # Caso a condição seja verdadeira, imprime a mensagem
    print('Nível de conhecimento pleno.')
# Caso nenhuma das condições anteriores seja verdadeira, imprime a mensagem
else:
    print('Nível de conhecimento sênior.')
