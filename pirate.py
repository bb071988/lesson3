# pirate bartender project
"""This project creates pirate drinks based on user input and preferences"""

import random
import sys

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adj = ['salty','shakey','old','scurvy','happy']
nouns = ['starboard','pirate','shipwreck','sailor']
    

answers = {}


def get_answers(questions):
    for i, key in enumerate(questions):
        print questions[key]
        drink_response = ''
        while(drink_response == ''):
            drink_response = raw_input("Respond with Y or N   -  ")
            if drink_response.upper() == 'Y':
                answers[key] = True
            elif drink_response.upper() =='N':
                answers[key] = False
            else:
                drink_response = ''
    print(answers)
    return(answers)


def make_drink(answers):
    my_drink = []
    for key in answers:
        if answers[key] == True:
            my_drink.append(random.choice(ingredients[key]))

    return(my_drink)

def print_drink(my_drink):
    print('Your drink is called: ') + name_drink(nouns,adj)
    print('Your drink is made of:')
    for item in my_drink:
        print(item)
    print('  *******************  Enjoy it you scurvy dog   ********************')
    
def name_drink(nouns,adj):
    drink_name = random.choice(adj) + ' ' + random.choice(nouns)
    return(drink_name)
    
###  Program starts here
demo= None

if __name__ == '__main__':

    try:
        demo = sys.argv[1]  
    except:
        pass

    if demo == 'demo':
        my_answers =  {'salty': True, 'strong': False, 'bitter': True, 'fruity': False, 'sweet': True} 
        print_drink(make_drink(my_answers))
    else:
        get_answers(questions)
        make_drink(answers)
        print_drink(make_drink(answers))

            
        