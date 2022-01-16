# ATENÇÃO: Caso o código seja executado fora de um Jupyter Notebook, algumas ferramentas ou métodos podem precisar de ajustes.

# Importar as bibliotecas necessárias
import random
import os
import re
import pandas as pd
import time
import sys
from colorama import Fore, Style

# Definir uma função de placar que mostre a pontuação do usuário (USER) e do programa (PC).
def placar(ponto_usuario, ponto_oponente):
    df = pd.DataFrame({'# -- USER':[ponto_usuario],
                        'x':' ',
                        'PC -- #':[ponto_oponente]})
    
    print(Fore.BLUE + df.to_string(index=False)) # Printa a tabela (dataframe) na cor AZUL.
    print(Style.RESET_ALL) # Reseta o método PRINT para a cor preta.
    
    time.sleep(1) # Aguarda 1 segundo para continuar a execução do código.

# Inicio do código.

""" Pedra, Papel, Tesoura! Vamos jogar contra o computador.
----------------------------------------
"""

pontos_usuario = 0
pontos_oponente = 0

escolhas = dict({'A':'Pedra',
                'B':'Papel',
                'C':'Tesoura'})

while (1 < 2):
    print("\n") # Usado para pular linha.
    print("## Para sair do jogo, escreva 'SAIR' ##\n")
    
    escolhaUsuario =(input("Escolha sua arma! [A] Pedra, [B] Papel, ou [C] Tesoura: ")).upper()
    
    # Se o usuário desejar sair do código...
    if escolhaUsuario == 'SAIR':
        print('Bom jogo! Vamos ver o placar final.')
        placar(pontos_usuario, pontos_oponente) # Chama a função "placar" definida anteriormente.
        
        if pontos_oponente>pontos_usuario:
            print('Não desanime! Você pode ter mais sorte da próxima vez.')
            sys.exit()
            
        else: 
            print('Oh... Não saia assim! Vamos reverter esse placar! xD')
            sys.exit()
    
    # Mas, se ele desejar jogar...
    elif not re.match("[ABC]", escolhaUsuario): # Caso o usuário não tenha inserido uma letra, o programa repete a pergunta.
        print("Por favor, escolha uma letra:")
        print("[A] Pedra, [B] Papel ou [C] Tesoura.")
        continue # Retorna para a linha inicial do Loop.

    # Confirma o input do usuário e a escolha aleatória do programa.
    print("\nVocê escolheu: " + escolhas[escolhaUsuario])
    
    escolhaOponente = random.choice(list(escolhas.keys())) # escolhe aleatoriamente uma das opções
    print("Eu escolhi: " + escolhas[escolhaOponente])
    
    # Caso as escolhas sejam iguais, empate!
    if escolhaOponente == escolhaUsuario:
        print("Empate! ")
        placar(pontos_usuario, pontos_oponente)
    
    # Caso contrário...
    elif escolhaOponente == 'A' and escolhaUsuario == 'C':
        print("Tesoura é mais forte que Pedra! Eu ganhei!")
        pontos_oponente += 1
        placar(pontos_usuario, pontos_oponente)
        continue

    elif escolhaOponente == 'C' and escolhaUsuario == 'B':
        print("Tesoura é mais forte que Papel! Eu ganhei! ")
        pontos_oponente += 1
        placar(pontos_usuario, pontos_oponente)
        continue

    elif escolhaOponente == 'B' and escolhaUsuario == 'A':
        print("Pedra é mais forte que Papel! Eu ganhei! ")
        pontos_oponente += 1
        placar(pontos_usuario, pontos_oponente)
        continue

    else:
        print("Você ganhou!")
        pontos_usuario += 1
        placar(pontos_usuario, pontos_oponente)

# Fim do código.
