#This module is for using the API call to generate a list of words, generate a random number, and use that number
#to generate a random word from the list
import json
import requests
import random

class WordList:

    total_list = []

    def __init__(self, category):
        self.category = category

    def makeList(self):
        url = "https://wordsapiv1.p.mashape.com/words/{cat}/hasParts".format(cat =self.category)#url string for the call
        headers={"X-Mashape-Key": "Xy7czqblF9msh3F4SqLcgFoYpL1Fp16ewAgjsnBJDvm9KVpFBA",   #API key and headers
                 "Accept": "application/json"}
        resp = requests.get(url, headers = headers)
        words = resp.json()
        #exception handling for custom category - ideally, won't allow you to choose a word with no
        #related words -- not working 100%
        try:
            for word in words['hasParts'][0:200]:
                self.total_list.append(word)
        except KeyError:
            print("There are not enough related words, please choose something more general.\n"
                  "Going back to the menu")


    #this method makes a random number based on the length of the list brought in and uses it to select a random word
    def choose_word(self):
        upper = len(self.total_list)
        rand_num = random.randrange(0, upper)
        final_word = self.total_list[rand_num]
        return final_word








