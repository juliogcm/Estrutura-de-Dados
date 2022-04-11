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

def countingSort(lista):
    k = max(lista)+1

    tam = len(lista)
    saida = [0] * tam

    # Inicializando lista de contagem
    aux = [0]*(k+1)

    # Armazena a contagem de cada elemento na lista
    for i in range(0, tam):
        aux[lista[i]] += 1

    # Armazena a contagem total
    for i in range(1, (k+1)):
        aux[i] += aux[i - 1]

    # Encontra o índice de cada elemento da lista original na lista auxiliar de contagem e armazena na lista de saída
    i = tam - 1
    while i >= 0:
        saida[aux[lista[i]] - 1] = lista[i]
        aux[lista[i]] -= 1
        i -= 1

    # Copia os elementos ordenados de volta para lista original
    for i in range(0, tam):
        lista[i] = saida[i]
    
    return

# Counting Sort é utilizado como auxiliar por se tratar apenas de uma ordenação de dígitos.

def countingSortRadix(lista, importancia):

    tam = len(lista)
    saida = [0]*tam
    
    # Como se tratando apenas de dígitos, já defino a lista auxiliar como tamanho 10.
    aux = [0] * 10
 
    for i in range(0, tam):
        index = lista[i] // importancia
        aux[index % 10] += 1
 
    for i in range(1, 10):
        aux[i] += aux[i - 1]
 
    i = tam - 1
    while i >= 0:
        index = lista[i] // importancia
        saida[aux[index % 10] - 1] = lista[i]
        aux[index % 10] -= 1
        i -= 1
 
    i = 0
    for i in range(0, len(lista)):
        lista[i] = saida[i]
    return
 
def radixSort(lista):
 
    # Encontra maior número
    maior = max(lista)
 
    # Chama o counting para os dígitos começando do menos importante até o mais importante.
    importancia = 1
    while maior / importancia > 1:
        countingSortRadix(lista, importancia)
        importancia *= 10
    return

def print_menu():
    print('\n---------- MENU ------------')
    print ('1 -- Counting Sort' )
    print ('2 -- Radix Sort' )
    print ('3 -- Sair' )

def main():
    arq = input('\nDigite o nome do arquivo na pasta raiz com extensão (ex.: meuarq.txt): ')
    dados = tuple(open(arq, 'r'))  #Abre o arquivo com cada linha sfimo um elemento.
    Coleta_dados(dados)                      #Coleta dados necessários e cria lista de elementos.

    #print(f"Número de elementos: {N}\n|Lista de elementos original: {lista}")

    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Escolha um item do MENU: '))
        except:
            print('Entrada inválida. Por favor, escolha um número ...')

        if option == 1:
            lista = mlista       #Reseta os elementos
            inicio = time.time()
            countingSort(lista)
            fim = time.time()
            print('Opção escolhida \'Counting Sort\'')
            print(f"\nLista ordenada: {lista}\n\nTempo de execução: {fim - inicio}ms\n")

        elif option == 2:
            lista = mlista       #Reseta os elementos
            inicio = time.time()
            radixSort(lista)
            fim = time.time()
            print('Opção escolhida \'Radix Sort\'')
            print(f"\nLista ordenada: {lista}\n\nTempo de execução: {fim - inicio}ms\n")

        elif option == 3:
            print('\nFim do algoritmo\n')
            exit()
        else:
            print('Opção inválida. Por favor insira um número entre 1 e 3.')

if __name__=="__main__":
    main()
