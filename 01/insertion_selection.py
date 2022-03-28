import time

mlista = []                               #Lista de elementos a ser ordenada.
N = 0                                    #Número total de elementos da lista.

def Coleta_dados(text):
    global N
    N = int(text[0])                     #Identifica o número total de elementos (cabeçalho).
    for x in range(1, N+1):
        elemento = int(text[x])          
        mlista.append(elemento)           #Adiciona elementos à lista.
    return

def insertionSort(lista):

    for i in range(1, len(lista)):
        key = lista[i]

        # Troca de lugar os elementos da lista que são maiores que a chave para uma posição a frente de sua posição atual.
        j = i-1                             
        while j >= 0 and key < lista[j] :
                lista[j + 1] = lista[j]
                j -= 1
        lista[j + 1] = key

def selectionSort(lista):
    for i in range(len(lista)):
        #Encontra o menor elemento que sobrar na lista desordenada.
        menor = i
        for j in range(i+1, len(lista)):
            if lista[menor] > lista[j]:
                menor = j
                
        #Troca o menor elemento que foi encontrado pelo primeiro elemento da lista.  
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux
    return

def print_menu():
    print('\n---------- MENU ------------')
    print ('1 -- Insertion Sort' )
    print ('2 -- Selection Sort' )
    print ('3 -- Sair' )

def main():
    arq = input('\nDigite o nome do arquivo na pasta raiz com extensão (ex.: meuarq.txt): ')
    dados = tuple(open(arq, 'r'))  #Abre o arquivo com cada linha sendo um elemento.
    Coleta_dados(dados)                      #Coleta dados necessários e cria lista de elementos.

    #print(f"Número de elementos: {N}\n|Lista de elementos original: {lista}")

    while(True):
        lista = mlista       #Reseta os elementos
        print_menu()
        option = ''
        try:
            option = int(input('Escolha um item do MENU: '))
        except:
            print('Entrada inválida. Por favor, escolha um número ...')

        if option == 1:
            inicio = time.time()
            insertionSort(lista)
            fim = time.time()
            print('Opção escolhida \'Insertion Sort\'')
            print(f"\nLista ordenada: {lista}\n\nTempo de execução: {fim - inicio}ms\n")

        elif option == 2:
            inicio = time.time()
            insertionSort(lista)
            fim = time.time()
            print('Opção escolhida \'Selection Sort\'')
            print(f"\nLista ordenada: {lista}\n\nTempo de execução: {fim - inicio}ms\n")

        elif option == 3:
            print('\nFim do algoritmo\n')
            exit()
        else:
            print('Opção inválida. Por favor insira um número entre 1 e 3.')

if __name__=="__main__":
    main()
