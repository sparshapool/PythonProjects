from replit import clear
import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]
chosen_word = random.choice(word_list)
display = []
character = len(chosen_word)
stagelen = len(stages) - 1

print(f"The choosen word is: {chosen_word}")
for char in range(character):
    display.append("_")
print(display)
end_game = False

while (not end_game):
    guess = input("Guess a letter: ").lower()
    clear()

    for letter in range(character):
        position = chosen_word[letter]
        if position == guess:
            display[letter] = position
    print(display)

    if guess not in chosen_word:
        stagelen -= 1
        print(stages[stagelen])
        if (stagelen == 0):
            print("You lose")
            end_game = True

    if ("_" not in display):
        end_game = True
        print("You win")
