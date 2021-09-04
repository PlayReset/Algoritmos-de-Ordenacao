import random
from algoritmos_ordenacao import *

# Controladores para criação da lista
lista = []
quantidade_de_chaves = 20000
limite_max_algarismo = 5000


def criar_lista(imprimir):
    if not lista:
        # Criando da Lista
        for i in range(quantidade_de_chaves):
            lista.append(random.randint(1, limite_max_algarismo))
        separador()
        print(f'\033[30;1;47mLista Criada\033[0;0m:\n')
        if imprimir == 0:
            print(lista)
        separador()
    else:
        print('A lista já foi criada, caso queira altera-la delete a lista primeiro.')


def deletar_lista():
    if not lista:
        print(f'A lista já está vazia')
    else:
        # Apagando a Lista
        lista.clear()
    separador()
    print(f'\033[30;1;47mLista Deletada\033[0;0m:\n', lista)
    separador()


while True:
    print(f'''
╔══════════════════════════╗
║           \033[1mMENU\033[0;0m           ║
║  (0) « \033[1mImprimir Lista\033[0;0m »  ║
║  (1) « \033[30;1;47mCriar Lista\033[0;0m »     ║
║  (2) « \033[30;1;41mDeletar Lista\033[0;0m »   ║
║  (3) « \033[1;32mBubble Sort\033[0;0m »     ║  
║  (4) « \033[1;33mInsertion Sort\033[0;0m »  ║      
║  (5) « \033[1;36mShell Sort\033[0;0m »      ║ 
║  (6) « \033[1;35mMerge Sort\033[0;0m »      ║ 
║  (7) « \033[1;34mQuick Sort\033[0;0m »      ║
║  (8)  « \033[30;1;46mComparar\033[0;0m »       ║
║  (9)   « Config »        ║
║  (X)    « \033[1;31mSair\033[0;0m »         ║
╚══════════════════════════╝\n''')

    escolha = (input('Digita a opção escolhida: ').upper())
    if escolha == '0':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print(lista)
        continue

    elif escolha == '1':
        print('Criando uma lista...')
        press = str(input('Deseja imprimir a lista?[S/N]: ')).upper()
        if press == 'S':
            criar_lista(0)
        else:
            criar_lista(1)
        continue

    elif escolha == '2':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Deletando a lista...')
            deletar_lista()
        continue

    elif escolha == '3':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Bubble Sort...')
            press = str(input('Deseja imprimir a lista?[S/N]: ')).upper()
            if press == 'S':
                ordenar_bubble(lista, 0)
            else:
                ordenar_bubble(lista, 1)
        continue

    elif escolha == '4':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Insertion Sort...')
            press = str(input('Deseja imprimir a lista?[S/N]: ')).upper()
            if press == 'S':
                ordenar_insertion(lista, 0)
            else:
                ordenar_insertion(lista, 1)
        continue

    elif escolha == '5':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Shell Sort...')
            press = str(input('Deseja imprimir a lista?[S/N]: ')).upper()
            if press == 'S':
                ordenar_shell(lista, 0)
            else:
                ordenar_shell(lista, 1)
        continue

    elif escolha == '6':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Merge Sort...')
            press = str(input('Deseja imprimir a lista?[S/N]: ')).upper()
            if press == 'S':
                ordenar_merge(lista, 0)
            else:
                ordenar_merge(lista, 1)
        continue

    elif escolha == '7':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Ordenando com Quick Sort...')
            press = str(input('Deseja imprimir a lista?[S/N]: ')).upper()
            if press == 'S':
                ordenar_quick(lista, 0)
            else:
                ordenar_quick(lista, 1)
        continue

    elif escolha == '8':
        if not lista:
            print('A lista está vazia, crie uma primeiro...')
        else:
            print('Comparando Algoritmos...')
            press = str(input('Deseja imprimir a lista?[S/N]: ')).upper()
            if press == 'S':
                ordenar_bubble(lista, 0)
                ordenar_insertion(lista, 0)
                ordenar_shell(lista, 0)
                ordenar_merge(lista, 0)
                ordenar_quick(lista, 0)
            else:
                ordenar_bubble(lista, 1)
                ordenar_insertion(lista, 1)
                ordenar_shell(lista, 1)
                ordenar_merge(lista, 1)
                ordenar_quick(lista, 1)
        continue

    elif escolha == '9':
        quantidade_de_chaves = int(input('Quantidade de Chaves da Lista\n (Padrão: 20000): '))
        limite_max_algarismo = int(input('Limite Máximo de Algarismo\n (Padrão: 5000): '))
        print('Configurações Salvas...')
        continue

    elif escolha == 'X':
        print('Finalizando o programa...')
        break

    else:
        print('Somente comandos disposto no MENU funcionam, boa tentativa meu chapa...')
