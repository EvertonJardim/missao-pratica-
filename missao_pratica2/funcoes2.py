# Definindo a função loginUsuario que recebe um parâmetro perfil
def loginUsuario(perfil):
    # Verificando se o valor do parâmetro perfil é igual a 'admin', ignorando maiúsculas e minúsculas
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamando a função loginUsuario com diferentes valores de parâmetro
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('ADMIN')
loginUsuario('AdMiN')

