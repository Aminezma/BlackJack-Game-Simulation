import random

import os


def cal_hand(hand):

    sum = 0

    non_aces = [card for card in hand if card != 'A'] 
    
    aces = [card for card in hand if card == 'A']

    for card in non_aces:

        if card in 'JQK':

            sum += 10

        else:

            sum += int(card)

    for card in aces:

        if sum <= 10:

            sum += 11

        else:
            sum += 1

cards = [
 '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
 '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
 '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
 '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
]


random.shuffle(cards)

dealer = []

player = []


player.append(cards.pop())

dealer.append(cards.pop())

player.append(cards.pop())

dealer.append(cards.pop())

standing = False

first_hand = True

while True:

    os.system('cls' if os.name == 'nt' else 'clear')

    player_score = cal_hand(player)
    
    dealer_score = cal_hand(dealer)

    if standing:

         print('Dealer Cards: [{}] ({})'.format(']['.join(dealer), dealer_score))

    else:

        print('Dealer Cards: [{}][?]'.format(dealer[0]))


    print('Dealer Cards: [{}][?]'.format(dealer[0]))

    print('Your Cards: [{}] ({})'.format(']['.join(player), player_score))

    print('')

    if standing:

        if dealer_score > 21:

            print('Dealer Busted, you win!')

        elif player_score == dealer_score:

            print('Push, nobody wins or loses')    

        elif player_score > dealer_score:

            print('You beat the dealer, you win!')

        else:

            print('You lose :(') 

        break


    if first_hand and player_score == 21:

        print('BlackJack! Nice!')

        break
    
    first_hand = False

    

    if player_score > 21:

        print('You busted!')

        break


    print('What would you like to do ?')

    print(' [1] Hit')

    print(' [2] Stand')

    print('')

    choice = input('Your Choice: ')
    
    print('')

    if choice == '1':

        player.append(cards.pop())

    elif choice == '2':

        standing = True
      
        while cal_hand(dealer) <= 16:
      
            dealer.append(cards.pop())
