import random

listtodie = ['Dylan', 'Kyler', 'Grant', 'Doyle', 'Henry', 'Max']
keep_playing = ''

while keep_playing != 'No':
    dead_man = input('Guess who will die next:')
    val = random.randint(0, len(listtodie))

    if dead_man == listtodie[val]:
        print('You were right! {} is going to die next!'.format(listtodie[val]))
        keep_playing = input('Do you want to keep playing? (Yes or No):')

    else:
        print('You were wrong. {} is going to die next!'.format(listtodie[val]))
        keep_playing = input('Do you want to keep playing? (Yes or No):')

print("Done")
