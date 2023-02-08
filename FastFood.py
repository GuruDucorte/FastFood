print('1- Hambúrguer - R$10,00')
print('2- Batata Frita - R$5,00')
print('3- Refrigerante - R$4,00')
print('4- Sorvete - R$2,00')

opcao = int(input('Digite o nº da opção desejadas: '))
quantidade = int(input('Digite a quantidade desejada: '))
nome = str(input('Digite o nome do cliente: '))

if opcao == 1:
    print('Hambúguer sendo preparado para ', nome)
    print('Tempo de espera de 15 minutos')
    total = quantidade * 10
    print('Total: R$', total)