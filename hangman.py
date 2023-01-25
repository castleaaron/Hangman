'''
By: Aaron Castle
Hangman
'''
import random
all_words = ["Turtle"," Garfield"," alligator"," headphones"," wedding dress"," violin"," newspaper"," raincoat"," chameleon","Cardboard"," Oar"," Drip"," Shampoo"," Time Machine"," Yardstick"," Think"," Lace"," Darts"," Avocado"," Bleach","Curtain"," Extension Cord"," Dent"," Birthday"," Lap"," Sandbox"," Bruise"," Fog"," Sponge"," Wig"," Pilot"," Mascot"," Fireman"," Zoo"," Sushi"," Fizz"," Ceiling"," Post Office"," Season"," Internet"," Chess"," Puppet"," Chime"," Koala"," Dentist"," Ping Pong"," Bonnet"," Sheets"," Sunburn"," Houseboat"," Sleep"," Kneel"," Crust"," Speakers"," Cheerleader"," Dust"," Salmon"," Cabin"," Handle","Swamp"," Cruise"," Pharmacist","Dream","Raft","Plank","Cliff"," Sweater"," Safe","Picnic"," Shrink"," Ray"," Leak","Deep"," Tiptoe","Hurdle"," Knight","Cloak","Bedbug Hot Tub"," Firefighter"," Charger"," Nightmare","Coach","Sneeze","Goblin","Chef","Applause","Golden Retriever","Joke","Comedian","Cupcake","Baker","Facebook","Convertible","Giant","Garden","Diving","Hopscotch","Stingray","Song","Trip","Backbone","Bomb","Treasure","Garbage","Park","Pirate","Ski","Whistle","State","Baseball","Coal","Queen","Photograph","Computer","Hockey","Hot Dog","Salt and Pepper"," iPad"," Frog"," Lawnmower"," Mattress"," Pinwheel"," Cake"," Circus"," Battery"," Mailman"," Cowboy","Password","Bicycle","Skate","Electricity","Thief","Teapot","Deep","Spring","Nature","Shallow","Outside","America","Bow tie","Wax","Light Bulb","Music","Popsicle","Brain","Birthday Cake"," Knee"," Pineapple"," Tusk"," Sprinkler"," Money"," Pool"," Lighthouse"," Doormat"," Face"," Flute"," Rug"," Snowball"," Purse"," Owl"," Gate"," Suitcase"," Stomach"," Doghouse"," Pajamas"," Bathroom"," Scale"," Peach"," Newspaper"," Watering Can"," Hook"," School"," French Fries"," Beehive"," Artist"," Flagpole"," Camera","Hair Dryer","Mushroom","TV","Quilt","Chalk","angle","ant","apple","arch","arm","army","baby","bag","ball","band","basin","basket","bath","bed","bee","bell","berry","bird","blade","board","boat","bone","book","boot","bottle","box","boy","brain","brake","branch","brick","bridge","brush","bucket","bulb","button","cake","camera","card","carriage","cart","cat","chain","cheese","chess","chin","church","circle","clock","cloud","coat","collar","comb","cord","cow","cup","curtain","cushion","dog","door","drain","drawer","dress","drop","ear","egg","engine","eye","face","farm","feather","finger","fish","flag","floor","fly","foot","fork","fowl","frame","garden","girl","glove","goat","gun","hair","hammer","hand","hat","head","heart","hook","horn","horse","hospital","house","island","jewel","kettle","key","knee","knife","knot","leaf","leg","line","lip","lock","map","match","monkey","moon","mouth","muscle","nail","neck","needle","nerve","net","nose","nut","office","orange","oven","parcel","pen","pencil","picture","pig","pin","pipe","plane","plate","plough","pocket","pot","potato","prison","pump","rail","rat","receipt","ring","rod","roof","root","sail","school","scissors","screw","seed","sheep","shelf","ship","shirt","shoe","skin","skirt","snake","sock","spade","sponge","spoon","spring","square","stamp","star","station","stem","stick","stocking","stomach","store","street","sun","table","tail","thread","throat","thumb","ticket","toe","tongue","tooth","town","train","tray","tree","trousers","umbrella","wall","watch","wheel","whip","whistle","window","wing","wire","worm"]

def drawing(counter):
    draw = ['''
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

    return draw[counter]


def check(lst):
    for i in lst:
        if i == '_':
            return False

    return True
    


def main():
    counter = 0
    random_word = random.randint(0, len(all_words) - 1)
    word = all_words[random_word].strip().lower()
    word = word.replace(' ', '')
    length_of_word = len(word)

    empty_spaces = []
    bad_letters = []


    for i in range(length_of_word):
        empty_spaces.append('_')

    while counter < 6:

        print(drawing(counter) + '\n')

        

        for i in empty_spaces:
            print(i, end = ' ')

        print('\nLetters already used:')
        for i in bad_letters:
            print(i, end = ' ')

        print()

        if check(empty_spaces) == True:
            break

        letter = input('Please guess a letter: ')
        letter = letter.lower()

        if len(letter) == 1 and (letter.isalpha() == True):
            if letter in word:
                if word.count(letter) > 1:
                    for i in range(len(word)):
                        if word[i] == letter:
                            empty_spaces[i] = letter
                            continue
                letter_location = word.index(letter)
                empty_spaces[letter_location] = letter
                continue
            else:
                if letter in bad_letters:
                    continue
                bad_letters.append(letter)
                counter += 1
        else:
            print('Not a valid response, try again.')

    if check(empty_spaces) == True:
        print('''                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                 oo             o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""  
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$       
                                """"$$$$$$$$$$$        
                                    $$$$$$$$$$$$       
                                     $$$$$$$$$$"      
                                      "$$$"""''')
        print(f'\nYou win! You correctly guessed the word: {word}, correctly!')
    else:
        print(drawing(counter) + '\n')
        print('You lose!')
        print('The word was:', word)


while True:
    main()
    ans = input('\nEnter "1" if you would like to play again, if not press anything else: ')
    if ans == '1':
        continue
    else:
        break
print('\nThank you for playing!')
input()