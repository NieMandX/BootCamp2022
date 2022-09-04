rounds = 10000
prizes = ['car', 'goat', 'goat']

win_counter_no_change = 0
win_counter_change = 0

def monty_hall(prize, change):
    
    if change:
        if prize == 'car':
            return False
        else:
            return True
    else:
        
        if prize =='car':
            return True
        else:
            return False
        
for _ in range(rounds):
    # doors = shuffle(prize)    
    # door = choice([0, 1, 2])
    
    win_counter_no_change += monty_hall(choice(prizes), change = False)
    win_counter_change += monty_hall(choice(prizes), change = True)

print(f'Probability without changing the door is : {round(win_counter_no_change / rounds, 2)}')
print(f'Probability with door changе is : {round(win_counter_change / rounds, 2)}')

