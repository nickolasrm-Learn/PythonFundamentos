# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
		|
		|
		|
		|
=========''', '''

+---+
|   |
O   |
		|
		|
		|
=========''', '''

+---+
|   |
O   |
|   |
		|
		|
=========''', '''

 +---+
 |   |
 O   |
/|   |
		 |
		 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
		 |
		 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
		 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
		 |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word: str):
        self.word = word
        self.word_letters = list(word)
        self.current = ['_' for letter in word]
        self.wrong_counter = 0

    # Método para adivinhar a letra
    def guess(self, letter):
        found = False
        for i, word_letter in enumerate(self.word_letters):
            if word_letter == letter:
                self.current[i] = letter
                found = True

        if not found:
            self.wrong_counter += 1

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or self.wrong_counter == (len(board) - 1)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        return self.current == self.word_letters

    # Método para não mostrar a letra no board
    def hide_word(self):
        pass

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.wrong_counter] + ''.join(self.current))

# Função para ler uma palavra de forma aleatória do banco de palavras


def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        letter = input("Informe a letra: ")[0]
        game.guess(letter)

    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
