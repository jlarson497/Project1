class SaveGame:
    ##simple class to handle the saving of a win/loss record
    def __init__(self, winloss):
        self.winloss = winloss

    def update_save_file(self):
        f = open('Hangman Record', 'a')
        f.writelines(self.winloss + ' ')
        f.close()

    def show_save_file(self):
        f = open('Hangman Record', 'r')
        for line in f:
            print(line)
        f.close()

class RandomCategory