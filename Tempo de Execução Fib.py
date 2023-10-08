from matplotlib import pyplot as plt
import time

## Fibonati looping

def fib(n):
    if n == 0:
        return 0
    res =  0
    temp = 1
    for _ in range(n):
        res += temp
        temp = res - temp
    return res

## Fibonati recursivo sem memorização

def fib2(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

## Fibonacci rescursivo com memorização

def fib3( n, dict = {}):

    if n == 0:
        return 0
    if n <= 2:
        return 1
    elif n in dict.keys():
        return dict[n]
    else:
        dict[n] = fib3(n-1) + fib3(n-2)
        return fib3(n)

tempos_de_resposta = []
numero_de_testes = int(input("Escolha o número de testes\n"))
escolha_de_funcoes = int(input("Você quer testar todas as funções de fibonnaci ou apenas as duas mais eficientes? [1/2]\n"))

if escolha_de_funcoes == 1:

    for i in range(numero_de_testes):
        tempo_funcoes =[]

        t1 = time.perf_counter()
        fib(i)
        t2 = time.perf_counter()
        tempo_funcoes.append((t2-t1)*1000)

        t1 = time.perf_counter()
        fib2(i)
        t2 = time.perf_counter()
        tempo_funcoes.append((t2-t1)*1000)

        t1 = time.perf_counter()
        fib3(i)
        t2 = time.perf_counter()
        tempo_funcoes.append((t2-t1)*1000)

        tempos_de_resposta.append(tempo_funcoes)

    n_testes = [i for i in range(numero_de_testes)]

    tempos_fib1 = [tempos_de_resposta[i][0] for i in range(numero_de_testes)]
    tempos_fib2 = [tempos_de_resposta[i][1] for i in range(numero_de_testes)]
    tempos_fib3 = [tempos_de_resposta[i][2] for i in range(numero_de_testes)]

    plt.plot(n_testes, tempos_fib3, color='blue', linestyle='dashed', marker = 'o', markersize=5, label = 'Recursividade com memorização')
    plt.plot(n_testes, tempos_fib2, color='red', linestyle='dashed', marker = 'o', markersize=5, label = 'Recursividade sem memorização')
    plt.plot(n_testes, tempos_fib1, color='green', linestyle='dashed', marker = 'o', markersize=5, label = 'Tabulação')

elif escolha_de_funcoes == 2:

    for i in range(numero_de_testes):
        tempo_funcoes =[]

        t1 = time.perf_counter()
        fib(i)
        t2 = time.perf_counter()
        tempo_funcoes.append((t2-t1)*1000)

        t1 = time.perf_counter()
        fib3(i)
        t2 = time.perf_counter()
        tempo_funcoes.append((t2-t1)*1000)

        tempos_de_resposta.append(tempo_funcoes)

    n_testes = [i for i in range(numero_de_testes)]

    tempos_fib1 = [tempos_de_resposta[i][0] for i in range(numero_de_testes)]
    tempos_fib3 = [tempos_de_resposta[i][1] for i in range(numero_de_testes)]

    plt.plot(n_testes, tempos_fib3, color='blue', linestyle='dashed', marker = 'o', markersize=5, label = 'Recursividade com memorização')
    plt.plot(n_testes, tempos_fib1, color='green', linestyle='dashed', marker = 'o', markersize=5, label = 'Tabulação')

    
else:
    print("Você não escolheu uma função válida")

plt.title("Tempos de resposta de diferentes funções fibonacci")

plt.legend(loc=9)
plt.xlabel("Nº fibonacci")
plt.ylabel("Tempo de resposta (ms)")
plt.show()

# input("Type something to quit")