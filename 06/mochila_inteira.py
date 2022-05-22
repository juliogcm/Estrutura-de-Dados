# Implementação da Max Heap em Python.
import time

pi = []                                   # Lista de pesos.
vi = []                                   # Lista de valores.
itens_inclusos = []
n = 0                                     # Número total de elementos a serem considerados.
M = 0                                     # Capacidade da mochila.

def Convert_to_list(string):
    li = list(string.split(" "))
    return li

def Coleta_info(string):
    global pi, vi
    string = Convert_to_list(string)

    pi.append(int(string[0]))              # Adiciona pesos.
    vi.append(int(string[1]))              # Adiciona valores.

    return

def Coleta_dados(arquivo):
    global n, M

    header = Convert_to_list(arquivo[0])
    
    n = int(header[0])                     # Coleta dados do cabeçalho.
    M = int(header[1])
    
    for x in range(1, n+1):
        elemento = arquivo[x]          
        Coleta_info(elemento)
    return

def mochilaInteira(M, pi, vi, n):
    global itens_inclusos

    K = [[0 for w in range(M + 1)] for i in range(n + 1)]
             
    # Constrói tabela da mochila inteira.
    for i in range(n + 1):
        for w in range(M + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif pi[i - 1] <= w:
                K[i][w] = max(vi[i - 1]
                  + K[i - 1][w - pi[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    # Resultado final.
    res = K[n][M]
    print("\nValor final: ", res)
     
    w = M
    for i in range(n, 0, -1):
        if res <= 0:
            break
        
        # Se houve mudança do valor final da tabela em relação ao da mesma coluna na linha superior, então o item atual foi incluido na solução ótima.
        if res == K[i - 1][w]:
            continue
        else:
 
            # Esse item foi incluido.
            if type(i) == int:
                itens_inclusos.append(int(i))
             
            # Se o item está na solução, reduz o seu peso da capacidade máxima da sacola.
            res = res - vi[i - 1]
            w = w - pi[i - 1]
    print("\nItens inclusos: ", itens_inclusos)
    return

def main():       
    arq = input('\nDigite o nome do arquivo na pasta raiz com extensão (ex.: meuarq.txt): ')
    dados = tuple(open(arq, 'r'))
    Coleta_dados(dados) 

    inicio = time.time()
    mochilaInteira(M, pi, vi, n)
    fim = time.time()
    
    print(f"\nTempo de execução: {fim - inicio}ms\n")

if __name__=="__main__":
    main()