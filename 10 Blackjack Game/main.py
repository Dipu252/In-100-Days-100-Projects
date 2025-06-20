import random
import art

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealer_card():
    num = random.choice(cards)
    return num

def blackjack() -> None:
    your_cards = []
    computer_cards = []
    your_score = 0
    computer_score = 0

    for i in range(2):
        your_cards.append(dealer_card())
        computer_cards.append(dealer_card())

    dealer = 'y'
    while dealer == 'y':
        your_score = sum(your_cards)
        print(f"Your cards: {your_cards}, current score: {your_score}")
        print("computer's first card: ", computer_cards[0])

        if your_score > 21:
            print(f"Your cards: {your_cards}, final score: {your_score}")
            computer_score = sum(computer_cards)
            print(f"computer cards: {computer_cards}, final score: {computer_score}")
            print("You want over. You lose")
            break

        dealer = input("Type 'y' to get another card, Type 'n' to pass: ")
        if dealer == 'y':
            num = dealer_card()
            if num == 11 and your_score + num > 21:
                num = 1
            your_cards.append(num)
    else:
        computer_score = sum(computer_cards)

        while computer_score < 17:
            num = dealer_card()
            if num == 11 and computer_score + num > 21:
                num = 1

            if computer_score + num > 21:
                break
            computer_cards.append(num)
            computer_score = sum(computer_cards)

        print(f"Your cards: {your_cards}, final score: {your_score}")
        print(f"computer cards: {computer_cards}, final score: {computer_score}")

        if computer_score > 21:
            print("You win")
        elif your_score < computer_score:
            print("You lose")
        elif your_score == computer_score:
            print("Draw")
        else:
            print("You win")

while play_game == 'y':
    print(art.logo)
    blackjack()
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
    if play_game == 'y':
        for _ in range(100):
            print("\n")



