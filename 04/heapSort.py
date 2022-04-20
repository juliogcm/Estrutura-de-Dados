# Implementação da Max Heap em Python.
import time
mlista = []                               # Lista de elementos a ser ordenada.
N = 0                                     # Número de elementoos na lista.

def Coleta_dados(text):
    global N
    N = int(text[0])                     #Identifica o número total de elementoos (cabeçalho).
    for x in range(1, N+1):
        elementoo = int(text[x])          
        mlista.append(elementoo)           #AdicionaElemento elementoos à lista.
    return

def printHeap(mheap):
    n = (len(mheap))
    print(f'Heap Máxima Inicial:\n')
    for i in range(0, (n // 2 -1)):
        print(" PAI : " + str(mheap[i]) + 
            " ESQUERDO : " + str(mheap[2*i + 1]) +
            " DIREITO : " + str(mheap[2*i + 2]))
    return

def heapMaximo(mheap, n, i):
    maior = i       # Inicializa a raiz de maior valor
    esq = 2 * i + 1     
    dir = 2 * i + 2     
  
    # Verifica se filho ESQUERDO existe e é maior que RAIZ
    if esq < n and mheap[i] < mheap[esq]:
        maior = esq
  
    # Verifica se filho DIREITO existe e é maior que RAIZ
    if dir < n and mheap[maior] < mheap[dir]:
        maior = dir
  
    # Troca a RAIZ se necessário
    if maior != i:
        mheap[i],mheap[maior] = mheap[maior],mheap[i]
        heapMaximo(mheap, n, maior)                     #Reaplica o heapMaximo para reorganizar

def constroiHeapMaxima(mheap):
    global N

    # Constrói a Heap Máxima.
    # O último elemento pai vai estar em ((n//2)-1), começamos por essa posição então.
    for i in range(N // 2 - 1, -1, -1):
        heapMaximo(mheap, N, i)
    
    printHeap(mheap)
    return

def heapSort(mheap):
    global N
  
    # Vai extraindo os elementos um por um para a lista ordenada final
    # Retira o elemento RAIZ, por ser sempre o maior na Heap Máxima, e o coloca no fim da lista ordenada final.  
    # O elemento RAIZ é substituido pelo último elemento da heap e ela tem seu tamanho diminuido. 
    # A função heapMaximo é aplicada novamente para que o maior elemento esteja na RAIZ e o processo se repita até 
    # o número de elementos ter acabado.
    for i in range(N-1, 0, -1):
        mheap[i], mheap[0] = mheap[0], mheap[i]   # Troca os elementos
        heapMaximo(mheap, i, 0)

def main():       
    arq = input('\nDigite o nome do arquivo na pasta raiz com extensão (ex.: meuarq.txt): ')
    dados = tuple(open(arq, 'r'))
    Coleta_dados(dados) 
    print(f'\nLista inicialmente desordenada:\n{mlista}\n')                   
    
    constroiHeapMaxima(mlista)

    inicio = time.time()
    heapSort(mlista)
    fim = time.time()
    
    print(f"\nLista ordenada: {mlista}\n\nTempo de execução: {fim - inicio}ms\n")

if __name__=="__main__":
    main()
