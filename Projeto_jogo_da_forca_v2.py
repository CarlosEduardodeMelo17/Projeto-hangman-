#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
from random import choice
from os import system, name

#função limpa tela
def clear_screen():
    #Limpa a tela do prompt se for windows
    if name == 'nt':
        _ = system('cls')
    
    #Mac ou linux
    else:
        _ = system(clear)

def screen(posicion):
    hangman = [# estágio 6
                ''' 
                      ______________
                      |            |     
                      |            0
                      |          \\ | /
                      |            |
                      |           / \\
                      |
                ''',
                #estágio 5
                ''' 
                      ______________
                      |            |     
                      |            0
                      |          \\ | /
                      |            |
                      |           / 
                      |
                ''',
                #estágio 4
                ''' 
                      ______________
                      |            |     
                      |            0
                      |          \\ | /
                      |            
                      |           
                      |
                ''',
                #estágio 3
                ''' 
                      ______________
                      |            |     
                      |            0
                      |          \\ | 
                      |            
                      |
                      |
                ''',
                #estágio 2
                ''' 
                      ______________
                      |            |     
                      |            0
                      |            | 
                      |
                      |
                      |
                ''',
               #estágio 1
                ''' 
                      ______________
                      |            |     
                      |            0
                      |            
                      |
                      |
                      |
                ''',
                #estágio 0
                ''' 
                      ______________
                      |            |     
                      |            
                      |           
                      |            
                      |           
                      |
                ''']
    print(hangman[posicion])

        
def game():
    clear_screen()
    username = str(input('Qual o nome do jogador?:  '))
    if username not in ' ': 
        print(f'\033[32mSeja bem vindo {username}\033[m')
    else:
        print(f'\033[32mSeja bem vindo noobmaster69\033[m')
    print('tente adivinhar a palavra')
    
    #lista de palavras
    with open('palavrasforca.csv', 'r', encoding='utf-8', newline = '\r\n') as arq:
        file = csv.reader(arq)
        words = list(file)
    
    #Escolhe a palavra e a dica aleatoriamente
    choise = choice(words)
    word = choise[0].lower()
    
    
    #Mostra as palavras para adivinhar
    letters = ['_' for v in word]
    print('')
    
    #Letras adivinhadas
    guessed_letters = []
    wrong_letters = []
    
    #numero de tentativas
    attempts = 6
    
    #loop equanto o número de tentativas for maior que zero
    while attempts > 0:
        
        #prints e escolha do jogador
        screen(attempts)
        print(letters)
        print(f'Letras descobertas: {guessed_letters}')
        print(f'Letras erradas: {wrong_letters}')
        letter = str(input('Escolha uma letra: ')) 
        while True:
            if letter == '':
                letter = str(input('\033[31mDigite apenas uma letra por favor: \033[m')) 
            else:
                break
        
        while True:
            if letter.isnumeric() == True:
                letter = str(input('\033[31mDigite apenas uma letra por favor: \033[m'))
            else:
                break
        
        print('')
        
        #condicional verificador da palavra 
        if letter in word:
            guessed_letters.append(letter)
            for p, v in enumerate(word):
                if v == letter:
                    letters[p] = letter 
        else:
            attempts -= 1
            wrong_letters.append(letter)
            print(f'\033[31mOps! Você errou tente novamente\033[m')
            print(f'\033[31m{attempts} tentativas\033[m\n')
    
        #condicional 
        if '_' not in letters:
            print(letters)
            print(f'\n\033[32mVocê conseguiu parabéns! A palavra era {word}\033[m')
            break
        
        else:
            if attempts == 0:
                print(f'\033[31mVocê perdeu por atingir o maximo de tentativas A palavra era {word}\033[m')
                break
          


#código principal
if __name__ == "__main__":
    game()

Pagain = str(input('Deseja jogar denovo?: [s/n]'))
if Pagain == 's':
    game()
else:
    print('Você decidiu não jogar denovo')