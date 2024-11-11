import time
import random


solucao = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

def gerar_tabuleiro_dificuldade(nivel):
    tabuleiro = [linha[:] for linha in solucao]
    if nivel == "fácil":
        num_remover = 10
    elif nivel == "médio":
        num_remover = 20
    elif nivel == "difícil":
        num_remover = 30
    else:
        print("Nível inválido!")
        return None

    removidos = 0
    while removidos < num_remover:
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)
        if tabuleiro[linha][coluna] != 0:
            tabuleiro[linha][coluna] = 0
            removidos += 1

    return tabuleiro

def exibir_tabuleiro(tabuleiro):
    for linha in range(9):
        if linha % 3 == 0 and linha != 0:
            print("-" * 21) 
        for coluna in range(9):
            if coluna % 3 == 0 and coluna != 0:
                print("|", end=" ")
            print(tabuleiro[linha][coluna] if tabuleiro[linha][coluna] != 0 else '.', end=" ")
        print()

def selecionar_nivel():
    while True:
        print("Selecione o nível de dificuldade:")
        print("1. Fácil (10 posições em branco)")
        print("2. Médio (20 posições em branco)")
        print("3. Difícil (30 posições em branco)")
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == '1':
            return "fácil"
        elif opcao == '2':
            return "médio"
        elif opcao == '3':
            return "difícil"
        else:
            print("Opção inválida. Tente novamente.")

def inserir_numero(tabuleiro):
    while True:
        try:
            linha = int(input("Digite a linha (0-8): "))
            coluna = int(input("Digite a coluna (0-8): "))
            if tabuleiro[linha][coluna] != 0:
                print("Essa posição já está preenchida. Escolha outra.")
                continue
            numero = int(input("Digite o número (1-9): "))
            if numero < 1 or numero > 9:
                print("Digite um número entre 1 e 9.")
                continue
            tabuleiro[linha][coluna] = numero
            print("Número inserido com sucesso!")
            break
        except (ValueError, IndexError):
            print("Entrada inválida. Digite números entre 0 e 8 para linha/coluna e entre 1 e 9 para o número.")

def tabuleiro_completo(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                return False
    return True

def salvar_ranking(nome, tempo, nivel, arquivo='ranking_sudoku.txt'):
    with open(arquivo, 'a') as f:
        f.write(f'{nome}: {tempo:.2f} {nivel}\n')

def exibir_ranking(arquivo='ranking_sudoku.txt'):
    try:
        with open(arquivo, 'r') as f:
            rankings = []
            for linha in f:
                nome, tempo_nivel_str = linha.strip().split(': ')
                tempo_str, nivel = tempo_nivel_str.split() 
                tempo = float(tempo_str)  
                nivel = linha.strip().split(' ')[-1]
                rankings.append((nome, tempo, nivel))  
            rankings.sort(key=lambda x: x[1])
            print("Ranking de Jogadores:")
            print("Nome...........:            Tempo.........:          Nível.........:")
            for nome, tempo, nivel in rankings:
                print(f"{nome:16s}            {tempo:.2f} segundos           {nivel:.15s}")
    except FileNotFoundError:
        print("Ainda não há rankings salvos.")

def regras():
    print("Regras do Sudoku:")
    print("1. Preencher a grade quadriculada com os números de 1 a 9.")
    print("2. Não repetir números nas linhas horizontais, verticais ou nos blocos quadrados 3 x 3.")
    print("3. O jogo termina quando toda a grade do Sudoku estiver preenchida corretamente com os números.")

def jogar_sudoku():
    nome = input("Digite seu nome: ")
    nivel = selecionar_nivel()  
    tabuleiro = gerar_tabuleiro_dificuldade(nivel)
    if tabuleiro is None:
        return

    tempo_inicial = time.time()

    while not tabuleiro_completo(tabuleiro):
        exibir_tabuleiro(tabuleiro)
        inserir_numero(tabuleiro)

    exibir_tabuleiro(tabuleiro)

    tempo_final = time.time()
    tempo_total = tempo_final - tempo_inicial

    print("Parabéns, você completou o Sudoku!")
    salvar_ranking(nome, tempo_total, nivel)
    exibir_ranking()

def menu():
    while True:
        print("|-----------Menu-----------|")
        print("|1.  Iniciar nova partida  |")
        print("|2.  Ranking               |")
        print("|3.  Regras                |")
        print("|4.  Sair                  |")
        print("|--------------------------|")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            jogar_sudoku()
        elif opcao == '2':
            exibir_ranking()
        elif opcao == '3':
            regras()
        elif opcao == '4':
            print("Hasta la vista! Baby!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
