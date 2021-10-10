# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

# Armazena as funções da calculadora
# Evita ifs
operacoes = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y
}

# Executa até o usuário escolher um operador que não existe
while True
    op = input(f'Escolha uma das operações a seguir {list(operacoes.keys())}: ')
    # Se há a operação na calculadora, pergunte os numeros e faça a operação
    if op in operacoes:
        operando_esq = float(input('Primeiro numero: '))
        operando_dir = float(input('Segundo numero: '))
        print("**********RESULTADO**********")
        print(operacoes.get(op)(operando_esq, operando_dir))
    # Ou finalize o programa
    else:
        break