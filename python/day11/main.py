"Black jack Project"

from random import randint

playing = True

player_cards = []
computer_cards = []

game_details = {
    "Player" : player_cards,
    "Computer" : computer_cards,
}
dealer = 21


while playing:
    wanna_play = input("Wanna play BlackJack? 'y' for yes, 'n'or any other input for no: ").lower()
    if wanna_play == 'y':
        for _ in game_details:
            player_card, computer_card = randint(1,11), randint(1,11)
            player_cards.append(player_card), computer_cards.append(computer_card)
        print(f"player cards = {player_cards}, computer card = {computer_cards[0]}")
        wanna_pick_a_new_card = input("Do you want to pick a new card or not? 'y' for yes, 'n'or any other input for no: ").lower()
        if wanna_pick_a_new_card == 'y':
            player_card, computer_card = randint(1,11), randint(1,11)
            player_cards.append(player_card), computer_cards.append(computer_card)
            player_cards_sum, computer_cards_sum = sum(player_cards), sum(computer_cards)
            if dealer > player_cards_sum and player_cards_sum > computer_cards_sum:
                print("After the second card pick...Hurray...You Won!!")
            elif dealer > computer_cards_sum and player_cards_sum == computer_cards_sum:
                print("After the second card pick...Sorry...You lost!!")
            else:
                print("Sorry...You lost!!")
            print(player_cards, computer_cards)
        elif wanna_pick_a_new_card == 'n':
            player_cards_sum, computer_cards_sum = sum(player_cards), sum(computer_cards)
            if player_cards_sum > computer_cards_sum:
                print("Hurray...You Won!!")
            elif player_cards_sum == computer_cards_sum:
                print("ohh oh....it's a draw")
            else:
                print("Sorry...You lost!!")
            print(player_cards, computer_cards)
        player_cards = []
        computer_cards = []
    else:
        print("GoodBye!!... Hoping to see you soon.")
        playing = False
    