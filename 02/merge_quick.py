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

def mergeSort(lista):
    if len(lista) > 1:
        i = j = k = 0                  
  
        mid = len(lista)//2             #Divide na metade para obter o elemento central.
        
        esq = lista[:mid]               #Separa a lista de acordo.
        dir = lista[mid:]
  
        mergeSort(esq)                  #Ordena cada metade.
        mergeSort(dir)
        
        #Armazena o que foi ordenado em listas temporárias.
        while i < len(esq) and j < len(dir):    
            if esq[i] < dir[j]:
                lista[k] = esq[i]
                i += 1
            else:
                lista[k] = dir[j]
                j += 1
            k += 1
  
        #Verificação
        while i < len(esq):
            lista[k] = esq[i]
            i += 1
            k += 1
  
        while j < len(dir):
            lista[k] = dir[j]
            j += 1
            k += 1
    return

def part(inicio, fim, lista):
     
    pivot_index = inicio                   # Define o inicio como pivô
    pivot = lista[pivot_index]
    
    # Continua até que o inicio cruze com fim para trocar o pivô com o elemento em fim.
    while inicio < fim:
         
        # Incrementa o inicio até achar um elemento maior que o pivô.
        while inicio < len(lista) and lista[inicio] <= pivot:
            inicio += 1
             
        # Decrementa fim até achar elemento menor que o pivô.
        while lista[fim] > pivot:
            fim -= 1

        # Troca os números de inicio e fim se ainda não tiverem passado direto pelo outro.  
        if(inicio < fim):
            lista[inicio], lista[fim] = lista[fim], lista[inicio]
     
    # Ajusta o pivô trocando o elementos com o que está em fim.
    lista[fim], lista[pivot_index] = lista[pivot_index], lista[fim]
    
    # Retorna fim
    return fim

def quickSort(inicio, fim, lista):
    if (inicio < fim):
         
        # p recebe o indíce para dividir a lista.
        p = part(inicio, fim, lista)
         
        # Ordena elementos antes e depois de part.
        quickSort(inicio, p - 1, lista)
        quickSort(p + 1, fim, lista)
    return



def print_menu():
    print('\n---------- MENU ------------')
    print ('1 -- Merge Sort' )
    print ('2 -- Quick Sort' )
    print ('3 -- Sair' )

def main():
    arq = input('\nDigite o nome do arquivo na pasta raiz com extensão (ex.: meuarq.txt): ')
    dados = tuple(open(arq, 'r'))  #Abre o arquivo com cada linha sfimo um elemento.
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
            mergeSort(lista)
            fim = time.time()
            print('Opção escolhida \'Merge Sort\'')
            print(f"\nLista ordenada: {lista}\n\nTempo de execução: {fim - inicio}ms\n")

        elif option == 2:
            inicio = time.time()
            quickSort(0, len(lista)-1, lista)
            fim = time.time()
            print('Opção escolhida \'Quick Sort\'')
            print(f"\nLista ordenada: {lista}\n\nTempo de execução: {fim - inicio}ms\n")

        elif option == 3:
            print('\nFim do algoritmo\n')
            exit()
        else:
            print('Opção inválida. Por favor insira um número entre 1 e 3.')

if __name__=="__main__":
    main()
