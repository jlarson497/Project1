#the game table encapsulates all the different methods and properties needed to play the game of hangman
import Words

class GameTable():
    challenge_word = ""
    hidden_string = []
    list_to_display = []
    string_to_display = ""
    number_of_incorrect_guesses = 0

    def __init__(self, chosen_word):
        self.chosen_word = chosen_word

    def start_game(self):
        list = Words.WordList(self.chosen_word)
        list.makeList()
        final_word = list.choose_word()
        return final_word

    def create_hidden_string(self):  #initialized the hidden word list based on the randomly generated wored
        final_word = self.start_game()
        self.challenge_word = final_word
        for letter in final_word:
            self.hidden_string.append(letter)


    def create_display_list(self):        #initializes the display list based on the hidden list
        for letter in self.hidden_string:
            self.list_to_display.append('_')

    def update_display_string(self):
        self.string_to_display = ''
        for letter in self.list_to_display:  #updates the display string based on the display list
            self.string_to_display += letter + ' '
        print(self.string_to_display)       # and prints it

    def make_guess(self):
        letter = input(print("Choose a letter: ")).lower()  #get guess and convert to lowercase
        while True:
            try:
                letter_index = self.hidden_string.index(letter)  #search for guessed letter in hidden string
                del self.list_to_display[letter_index]           #delete character at letter index in both lists
                del self.hidden_string[letter_index]
                self.list_to_display.insert(letter_index, letter)
                self.hidden_string.insert(letter_index, '_')
                self.update_display_string() #updates the display string and prints it
                print("Number of incorrect guesses: " + str(self.number_of_incorrect_guesses))#show number of incorrect guesses
                return False
            except ValueError:  #Catch error if guess is not in the list
                print("Wrong!  Try again")
                self.number_of_incorrect_guesses += 1
                print("Number of incorrect guesses: " + str(self.number_of_incorrect_guesses))#show number of incorrect guesses
                return False


