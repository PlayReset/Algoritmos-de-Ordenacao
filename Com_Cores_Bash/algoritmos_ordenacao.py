import time
import shutil


# Execução e calculo de tempo dos algoritmos de ordenação
def ordenar_bubble(lista_bubble, imprimir):
    lista_desordenada = lista_bubble.copy()
    # Bubble Sort
    abertura_bubble = time.time()
    bubble_sort(lista_desordenada, imprimir)
    termino_bubble = time.time()
    total_blubble = (termino_bubble - abertura_bubble)
    print(f'Tempo \033[1;32mBubble Sort\033[0;0m:    \033[31m{total_blubble}\033[0;0m segundos.')
    separador()


def ordenar_insertion(lista_insertion, imprimir):
    lista_desordenada = lista_insertion.copy()
    # Insertion Sort
    abertura_insertion = time.time()
    insertion_sort(lista_desordenada, imprimir)
    termino_insertion = time.time()
    total_insert = (termino_insertion - abertura_insertion)
    print(f'Tempo \033[1;33mInsertion Sort\033[0;0m: \033[31m{total_insert}\033[0;0m segundos.')
    separador()


def ordenar_shell(lista_shell, imprimir):
    lista_desordenada = lista_shell.copy()
    # Shell Sort
    abertura_shell = time.time()
    shell_sort(lista_desordenada, imprimir)
    termino_shell = time.time()
    total_shell = (termino_shell - abertura_shell)
    print(f'Tempo \033[1;36mShell Sort\033[0;0m:     \033[31m{total_shell}\033[0;0m segundos.')
    separador()


def ordenar_merge(lista_merge, imprimir):
    lista_desordenada = lista_merge.copy()
    # Merge Sort
    abertura_merge = time.time()
    merge_sort(lista_desordenada, imprimir)
    termino_merge = time.time()
    total_merge = (termino_merge - abertura_merge)
    print(f'Tempo \033[1;35mMerge Sort\033[0;0m:     \033[31m{total_merge}\033[0;0m segundos.')
    separador()


def ordenar_quick(lista_quick, imprimir):
    lista_desordenada = lista_quick.copy()
    # Quick Sort
    abertura_quick = time.time()
    quick_sort(lista_desordenada, imprimir)
    termino_quick = time.time()
    total_quick = (termino_quick - abertura_quick)
    print(f'Tempo \033[1;34mQuick Sort\033[0;0m:     \033[31m{total_quick}\033[0;0m segundos.')
    separador()


# Algoritmos

# Bubble Sort
def bubble_sort(lista, imprimir):
    elementos = len(lista) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = False
    separador()
    print('\033[1;32mBubble Sort\033[0;0m - lista ordenada:\n')
    if imprimir == 0:
        print(lista)


# Insertion Sort
def insertion_sort(lista, imprimir):
    for i in range(1, len(lista)):
        valor_atual = lista[i]
        posicao_atual = i
        while posicao_atual > 0 and lista[posicao_atual - 1] > valor_atual:
            lista[posicao_atual] = lista[posicao_atual - 1]
            posicao_atual = posicao_atual - 1

        lista[posicao_atual] = valor_atual
    separador()
    print(f'\033[1;33mInsertion Sort\033[0;0m - lista ordenada:\n')
    if imprimir == 0:
        print(lista)


# Shell Sort
def shell_sort(lista, imprimir):
    tamanho = len(lista)
    intervalo = tamanho // 2
    while intervalo > 0:
        for i in range(intervalo, tamanho):
            valor_atual = lista[i]
            posicao_atual = i
            while posicao_atual >= intervalo and lista[posicao_atual - intervalo] > valor_atual:
                lista[posicao_atual] = lista[posicao_atual - intervalo]
                posicao_atual -= intervalo

            lista[posicao_atual] = valor_atual
        intervalo //= 2
    separador()
    print(f'\033[1;36mShell Sort\033[0;0m - lista ordenada:\n')
    if imprimir == 0:
        print(lista)


# Merge Sort
def merge_sort(lista, imprimir):

    def merge(lista_sort):
        if len(lista_sort) > 1:
            metade = len(lista_sort) // 2
            esquerda = lista_sort[:metade]
            direita = lista_sort[metade:]
            merge(esquerda)
            merge(direita)
            i = j = k = 0
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    lista_sort[k] = esquerda[i]
                    i += 1
                else:
                    lista_sort[k] = direita[j]
                    j += 1
                k += 1
            while i < len(esquerda):
                lista_sort[k] = esquerda[i]
                i += 1
                k += 1
            while j < len(direita):
                lista_sort[k] = direita[j]
                j += 1
                k += 1

    merge(lista)
    separador()
    print(f'\033[1;35mMerge Sort\033[0;0m - lista ordenada:\n')
    if imprimir == 0:
        print(lista)


# Quick Sort
def quick_sort(lista, imprimir):

    def partition(lista_sort, menor, maior):
        i = (menor - 1)
        pivot = lista_sort[maior]  # pivô
        for j in range(menor, maior):
            if lista_sort[j] <= pivot:
                i = i + 1
                lista_sort[i], lista_sort[j] = lista_sort[j], lista_sort[i]
        lista_sort[i + 1], lista_sort[maior] = lista_sort[maior], lista_sort[i + 1]
        return i + 1

    def quick(lista_sort, menor, maior):
        if len(lista_sort) == 1:
            return lista_sort
        if menor < maior:
            pi = partition(lista_sort, menor, maior)
            quick(lista_sort, menor, pi - 1)
            quick(lista_sort, pi + 1, maior)

    quick(lista, 0, len(lista) - 1)
    separador()
    print(f'\033[1;34mQuick Sort\033[0;0m: - lista ordenada:\n')
    if imprimir == 0:
        print(lista)


# Função separadora baseada nas colunas do terminal de execução
def separador():
    tamanho_terminal = shutil.get_terminal_size((180, 20))
    colunas = tamanho_terminal.columns
    # quant_pycharm = 180
    print('-' * colunas)
