import time
import unit_prim as prim
import unit_kruskal as kruskral
import unit_dijikstra as dj


mlista = []                               #Lista de elementos a ser ordenada.
N = 0                                    # Tamanho da matriz.

def Remove_endline(string):
    aux = string.replace("\n","")
    return aux

def Convert_to_list(string):
    li = list(string.split(" "))
    return li

def Coleta_info(string,i):
    global mlista
    string = Remove_endline(string)
    string = Convert_to_list(string)
    
    #Remove último elemento que é um caractere não utilizado.
    for x in range(0, len(string)):
        if string[x] == '':
            del(string[x])

    string = [int(x) for x in string]
    for x in range(i):
        string.insert(0,0)
    mlista.append(string)

    return

def Coleta_dados(text):
    global N, mlista
    N = int(text[0])                     #Identifica o número total de elementos (cabeçalho).
    for x in range(1, N):
        elemento = text[x]          
        Coleta_info(elemento,x)           #Adiciona elementos à lista.
    mlista.append([0]*N)
    return

def Constroi_matriz(matriz):
    global N
    for x in range(0,N-1):
        for y in range(x+1,len(matriz[x])):
            matriz[y][x] = matriz[x][y]
    return

def print_menu():
    print('\n---------- MENU ------------')
    print ('1 -- Dijkstra' )
    print ('2 -- Prim' )
    print ('3 -- Kruskal' )
    print ('4 -- Sair' )

def main():
    arq = input('\nDigite o nome do arquivo na pasta raiz com extensão (ex.: meuarq.txt): ')
    dados = tuple(open(arq, 'r'))           #Abre o arquivo com cada linha sfimo um elemento.
    Coleta_dados(dados)                      #Coleta dados necessários e cria lista de elementos.
    Constroi_matriz(mlista)
    print("As instâncias têm diferenças em relação à utilização de '/t' e '/n' nos txt.\nO modelo revisado foi o da instância dij10.txt")

    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Escolha um item do MENU: '))
        except:
            print('Entrada inválida. Por favor, escolha um número ...')

        if option == 1:
            o = dj.Graph(N)
            o.graph = mlista
            print('Opção escolhida \'Dijkstra\'')

            inicio = time.time()
            o.dijkstra(0)
            fim = time.time()

            print(f"\nTempo de execução: {fim - inicio}ms\n")

        elif option == 2:
            g = prim.Graph(N)
            g.graph = mlista
            print('Opção escolhida \'Prim\'')

            inicio = time.time()
            g.primMST()
            fim = time.time()

            print(f"\nTempo de execução: {fim - inicio}ms\n")
        
        elif option == 3:
            h = kruskral.Graph(N)
            for x in range(0, N):
                for y in range(0,N):
                    dist = mlista[x][y]
                    h.addEdge(x, y, dist)
            print('Opção escolhida \'Kruskal\'')

            inicio = time.time()
            h.KruskalMST()
            fim = time.time()
            
            print(f"\nTempo de execução: {fim - inicio}ms\n")

        elif option == 4:
            print('\nFim do algoritmo\n')
            exit()
        else:
            print('Opção inválida. Por favor insira um número entre 1 e 3.')

if __name__=="__main__":
    main()
