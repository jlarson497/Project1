#This is a hangman game.  It pulls a word from a dictionary API and then gives the user so many guesses based on
#the difficulty.

import json
import requests
import Words
import game_play

def menu():
    print("Welcome to hangman!")
    print("What would you like to do?")
    choice = input(print('[S]tart game with random category '
                         '\nStart game with [C]ustom category '
                         '\n[V]iew record: ')).lower()
    if choice=='s':
        play_game('building')
        #File I/O will go here, there will be a file with a list of pre set words, read into a list, randomly choose
        #one
    if choice=='c':
        play_game(input('Choose your category: '))
        #having some trouble here with throwing exceptions, game not continuing after throwing exceptions
    if choice=='v':
        print("You've lost a lot")
        #File I/O will go here - record when a game is won and lost to a file and read it back in a formatted view

#def custom_game():
#        while True:
#            try:
#                play_game(input('Choose your category: '))
#                return False
#            except ValueError:
#
#                 continue
def play_game(chosen_word):
    game_table = game_play.GameTable(chosen_word) #instantiate a game table
    game_table.start_game()                       #start the game
    game_table.create_hidden_string()             #set up the necessary lists
    game_table.create_display_list()
    game_table.update_display_string()            #update the display string
    while game_table.number_of_incorrect_guesses < 10:  #give arbitrary number of guesses - will make variable later with
        game_table.make_guess()                         #difficulty settings
        if '_' in game_table.string_to_display:         #as long as there is an _ in the display string, keep going
            continue                                    #if there are no more _, they are all letters and you've one
        else:
            print('You win! Way to go!')
            break
    if game_table.number_of_incorrect_guesses == 10:    #if you've exceeded the number of guesses, you lose
        print('You have lost, sorry about that')        #print a lose message and the challenge word
        print('The word was {w1}'.format(w1 = game_table.challenge_word))

menu()