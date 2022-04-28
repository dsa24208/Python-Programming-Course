import random

eightball = ['Go fuck yourself', "That's not likely", "That'll be the day", "I could see that", 'Darn Tootin', 'Pretty solid maybe', 'Absolutely']
keep_playing = ''

while keep_playing != 'No':
    input('What would you like to ask the magic 8 ball:')
    val = random.randint(0, len(eightball))
    print(eightball[val])
    keep_playing = input('Do you have another question? (Yes or No):')

print("Done")
